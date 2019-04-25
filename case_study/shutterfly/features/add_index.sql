USE Shutterfly;

ALTER TABLE `Purchase`
  ADD KEY `ix_custno_index` (`custno`);

ALTER TABLE `Purchase` CHANGE `orderdate` `orderdate` DATETIME NULL DEFAULT NULL;

ALTER TABLE `Purchase`
  ADD KEY `ix_orderdate_index` (`orderdate`);

ALTER TABLE `Online`
  ADD KEY `ix_custno_index` (`custno`);

ALTER TABLE `Online` CHANGE `dt` `dt` DATETIME NULL DEFAULT NULL;

ALTER TABLE `Online`
  ADD KEY `ix_dt_index` (`dt`);