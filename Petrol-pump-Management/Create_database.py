import mysql.connector

try:
    # Establishing a connection to the MySQL server
    with mysql.connector.connect(
        host="localhost",
        user="root",
        password="Abhi6190@mysql",
    ) as mydb:
        # Creating a cursor object
        with mydb.cursor() as c:
            # Creating the database if it doesn't exist
            c.execute("CREATE DATABASE IF NOT EXISTS PetrolPump_Management")
            print("Database 'PetrolPump_Management' created successfully.")
except mysql.connector.Error as err:
    print(f"Error: {err}")