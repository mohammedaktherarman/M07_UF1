import psycopg2
from connection import conexio

def crearTabla():
    try:
        conn = conexio()

        cursor = conn.cursor()

        sql = '''CREATE TABLE USERS(
                        user_id SERIAL PRIMARY KEY, 
                        user_name VARCHAR(255) NOT NULL, 
                        user_surname VARCHAR(255) NOT NULL, 
                        user_age INT NOT NULL, 
                        user_email VARCHAR(255) NOT NULL
        )'''

        cursor.execute(sql)
        conn.commit()

    except (Exception, psycopg2.Error) as error:
        print("Error", error)

    finally:
        conn.close()
