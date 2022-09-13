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
with open("./datasets/files/iso-639-3-macrolanguages_20220311.tab") as fp:
    for line in fp.readlines():
      if first:
        first = False
        continue
      segs = line.split('\t')

      print(f"m_id: {segs[0]}, i_id: {segs[1]} i_status: {segs[2]} ")
      
      cur.execute("insert into iso_639_3_macrolanguages (m_id, i_id, i_status) VALUES (%s, %s, %s)", 
        (segs[0], segs[1], segs[2].strip())
      )
      conn.commit()

cur.close()
conn.close()

