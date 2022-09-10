# brew install postgresql
# pip install psycopg2-binary
import psycopg2

conn = psycopg2.connect(dbname="eil_db_1", user="postgres",
                        password="asdfasdf", host="localhost", port="5432")
cur = conn.cursor()

# run from /dev, assumes datasets repo is cloned peer to this repo
first = True
with open("./datasets/files/sil-CountryCodes.tab") as fp:
    for line in fp.readlines():
        if first:
            first = False
            continue
        segs = line.split('\t')

        print(f"CountryID: {segs[0]}, Name: {segs[1]}, Area: {segs[2]} ")

        cur.execute("insert into sil_country_codes (code, name, area) VALUES (%s, %s, %s)",
                    (segs[0], segs[1], segs[2]))
        conn.commit()

cur.close()
conn.close()
