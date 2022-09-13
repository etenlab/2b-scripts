# pip3 install beautifulsoup4
from bs4 import BeautifulSoup

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
first = True
# run from /dev, assumes datasets repo is cloned peer to this repo
with open("./datasets/files/uf-countries-list.html") as fp:
    soup = BeautifulSoup(fp, "html.parser")
    rows = soup.find_all("tr")

    for row in rows:
        if first:
            first = False
            continue
        lines = row.text.split('\n')
        print(
            f"Code: {lines[1]}\nAlpha 3 Code: {lines[2]}\nName: {lines[3]}\nRegion: {lines[4]}\nWA Region: {lines[5]}\nPopulation: {lines[6]}\n \n\n")

        cur.execute("insert into uf_countries_list (code, alpha_3_code, name, region, wa_region, population) VALUES (%s, %s, %s, %s, %s, %s)",
                    (lines[1], lines[2], lines[3], lines[4], lines[5], None if lines[6] == '' else lines[6]))
        conn.commit()

cur.close()
conn.close()
