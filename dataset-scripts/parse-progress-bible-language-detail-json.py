# brew install postgresql
# pip install psycopg2-binary
import psycopg2
import json

conn = psycopg2.connect(dbname="eil_db_1", user="postgres",
                        password="asdfasdf", host="localhost", port="5432")
cur = conn.cursor()

# run from /dev, assumes datasets repo is cloned peer to this repo
first = True
file = open("./datasets/files/progress-bible-language-detail.json")
data = json.load(file)

for res in data["resource"]:

    print(f"UnitCode: {res['UnitCode']}, UnitType: {res['UnitType']}, UnitName: {res['UnitName']}, UnitFullName: {res['UnitFullName']}, EthnologueName: {res['EthnologueName']}, ISO_639_3Code: {res['ISO_639_3Code']}, IsSignLanguage: {res['IsSignLanguage']}, CodeStatus {res['CodeStatus']}, LanguageStatus {res['LanguageStatus']}, LanguageScope {res['LanguageScope']}, PrimaryContinent {res['PrimaryContinent']}, PrimaryCountryName {res['PrimaryCountryName']}, PrimaryCountryCode {res['PrimaryCountryCode']}, RetirementExplanation {res['RetirementExplanation']}, HowToFix {res['HowToFix']}, RetiredDate {res['RetiredDate']}, ShowActiveLanguage {res['ShowActiveLanguage']}, ShowRetiredLanguage {res['ShowRetiredLanguage']}, ShowActiveDialect {res['ShowActiveDialect']}, ShowRetiredDialect {res['ShowRetiredDialect']}, ShowSignLanguage {res['ShowSignLanguage']} ")

    countryCode = None
    if res['PrimaryCountryCode'] is not None:
        if len(res['PrimaryCountryCode']) > 2:
            countryCode = None
        else:
            countryCode = res['PrimaryCountryCode']

    cur.execute("insert into progress_bible_language_details (unit_code, unit_type, unit_name, Unit_full_name, ethnologue_name, iso_639_3_code, is_sign_language, code_status, language_status, language_scope, primary_continent, primary_country_name, primary_country_code, retirement_explanation, how_to_fix, retired_date, show_active_language, show_retired_language, show_active_dialect, show_retired_dialect, show_sign_language) VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)",
                (res['UnitCode'], res['UnitType'], res['UnitName'], res['UnitFullName'], res['EthnologueName'], res['ISO_639_3Code'], res['IsSignLanguage'], res['CodeStatus'], res['LanguageStatus'], res['LanguageScope'], res['PrimaryContinent'], res['PrimaryCountryName'], countryCode, res['RetirementExplanation'], res['HowToFix'], res['RetiredDate'], res['ShowActiveLanguage'], res['ShowRetiredLanguage'], res['ShowActiveDialect'], res['ShowRetiredDialect'], res['ShowSignLanguage']))
    conn.commit()

cur.close()
conn.close()
