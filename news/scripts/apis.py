import requests
import time

API = '3fca42bc01msh17537ec4b1f9b32p16aee0jsn02c6c72ddaae'
LEAGUES = {
    'Premier League EN': 39,
    'Premier League RU': 235,
    # 'Ligue 1 FR': 61,
    # 'La Liga ES': 140,
    # 'Bundesliga 1 DE': 78,
    # 'Serie A IT': 135
}

CLUBS = {
    'Manchester City': 50,
    'Liverpool': 40,
    'Chelsea': 49,
    'Manchester United': 33,
    'Arsenal': 42,
    'Zenit': 596,
    'CSKA': 555,
    'Lokomotiv': 597,
    'Spartak': 558,
    'PSG': 85,
    'Real Madrid': 541,
    'Barcelona': 529,
    'Atletico': 530,
    'Bayern': 157,
    'Borussia Dortmund': 165,
    'Milan': 489,
    'Inter': 505,
    'Juventus': 496
}


def get_league_table(*args):
    ids = list(*args)
    data = []

    for id in ids:
        url = "https://api-football-v1.p.rapidapi.com/v3/standings"
        querystring = {"season": "2021", "league": f"{id}"}
        headers = {
            'x-rapidapi-host': "api-football-v1.p.rapidapi.com",
            'x-rapidapi-key': API
        }

        response = requests.request("GET", url, headers=headers, params=querystring).json()

        for ind in range(len(response['response'][0]['league']['standings'][0])):
            data.append([
                response['response'][0]['league']['country'],
                int(response['response'][0]['league']['standings'][0][ind]['rank']),
                response['response'][0]['league']['standings'][0][ind]['team']['name'],
                int(response['response'][0]['league']['standings'][0][ind]['all']['played']),
                int(response['response'][0]['league']['standings'][0][ind]['all']['win']),
                int(response['response'][0]['league']['standings'][0][ind]['all']['draw']),
                int(response['response'][0]['league']['standings'][0][ind]['all']['lose']),
                response['response'][0]['league']['standings'][0][ind]['goalsDiff'],
                int(response['response'][0]['league']['standings'][0][ind]['points'])
            ])
        time.sleep(3)
    return data

def get_club_stands(*args):
    ids = list(*args)
    data = []

    for id in ids:
        url = "https://api-football-v1.p.rapidapi.com/v3/players"
        querystring = {"team": f"{id}", "season": "2021"}
        headers = {
            'x-rapidapi-host': "api-football-v1.p.rapidapi.com",
            'x-rapidapi-key': "3fca42bc01msh17537ec4b1f9b32p16aee0jsn02c6c72ddaae"
        }

        response = requests.request("GET", url, headers=headers, params=querystring).json()
        pages = response['paging']['total']

        # Обработка первой страницы
        for i in range(len(response['response'])):
            if response['response'][i]['statistics'][0]['games']['rating']:
                data.append([
                    response['response'][i]['statistics'][0]['team']['name'],
                    response['response'][i]['player']['name'],
                    response['response'][i]['player']['age'],
                    response['response'][i]['statistics'][0]['games']['position'],
                    response['response'][i]['statistics'][0]['games']['appearences'],
                    response['response'][i]['statistics'][0]['goals']['total'],
                    response['response'][i]['statistics'][0]['goals']['assists'],
                    round(float(response['response'][i]['statistics'][0]['games']['rating']), 2)
                ])
            print(f"Get {response['response'][i]['statistics'][0]['team']['name']}")
        time.sleep(3)
        # Обработка остальных страниц
        for i in range(2, pages + 1):
            querystring = {"team": f"{id}", "season": "2021", "page":f"{i}"}
            response = requests.request("GET", url, headers=headers, params=querystring).json()
            for i in range(len(response['response'])):
                if response['response'][i]['statistics'][0]['games']['rating']:
                    data.append([
                        response['response'][i]['statistics'][0]['team']['name'],
                        response['response'][i]['player']['name'],
                        response['response'][i]['player']['age'],
                        response['response'][i]['statistics'][0]['games']['position'],
                        response['response'][i]['statistics'][0]['games']['appearences'],
                        response['response'][i]['statistics'][0]['goals']['total'],
                        response['response'][i]['statistics'][0]['goals']['assists'],
                        round(float(response['response'][i]['statistics'][0]['games']['rating']), 2)
                    ])
            print(f"Get {response['response'][i]['statistics'][0]['team']['name']}")
            time.sleep(3)
    return data

# print(get_league_table(LEAGUES.values()))