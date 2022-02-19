import sqlite3


def add_club_info(name, coach, players, logo):

    try:
        sql_connection = sqlite3.connect('Z:\Django\Django\\football\db.sqlite3')
        cursor = sql_connection.cursor()
        print("База данных подключена к SQLite")

        table = 'news_club'
        sqlite_insert_query = f"""INSERT INTO {table}
                                    (name, coach, players, logo)  VALUES  
                                    ('{name}', '{coach}', '{players}', '{logo}')"""
        cursor.execute(sqlite_insert_query)
        sql_connection.commit()
        print(f"Запись '{name}' успешно вставлена в таблицу {table} ", cursor.rowcount)
        cursor.close()
    except sqlite3.Error as error:
        print(error)
    finally:
        if (sql_connection):
            sql_connection.close()
            print("Соединение с SQLite закрыто")


def get_club_info():
    try:
        sql_connection = sqlite3.connect('Z:\Django\Django\\football\db.sqlite3')
        cursor = sql_connection.cursor()
        print("База данных подключена к SQLite")

        table = 'news_club'
        sqlite_select_query = f"""SELECT name from {table}"""
        cursor.execute(sqlite_select_query)
        result = cursor.fetchall()
        name = result

        sqlite_select_query = f"""SELECT logo from {table}"""
        cursor.execute(sqlite_select_query)
        result = cursor.fetchall()
        logo = result
        cursor.close()
    except sqlite3.Error as error:
        print(error)
    finally:
        if (sql_connection):
            sql_connection.close()
            info = {n[0].split(',')[0]: [n[0].split(',')[1], l[0]] for n, l in zip(name, logo)}
            print("Соединение с SQLite закрыто")
            return info


def get_club_names():
    try:
        sql_connection = sqlite3.connect('Z:\Django\Django\\football\db.sqlite3')
        cursor = sql_connection.cursor()
        print("База данных подключена к SQLite")

        table = 'news_club'

        sqlite_select_query = f"""SELECT name from {table}"""
        cursor.execute(sqlite_select_query)
        result = cursor.fetchall()
        name = result

        sqlite_select_query = f"""SELECT coach from {table}"""
        cursor.execute(sqlite_select_query)
        result = cursor.fetchall()
        coach = result

        sqlite_select_query = f"""SELECT players from {table}"""
        cursor.execute(sqlite_select_query)
        result = cursor.fetchall()
        players = result

        cursor.close()
    except sqlite3.Error as error:
        print(error)
    finally:
        if (sql_connection):
            sql_connection.close()
            info = [sum([n[0].split(','), list(c), list(p[0].split(','))], []) for n, c, p in zip(name, coach, players)]
            print("Соединение с SQLite закрыто")
            return info
# print(get_club_names())