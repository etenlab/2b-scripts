# brew install postgresql
# pip install psycopg2-binary
import psycopg2
import json
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
first = True
file = open("./datasets/files/rod_dialects.json")
data = json.load(file)

for res in data["data"]:

    print(f"dialect_code: {res['dialect_code']},\n language_code: {res['language_code']}, country_code: {res['country_code']}, dialect_name: {res['dialect_name']}, language_name: {res['language_name']}, location_name: {res['location_name']}\n\n ")

    cur.execute("insert into rod_dialects (dialect_code, language_code, country_code, dialect_name, language_name, location_name) VALUES (%s, %s, %s, %s, %s, %s)",
                (res['dialect_code'], res['language_code'], res['country_code'], res['dialect_name'], res['language_name'], res['location_name']))
    conn.commit()

cur.close()
conn.close()
