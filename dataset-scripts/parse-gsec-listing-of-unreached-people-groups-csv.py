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

with open("./datasets/files/2022-08_GSEC_Listing_of_Unreached_People_Groups.csv", newline='') as csvfile:
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
            print(f"PEID {row[0]}\n Affinity Bloc {row[1]}\n People Cluster {row[2]}\n Continent {row[3]}\n Sub-Continent {row[4]}\n Country {row[5]}\n Country of Origin {row[6]}\n People Group {row[7]}\n Global Status of  Evangelical Christianity {row[8]}\n Evangelical Engagement {row[9]}\n Population {row[10]}\n Dispersed (Yes/No) {row[11]}\n ROL {row[12]}\n Language {row[13]}\n Religion {row[14]}\n Nomadic {row[15]}\n Nomadic Type {row[16]}\n Nomadic Description {row[17]}\n Published Scripture {row[18]}\n Jesus Film {row[19]}\n Radio Broadcast {row[20]}\n Gospel Recording {row[21]}\n Audio Scripture {row[22]}\n Gospel Films {row[23]}\n The HOPE {row[24]}\n Resources {row[25]}\n Physical Exertion {row[26]}\n Freedom Index {row[27]}\n Government Restrictions Index {row[28]}\n Social Hostilities Index {row[29]}\n Threat Level {row[30]}\n ROP1 {row[31]}\n ROP2 {row[32]}\n ROP3 {row[33]}\n ROP PeopleName {row[34]}\n GENC {row[35]}\n FIPS {row[36]}\n FIPS of Origin {row[37]}\n Latitude {row[38]}\n Longitude {row[39]}\n IMB Affinity Group {row[40]}\n Not Engaged Anywhere {row[41]}\n SPI {row[42]}\n Strategic Priority Index {row[43]}\n\n\n")
            # break

            cur.execute("insert into gsec_listing_of_unreached_people_groups (peid,affinity_bloc,people_cluster,continent,sub_continent,country,country_of_origin,people_group,global_status_of_evangelical_christianity,evangelical_engagement,population,dispersed,rol,language,religion,nomadic,nomadic_type,nomadic_description,published_scripture,jesus_film,radio_broadcast,gospel_recording,audio_scripture,gospel_films,the_hope,resources,physical_exertion,freedom_index,government_restrictions_index,social_hostilities_index,threat_level,rop1,rop2,rop3,rop_people_name,genc,fips,fips_of_origin,latitude,longitude,imb_affinity_group,not_engaged_anywhere,spi,strategic_priority_index) VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)",
                        ((row[0] or None), row[1], row[2], row[3], row[4], row[5], row[6], row[7], (row[8] or None), (row[9] or None), (row[10].replace(",", "") or None), (row[11] or None), row[12], row[13], row[14], (None if row[15] == '' else row[15]), (row[16] or None), row[17], (row[18] or None), (row[19] or None), (row[20] or None), (row[21] or None), (row[22] or None), (row[23] or None), (row[24] or None), (row[25] or None), row[26], row[27], row[28], row[29], row[30], row[31], row[32], (row[33] or None), row[34], row[35], row[36], row[37], row[38], row[39], row[40], row[41], (row[42].replace(",", "") or None), row[43]))
            conn.commit()

cur.close()
conn.close()
