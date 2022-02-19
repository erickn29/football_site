import random
import time

import requests
from bs4 import BeautifulSoup as bs
from transliterate import slugify
# from news.scripts.scrapp.news_sql import get_titles
# from news.scripts.scrapp.clubs_sql import get_club_names
from .news_sql import get_titles
from .clubs_sql import get_club_names

HEADERS = {
    'user-agent': 'Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/97.0.4692.99 Safari/537.36',
    'accept-language': 'ru-RU,ru;q=0.9,en-US;q=0.8,en;q=0.7',
    'accept-encoding': 'gzip, deflate, br'
}

db_list = get_titles()
parsing_categories = {
    'transfers': 'https://www.sports.ru/football/topnews/'
}

club_names = get_club_names()

no_parse_titles = [
    'Чемпионат Италии',
    'Чемпионат Испании',
    'Чемпионат Англии',
    'Чемпионат Германии',
    'Чемпионат Франции',
    'Чемпионат России',
    'новости утра',
    'другие новости'
]

all_news = []

def get_parser():
    try:
        for key, url in parsing_categories.items():
            page = requests.request('GET', url, headers=HEADERS).text
            news_list = []
            soup = bs(page, 'html.parser')

            for link in soup.find_all('a', class_='short-text'):
                if link.text in db_list:
                    continue
                for t in no_parse_titles:
                    if t in link.text:
                        continue
                news_by_club = set()
                for club in club_names:
                    for name in club:
                        if name in link.text:
                            news_by_club.add(club[0])
                if len(news_by_club) < 1:
                    continue
                try:
                    article_page = requests.request('GET', f'https://www.sports.ru{link.get("href")}', headers=HEADERS).text
                except:
                    print('Connection error')
                    break
                soup_text = bs(article_page, 'html.parser')
                news_title = link.text
                news_slug = slugify(link.text.split('.')[0])
                news_donor = link.get('href')
                news_text = soup_text.find('div', class_='news-item__content').text.replace('\'', '')
                
                news_list.append([','.join(news_by_club), news_title, news_text, news_slug, news_donor])
                news_by_club.clear()
                time.sleep(random.randint(1, 3))
                print(f'Нашел {news_title}')
            all_news.append(news_list)
        return all_news
    except requests.exceptions.RequestException as e:
        raise SystemExit(e)
