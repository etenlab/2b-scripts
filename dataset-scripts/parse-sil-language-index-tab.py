# brew install postgresql
# pip install psycopg2-binary
import psycopg2

conn = psycopg2.connect(dbname="eil_db_1", user="postgres",
                        password="asdfasdf", host="localhost", port="5432")
cur = conn.cursor()

# run from /dev, assumes datasets repo is cloned peer to this repo
first = True
with open("./datasets/files/sil-LanguageIndex.tab") as fp:
    for line in fp.readlines():
        if first:
            first = False
            continue
        segs = line.split('\t')

        print(
            f"LangID: {segs[0]}, CountryID: {segs[1]}, NameType: {segs[2]}, Name: {segs[3]} ")

        cur.execute("insert into sil_language_index (language_code, country_code, name_type, name) VALUES (%s, %s, %s, %s)",
                    (segs[0], segs[1], segs[2], segs[3]))
        conn.commit()

cur.close()
conn.close()
