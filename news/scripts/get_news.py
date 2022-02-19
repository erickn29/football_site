from scrapp.news_sql import add_article
from scrapp.news_parser import get_parser


def main():
    # Парсим новости со спортс ру
    news_list = get_parser()

    # Добавляем новости в БД
    for cat in news_list:
        for row in cat:
            add_article(row[0], row[1], row[2], row[3])


if __name__ == '__main__':
    main()