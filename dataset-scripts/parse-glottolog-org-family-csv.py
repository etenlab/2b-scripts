# brew install postgresql
# pip install psycopg2-binary
import psycopg2
import csv
import eilcommon

conn = psycopg2.connect(
    dbname=eilcommon.pg_database,
    user=eilcommon.pg_user,
    password=eilcommon.pg_password,
    host=eilcommon.pg_host,
    port=eilcommon.pg_port
)
cur = conn.cursor()

first = True
csvStart = False

with open("./datasets/files/data-glottolog-org-family.csv", newline='') as csvfile:
    dialect = csv.Sniffer().sniff(csvfile.read(1024))
    csvfile.seek(0)
    reader = csv.reader(csvfile, dialect)
    next(reader)
    for row in reader:
        # rows.append(row)
        # if csvStart == False and row[0]:
        #     csvStart = True
        #     continue
        if not all(i is '' for i in row):
            print(
                f"Name {row[0]}\n,Level{row[1]}\n,Macro-area{row[2]}\n,Sub-families{row[3]}\n,Child languages{row[4]}\n,Top-level family{row[5]}\n\n\n")
            # break

            cur.execute("insert into glottolog_family (name, level, macro_area, sub_families, child_languages, top_level_family) VALUES (%s, %s, %s, %s, %s, %s)",
                        ((row[0] or None), row[1], row[2], row[3], row[4], (row[5] or None)))
            conn.commit()

cur.close()
conn.close()
