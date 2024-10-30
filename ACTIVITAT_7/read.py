import psycopg2
from connection import conexio

def leerRegistros():
    try:
        conn = conexio()

        cursor = conn.cursor()

        sql = '''select * from USERS'''

        cursor.execute(sql)

        registres = cursor.fetchall()

        return registres

    except (Exception, psycopg2.Error) as error:
        print("Error", error)

    finally:
        conn.close()
