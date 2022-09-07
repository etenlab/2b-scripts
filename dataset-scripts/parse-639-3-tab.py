# brew install postgresql
# pip install psycopg2-binary
import psycopg2

conn = psycopg2.connect(dbname="eil_db_1", user="postgres", password="asdfasdf", host="localhost", port="5432")
cur = conn.cursor()

# run from /dev, assumes datasets repo is cloned peer to this repo
first = True
with open("./datasets/files/iso-639-3_20220311.tab") as fp:
    for line in fp.readlines():
      if first:
        first = False
        continue
      segs = line.split('\t')

      print(f"id: {segs[0]}, 2b: {segs[1]}, 2t: {segs[2]} part1: {segs[3]} scope: {segs[4]} l type: {segs[5]} ref: {segs[6]} comment {segs[7]} ")
      
      cur.execute("insert into iso_639_3 (iso_639_3, part_2b, part_2t, part_1, scope, entry_type, ref_name, comment) VALUES (%s, %s, %s, %s, %s, %s, %s, %s)", 
      (segs[0], segs[1], segs[2], segs[3], segs[4], segs[5], segs[6], segs[7]))
      conn.commit()

cur.close()
conn.close()

