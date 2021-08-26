.mode csv
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

.import dbs/fileA A
.import dbs/fileB B

.save sqlite/cs315.db