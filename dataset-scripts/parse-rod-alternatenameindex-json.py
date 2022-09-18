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
file = open("./datasets/files/rod_alternatenameindex.json")
data = json.load(file)

for res in data["data"]:
    print(res)

    print(
        f"dialect_code: {res['dialect_code']},\n variant_name: {res['variant_name']}\n\n ")

    # countryCode = None
    # if res['PrimaryCountryCode'] is not None:
    #     if len(res['PrimaryCountryCode']) > 2:
    #         countryCode = None
    #     else:
    #         countryCode = res['PrimaryCountryCode']

    cur.execute("insert into rod_alternatenameindex (dialect_code, variant_name) VALUES (%s, %s)",
                (res['dialect_code'], res['variant_name']))
    conn.commit()

cur.close()
conn.close()
