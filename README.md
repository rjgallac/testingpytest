
# Python testing

pytest from root runs test

run program 
    python src/main.py

docker run --name some-postgres -p5432:5432 -e POSTGRES_PASSWORD=mysecretpassword -d postgres

docker exec -it some-postgres psql -U postgres -c "CREATE TABLE DB_table ( name TEXT, age INT );"

docker exec -it some-postgres psql -U postgres -c "INSERT INTO DB_table(name, age) VALUES('Alice', 21);"


docker exec -it -u postgres some-postgres sh
