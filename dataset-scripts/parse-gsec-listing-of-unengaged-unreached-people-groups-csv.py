# brew install postgresql
# pip install psycopg2-binary
import psycopg2
import csv
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
csvStart = False

with open("./datasets/files/2022-08_GSEC_Listing_of_Unengaged_Unreached_People_Groups.csv", newline='') as csvfile:
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
        if row:
            print(f"peid {row[0]}\n affinity_bloc {row[1]}\n people_cluster {row[2]}\n continent {row[3]}\n sub-continent {row[4]}\n country {row[5]}\n country_of_origin {row[6]}\n people_group {row[7]}\n global_status_of_evangelical_christianity {row[8]}\n evangelical_engagement {row[9]}\n population {row[10]}\n dispersed {row[11]}\n rol {row[12]}\n language {row[13]}\n religion {row[14]}\n nomadic {row[15]}\n nomadic_type {row[16]}\n nomadic_description {row[17]}\n published_scripture {row[18]}\n jesus_film {row[19]}\n radio_broadcast {row[20]}\n gospel_recording {row[21]}\n audio_scripture {row[22]}\n gospel_films {row[23]}\n the_hope {row[24]}\n resources {row[25]}\n physical_exertion {row[26]}\n freedom_index {row[27]}\n government_restrictions_index {row[28]}\n social_hostilities_index {row[29]}\n threat_level {row[30]}\n rop1 {row[31]}\n rop2 {row[32]}\n rop3 {row[33]}\n rop_peoplename {row[34]}\n genc {row[35]}\n fips {row[36]}\n fips_of_origin {row[37]}\n latitude {row[38]}\n longitude {row[39]}\n imb_affinity_group {row[40]}\n not_engaged_anywhere {row[41]}\n spi {row[42]}\n strategic_priority_index {row[43]}\n ror {row[44]}\n diaspora {row[45]}\n\n\n")
            # break

            cur.execute("insert into gsec_listing_of_unengaged_unreached_people_groups (peid, affinity_bloc, people_cluster, continent, sub_continent, country, country_of_origin, people_group, global_status_of_evangelical_christianity, evangelical_engagement, population, dispersed, rol, language, religion, nomadic, nomadic_type, nomadic_description, published_scripture, jesus_film, radio_broadcast, gospel_recording, audio_scripture, gospel_films, the_hope, resources, physical_exertion, freedom_index, government_restrictions_index, social_hostilities_index, threat_level, rop1, rop2, rop3, rop_people_name, genc, fips, fips_of_origin, latitude, longitude, imb_affinity_group, not_engaged_anywhere, spi, strategic_priority_index, ror, diaspora) VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)",
                        ((row[0] or None), row[1], row[2], row[3], row[4], row[5], row[6], row[7], (row[8] or None), (row[9] or None), (row[10].replace(",", "") or None), (row[11] or None), row[12], row[13], row[14], (None if row[15] == '' else row[15]), (row[16] or None), row[17], (row[18] or None), (row[19] or None), (row[20] or None), (row[21] or None), (row[22] or None), (row[23] or None), (row[24] or None), (row[25] or None), row[26], row[27], row[28], row[29], row[30], row[31], row[32], (row[33] or None), row[34], row[35], row[36], row[37], row[38], row[39], row[40], row[41], (row[42] or None), row[43], (row[44] or None), ((None if row[45] == 'NULL' else row[45]) or None)))
            conn.commit()

cur.close()
conn.close()
