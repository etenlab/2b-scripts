# brew install postgresql
# pip install psycopg2-binary
import psycopg2
import json
from datetime import datetime

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
file = open("./datasets/files/rod_changelist.json")
data = json.load(file)

for res in data["data"]:

    print(f"dialect_code: {res['dialect_code']},\n date: {res['date']}, change_type: {res['change_type']}, prev_language_code: {res['prev_language_code']}, new_language_code: {res['new_language_code']}, explanation: {res['explanation']}\n\n ")

    # countryCode = None
    # if res['PrimaryCountryCode'] is not None:
    #     if len(res['PrimaryCountryCode']) > 2:
    #         countryCode = None
    #     else:
    #         countryCode = res['PrimaryCountryCode']

    cur.execute("insert into rod_changelist (dialect_code, date, change_type, prev_language_code, new_language_code, explanation) VALUES (%s, %s, %s, %s, %s, %s)",
                (res['dialect_code'], (None if res['date'] == '' else datetime.strptime(res['date'], '%Y-%m-%d')), res['change_type'], res['prev_language_code'], res['new_language_code'], res['explanation']))
    conn.commit()

cur.close()
conn.close()
