import psycopg2
from connection import conexio

def actualitzaRegistro(user_name, user_surname, user_age, user_email, id):
    try:

        conn = conexio()
        cursor = conn.cursor()

        sql = "update users SET "

        values = []

        updates = []

        if user_name:
            updates.append("user_name = %s")
            values.append(user_name)

        if user_surname:
            updates.append("user_surname = %s")
            values.append(user_surname)

        if user_age:
            updates.append("user_age = %s")
            values.append(user_age)

        if user_email:
            updates.append("user_email = %s")
            values.append(user_email)

        for i in range(len(updates)):
            sql = sql + updates[i]

            if i < (len(updates) - 1):
                sql = sql + ", "

        sql = sql + " where user_id = %s"
        values.append(id)

        cursor.execute(sql, values)
        conn.commit()

    except (Exception, psycopg2.Error) as error:
        print("Error:", error)

    finally:
        conn.close()
