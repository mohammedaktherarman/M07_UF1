import psycopg2
from connection import conexio

def leerRegistros():
    try:
        conn = conexio()
        cursor = conn.cursor()

        sql = '''select * from USERS'''

        cursor.execute(sql)
        registres = cursor.fetchall()

        if registres:
            print("Registres:")
            for registro in registres:
                print(registro)
        else:
            print("No hi ha registres.")

        return registres

    except (Exception, psycopg2.Error) as error:
        print("Error:", error)

    finally:
        conn.close()
