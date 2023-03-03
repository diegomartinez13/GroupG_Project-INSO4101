import os

pg_config = {
    'user': os.getenv("DB_USER"),
    'password': os.getenv("DB_PASSWORD"),
    'host': os.getenv("DB_HOST"),
    'dbname': os.getenv("DB_NAME"),
    'port': os.getenv("DB_PORT")
}