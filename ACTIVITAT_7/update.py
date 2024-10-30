import psycopg2
from connection import conexio

def actualitzaRegistro(user_name, user_surname, user_age, user_email, id):
    try:
        conn = conexio()

        cursor = conn.cursor()

        sql = '''update users set user_name = %s, user_surname = %s, user_age = %s, user_email = %s where user_id = %s'''

        values = (user_name, user_surname, user_age, user_email, id)
        cursor.execute(sql, values)

        conn.commit()

    except (Exception, psycopg2.Error) as error:
        print("Error", error)

    finally:
        conn.close()
