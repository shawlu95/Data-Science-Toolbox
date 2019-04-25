USE Shutterfly;

DROP TABLE IF EXISTS features_group_2;

CREATE TABLE IF NOT EXISTS features_group_2
SELECT 
  o1.index
  ,SUM(o2.category = 1) AS category_1_count
  ,SUM(o2.category = 2) AS category_2_count
  ,SUM(o2.category = 3) AS category_3_count
  ,SUM(o2.event1 IS NOT NULL AND o2.event1 = 1) AS event1_1_count
  ,SUM(o2.event1 IS NOT NULL AND o2.event1 = 2) AS event1_2_count
  ,SUM(o2.event1 IS NOT NULL AND o2.event1 = 4) AS event1_4_count
  ,SUM(o2.event1 IS NOT NULL AND o2.event1 = 5) AS event1_5_count
  ,SUM(o2.event1 IS NOT NULL AND o2.event1 = 6) AS event1_6_count
  ,SUM(o2.event1 IS NOT NULL AND o2.event1 = 7) AS event1_7_count
  ,SUM(o2.event1 IS NOT NULL AND o2.event1 = 8) AS event1_8_count
  ,SUM(o2.event1 IS NOT NULL AND o2.event1 = 9) AS event1_9_count
  ,SUM(o2.event1 IS NOT NULL AND o2.event1 = 10) AS event1_10_count
  ,SUM(o2.event1 IS NOT NULL AND o2.event1 = 11) AS event1_11_count
  ,SUM(o2.event1 IS NULL) AS event1_null_count
  ,SUM(o2.event2 = 1) AS event2_1_count
  ,SUM(o2.event2 = 2) AS event2_2_count
  ,SUM(o2.event2 = 3) AS event2_3_count
  ,SUM(o2.event2 = 4) AS event2_4_count
  ,SUM(o2.event2 = 5) AS event2_5_count
  ,SUM(o2.event2 = 6) AS event2_6_count
  ,SUM(o2.event2 = 7) AS event2_7_count
  ,SUM(o2.event2 = 8) AS event2_8_count
  ,SUM(o2.event2 = 9) AS event2_9_count
  ,SUM(o2.event2 = 10) AS event2_10_count
FROM Online AS o1
JOIN Online AS o2
  ON o1.custno = o2.custno
  AND o1.dt >= o2.dt
GROUP BY o1.index;

ALTER TABLE `features_group_2`
  ADD KEY `ix_features_group_2_index` (`index`);