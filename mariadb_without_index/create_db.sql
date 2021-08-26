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
INFILE 'dbs/fileA' INTO TABLE A fields terminated by ',' IGNORE 1 LINES;

LOAD DATA LOCAL
INFILE 'dbs/fileB' INTO TABLE B fields terminated by ',' IGNORE 1 LINES;
