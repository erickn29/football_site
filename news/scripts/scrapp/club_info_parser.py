import requests

API = '3fca42bc01msh17537ec4b1f9b32p16aee0jsn02c6c72ddaae'

headers = {
    'x-rapidapi-host': "api-football-v1.p.rapidapi.com",
    'x-rapidapi-key': API
    }

url = "https://api-football-v1.p.rapidapi.com/v3/players"
querystring = {"team":"489","league":"135","season":"2021","page":"1"}



response = requests.request("GET", url, headers=headers, params=querystring)
print(response.text)