# brew install postgresql
# pip install psycopg2-binary
import psycopg2
import eilcommon

conn = psycopg2.connect(
    dbname=eilcommon.pg_database, 
    user=eilcommon.pg_user, 
    password=eilcommon.pg_password, 
    host=eilcommon.pg_host, 
    port=eilcommon.pg_port
)
cur = conn.cursor()

# run from /dev, assumes datasets repo is cloned peer to this repo
first = True
with open("./datasets/files/sil-LanguageCodes.tab") as fp:
    for line in fp.readlines():
        if first:
            first = False
            continue
        segs = line.split('\t')

        print(
            f"LangID: {segs[0]}, CountryID: {segs[1]}, LangStatus: {segs[2]}, Name: {segs[3]} ")

        cur.execute("insert into sil_language_codes (code, country_code, status, name) VALUES (%s, %s, %s, %s)",
                    (segs[0], segs[1], segs[2], segs[3]))
        conn.commit()

cur.close()
conn.close()
