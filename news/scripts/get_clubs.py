from scrapp.clubs_sql import add_club_info
from scrapp.clubs_parser import get_clubs_info


def main():
    # Запускаем парсер информации клуба
    club_info = get_clubs_info()

    # Записываем информацию о клубе в БД
    for club in club_info:
        add_club_info(club[0], club[1], club[2], club[3])


if __name__ == '__main__':
    main()