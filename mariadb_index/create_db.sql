DROP database if EXISTS cs315_index;
create database cs315_index;
use cs315_index;
create table A
(
    A1 INTEGER PRIMARY KEY,
    A2 VARCHAR(100)
);

create table B
(
    B1 INTEGER PRIMARY KEY,
    B2 INTEGER,
    B3 VARCHAR(100),
    FOREIGN KEY(B2) REFERENCES A(A1)
);


LOAD DATA LOCAL
INFILE 'dbs/fileA' INTO TABLE A fields terminated by ',' IGNORE 1 LINES;

LOAD DATA LOCAL
INFILE 'dbs/fileB' INTO TABLE B fields terminated by ',' IGNORE 1 LINES;

CREATE INDEX b3 on B(B3);
