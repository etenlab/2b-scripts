# pip3 install beautifulsoup4
from bs4 import BeautifulSoup

# brew install postgresql
# pip install psycopg2-binary
import psycopg2

conn = psycopg2.connect(dbname="eil_db_1", user="postgres", password="asdfasdf", host="localhost", port="5432")
cur = conn.cursor()

# run from /dev, assumes datasets repo is cloned peer to this repo
with open("./2b-datasets/iso-639-5.html") as fp:
    soup = BeautifulSoup(fp, "html.parser")
    rows = soup.find_all("tr")

    for row in rows:
      lines = row.text.split('\n')

      print(f"identifier: {lines[1]}\nenglish name: {lines[2]}\nfrench name: {lines[3]}\niso_639-2: {lines[4]}\nhierarchy: {lines[5]}\n \n\n")

      cur.execute("insert into iso_639_5 (identifier, english_name, french_name, iso_639_2, hierarchy) VALUES (%s, %s, %s, %s, %s)", 
      (lines[1], lines[2], lines[3], lines[4], lines[5]))
      conn.commit()

cur.close()
conn.close()

