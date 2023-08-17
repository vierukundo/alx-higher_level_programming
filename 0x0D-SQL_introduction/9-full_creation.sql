-- Script should create maximum of 4 records
CREATE TABLE IF NOT EXISTS second_table (id INT, name VARCHAR(256), score INT);
-- insert first record
INSERT INTO `second_table` (`id`, `name`, `score`) VALUES (1, "John", 10);
-- insert second record
INSERT INTO `second_table` (`id`, `name`, `score`) VALUES (2, "Alex", 3);
-- insert third record
INSERT INTO `second_table` (`id`, `name`, `score`) VALUES (3, "Bob", 14);
-- insert fourth record
INSERT INTO `second_table` (`id`, `name`, `score`) VALUES (4, "George", 8);
