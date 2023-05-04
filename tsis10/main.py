import psycopg2


def add_user(username, phonenumber):
    sql = "INSERT INTO phonebook(name, phone) VALUES(%s, %s)"
    connection = None
    try:
        connection = psycopg2.connect(host="localhost", database="postgres", user="postgres", password="qwerty")
        with connection.cursor() as cursor:
            cursor.execute(sql, (username, phonenumber))
        connection.commit()
    except (Exception, psycopg2.DatabaseError) as error:
        print(error)
    finally:
        if connection is not None:
            connection.close()


def upload_csv(path):
    sql = "COPY phonebook(name, phone) FROM STDIN DELIMITER ';' CSV HEADER"
    connection = None
    try:
        connection = psycopg2.connect(host="localhost", database="postgres", user="postgres", password="qwerty")
        with connection.cursor() as cursor:
            with open(path, 'r') as csv:
                cursor.copy_expert(sql=sql, file=csv)
        connection.commit()
    except (Exception, psycopg2.DatabaseError) as error:
        print(error)
    finally:
        if connection is not None:
            connection.close()


def update_data(user_id, username, phonenumber):
    sql = "UPDATE phonebook SET name = %s, phone = %s WHERE id = %s"
    connection = None
    try:
        connection = psycopg2.connect(host="localhost", database="postgres", user="postgres", password="qwerty")
        with connection.cursor() as cursor:
            cursor.execute(sql, (username, phonenumber, user_id))
        connection.commit()
    except (Exception, psycopg2.DatabaseError) as error:
        print(error)
    finally:
        if connection is not None:
            connection.close()


def query_data(filter_col=None, filter_val=None):
    sql = "SELECT * FROM phonebook WHERE {} = %s".format(filter_col)
    sql_else = "SELECT * FROM phonebook"
    connection = None
    try:
        connection = psycopg2.connect(host="localhost", database="postgres", user="postgres", password="qwerty")
        with connection.cursor() as cursor:
            if filter_col and filter_val:
                cursor.execute(sql, (filter_val,))
            else:
                cursor.execute(sql_else)
            rows = cursor.fetchall()
            for row in rows:
                print(row)
    except (Exception, psycopg2.DatabaseError) as error:
        print(error)
    finally:
        if connection is not None:
            connection.close()


def delete_user(username):
    sql = "DELETE from phonebook WHERE name = %s"
    connection = None
    try:
        connection = psycopg2.connect(host="localhost", database="postgres", user="postgres", password="qwerty")
        with connection.cursor() as cursor:
            cursor.execute(sql, (username,))
        connection.commit()
    except (Exception, psycopg2.DatabaseError) as error:
        print(error)
    finally:
        if connection is not None:
            connection.close()


if __name__ == '__main__':
    # user = input("User name: ")
    # phone = input("Phone number: ")
    # add_user(user, phone)

    # user = input("User name: ")
    # phone = input("Phone number: ")
    # user_id = input("ID: ")
    # update_data(user_id, user, phone)

    # query_data("phone", "404")

    # delete_user("Artem")
    # delete_user("Vasiliy")

    upload_csv("./table.csv")





