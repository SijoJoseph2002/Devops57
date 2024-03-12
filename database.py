import psycopg2

# Establish connection to the database
conn = psycopg2.connect(
    dbname="postgres",
    user="postgres",
    password="password",
    host="localhost",
    port="5432"
)
