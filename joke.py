import requests


def get_joke(category, flags):
    url = f'https://v2.jokeapi.dev/joke/{category}'
    params = {'blacklistFlags': flags}
    response = requests.get(url, params=params)
    if response.status_code == 200:
        joke_data = response.json()
        if 'type' in joke_data:
            if joke_data['type'] == 'single':
                return joke_data['joke']
            else:
                return f"{joke_data['setup']} - {joke_data['delivery']}"
        else:
            return "No joke found."

# print(get_joke('Programming', 'nsfw,religious'))

def search_jokes(term):
    url = 'https://v2.jokeapi.dev/joke/Any'
    params = {'contains': term}
    response = requests.get(url, params=params)
    if response.status_code == 200:
        joke_data = response.json()
        if 'type' in joke_data:
            if joke_data['type'] == 'single':
                return joke_data['joke']
            else:
                return f"{joke_data['setup']} - {joke_data['delivery']}"
        else:
            return "No joke found."

# print(search_jokes('bar'))