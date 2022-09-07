# brew install postgresql
# pip install psycopg2-binary
import psycopg2

conn = psycopg2.connect(dbname="eil_db_1", user="postgres", password="asdfasdf", host="localhost", port="5432")
cur = conn.cursor()

# run from /dev, assumes datasets repo is cloned peer to this repo
first = True
with open("./datasets/files/iso-639-3_Retirements_20220311.tab") as fp:
    for line in fp.readlines():
      if first:
        first = False
        continue
      segs = line.split('\t')

      print(f"iso: {segs[0]}, name: {segs[1]} reason: {segs[2]} change: {segs[3]} remedy: {segs[4]} effective: {segs[5]} ")
      
      cur.execute("insert into iso_639_3_retirements (iso_639_3, ref_name, ret_reason, change_to, ret_remedy, effective) VALUES (%s, %s, %s, %s, %s, %s)", 
        (segs[0], segs[1], segs[2], segs[3], segs[4], segs[5].strip())
      )
      conn.commit()

cur.close()
conn.close()

