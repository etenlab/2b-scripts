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
with open("./datasets/files/iso-639-3_Name_Index_20220311.tab") as fp:
    for line in fp.readlines():
      if first:
        first = False
        continue
      segs = line.split('\t')

      print(f"id: {segs[0]}, print: {segs[1]} inverted: {segs[2]} ")
      
      cur.execute("insert into iso_639_3_names (iso_639_3, print_name, inverted_name) VALUES (%s, %s, %s)", 
        (segs[0], segs[1], segs[2])
      )
      conn.commit()

cur.close()
conn.close()

