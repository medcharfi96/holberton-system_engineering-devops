#!/usr/bin/python3
"""
Api to print the 10 most  hot
"""


import requests


def top_ten(subreddit):
    utlisateur = {
        "User-Agent": "3ezedinmeltelililzaweli"
        }
    URadres = 'https://www.reddit.com/r/{}/hot.json?limit=10'.format(subreddit)
    reponse = requests.get(URadres, headers=utlisateur)
    if reponse.status_code != 200:
        print(None)
    try:
        for i in reponse.json().get('data').get('children'):
            print(i.get('data').get('title'))
    except:
        pass
