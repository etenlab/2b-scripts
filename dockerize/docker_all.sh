# run from dev folder

echo "\n\nremember to run from dev folder\n\n"

# authentication api
echo "\nauthentication-api"
cd authentication-api
./gradlew bootJar
docker build -t etenlab/authentication-api .

# dataset iso-639-2
echo "\n\ndataset-api-iso-639-2"
cd ../dataset-api-iso-639-2
./gradlew bootJar
docker build -t etenlab/iso-639-2-api .

# database api
echo "\n\ndatabase-api"
cd ../database-api
./gradlew bootJar
docker build -t etenlab/database-api .

cd ..

echo "\n\nfinished. you should be ready to run docker compose.\n\n"