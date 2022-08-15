# run from dev folder

echo "\n\nremember to run from dev folder\n\n"

# authentication api
echo "\n2b-authentication-api"
cd 2b-authentication-api
./gradlew bootJar
docker build -t etenlab/2b-authentication-api .

# dataset iso-639-2
echo "\n\n2b-dataset-api-iso-639-2"
cd ../2b-dataset-api-iso-639-2
./gradlew bootJar
docker build -t etenlab/2b-dataset-api-iso-639-2 .

cd ..

echo "\n\nfinished. you should be ready to run docker compose.\n\n"