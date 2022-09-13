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
with open("./datasets/files/uf-additional-languages.html") as fp:
    soup = BeautifulSoup(fp, "html.parser")
    rows = soup.find_all("tr")

    for row in rows:
        if first:
            first = False
            continue
        lines = row.text.split('\n')
        print(
            f"IETF Tag: {lines[1]}\nTwo Letter: {lines[2]}\nThree Letter: {lines[3]}\nCommon Name: {lines[4]}\nNative Name: {lines[5]}\nDirection: {lines[5]}\nComment: {lines[5]}\n \n\n")

        cur.execute("insert into uf_additional_languages (ietf_tag, two_letter, three_letter, common_name, native_name, direction, comment) VALUES (%s, %s, %s, %s, %s, %s, %s)",
                    (lines[1], lines[2], lines[3], lines[4], lines[5], lines[6], lines[7]))
        conn.commit()

cur.close()
conn.close()
