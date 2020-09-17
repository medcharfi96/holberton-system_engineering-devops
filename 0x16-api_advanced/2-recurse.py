#!/usr/bin/python3
"""
decription for task 3
yezzi mel cheat
lel jmou3 elli 7al lgit mte3i
"""


import requests


def recurse(subreddit, hot_list=[]):
    utlisateur = {
        "User-Agent": "3ezedinmeltelililzaweli"
        }
    nexst = {
        "after": after
        }
    URadres = 'https://www.reddit.com/r/{}/hot.json'.format(subreddit)
    reponse = requests.get(URadres, params=nexst, headers=utlisateur)
    if reponse.status_code != 200:
        print(None)
    try:
        for i in reponse.json().get('data').get('children'):
            hot_list.append(i.get("data").get("title"))
        if after is not None:
            return recurse(subreddit, hot_list, nexst)
        else:
            return hot_list
    except:
        pass
