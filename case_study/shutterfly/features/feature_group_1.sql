USE Shutterfly;

DROP TABLE IF EXISTS features_group_1;

CREATE TABLE IF NOT EXISTS features_group_1
SELECT o.index
  ,LEFT(o.dt, 10) AS day
  ,COUNT(*) AS order_count
  ,SUM(p.revenue) AS revenue_sum
  ,MAX(p.revenue) AS revenue_max
  ,MIN(p.revenue) AS revenue_min
  ,SUM(p.revenue) / COUNT(*) AS rev_p_order
  ,COUNT(p.prodcat1) AS prodcat1_count
  ,COUNT(p.prodcat2) AS prodcat2_count
  ,DATEDIFF(o.dt, MAX(p.orderdate)) AS days_last_order
  ,DATEDIFF(o.dt, MAX(CASE WHEN p.prodcat1 IS NOT NULL THEN p.orderdate ELSE NULL END)) AS days_last_prodcat1
  ,DATEDIFF(o.dt, MAX(CASE WHEN p.prodcat2 IS NOT NULL THEN p.orderdate ELSE NULL END)) AS days_last_prodcat2
  ,SUM(p.prodcat1 = 1) AS prodcat1_1_count
  ,SUM(p.prodcat1 = 2) AS prodcat1_2_count
  ,SUM(p.prodcat1 = 3) AS prodcat1_3_count
  ,SUM(p.prodcat1 = 4) AS prodcat1_4_count
  ,SUM(p.prodcat1 = 5) AS prodcat1_5_count
  ,SUM(p.prodcat1 = 6) AS prodcat1_6_count
  ,SUM(p.prodcat1 = 7) AS prodcat1_7_count
FROM Online AS o 
JOIN Purchase AS p
  ON o.custno = p.custno
  AND p.orderdate <= o.dt
GROUP BY o.index;

ALTER TABLE `features_group_1`
  ADD KEY `ix_features_group_1_index` (`index`);