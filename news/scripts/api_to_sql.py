import sqlite3

def add_tables(country, rank, cname, played, win, draw, lose, goalsDiff, points):
    try:
        sql_connection = sqlite3.connect('Z:\Django\Django\\football\db.sqlite3')
        cursor = sql_connection.cursor()
        print("База данных подключена к SQLite")
        table = 'news_league_tables'
        # Пытаемся найти клуб в базе, да - обновляем, нет - добавляем
        try:
            find_club = """SELECT * FROM news_league_tables WHERE name = ?"""
            cursor.execute(find_club, (cname,))
            result = cursor.fetchall()
            sql_connection.commit()
            cursor.close()
            # Проверяем, есть название клуба в ответе
            try:
                if result[0][3]:
                    cursor = sql_connection.cursor()
                    sqlite_update_query = """UPDATE news_league_tables SET 
                                    rank = ?, played = ?, win = ?, draw = ?, 
                                    lose = ?, goalsDiff = ?, points = ? WHERE name = ?"""
                    data = (rank, played, win, draw, lose, goalsDiff, points, cname)
                    cursor.execute(sqlite_update_query, data)
                    sql_connection.commit()
                    print(f"Запись '{rank}' успешно обновлена ", cursor.rowcount)
                    cursor.close()
            # Если нет, добавляем
            except:
                try:
                    cursor = sql_connection.cursor()
                    sqlite_insert_query = """INSERT INTO news_league_tables
                                            (country, rank, name, played, win, draw, lose, goalsDiff, points)  
                                            VALUES  
                                            (?, ?, ?, ?, ?, ?, ?, ?, ?);"""
                    data = (country, rank, cname, played, win, draw, lose, goalsDiff, points)
                    cursor.execute(sqlite_insert_query, data)
                    sql_connection.commit()
                    print(f"Запись '{rank}' успешно вставлена в таблицу {table} ", cursor.rowcount)
                    cursor.close()
                except sqlite3.Error as error:
                    print(error)
        except sqlite3.Error as error:
                    print(error)
    finally:
        if sql_connection:
            sql_connection.close()
            print("Соединение с SQLite закрыто")


def add_players(club, pname, age, position, appearences, total, assists, rating):
    try:
        sql_connection = sqlite3.connect('Z:\Django\Django\\football\db.sqlite3')
        cursor = sql_connection.cursor()
        print("База данных подключена к SQLite")
        table = 'news_club_players_stats'
        # Пытаемся найти клуб в базе, да - обновляем, нет - добавляем
        try:
            find_club = """SELECT * FROM news_club_players_stats WHERE name = ?"""
            cursor.execute(find_club, (pname,))
            result = cursor.fetchall()
            sql_connection.commit()
            cursor.close()
            # Проверяем, есть название клуба в ответе
            try:
                if result[0][3]:
                    cursor = sql_connection.cursor()
                    sqlite_update_query = """UPDATE news_club_players_stats SET 
                                    club = ?, age = ?, appearences = ?, total = ?, 
                                    assists = ?, rating = ? WHERE name = ?"""
                    data = (club, age, appearences, total, assists, rating, pname)
                    cursor.execute(sqlite_update_query, data)
                    sql_connection.commit()
                    print(f"Запись '{pname}' успешно обновлена ", cursor.rowcount)
                    cursor.close()
            # Если нет, добавляем
            except:
                try:
                    cursor = sql_connection.cursor()
                    sqlite_insert_query = """INSERT INTO news_club_players_stats
                                            (club, name, age, position, appearences, total, assists, rating)  
                                            VALUES  
                                            (?, ?, ?, ?, ?, ?, ?, ?);"""
                    data = (club, pname, age, position, appearences, total, assists, rating)
                    cursor.execute(sqlite_insert_query, data)
                    sql_connection.commit()
                    print(f"Запись '{pname}' успешно вставлена в таблицу {table} ", cursor.rowcount)
                    cursor.close()
                except sqlite3.Error as error:
                    print(error)
        except sqlite3.Error as error:
                    print(error)
    finally:
        if sql_connection:
            sql_connection.close()
            print("Соединение с SQLite закрыто")

data = [
['Manchester City', 'Ederson Moraes', 29, 'Goalkeeper', 24, 0, None, 6.94],
['Manchester City', 'Z. Steffen', 27, 'Goalkeeper', 1, 0, None, 7.3],
['Manchester City', 'Rodri', 26, 'Midfielder', 20, 3, 1, 7.33],
['Manchester City', 'Rúben  dos Santos Gato Alves Dias', 25, 'Defender', 23, 2, 3, 7.18],
['Manchester City', 'Aymeric Laporte', 28, 'Defender', 20, 3, None, 7.21],
['Manchester City', 'B. Mendy', 28, 'Defender', 1, 0, None, 6.2],
['Manchester City', 'J. Stones', 28, 'Defender', 8, 1, None, 7.21],
['Manchester City', 'K. Walker', 32, 'Defender', 15, 0, 2, 7.01],
['Manchester City', 'K. De Bruyne', 31, 'Midfielder', 18, 7, 2, 7.59],
['Manchester City', 'P. Foden', 22, 'Midfielder', 17, 6, 3, 7.33],
['Manchester City', 'İ. Gündoğan', 32, 'Midfielder', 17, 4, 3, 7.36],
['Manchester City', 'Bernardo Silva', 28, 'Midfielder', 24, 7, 1, 7.21],
['Manchester City', 'Fernandinho', 37, 'Midfielder', 13, 1, 1, 6.78],
['Manchester City', 'O. Zinchenko', 26, 'Midfielder', 8, 0, 1, 7.09],
['Manchester City', 'João Cancelo', 28, 'Defender', 23, 1, 5, 7.36],
['Manchester City', 'N. Aké', 27, 'Defender', 9, 1, None, 7.12],
['Manchester City', 'J. Grealish', 27, 'Midfielder', 17, 2, 2, 7.1],
['Manchester City', 'R. Mahrez', 31, 'Attacker', 18, 7, 4, 7.31],
['Manchester City', 'Gabriel Jesus', 25, 'Attacker', 19, 2, 7, 7.06],
['Manchester City', 'R. Sterling', 28, 'Attacker', 21, 10, 1, 7.07],
['Manchester City', 'Ferran Torres García', 22, 'Attacker', 4, 2, 1, 7.25],
['Manchester City', 'C. Palmer', 20, 'Midfielder', 4, 0, None, 6.6],
['Manchester City', 'J. McAtee', 20, 'Midfielder', 2, 0, None, 6.3],
['Manchester City', 'L. Delap', 19, 'Attacker', 1, 0, None, 7.0],
['Manchester City', 'Kayky', 19, 'Attacker', 1, 0, None, 6.2],
['Liverpool', 'Alisson Ramsés Becker', 30, 'Goalkeeper', 22, 0, None, 7.11],
['Liverpool', 'N. Williams', 21, 'Defender', 1, 0, 1, 7.2],
['Liverpool', 'C. Kelleher', 24, 'Goalkeeper', 2, 0, None, 7.1],
['Liverpool', 'Trent Alexander-Arnold', 24, 'Defender', 22, 2, 10, 7.72],
['Liverpool', 'Joe Gomez', 25, 'Defender', 4, 0, None, 6.3],
['Liverpool', 'J. Matip', 31, 'Defender', 19, 0, 1, 7.21], ['Liverpool', 'A. Robertson', 28, 'Defender', 18, 1, 8, 7.36], ['Liverpool', 'V. van Dijk', 31, 'Defender', 22, 2, 1, 7.3], ['Liverpool', 'N. Keïta', 27, 'Midfielder', 12, 2, 1, 7.2], ['Liverpool', 'J. Milner', 36, 'Midfielder', 16, 0, 1, 7.02], ['Liverpool', 'Fabinho', 29, 'Midfielder', 18, 4, 1, 7.06], ['Liverpool', 'Thiago Alcântara', 31, 'Midfielder', 13, 1, 1, 7.02], ['Liverpool', 'I. Konaté', 23, 'Defender', 7, 0, None, 7.03], ['Liverpool', 'Konstantinos Tsimikas', 26, 'Defender', 9, 0, 1, 7.04], ['Liverpool', 'J. Henderson', 32, 'Midfielder', 21, 2, 3, 7.06], ['Liverpool', 'C. Jones', 21, 'Midfielder', 9, 1, 1, 6.78], ['Liverpool', 'A. Oxlade-Chamberlain', 29, 'Midfielder', 16, 2, 1, 6.88], ['Liverpool', 'Roberto Firmino Barbosa de Oliveira', 31, 'Attacker', 15, 4, 3, 6.97], ['Liverpool', 'Sadio Mané', 30, 'Attacker', 21, 8, 1, 7.02], ['Liverpool', 'Divock Okoth Origi', 27, 'Attacker', 3, 2, None, 7.2], ['Liverpool', 'Mohamed Salah Ghaly', 30, 'Attacker', 22, 16, 9, 7.48], ['Liverpool', 'Takumi Minamino', 27, 'Attacker', 9, 2, None, 6.77], ['Liverpool', 'L. Díaz', 25, 'Attacker', 1, 0, None, 6.9], ['Liverpool', 'Diogo Jota', 26, 'Attacker', 23, 12, 1, 7.09], ['Liverpool', 'H. Elliott', 19, 'Midfielder', 5, 0, None, 6.74], ['Liverpool', 'T. Morton', 20, 'Midfielder', 2, 0, None, 6.5], ['Liverpool', 'K. Gordon', 18, 'Attacker', 1, 0, None, 6.0]
]
for player in data:
    add_players(*player)