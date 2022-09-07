# brew install postgresql
# pip install psycopg2-binary
import psycopg2

conn = psycopg2.connect(dbname="eil_db_1", user="postgres", password="asdfasdf", host="localhost", port="5432")
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

