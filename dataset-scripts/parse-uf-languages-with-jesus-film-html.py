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
with open("./datasets/files/uf-languages-with-jesus-film.html") as fp:
    soup = BeautifulSoup(fp, "html.parser")
    rows = soup.find_all("tr")

    for row in rows:
        # if first:
        #     first = False
        #     continue
        # lines = row.text.split('\n')
        cols = row.find_all('td')
        cols = [ele.text.strip() for ele in cols]
        # print(cols)
        if cols:
            print(
                f"Language: {cols[1]}\nMedia: {cols[2]}\nPublished: {cols[3]}\nInfo: {cols[4]}\n\n\n")
            # break
            cur.execute("insert into uf_languages_with_jesus_film (language, media, published, info) VALUES (%s, %s, %s, %s)",
                        (cols[1], cols[2], cols[3], cols[4]))
            conn.commit()

cur.close()
conn.close()
