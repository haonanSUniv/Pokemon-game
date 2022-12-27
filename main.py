# -*- coding: utf-8 -*-
"""
Created on Wed Jan 12 22:09:55 2022

@author: 

Haonan Yuan
Valentin Cointrel
Sonia Slimi

"""

# import

import numpy as np
import os
import time
import sys

sys.path.append(os.path.join(os.path.dirname(__file__) ,"module" ))
from module.Pokemon import Pokemon
from module.dresseur import dresseur
from module.JcJ import JcJ
from module.JcE import JcE
from donnees import biblioComAttaque,biblioComDefense,biblioPokemon,data_pokemon


# In[8]
def tournoi(user):
    # on recupere le repertoire actuel
    chemin = os.getcwd()   
    
#-------------------- s'il n'existe pas un fichier de tournoi pour user actuel, on cree un nouveau tournoi avec des ordinateurs quelconques--------------------------------

    if not os.path.exists(chemin + "/save/biblioJoueur{}.txt".format(user.nom)):     
        # initialiser tous les joueur ordinateurs, il y en a 15
        biblioOrdinateur = []
        for i in range(15):
            temp = []
            R = [np.random.randint(len(data_pokemon)) for m in range(3)]
            for r in R:
                tempCompetences = []
                for j in range(len(data_pokemon[r][9])):
                    for k in range(len(biblioComAttaque)):
                        if data_pokemon[r][9][j] == biblioComAttaque[k].nom:
                            tempCompetences.append(biblioComAttaque[k])
                    for l in range(len(biblioComDefense)):
                        if data_pokemon[r][9][j] == biblioComDefense[l].nom:
                            tempCompetences.append(biblioComDefense[l])
                temp.append(Pokemon(data_pokemon[r][0], data_pokemon[r][3], data_pokemon[r][4][0], 100*data_pokemon[r][4][0], data_pokemon[r][4], data_pokemon[r][5], data_pokemon[r][6], data_pokemon[r][7], data_pokemon[r][8], tempCompetences))    
            biblioOrdinateur.append(dresseur("Ordinateur{}".format(i+1),[temp[0],temp[1],temp[2]],[temp[0],temp[1],temp[2]]))
            
        biblioJoueur = biblioOrdinateur
        biblioJoueur.append(user)
        compte = 0
        
        for i in range(len(biblioJoueur)):
            biblioJoueur[i].sauvegarder()
        editeur = open(chemin + "/save/biblioJoueur{}.txt".format(user.nom),"w")
        for j in biblioJoueur:
            editeur.write(j.nom+'\n')
        editeur.close()

#-----------------------s'il existe deja un fichier de tournoi, on recupere toutes les donnes contenu dans le fichier et continue le tournoi--------------------------------------
        
    else:
        biblioJoueur = []
        fo = open(chemin + "/save/biblioJoueur{}.txt".format(user.nom))
        stokage = fo.readlines()
        fo.close()
        for i in range(len(stokage)-1):
            stokage[i] = stokage[i][0:-1]
        compte = int(stokage[-1])
        
        for m in range(len(stokage)-1):
            fo = open(chemin + "/save/" + stokage[m] + ".txt")
            reader = fo.readlines()
            pokemon_nom_save = []
            pokemon_niveau_save = []
            pokemon_exp_save = []
            pokemons = []
            for i in range(3,len(reader)):
                pokemon_nom_save.append(reader[i].split(' ')[0])
                pokemon_niveau_save.append(reader[i].split(' ')[1])
                pokemon_exp_save.append(reader[i].split(' ')[2])
                tempo = biblioPokemon
                for j in tempo:
                    if j.nom == pokemon_nom_save[i-3]:
                        code1 = pokemon_nom_save.index(j.nom)
                        j.niveau = int(pokemon_niveau_save[code1])
                        j.exp = int(pokemon_exp_save[code1])
                        j.renewLevel()
                        pokemons.append(j)
            deck = []
            for i in range(0,3):
                deck.append(pokemons[pokemon_nom_save.index(reader[i].replace("\n",''))]) 
            biblioJoueur.append(dresseur(stokage[m],pokemons,deck))  
            fo.close()
        print("Les gagnants precedents:")
        for j in range(len(biblioJoueur)):
            print(biblioJoueur[j].nom + '\n')        
        time.sleep(2)
        
#--------------------------------les fonctions principales pour effectuer le tournoi---------------------------------------------------
        
    pause = 'N'
    while len(biblioJoueur) > 1 and pause != 'Y':
        compte += 1 # pour compter le numero du round
        biblioWinner = [] # pour stocker les gagnant a la fin de chaque round
        for i in range(0,len(biblioJoueur),2): # la boucle est avec un pas de 2 parce que on forme un combat avec 2 joueurs
            print("----------- Round {} --------------".format(compte))
            # si le nombre de joueurs est un chiffre impair, le dernier joueur gagne automatiquement le combat et accede au prochain round
            if i == len(biblioJoueur)-1:
                biblioWinner.append(biblioJoueur[i])
            else:
            # le troisieme parametre du constructeur de JcJ est la difficulte. 0 pour ordi vs ordi, 3 pour player vs ordi avec une difficulte difficile
                if biblioJoueur[i].nom == user.nom:
                    combat1 = JcJ(biblioJoueur[i],biblioJoueur[i+1], 3)
                    combat1.combat()
                    biblioWinner.append(combat1.gagnant)
                elif biblioJoueur[i+1].nom == user.nom:
                    combat1 = JcJ(biblioJoueur[i+1],biblioJoueur[i], 3)
                    combat1.combat()
                    biblioWinner.append(combat1.gagnant)
                else:
                    combat1 = JcJ(biblioJoueur[i+1],biblioJoueur[i], 0)
                    combat1.combat()
                    biblioWinner.append(combat1.gagnant)
        biblioJoueur = biblioWinner
        editeur = open(chemin + "/save/biblioJoueur{}.txt".format(user.nom),"w")
        editeur.seek(0)
        editeur.truncate() # Reinitialisation du fichier biblioJoueur.txt
        # A chaque round, on sauvegarde les gagnants ainsi que le numero du round(compte)
        for j in biblioJoueur:
            editeur.write(j.nom+'\n')
        editeur.close()
        editeurCompte = open(chemin + "/save/biblioJoueur{}.txt".format(user.nom),"a")
        editeurCompte.write('{}'.format(compte))
        editeurCompte.close()
        
        # on sauvegarde également a chaque round tous les dresseur avec les informations de leurs pokemons
        for i in range(len(biblioJoueur)):
            biblioJoueur[i].sauvegarder()
        # Affichage des gagnants a la fin de chaque round
        print("Les gagnants de ce round sont: \n")
        for j in range(len(biblioWinner)):
            print(biblioWinner[j].nom + '\n')
        time.sleep(1)
        # si il reste seulement un gagnant, cela veut dire que le tournoi est fini, on affiche le gagnant final et supprime le fichier biblioJoueur
        if len(biblioJoueur) == 1:
            os.remove(chemin + "/save/biblioJoueur{}.txt".format(user.nom))
        else:
            pause = input("Voulez vous mettre en pause le tournoi? (Y/N)")
        # on pourrait mettre en pause le tournoi et le reprendre plus tard avec les fichiers sauvegardes
        
# In[10]
# main fonciton
# On creer deux dresseurs en tant qu'exemple ainsi qu'une bibliotheque des dresseurs pour stocker tous les dresseurs que l'on va creer
Player1 = dresseur("Player1", [biblioPokemon[0],biblioPokemon[1],biblioPokemon[2],biblioPokemon[3]], [biblioPokemon[1],biblioPokemon[2],biblioPokemon[3]])
Player2 = dresseur("Player2", [biblioPokemon[6],biblioPokemon[7],biblioPokemon[8],biblioPokemon[9]], [biblioPokemon[7],biblioPokemon[8],biblioPokemon[9]])
Player1.pokemon[3].experience += 500
Player1.sauvegarder()
Player2.sauvegarder()
bibliothequeDresseur = [Player1,Player2]

#--------------chercher dans le repertoire les dossiers sauvegardes et les recuperer ou creer un nouveau dresseur---------------

chemin = os.getcwd() 
if not os.path.exists(chemin + "/save"):
    os.mkdir(chemin + "/save")
if os.path.exists(chemin + "/save"):
    if not os.listdir(chemin + "/save") == []:     
        print("Ici, vos comptes sauvgardés :")
        for fichier in os.listdir(chemin + "/save/"):
            print (fichier[0:-4])
        while True:
            username = input("Quel est votre nom ?")
            if not os.path.isfile(chemin + "/save/" + username + ".txt"):
            # si on ne trouve pas de fichier avec ce nom, on demande si l'on veut creer un nouveau dresseur ou re-saisir le nom                    
                option = input("\nCe dresseur n'existe pas. Voulez vous creer un nouveau dresseur?(Y/N)\n")
                if option == 'Y':
                # on creer un nouveau dresseur avec 3 pokemons aleatoire et differents si l'option est 'Y'
                    a1 = np.random.randint(0,len(biblioPokemon)-1)
                    a2 = np.random.randint(0,len(biblioPokemon)-1)
                    a3 = np.random.randint(0,len(biblioPokemon)-1)
                    while True:
                        if a1 != a2 and a1 != a3 and a2 != a3:
                            break
                        else:
                            a1 = np.random.randint(0,len(biblioPokemon)-1)
                            a2 = np.random.randint(0,len(biblioPokemon)-1)
                            a3 = np.random.randint(0,len(biblioPokemon)-1)                               
                    pokemon1 = Pokemon(biblioPokemon[a1].nom,biblioPokemon[a1].element,biblioPokemon[a1].niveau,biblioPokemon[a1].experience,biblioPokemon[a1].niveauRange,biblioPokemon[a1].vieRange,biblioPokemon[a1].energieRange,biblioPokemon[a1].regeneRange,biblioPokemon[a1].resistanceRange,biblioPokemon[a1].Competence)
                    pokemon2 = Pokemon(biblioPokemon[a2].nom,biblioPokemon[a2].element,biblioPokemon[a2].niveau,biblioPokemon[a2].experience,biblioPokemon[a2].niveauRange,biblioPokemon[a2].vieRange,biblioPokemon[a2].energieRange,biblioPokemon[a2].regeneRange,biblioPokemon[a2].resistanceRange,biblioPokemon[a2].Competence)
                    pokemon3 = Pokemon(biblioPokemon[a3].nom,biblioPokemon[a3].element,biblioPokemon[a3].niveau,biblioPokemon[a3].experience,biblioPokemon[a3].niveauRange,biblioPokemon[a3].vieRange,biblioPokemon[a3].energieRange,biblioPokemon[a3].regeneRange,biblioPokemon[a3].resistanceRange,biblioPokemon[a3].Competence)
                    bibliothequeDresseur.append(dresseur(username,[pokemon1,pokemon2,pokemon3],[pokemon1,pokemon2,pokemon3]))
                    user = bibliothequeDresseur[-1] 
                    break                                      
            else:
            # si on a trouve un fichier avec ce nom, on recupere les donnees dans le fichier et reconstruit tous les donnees de pokemons
                reader = open(chemin + "/save/" + username + ".txt").readlines()
                pokemon_nom_save = []
                pokemon_niveau_save = []
                pokemon_exp_save = []
                pokemons = []
                for i in range(3,len(reader)):
                    pokemon_nom_save.append(reader[i].split(' ')[0])
                    pokemon_niveau_save.append(reader[i].split(' ')[1])
                    pokemon_exp_save.append(reader[i].split(' ')[2])
                    tempo = biblioPokemon
                    for j in tempo:
                        if j.nom == pokemon_nom_save[i-3]:
                            code1 = pokemon_nom_save.index(j.nom)
                            j.niveau = int(pokemon_niveau_save[code1])
                            j.exp = int(pokemon_exp_save[code1])
                            j.renewLevel()
                            pokemons.append(j)
                deck = []
                for i in range(0,3):
                    deck.append(pokemons[pokemon_nom_save.index(reader[i].replace("\n",''))]) 
                bibliothequeDresseur.append(dresseur(username,pokemons,deck))
                user = bibliothequeDresseur[-1]
                break
    else :
    # s'il existe pas de fichier dans le dossier "save", on est oblige de creer un nouveau dresseur pour jouer au jeu
        print("Dossier vide ! Commencez un nouveau jeu!")
        username = input("Quel est votre nom ?")
        time.sleep(0.5)
        a1 = np.random.randint(0,len(biblioPokemon)-1)
        a2 = np.random.randint(0,len(biblioPokemon)-1)
        a3 = np.random.randint(0,len(biblioPokemon)-1)
        while True:
            if a1 != a2 and a1 != a3 and a2 != a3:
                break
            else:
                a1 = np.random.randint(0,len(biblioPokemon)-1)
                a2 = np.random.randint(0,len(biblioPokemon)-1)
                a3 = np.random.randint(0,len(biblioPokemon)-1)                               
        pokemon1 = Pokemon(biblioPokemon[a1].nom,biblioPokemon[a1].element,biblioPokemon[a1].niveau,biblioPokemon[a1].experience,biblioPokemon[a1].niveauRange,biblioPokemon[a1].vieRange,biblioPokemon[a1].energieRange,biblioPokemon[a1].regeneRange,biblioPokemon[a1].resistanceRange,biblioPokemon[a1].Competence)
        pokemon2 = Pokemon(biblioPokemon[a2].nom,biblioPokemon[a2].element,biblioPokemon[a2].niveau,biblioPokemon[a2].experience,biblioPokemon[a2].niveauRange,biblioPokemon[a2].vieRange,biblioPokemon[a2].energieRange,biblioPokemon[a2].regeneRange,biblioPokemon[a2].resistanceRange,biblioPokemon[a2].Competence)
        pokemon3 = Pokemon(biblioPokemon[a3].nom,biblioPokemon[a3].element,biblioPokemon[a3].niveau,biblioPokemon[a3].experience,biblioPokemon[a3].niveauRange,biblioPokemon[a3].vieRange,biblioPokemon[a3].energieRange,biblioPokemon[a3].regeneRange,biblioPokemon[a3].resistanceRange,biblioPokemon[a3].Competence)
        bibliothequeDresseur.append(dresseur(username,[pokemon1,pokemon2,pokemon3],[pokemon1,pokemon2,pokemon3]))
        user = bibliothequeDresseur[-1] 
else:
    print("Aucun compte sauvgardé ! Ressayez!")
    time.sleep(0.5) 

#----------------------------fin de recherche dans le repertoire-----------------------------



#--------------------------le debut du jeu et la page d'acceuil------------------------------

print("----------------------------Acceuil----------------------------------")    
print("Bienvenue,",username,"!\n"), time.sleep(0.3)
print("Voila votre dresseur: {}: {} Pokemon. Le deck est: \n {}".format(user.nom,len(user.pokemon),user.afficheDeck()))

while True:
    print("1/ Voir vos pokemons \n2/ Changer le deck \n3/ Combattre / Capturer un pokemon \n/4 Combattre contre un autre dresseur \n/5 Creer un nouveau dresseur \n/6 Faire un tournoi \n/7 Quitter")
    choix = input("Que voulez vous faire? (1-7)")
    if choix == "1":
        user.affichePokemon()
    if choix == "2":
        user.changeDeck()
    if choix == "3":
    # un combat JcE avec un pokemon au choix
        for i in range(len(biblioPokemon)):
            print(biblioPokemon[i].nom)
        s = input("Choisissez le pokemon contre lequel vous souhaitez combattre: ")
        for i in range(len(biblioPokemon)):
            if s == biblioPokemon[i].nom:
                guest = Pokemon(biblioPokemon[i].nom,biblioPokemon[i].element,biblioPokemon[i].niveau,biblioPokemon[i].experience,biblioPokemon[i].niveauRange,biblioPokemon[i].vieRange,biblioPokemon[i].energieRange,biblioPokemon[i].regeneRange,biblioPokemon[i].resistanceRange,biblioPokemon[i].Competence)
                Game = JcE(user,guest)
                break
        Game.combat()
    if choix == "4":
    # un combat JcE avec un dresseur au choix
    # on peut choisir Joueur contre Joueur ou Joueur contre Ordinateur
        while True:    
            s = input("Choisissez un dresseur contre lequel vous souhaitez combattre:")
            for i in range(len(bibliothequeDresseur)):
                if s == bibliothequeDresseur[i].nom:
                    guest = bibliothequeDresseur[i]
            if guest == None:
                print("Il existe pas un dresseur avec ce nom")
                continue
            s = input("Choisissez un mode de combat:\n1. Joueur contre Joueur \n2. Joueur contre Ordinateur")
            if s == '1':
                Game = JcJ(user,guest,-1)
                break
            elif s == '2':
                Game = JcJ(user,guest,3)
                break
            else:
                print("input error!")
                continue
        Game.combat()      
    if choix == "5":
    # on cree un nouveau compte soit un nouveau dresseur
        a1 = np.random.randint(0,len(biblioPokemon)-1)
        a2 = np.random.randint(0,len(biblioPokemon)-1)
        a3 = np.random.randint(0,len(biblioPokemon)-1)
        while True:
            if a2 == a1:
                a2 = np.random.randint(0,len(biblioPokemon)-1)
            if a3 == a2:
                a3 = np.random.randint(0,len(biblioPokemon)-1)
            if a3 == a1:
                a3 = np.random.randint(0,len(biblioPokemon)-1)
            if a1 != a2 and a1 != a3 and a2 != a3:
                break         
        pokemon1 = Pokemon(biblioPokemon[a1].nom,biblioPokemon[a1].element,biblioPokemon[a1].niveau,biblioPokemon[a1].experience,biblioPokemon[a1].niveauRange,biblioPokemon[a1].vieRange,biblioPokemon[a1].energieRange,biblioPokemon[a1].regeneRange,biblioPokemon[a1].resistanceRange,biblioPokemon[a1].Competence)
        pokemon2 = Pokemon(biblioPokemon[a2].nom,biblioPokemon[a2].element,biblioPokemon[a2].niveau,biblioPokemon[a2].experience,biblioPokemon[a2].niveauRange,biblioPokemon[a2].vieRange,biblioPokemon[a2].energieRange,biblioPokemon[a2].regeneRange,biblioPokemon[a2].resistanceRange,biblioPokemon[a2].Competence)
        pokemon3 = Pokemon(biblioPokemon[a3].nom,biblioPokemon[a3].element,biblioPokemon[a3].niveau,biblioPokemon[a3].experience,biblioPokemon[a3].niveauRange,biblioPokemon[a3].vieRange,biblioPokemon[a3].energieRange,biblioPokemon[a3].regeneRange,biblioPokemon[a3].resistanceRange,biblioPokemon[a3].Competence)
        nomUser = input("Nom de votre nouveau dresseur? : ")
        bibliothequeDresseur.append(dresseur(nomUser,[pokemon1,pokemon2,pokemon3],[pokemon1,pokemon2,pokemon3]))
        user = bibliothequeDresseur[-1]
        print("Changement de dresseur: Utilisateur actuel: {}".format(user.nom))
    if choix == "6":
    # on participe au tournoi(un nouveau ou un qui a été sauvegarde)
        tournoi(user)
    if choix == "7":
    # on quitte le jeu et sauvegarde les données du dresseur
        user.sauvegarder()
        break