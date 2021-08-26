import csv
import matplotlib.pyplot as plt
import numpy as np

DBs = [("A-100.csv", "B-100-3-4.csv"), ("A-100.csv", "B-100-5-2.csv"), ("A-100.csv", "B-100-10-1.csv"), ("A-1000.csv", "B-1000-5-2.csv"), ("A-1000.csv",
                                                                                                                                           "B-1000-10-1.csv"), ("A-1000.csv", "B-1000-50-3.csv"), ("A-10000.csv", "B-10000-5-1.csv"), ("A-10000.csv", "B-10000-50-3.csv"), ("A-10000.csv", "B-10000-500-4.csv")]

ind = {}

for i in range(len(DBs)):
    ind[DBs[i]] = i

sqlite_times = [[[] for j in range(4)] for i in range(9)]
sqlite_avg = [[0 for j in range(4)] for i in range(9)]
with open('sqlite/times.txt') as sqlite:
    csv_reader = csv.reader(sqlite, delimiter=',')
    for row in csv_reader:
        index = ind[(row[1], row[2])]
        qry = int(row[0])-1
        time = float(row[-1])
        sqlite_times[index][qry].append(time)

print("==============================================================")
print("                     SQLITE                                   ")
print("==============================================================")

for db in range(9):
    for qry in range(4):
        sqlite_times[db][qry].sort()
        print(DBs[db], qry+1, round(np.average(np.array(sqlite_times[db][qry][1:-1])), 3),
              round(np.std(np.array(sqlite_times[db][qry][1:-1])), 3))
        sqlite_avg[db][qry] = (np.average(np.array(
            sqlite_times[db][qry][1:-1])), np.std(np.array(sqlite_times[db][qry][1:-1])))


mariadb_index_times = [[[] for j in range(4)] for i in range(9)]
mariadb_index_avg = [[0 for j in range(4)] for i in range(9)]

with open('mariadb_index/times.txt') as mariadb_index:
    csv_reader = csv.reader(mariadb_index, delimiter=',')
    for row in csv_reader:
        index = ind[(row[1], row[2])]
        qry = int(row[0])-1
        time = float(row[-1])
        mariadb_index_times[index][qry].append(time)

print("==========================================================================")
print("                         MARIADB_WITH_INDEX                               ")
print("==========================================================================")

for db in range(9):
    for qry in range(4):
        mariadb_index_times[db][qry].sort()
        print(DBs[db], qry+1, round(np.average(np.array(mariadb_index_times[db][qry][1:-1])), 3),
              round(np.std(np.array(mariadb_index_times[db][qry][1:-1])), 3))
        mariadb_index_avg[db][qry] = (np.average(np.array(
            mariadb_index_times[db][qry][1:-1])), np.std(np.array(mariadb_index_times[db][qry][1:-1])))


mariadb_without_index_times = [[[] for j in range(4)] for i in range(9)]
mariadb_without_index_avg = [[0 for j in range(4)] for i in range(9)]

with open('mariadb_without_index/times.txt') as mariadb_without_index:
    csv_reader = csv.reader(mariadb_without_index, delimiter=',')
    for row in csv_reader:
        index = ind[(row[1], row[2])]
        qry = int(row[0])-1
        time = float(row[-1])
        mariadb_without_index_times[index][qry].append(time)

print("=============================================================================")
print("                         MARIADB_WITHOUT_INDEX                               ")
print("=============================================================================")

for db in range(9):
    for qry in range(4):
        mariadb_without_index_times[db][qry].sort()
        print(DBs[db], qry+1, round(np.average(np.array(mariadb_without_index_times[db][qry][1:-1])), 3),
              round(np.std(np.array(mariadb_without_index_times[db][qry][1:-1])), 3))
        mariadb_without_index_avg[db][qry] = (np.average(
            np.array(mariadb_without_index_times[db][qry][1:-1])), np.std(np.array(mariadb_without_index_times[db][qry][1:-1])))


mongo_times = [[[] for j in range(4)] for i in range(9)]
mongo_avg = [[0 for j in range(4)] for i in range(9)]

with open('mongo/times.txt') as mongo:
    csv_reader = csv.reader(mongo, delimiter=',')
    for row in csv_reader:
        index = ind[(row[1], row[2])]
        qry = int(row[0])-1
        time = float(row[-1])
        mongo_times[index][qry].append(time)

print("==========================================================================")
print("                         MONGODB                                          ")
print("==========================================================================")

for db in range(9):
    for qry in range(4):
        mongo_times[db][qry].sort()
        print(DBs[db], qry+1, round(np.average(np.array(mongo_times[db][qry][1:-1])), 3),
              round(np.std(np.array(mongo_times[db][qry][1:-1])), 3))
        mongo_avg[db][qry] = (np.average(np.array(
            mongo_times[db][qry][1:-1])), np.std(np.array(mongo_times[db][qry][1:-1])))

colors = ['tab:blue', 'tab:orange', 'tab:green', 'tab:red',
          'tab:purple', 'tab:brown', 'tab:pink', 'tab:gray', 'tab:cyan']
for qry in range(4):
    plt.figure(figsize=(10, 6))
    for db in range(9):
        times = []
        for lst in [sqlite_avg, mariadb_index_avg, mariadb_without_index_avg, mongo_avg]:
            times.append(lst[db][qry][0])

        dbms = ["SQLite3", "MariaDB_with_INDEXES",
                "MARIADB_WITHOUT_INDEXES", "MONGODB"]
        plt.plot(dbms, times, marker='o',
                 color=colors[db], label=f"({DBs[db][0]},{DBs[db][1]})")
    plt.title(
        f'DBMS vs Time taken for query {qry+1}')
    plt.xlabel('DBMS')
    plt.ylabel('Time Taken in seconds')
    plt.legend()
    plt.savefig(f'graphs/dbms_time/{qry+1}.png')
    plt.close()

dbms = ["SQLite3", "MariaDB_with_INDEXES",
        "MARIADB_WITHOUT_INDEXES", "MONGODB"]
for qry in range(4):
    plt.figure(figsize=(10, 6))
    i = 0
    for lst in [sqlite_avg, mariadb_index_avg, mariadb_without_index_avg, mongo_avg]:
        times = []
        dbs = []
        for db in range(9):
            times.append(lst[db][qry][0])
            dbs.append(db + 1)
        plt.plot(dbs, times, marker='o', color=colors[i], label=dbms[i])
        plt.title(
            f'Time taken for query {qry+1} as size of Data Base increases')
        i += 1

    plt.xlabel('Database')
    plt.ylabel('Time taken in seconds')
    plt.legend()
    plt.savefig(f'graphs/db_size_time/{qry+1}.png')
    plt.close()


for db in range(9):
    plt.figure(figsize=(10, 6))
    i=0
    for lst in [sqlite_avg, mariadb_index_avg, mariadb_without_index_avg, mongo_avg]:
        times = []
        qrs = []
        for qry in range(4):
            times.append(lst[db][qry][0])
            qrs.append(qry + 1)
        plt.plot(qrs, times, marker='o',color=colors[i],label=f'{dbms[i]}')
        plt.title(
            f'Time taken for different queries for Database {DBs[db]}')
        i += 1
    plt.xticks([1,2,3,4])
    plt.xlabel('Query')
    plt.ylabel('Time taken in seconds')
    plt.legend()
    plt.savefig(f'graphs/db_qry_time/{db+1}.png')
    plt.close()
    
for qry in range(4):
    for db in range(9):
        times = []
        for lst in [sqlite_avg, mariadb_index_avg, mariadb_without_index_avg, mongo_avg]:
            times.append(lst[db][qry][0])

        dbms = ["SQLite3", "MariaDB_with_INDEXES",
                "MARIADB_WITHOUT_INDEXES", "MONGODB"]
        plt.figure(figsize=(10, 6))
        plt.plot(dbms, times, marker='o',
                 color=colors[db], label=f"({DBs[db][0]},{DBs[db][1]})")
        plt.title(
            f'DBMS vs Time taken for query {qry+1} and DB {DBs[db]}')
        plt.xlabel('DBMS')
        plt.ylabel('Time Taken in seconds')
        plt.savefig(f'graphs/extra/dbms_time/{db+1}_{qry+1}.png')
        plt.close()

dbms = ["SQLite3", "MariaDB_with_INDEXES",
        "MARIADB_WITHOUT_INDEXES", "MONGODB"]
for qry in range(4):
    i = 0
    for lst in [sqlite_avg, mariadb_index_avg, mariadb_without_index_avg, mongo_avg]:
        times = []
        dbs = []
        for db in range(9):
            times.append(lst[db][qry][0])
            dbs.append(db + 1)
        plt.figure(figsize=(10, 6))
        plt.plot(dbs, times, marker='o', color=colors[i], label=dbms[i])
        plt.title(
            f'Time taken for query {qry+1} and dbms {dbms[i]} as size of Data Base increases')
        plt.xlabel('Database')
        plt.ylabel('Time taken in seconds')
        plt.legend()
        plt.savefig(f'graphs/extra/db_size_time/{dbms[i]}_{qry+1}.png')
        plt.close()
        i += 1



for db in range(9):
    i = 0
    for lst in [sqlite_avg, mariadb_index_avg, mariadb_without_index_avg, mongo_avg]:
        times = []
        qrs = []
        for qry in range(4):
            times.append(lst[db][qry][0])
            qrs.append(qry + 1)
        plt.figure(figsize=(10, 6))
        plt.plot(qrs, times, marker='o', color=colors[i], label=f'{dbms[i]}')
        plt.title(
            f'Time taken for different queries for Database {DBs[db]} and dbms {dbms[i]}')
        plt.xticks([1, 2, 3, 4])
        plt.xlabel('Query')
        plt.ylabel('Time taken in seconds')
        plt.legend()
        plt.savefig(f'graphs/extra/db_qry_time/{dbms[i]}_{db+1}.png')
        plt.close()
        i += 1


