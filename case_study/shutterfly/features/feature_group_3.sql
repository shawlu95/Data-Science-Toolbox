USE Shutterfly;

DROP TABLE IF EXISTS features_group_3;

CREATE TABLE IF NOT EXISTS features_group_3
SELECT
  offset.index
  ,o3.category AS last_category
  ,o3.event1 AS last_event1
  ,o3.event2 AS last_event2
FROM
(SELECT 
  o1.index
  ,o1.custno
  ,MAX(o2.dt) AS last_dt
FROM Online AS o1
JOIN Online AS o2
  ON o1.custno = o2.custno
  AND o1.dt > o2.dt
GROUP BY o1.index, o1.custno) AS offset
JOIN Online AS o3
ON offset.custno = o3.custno
AND offset.last_dt = o3.dt;

ALTER TABLE `features_group_3`
  ADD KEY `ix_features_group_3_index` (`index`);