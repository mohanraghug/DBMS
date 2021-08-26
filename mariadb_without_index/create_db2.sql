DROP database if EXISTS cs315;
create database cs315;
use cs315;

create table A
(
    A1 INTEGER,
    A2 VARCHAR(100)
);

create table B
(
    B1 INTEGER,
    B2 INTEGER,
    B3 VARCHAR(100)
);


LOAD DATA LOCAL
INFILE 'dbs/A-10000.csv' INTO TABLE A fields terminated by ',' IGNORE 1 LINES;

LOAD DATA LOCAL
INFILE 'dbs/B-10000-500-4.csv' INTO TABLE B fields terminated by ',' IGNORE 1 LINES;
