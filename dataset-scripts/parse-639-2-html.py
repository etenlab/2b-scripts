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

# run from /dev, assumes datasets repo is cloned peer to this repo
with open("./datasets/files/iso-639-2.html") as fp:
    soup = BeautifulSoup(fp, "html.parser")
    rows = soup.find_all("tr")

    for row in rows:
        lines = row.text.split('\n')

        print(
            f"ISO 639-2: {lines[1]}\nISO 639-1: {lines[2]}\nEnglish: {lines[3]}\nFrench: {lines[4]}\nGerman: {lines[5]} \n\n")

        if len(lines[1]) > 3:
            first = lines[1][slice(0, 3)]
            second = lines[1][slice(7, 10)]

            cur.execute("insert into iso_639_2 (iso_639_2, entry_type, iso_639_1, english_name, french_name, german_name) VALUES (%s, %s, %s, %s, %s, %s)",
                        (first, 'B', lines[2], lines[3], lines[4], lines[5]))
            conn.commit()

            cur.execute("insert into iso_639_2 (iso_639_2, entry_type, iso_639_1, english_name, french_name, german_name) VALUES (%s, %s, %s, %s, %s, %s)",
                        (second, 'T', lines[2], lines[3], lines[4], lines[5]))
            conn.commit()
        else:
            cur.execute("insert into iso_639_2 (iso_639_2, iso_639_1, english_name, french_name, german_name) VALUES (%s, %s, %s, %s, %s)",
                        (lines[1], lines[2], lines[3], lines[4], lines[5]))
            conn.commit()

cur.close()
conn.close()
