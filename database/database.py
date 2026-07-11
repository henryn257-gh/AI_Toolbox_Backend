import sqlite3
import os


DATABASE_PATH = "database/database.db"



def get_connection():

    os.makedirs(
        "database",
        exist_ok=True
    )

    return sqlite3.connect(
        DATABASE_PATH
    )



def setup_database():

    connection = get_connection()

    cursor = connection.cursor()


    cursor.execute("""
    CREATE TABLE IF NOT EXISTS devices(

        id INTEGER PRIMARY KEY,

        name TEXT,

        token TEXT UNIQUE,

        enabled INTEGER DEFAULT 1,

        requests INTEGER DEFAULT 0

    )
    """)


    connection.commit()

    connection.close()
