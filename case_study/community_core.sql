create table if not exists fds_ds.seller_comm_detect (
  vendorid string,
  commid int,
  degree int,
  core boolean
) partitioned by (update_dt string)
row format delimited
  fields terminated by ',';

set hive.mapred.mode = 'unstrict';

drop table if exists fds_ds_scratch.seller_comm_detect_inherited;
create table fds_ds_scratch.seller_comm_detect_inherited as
with dt_ranked as (
select
  *, dense_rank() over (order by update_dt desc) as rn
from fds_ds.seller_comm_detect
where core = true
),
previous_core as (
select * from dt_ranked where rn = 1
)
select
  a.id as vendorid
  ,a.component_id as component_id
  ,b.commid
from fds_ds.seller_comm_detect_tmp as a
join previous_core as b
on a.id = b.vendorid;

drop table if exists fds_ds_scratch.seller_comm_detect_merge;
create table fds_ds_scratch.seller_comm_detect_merge as
select
  component_id
  ,min(commid) as commid
from fds_ds_scratch.seller_comm_detect_inherited
group by component_id;

drop table if exists fds_ds_scratch.seller_comm_detect_propagate;
create table fds_ds_scratch.seller_comm_detect_propagate as
select
  a.id as vendorid
  ,a.component_id as component_id
  ,case when c.comp_size >= 3 then b.commid else null end as commid
from fds_ds.seller_comm_detect_tmp as a
left join fds_ds_scratch.seller_comm_detect_merge as b
on a.component_id = b.component_id
left join (
  select component_id, count(*) as comp_size
  from fds_ds.seller_comm_detect_tmp
  group by component_id
) as c
on a.component_id = c.component_id;

set hive.mapred.mode = 'unstrict';

drop table if exists fds_ds_scratch.seller_comm_detect_max_commid;
create table fds_ds_scratch.seller_comm_detect_max_commid as
select coalesce(max(commid), 0) as max_commid from fds_ds.seller_comm_detect;

drop table if exists fds_ds_scratch.seller_comm_detect_new;
create table fds_ds_scratch.seller_comm_detect_new as
with unassigned as (
select
  component_id
  ,count(*) as nrow
from fds_ds_scratch.seller_comm_detect_propagate
where commid is null
group by component_id
),
filtered as (
select *, row_number() over (order by nrow desc) as tmp
from unassigned
where nrow >= 3
)
select
  a.component_id
  ,a.nrow
  ,a.tmp + b.max_commid as commid
from filtered as a, fds_ds_scratch.seller_comm_detect_max_commid as b;

set hive.exec.dynamic.partition.mode=nonstrict;
drop table if exists fds_ds_scratch.seller_comm_detect_complete_commid;
create table fds_ds_scratch.seller_comm_detect_complete_commid as
select
  a.vendorid
  ,a.component_id
  ,coalesce(a.commid, b.commid) as commid
from fds_ds_scratch.seller_comm_detect_propagate as a
left join fds_ds_scratch.seller_comm_detect_new as b
on a.component_id = b.component_id;

with degree_ranked as (
select
  a.vendorid, b.degree as degree, a.component_id, a.commid
  ,row_number() over (partition by a.component_id order by b.degree desc, a.vendorid asc) as rk
from fds_ds_scratch.seller_comm_detect_complete_commid as a
join fds_ds.seller_comm_detect_degree as b
  on a.vendorid = b.id
)
insert into table fds_ds.seller_comm_detect partition (update_dt)
select
  vendorid, commid, degree
  ,case when commid is null then null when rk = 1 then True else False end as core
  ,${update_dt} as update_dt
from degree_ranked;

drop table if exists fds_ds_scratch.seller_comm_detect_inherited;
drop table if exists fds_ds_scratch.seller_comm_detect_merge;
drop table if exists fds_ds_scratch.seller_comm_detect_max_commid;
drop table if exists fds_ds_scratch.seller_comm_detect_propagate;
drop table if exists fds_ds_scratch.seller_comm_detect_new;
drop table if exists fds_ds_scratch.seller_comm_detect_complete_commid;
