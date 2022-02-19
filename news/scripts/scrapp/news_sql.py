import datetime
import sqlite3

def get_titles():
    try:
        sql_connection = sqlite3.connect('Z:\Django\Django\\football\db.sqlite3')
        cursor = sql_connection.cursor()
        print("База данных подключена к SQLite")

        table = 'news_news'
        sqlite_select_query = f"""SELECT title from {table}"""
        cursor.execute(sqlite_select_query)
        result = cursor.fetchall()
        titles = [i[0] for i in result]
        cursor.close()
    except sqlite3.Error as error:
        print(error)
    finally:
        if (sql_connection):
            sql_connection.close()
            print("Соединение с SQLite закрыто")
            return titles


def add_article(club, title, content, url):
    try:
        sql_connection = sqlite3.connect('Z:\Django\Django\\football\db.sqlite3')
        cursor = sql_connection.cursor()
        print("База данных подключена к SQLite")

        table = 'news_news'
        sqlite_insert_query = f"""INSERT INTO {table}
                                  (club, title, content, url, date)  VALUES  
                                  ('{club}', '{title}', '{content}', '{url}', '{datetime.datetime.now()}')"""

        cursor.execute(sqlite_insert_query)
        sql_connection.commit()
        print(f"Запись '{title}' успешно вставлена в таблицу {table} ", cursor.rowcount)
        cursor.close()
    except sqlite3.Error as error:
        print(error)
    finally:
        if (sql_connection):
            sql_connection.close()
            print("Соединение с SQLite закрыто")
