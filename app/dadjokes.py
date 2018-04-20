import requests


def get_joke():
    url = 'https://icanhazdadjoke.com/'
    headers = {
        'User-Agent': 'https://repl.it/@sophiabrandt/icanhazdadjoke-machine',
        'Accept': 'text/plain',
    }

    resp = requests.get(url, headers=headers)
    resp.raise_for_status()

    return resp.text
