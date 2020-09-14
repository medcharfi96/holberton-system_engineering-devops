#!/usr/bin/python3
"""
task0
"""


import json
import requests
from sys import argv
if __name__ == '__main__':
    url = "https://jsonplaceholder.typicode.com/users/"
    url102 = "https://jsonplaceholder.typicode.com/todos/"
    employe = int(argv[1])
    user = requests.get(url + "{}".format(int(argv[1])))
    nom = user.json().get('name')
    kraya = requests.get(url102, params={"userId": argv[1]})
    matiere = kraya.json()
    mat_thazet = 0
    mat_gen = 0
    tabledemat = []
    for z in matiere:
        mat_gen += 1
        if z.get('completed'):
            mat_thazet += 1
            tabledemat.append(z.get("title"))
    print('Employee {} is done with tasks({}/{}):'
          .format(nom, mat_thazet, mat_gen))
    print('\n')
    for i in range(0, len(tabledemat)):
        print("\t" + tabledemat[i] + '\n')
