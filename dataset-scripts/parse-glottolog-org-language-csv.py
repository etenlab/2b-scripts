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

with open("./datasets/files/data-glottolog-org-language.csv", newline='') as csvfile:
    dialect = csv.Sniffer().sniff(csvfile.read(1024))
    csvfile.seek(0)
    reader = csv.reader(csvfile, dialect)
    next(reader)
    next(reader)
    next(reader)
    next(reader)
    next(reader)
    for row in reader:
        # rows.append(row)
        # if csvStart == False and row[0]:
        #     csvStart = True
        #     continue
        if not all(i is '' for i in row):
            print(f"Glottocode {row[0]}\n Name {row[1]}\n Top-level family {row[2]}\n ISO-639-3 {row[3]}\n Macro-area {row[4]}\n Child dialects {row[5]}\n Latitude {row[6]}\n Longitude {row[7]}\n\n\n\n")
            # break

            cur.execute("insert into glottolog_language (glottocode, name, top_level_family, iso_639_3, macro_area, child_dialects, latitude, longitude) VALUES (%s, %s, %s, %s, %s, %s, %s, %s)",
                        ((row[0] or None), row[1], row[2], row[3], row[4], (row[5] or None), row[6], row[7]))
            conn.commit()

cur.close()
conn.close()
