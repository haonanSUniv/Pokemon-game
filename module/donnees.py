# -*- coding: utf-8 -*-
"""
Created on Wed Jan 12 22:09:55 2022

@author: 

Haonan Yuan
Valentin Cointrel
Sonia Slimi

"""

# Dans ce fichier, on importe les donnees dans les fichiers txt qui sont donnees par le sujet
# defense.txt -------- attaque.txt -------- pokemon.txt

# on fait la standardisation et les stocker dans les variables listes pour recuperer plus facilement
# data_defense -------- data_attaque --------- data_pokemon

# on cree les bibliotheques pour stocker toutes ces donnees
# biblioComAttaque -------- biblioComDefense ----------- biblioPokemon


import numpy as np
from module.ComAttaque import ComAttaque
from module.ComDefense import ComDefense
from module.Pokemon import Pokemon

f = np.genfromtxt('defense.txt',dtype=str, delimiter = '\t') # on recupere les donnees dans une matrice en les separant par "\t"
data_defense = []
for i in range(1,len(f)):
    temp = []
    temp.append(f[i][0])
    temp.append(f[i][1])
    temp.append(f[i][2])
    if f[i][3] == '':
        temp.append(f[i][3])
    for j in range(3,5):
        for k in range(len(f[i][j])):
            if f[i][j][k] == "-":
                if len(f[i][j]) == 5:
                    chiffre_1 = int(f[i][j][k-2] + f[i][j][k-1])
                    chiffre_2 = int(f[i][j][k+1] + f[i][j][k+2])
                    temp.append([chiffre_1,chiffre_2])
                elif len(f[i][j]) == 4:
                    chiffre_1 = int(f[i][j][k-1])
                    chiffre_2 = int(f[i][j][k+1] + f[i][j][k+2])
                    temp.append([chiffre_1,chiffre_2])
                if len(f[i][j]) == 6:
                    chiffre_1 = int(f[i][j][k-2] + f[i][j][k-1])
                    chiffre_2 = int(f[i][j][k+1] + f[i][j][k+2] + f[i][j][k+3])
                    temp.append([chiffre_1,chiffre_2])
                elif len(f[i][j]) == 7:
                    chiffre_1 = int(f[i][j][k-3] + f[i][j][k-2] + f[i][j][k-1])
                    chiffre_2 = int(f[i][j][k+1] + f[i][j][k+2] + f[i][j][k+3])
                    temp.append([chiffre_1,chiffre_2])                                         
    if f[i][4] == '':
        temp.append(f[i][4])
    temp.append(int(f[i][5]))
    data_defense.append(temp)    


#importer les competences d'attaque
f = np.genfromtxt('attaque.txt',dtype=str, delimiter = '\t')
data_attaque = []
for i in range(1,len(f)):
    temp = []
    temp.append(f[i][0])
    temp.append(f[i][1])
    temp.append(f[i][2])
    temp.append(int(f[i][3]))
    temp.append(int(f[i][4]))       
    temp.append(int(f[i][5]))
    data_attaque.append(temp)    


# importer les pokemons
f = np.genfromtxt('pokemon.txt',dtype=str, delimiter = '\t')
data_pokemon = []
for i in range(1,len(f)):
    temp = []
    temp.append(f[i][0])
    temp.append(f[i][1])
    temp.append(f[i][2])
    temp.append(f[i][3])
    for j in range(4,9):
        for k in range(len(f[i][j])):
            if f[i][j][k] == "-":
                if len(f[i][j]) == 7:
                    chiffre_1 = int(f[i][j][k-3] + f[i][j][k-2])
                    chiffre_2 = int(f[i][j][k+2] + f[i][j][k+3])
                    temp.append([chiffre_1,chiffre_2])
                elif len(f[i][j]) == 5:
                    chiffre_1 = int(f[i][j][k-2])
                    chiffre_2 = int(f[i][j][k+2])
                    temp.append([chiffre_1,chiffre_2])
                elif len(f[i][j]) == 6:
                    chiffre_1 = int(f[i][j][k-2])
                    chiffre_2 = int(f[i][j][k+2] + f[i][j][k+3])
                    temp.append([chiffre_1,chiffre_2])
                elif len(f[i][j]) == 8:
                    chiffre_1 = int(f[i][j][k-3] + f[i][j][k-2])
                    chiffre_2 = int(f[i][j][k+2] + f[i][j][k+3] + f[i][j][k+4])
                    temp.append([chiffre_1,chiffre_2])
                elif len(f[i][j]) == 9:
                    chiffre_1 = int(f[i][j][k-4] + f[i][j][k-3] + f[i][j][k-2])
                    chiffre_2 = int(f[i][j][k+2] + f[i][j][k+3] + f[i][j][k+4])
                    temp.append([chiffre_1,chiffre_2])      
    temp_string = []
    for k in range(len(f[i][9])):
        a = ''
        if f[i][9][k] == '[':
            p1 = k
        if f[i][9][k] == ',' or f[i][9][k] ==']':
            p2 = k
            for l in range(p1+1,p2):
                a += f[i][9][l]
            temp_string.append(a)
            p1 = p2+1
    temp.append(temp_string)
    data_pokemon.append(temp) 
    
    
biblioComAttaque = []
for i in range(len(data_attaque)):
    biblioComAttaque.append(ComAttaque(data_attaque[i][0], data_attaque[i][1], data_attaque[i][2], data_attaque[i][3], data_attaque[i][4], data_attaque[i][5]))

biblioComDefense = []
for i in range(len(data_defense)):
    biblioComDefense.append(ComDefense(data_defense[i][0], data_defense[i][1], data_defense[i][2], data_defense[i][3], data_defense[i][4], data_defense[i][5]))

biblioPokemon = []
for i in range(len(data_pokemon)):
    tempCompetences = []
    for j in range(len(data_pokemon[i][9])):
        for k in range(len(biblioComAttaque)):
            if data_pokemon[i][9][j] == biblioComAttaque[k].nom:
                tempCompetences.append(biblioComAttaque[k])
        for l in range(len(biblioComDefense)):
            if data_pokemon[i][9][j] == biblioComDefense[l].nom:
                tempCompetences.append(biblioComDefense[l])   
    biblioPokemon.append(Pokemon(data_pokemon[i][0], data_pokemon[i][3], data_pokemon[i][4][0], 100*data_pokemon[i][4][0], data_pokemon[i][4], data_pokemon[i][5], data_pokemon[i][6], data_pokemon[i][7], data_pokemon[i][8], tempCompetences))
