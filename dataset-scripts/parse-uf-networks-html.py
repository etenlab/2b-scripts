# pip3 install beautifulsoup4
from bs4 import BeautifulSoup

# brew install postgresql
# pip install psycopg2-binary
import psycopg2

conn = psycopg2.connect(dbname="eil_db_1", user="postgres",
                        password="asdfasdf", host="localhost", port="5432")
cur = conn.cursor()
first = True
# run from /dev, assumes datasets repo is cloned peer to this repo
with open("./datasets/files/uf-networks.html") as fp:
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
            cur.execute("insert into uf_networks (code, iso_639_3, name, alternate_name, anglicized_name, country, gateway_language, gw) VALUES (%s, %s, %s, %s, %s, %s, %s, %s)",
                        (cols[0], cols[1], cols[2], cols[3], cols[4], cols[5], cols[6], cols[7]))
            conn.commit()

cur.close()
conn.close()
