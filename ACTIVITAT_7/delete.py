import psycopg2
from connection import conexio

def borrarRegistro(id):
    try:
        conn = conexio()

        cursor = conn.cursor()

        sql = '''delete from USERS where user_id = %s'''

        values = (id,)

        cursor.execute(sql, values)

        conn.commit()

    except (Exception, psycopg2.Error) as error:
        print("Error", error)

    finally:
        conn.close()
