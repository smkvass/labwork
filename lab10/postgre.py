import psycopg2
from config import host, user, password, db_name
import csv

try:
    #connect existing database
    connection = psycopg2.connect(
        host=host,
        user=user,
        password=password,
        database=db_name
    )

    connection.autocommit = True

    #cursor for performing database operations
    with connection.cursor() as cursor:
        cursor.execute(
            "SELECT version();"
        )
        print(f"Select version: {cursor.fetchone()}")


    

    #delete data from table
    with connection.cursor() as cursor:
        cursor.execute(
            """DELETE FROM users WHERE id = 1;"""
        )
        print("[INFO] Data succesfully deleted")
    
except Exception as _ex:
    print("[INFO] Error while working with PostgreSQL", _ex)
finally:
    if connection:
        connection.close()
        print("[INFO] PostgreSQL connection closed")