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
    usnom = user.json().get('username')
    kraya = requests.get(url102, params={"userId": argv[1]})
    matiere = kraya.json()
    mat_thazet = 0
    mat_gen = 0
    tabledemat = []
    tabledemat_2 = []
    for z in matiere:
        mini_cel = {}
        mat_gen += 1
        mini_cel['task'] = z.get("title")
        mini_cel['completed'] = z.get("completed")
        mini_cel['username'] = usnom
        tabledemat_2.append(mini_cel)
        if z.get('completed'):
            mat_thazet += 1
            tabledemat.append(z.get("title"))
    print('Employee {} is done with tasks({}/{}):'
          .format(nom, mat_thazet, mat_gen))
    for i in range(0, len(tabledemat)):
        print("\t " + tabledemat[i])
    nom_fichier = str(argv[1]) + '.json'
    mini_cel = {}
    mini_cel[int(argv[1])] = tabledemat_2
    with open(nom_fichier, 'w') as ligne:
        json.dump(mini_cel, ligne)
