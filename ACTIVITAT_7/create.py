import psycopg2
from connection import conexio

def crearRegistro(user_name: str, user_surname: str, user_age: int, user_email: str):

    try:
        conn = conexio()

        cursor = conn.cursor()

        sql = '''insert into USERS (user_name, user_surname, user_age, user_email) values (%s, %s, %s, %s)'''

        values = (user_name, user_surname, user_age, user_email)
        cursor.execute(sql, values)

        conn.commit()

    except (Exception, psycopg2.Error) as error:
        print("Error", error)

    finally:
        conn.close()
