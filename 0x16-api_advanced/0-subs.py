
#!/usr/bin/python3
"""
function that give the number of user iven not active
"""


import requests


def number_of_subscribers(subreddit):
    utlisateur = {
        "User-Agent": "User-Agent"
    }
    URLadress = 'https://www.reddit.com/r/{}/about.json'.format(subreddit)
    request = requests.get(URLadress, headers=utlisateur)
    try:
        return request.json().get('data').get('subscribers')
    except Exception:
	    pass
    return(0)