import random
import time

import requests
from bs4 import BeautifulSoup as bs

# Клубы для сбора данных
clubs_list = {
    ('milan','Милан', 'Россонери'): 'https://www.sports.ru/milan/team/',
    ('juventus', 'Ювентус', 'Юве', 'Бьянконери'): 'https://www.sports.ru/juventus/team/',
    ('inter','Интер'): 'https://www.sports.ru/inter/team/',
    # ('napoli', 'Наполи'): 'https://www.sports.ru/napoli/team/',
    # ('roma', 'Рома'): 'https://www.sports.ru/roma/team/',
    # ('lazio', 'Лацио'): 'https://www.sports.ru/lazio/team/',
    ('manchester-city', 'Манчестер Сити', 'Ман Сити'): 'https://www.sports.ru/manchester-city/team/',
    ('liverpool', 'Ливерпуль'): 'https://www.sports.ru/liverpool/team/',
    ('chelsea', 'Челси'): 'https://www.sports.ru/chelsea/team/',
    ('mu', 'Манчестер Юнайтед', 'МЮ'): 'https://www.sports.ru/mu/team/',
    ('arsenal', 'Арсенал'): 'https://www.sports.ru/arsenal/team/',
    ('real', 'Реал Мадрид', 'Реал'): 'https://www.sports.ru/real/team/',
    ('barcelona', 'Барселона', 'Барса'): 'https://www.sports.ru/barcelona/team/',
    ('atletico', 'Атлетико'): 'https://www.sports.ru/atletico/team/',
    ('bayern', 'Бавария'): 'https://www.sports.ru/bayern/team/',
    ('borussia', 'Боруссия Дортмунд', 'Дортмунд'): 'https://www.sports.ru/borussia/team/',
    ('psg', 'ПСЖ'): 'https://www.sports.ru/psg/team/',
    ('zenit', 'Зенит'): 'https://www.sports.ru/zenit/team/',
    ('spartak', 'Спартак'): 'https://www.sports.ru/spartak/team/',
    ('cska', 'ЦСКА'): 'https://www.sports.ru/cska/team/',
    ('lokomotiv', 'Локомотив', 'Локо'): 'https://www.sports.ru/lokomotiv/team/',

}

HEADERS = {
    'user-agent': 'Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/97.0.4692.99 Safari/537.36',
    'accept-language': 'ru-RU,ru;q=0.9,en-US;q=0.8,en;q=0.7',
    'accept-encoding': 'gzip, deflate, br'
}

clubs_info = []

def get_clubs_info():
    try:
        for club_name, url in clubs_list.items():
            page = requests.request('GET', url, headers=HEADERS).text
            soup = bs(page, 'html.parser')
            table_coach = soup.find('table', class_='profile-table')
            coach = str(table_coach.find_all('td')[1].text.strip().split()[-1])

            image = soup.find('div', class_='img-box')
            img_url = image.img['src']

            table_players = soup.find('table', class_='stat-table sortable-table')
            players = table_players.find_all('tr')
            players_list = []
            for player in players[1:]:
                players_list.append(str(player.find_all('td')[1].text.strip().split()[-1]))
            clubs_info.append([','.join(club_name), coach, ','.join(players_list), img_url])
            print(f'Получил информацию о клубе {club_name}')
            time.sleep(random.randint(3,7))

        return clubs_info
    except requests.exceptions.RequestException as e:
        raise SystemExit(e)
