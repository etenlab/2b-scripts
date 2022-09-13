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
with open("./datasets/files/uf-languages.html") as fp:
    soup = BeautifulSoup(fp, "html.parser")
    rows = soup.find_all("tr")

    for row in rows:
        # if first:
        #     first = False
        #     continue
        # lines = row.text.split('\n')
        cols = row.find_all('td')
        cols = [ele.text.strip() for ele in cols]

        if cols:
            print(
                f"Code: {cols[0]}\n ISO-639-3: {cols[1]}\n Name: {cols[2]}\n Alternate Name: {cols[3]}\n Anglicized Name: {cols[4]}\n Country: {cols[5]}\n Gateway Language: {cols[6]}\n GW: {cols[7]}\n\n\n")
            # break
            cur.execute("insert into uf_languages (code, iso_639_3, name, alternate_name, anglicized_name, country, gateway_language, gw) VALUES (%s, %s, %s, %s, %s, %s, %s, %s)",
                        (cols[0], cols[1], cols[2], cols[3], cols[4], cols[5], cols[6], cols[7]))
            conn.commit()

cur.close()
conn.close()
