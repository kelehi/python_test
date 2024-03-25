import requests


def script():
    master = requests.get('https://www.youtube.com/')
    print(master.text)
