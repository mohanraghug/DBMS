#!/bin/bash
filesA=("A-100.csv" "A-100.csv" "A-100.csv" "A-1000.csv" "A-1000.csv" "A-1000.csv" "A-10000.csv" "A-10000.csv" "A-10000.csv")
filesB=("B-100-3-" "B-100-5-" "B-100-10-" "B-1000-5-" "B-1000-10-" "B-1000-50-" "B-10000-5-" "B-10000-50-" "B-10000-500-")

TIMEFORMAT=%3R
touch sqlite/times.txt
touch mariadb_index/times.txt
touch mariadb_without_index/times.txt
touch mongo/times.txt
k=0
for i in {2,6,8}; do
    for j in {2,6,8}; do
        
        ((val=$i*$j%5))
        
        fileA=${filesA[k]}
        fileB=${filesB[k]}$val.csv
        
        # data loading 
        cat sqlite/create_db.sql | sed 's/fileA/'"$fileA"'/' | sed 's/fileB/'"$fileB"'/' > sqlite/create_db2.sql
        sqlite3 < sqlite/create_db2.sql
        
        cat mariadb_index/create_db.sql | sed 's/fileA/'"$fileA"'/' | sed 's/fileB/'"$fileB"'/' > mariadb_index/create_db2.sql
        mariadb < mariadb_index/create_db2.sql

        cat mariadb_without_index/create_db.sql | sed 's/fileA/'"$fileA"'/' | sed 's/fileB/'"$fileB"'/' > mariadb_without_index/create_db2.sql
        mariadb < mariadb_without_index/create_db2.sql

        mongoimport --type csv -c A --headerline --drop dbs/"$fileA"
        mongoimport --type csv -c B --headerline --drop dbs/"$fileB"
        
        time1=$({ time sqlite3 sqlite/cs315.db < sqlite/qry1.sql > sqlite/out1; } 2>&1)
        echo 1,$fileA,$fileB,$time1 >> sqlite/times.txt

        time1=$({ time mariadb < mariadb_index/qry1.sql > mariadb_index/out1; } 2>&1)
        echo 1,$fileA,$fileB,$time1 >> mariadb_index/times.txt

        time1=$({ time mariadb < mariadb_without_index/qry1.sql > mariadb_without_index/out1; } 2>&1)
        echo 1,$fileA,$fileB,$time1 >> mariadb_without_index/times.txt

        time1=$({ time mongo < mongo/qry1.mongo > mongo/out1; } 2>&1)
        echo 1,$fileA,$fileB,$time1 >> mongo/times.txt
        
        time2=$({ time sqlite3 sqlite/cs315.db < sqlite/qry2.sql > sqlite/out2; } 2>&1)
        echo 2,$fileA,$fileB,$time2 >> sqlite/times.txt

        time2=$({ time mariadb < mariadb_index/qry2.sql > mariadb_index/out2; } 2>&1)
        echo 2,$fileA,$fileB,$time2 >> mariadb_index/times.txt

        time2=$({ time mariadb < mariadb_without_index/qry2.sql > mariadb_without_index/out2; } 2>&1)
        echo 2,$fileA,$fileB,$time2 >> mariadb_without_index/times.txt

        time2=$({ time mongo < mongo/qry2.mongo > mongo/out2; } 2>&1)
        echo 2,$fileA,$fileB,$time2 >> mongo/times.txt
        
        
        time3=$({ time sqlite3 sqlite/cs315.db < sqlite/qry3.sql > sqlite/out3; } 2>&1)
        echo 3,$fileA,$fileB,$time3 >> sqlite/times.txt

        time3=$({ time mariadb < mariadb_index/qry3.sql > mariadb_index/out3; } 2>&1)
        echo 3,$fileA,$fileB,$time3 >> mariadb_index/times.txt

        time3=$({ time mariadb < mariadb_without_index/qry3.sql > mariadb_without_index/out3; } 2>&1)
        echo 3,$fileA,$fileB,$time3 >> mariadb_without_index/times.txt

        time3=$({ time mongo < mongo/qry3.mongo > mongo/out3; } 2>&1)
        echo 3,$fileA,$fileB,$time3 >> mongo/times.txt
        
        time4=$({ time sqlite3 sqlite/cs315.db < sqlite/qry4.sql > sqlite/out4; } 2>&1)
        echo 4,$fileA,$fileB,$time4 >> sqlite/times.txt

        time4=$({ time mariadb < mariadb_index/qry4.sql > mariadb_index/out4; } 2>&1)
        echo 4,$fileA,$fileB,$time4 >> mariadb_index/times.txt

        time4=$({ time mariadb < mariadb_without_index/qry4.sql > mariadb_without_index/out4; } 2>&1)
        echo 4,$fileA,$fileB,$time4 >> mariadb_without_index/times.txt

        time4=$({ time mongo < mongo/qry4.mongo > mongo/out4; } 2>&1)
        echo 4,$fileA,$fileB,$time4 >> mongo/times.txt
        

        
        ((k=k+1))
    done
done


