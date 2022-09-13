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
with open("./datasets/files/uf-langnames.txt") as fp:
    for line in fp.readlines():
        # if first:
        #     first = False
        #     continue
        segs = line.split('\t')

        print(f"LangID: {segs[0]}\nName: {segs[1]}\n\n\n")

        cur.execute("insert into uf_langnames (code, name) VALUES (%s, %s)",
                    (segs[0], segs[1]))
        conn.commit()

cur.close()
conn.close()
