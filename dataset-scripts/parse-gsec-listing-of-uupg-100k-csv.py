# brew install postgresql
# pip install psycopg2-binary
import psycopg2
import csv
from datetime import datetime

conn = psycopg2.connect(dbname="eil_db_1", user="postgres",
                        password="asdfasdf", host="localhost", port="5432")
cur = conn.cursor()

first = True
csvStart = False

with open("./datasets/files/2022-08_GSEC_Listing_of_UUPG_100K.csv", newline='') as csvfile:
    dialect = csv.Sniffer().sniff(csvfile.read(1024))
    csvfile.seek(0)
    reader = csv.reader(csvfile, dialect)
    next(reader)
    next(reader)
    next(reader)
    next(reader)
    next(reader)
    for row in reader:
        # rows.append(row)
        # if csvStart == False and row[0]:
        #     csvStart = True
        #     continue
        if not all(i is '' for i in row):
            print(f"PEID {row[0]}\n Affinity Bloc {row[1]}\n People Cluster {row[2]}\n Continent {row[3]}\n Sub-Continent {row[4]}\n Country {row[5]}\n Country of Origin {row[6]}\n People Group {row[7]}\n Global Status of  Evangelical Christianity {row[8]}\n ROL {row[9]}\n Language {row[10]}\n Religion {row[11]}\n Nomadic {row[12]}\n Nomadic Type {row[13]}\n Nomadic Description {row[14]}\n Population {row[15]}\n Dispersed (Yes/No) {row[16]}\n Published Scripture {row[17]}\n Jesus Film {row[18]}\n Radio Broadcast {row[19]}\n Gospel Recording {row[20]}\n Audio Scripture {row[21]}\n Gospel Films {row[22]}\n The HOPE {row[23]}\n Resources {row[24]}\n Physical Exertion {row[25]}\n Freedom Index {row[26]}\n Government Restrictions Index {row[27]}\n Social Hostilities Index {row[28]}\n Threat Level {row[29]}\n ROP1 {row[30]}\n ROP2 {row[31]}\n ROP3 {row[32]}\n People Name {row[33]}\n GENC {row[34]}\n FIPS {row[35]}\n FIPS of Origin {row[36]}\n Latitude {row[37]}\n Longitude {row[38]}\n Addition {row[39]}\n Addition Date {row[40]}\n Addition Reasons {row[41]}\n IMB Affinity Group {row[42]}\n Not Engaged Anywhere {row[43]}\n SPI {row[44]}\n Strategic Priority Index {row[45]}\n\n\n")
            # break

            cur.execute("insert into gsec_listing_of_uupg_100k (peid, affinity_bloc, people_cluster, continent, sub_continent, country, country_of_origin, people_group, global_status_of_evangelical_christianity, rol, language, religion, nomadic, nomadic_type, nomadic_description, population, dispersed, published_scripture, jesus_film, radio_broadcast, gospel_recording, audio_scripture, gospel_films, the_hope, resources, physical_exertion, freedom_index, government_restrictions_index, social_hostilities_index, threat_level, rop1, rop2, rop3, people_name, genc, fips, fips_of_origin, latitude, longitude, addition, addition_date, addition_reasons, imb_affinity_group, not_engaged_anywhere, spi, strategic_priority_index) VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)",
                        ((row[0] or None), (row[1] or None), (row[2] or None), (row[3] or None), (row[4] or None), (row[5] or None), (row[6] or None), (row[7] or None), (row[8] or None), (row[9] or None), (row[10].replace(",", "") or None), (row[11] or None), (row[12] or None), (row[13] or None), (row[14] or None), (row[15].replace(",", "").strip() or None), (row[16].strip() or None), (row[17] or None), (row[18] or None), (row[19] or None), (row[20] or None), (row[21] or None), (row[22] or None), (row[23] or None), (row[24] or None), (row[25] or None), (row[26] or None), (row[27] or None), (row[28] or None), (row[29] or None), (row[30] or None), (row[31] or None), (row[32] or None), (row[33] or None), (row[34] or None), (row[35] or None), (row[36] or None), (row[37] or None), (row[38] or None), (row[39] or None), (None if (row[40] == '' or row[40] == 'NULL') else datetime.strptime(row[40], '%m/%d/%y')), (row[41] or None), (row[42] or None), (row[43] or None), (row[44] or None), (row[45] or None)))
            conn.commit()

cur.close()
conn.close()
