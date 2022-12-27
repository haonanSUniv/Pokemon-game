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
from module.ComAttaque import ComAttaque
from module.ComDefense import ComDefense
from donnees import biblioComAttaque,biblioComDefense,data_pokemon
# In[6]
class JcJ:
    def __init__(self,dresseur1,dresseur2,difficulte):
        self.__dresseur1 = dresseur1
        self.__dresseur2 = dresseur2
        self.__difficulte = difficulte
        
    @property
    def dresseur1(self):
        return self.__dresseur1
    @dresseur1.setter
    def dresseur1(self,dresseur1):
        self.__dresseur1 = dresseur1 
        
    @property
    def dresseur2(self):
        return self.__dresseur2
    @dresseur2.setter
    def dresseur2(self,dresseur2):
        self.__dresseur2 = dresseur2 
        
    @property
    def difficulte(self):
        return self.__difficulte
    @difficulte.setter
    def difficulte(self,difficulte):
        self.__difficulte = difficulte        
        
    def __utilCompetence(self,competence,pokemonAssaillant,pokemonAssailli):
        if pokemonAssaillant.energie < competence.cout:
            return        
        pokemonAssaillant.energie -= competence.cout
        if isinstance(competence,ComAttaque):
            degat = competence.utilCompetence(pokemonAssaillant,pokemonAssailli)
            pokemonAssailli.vie -= degat
            if degat == 0:
                print("attaque echoue...")
            else:
                print("attaque reussi({}): {} degats\n".format(competence.nom,degat))
        elif isinstance(competence,ComDefense):
            competence.utilCompetence(pokemonAssaillant)
            if competence.valeurEnergie == '':
                print("soin reussi({})".format(competence.nom))
            else:
                print("regeneration d'energie reussi({})".format(competence.nom))
                
    def __changePokemon(self,dresseurActive,Pokemon):
        if dresseurActive == self.__dresseur1:
            self.__pokemonActive1 = Pokemon
        else:
            self.__pokemonActive2 = Pokemon
        
    def __forfait(self,dresseur):
        print("{} a perdu le combat!".format(dresseur.nom))
        
    def __reglement(self):
        print("{} a gagne le combat!".format(self.gagnant.nom))
        niveauMoyen = (self.perdant.deck[0].niveau + self.perdant.deck[1].niveau + self.perdant.deck[2].niveau)/3
        self.gagnant.deck[0].experience += round(10 + niveauMoyen - self.gagnant.deck[0].niveau)
        print("{} a gagne {} experiences".format(self.gagnant.deck[0].nom,10 + niveauMoyen - self.gagnant.deck[0].niveau))
        if self.gagnant.deck[0].experience >= 100*(self.gagnant.deck[0].niveau + 1):
            self.gagnant.deck[0].niveau += 1
        self.gagnant.deck[1].experience += round(10 + niveauMoyen - self.gagnant.deck[1].niveau)
        print("{} a gagne {} experiences".format(self.gagnant.deck[1].nom,10 + niveauMoyen - self.gagnant.deck[1].niveau))
        if self.gagnant.deck[1].experience >= 100*(self.gagnant.deck[1].niveau + 1):
            self.gagnant.deck[1].niveau += 1
        self.gagnant.deck[2].experience += round(10 + niveauMoyen - self.gagnant.deck[2].niveau)
        print("{} a gagne {} experiences".format(self.gagnant.deck[2].nom,10 + niveauMoyen - self.gagnant.deck[2].niveau))
        if self.gagnant.deck[2].experience >= 100*(self.gagnant.deck[2].niveau + 1):
            self.gagnant.deck[2].niveau += 1
        self.__evolution()    

#-------------------------la partie d'evolution des pokemons-------------------------------------
    
    def __evolution(self):
        #on stocke le nom des pokemons dans un tableau
        name_list = [g[0] for g in data_pokemon]
        for h in [0,1,2]:
            #pour chaque pokemon du deck du gagnant on relève son indice dans le tableau
            ind = name_list.index(self.gagnant.deck[h].nom)
            #si le pokemon gagnant que l'on considère dispose d'une evolution (dans le fichier data_pokemon fourni)
            #alors on regarde si son niveau actuelle (le niveau apres avoir gagné l'experience du combat car on appelle la fonction evolution apres le gain d'XP)
            #est supérieure au niveau que doit avoir son Pokemon pour evoluer
            #si c'est le cas on regarde le nom de son evolution
            #on recupere dans le fichier data les données du Pokemon correspondant à son evolution
            #On remplace alors toutes les données de notre Pokemon considéré (nom,XP,element,niveau,competence,...)
            #par les données de son Evolution (On a donc remplacé notre Pokemon par son Evolution)
            if data_pokemon[ind][2] != "":
                if (self.gagnant.deck[h].niveau > data_pokemon[ind][4][1]):
                    evol_name = data_pokemon[ind][2]
                    evol_ind = name_list.index(evol_name)
                    comp=[]
                    for j in range(len(data_pokemon[evol_ind][9])):
                        for k in range(len(biblioComAttaque)):
                            if data_pokemon[evol_ind][9][j] == biblioComAttaque[k].nom:
                                comp.append(biblioComAttaque[k])
                        for l in range(len(biblioComDefense)):
                            if data_pokemon[evol_ind][9][j] == biblioComDefense[l].nom:
                                comp.append(biblioComDefense[l])   
                    
                    self.gagnant.deck[h].nom = data_pokemon[evol_ind][0]
                    self.gagnant.deck[h].element = data_pokemon[evol_ind][3]
                    self.gagnant.deck[h].niveau = data_pokemon[evol_ind][4][0]
                    self.gagnant.deck[h].experience = 100*data_pokemon[evol_ind][4][0]
                    self.gagnant.deck[h].niveauRange = data_pokemon[evol_ind][4]
                    self.gagnant.deck[h].vieRange = data_pokemon[evol_ind][5]
                    self.gagnant.deck[h].energieRange = data_pokemon[evol_ind][6]
                    self.gagnant.deck[h].regeneRange = data_pokemon[evol_ind][7]
                    self.gagnant.deck[h].resistanceRange = data_pokemon[evol_ind][8]
                    self.gagnant.deck[h].Competence = comp    
          
                      
    
    def __reinitialisation(self):
        self.gagnant.deck[0].vie = self.gagnant.deck[0].vieMax
        self.gagnant.deck[1].vie = self.gagnant.deck[1].vieMax
        self.gagnant.deck[2].vie = self.gagnant.deck[2].vieMax
        self.perdant.deck[0].vie = self.perdant.deck[0].vieMax
        self.perdant.deck[1].vie = self.perdant.deck[1].vieMax
        self.perdant.deck[2].vie = self.perdant.deck[2].vieMax
        self.gagnant.deck[0].energie = self.gagnant.deck[0].energieMax
        self.gagnant.deck[1].energie = self.gagnant.deck[1].energieMax
        self.gagnant.deck[2].energie = self.gagnant.deck[2].energieMax
        self.perdant.deck[0].energie = self.perdant.deck[0].energieMax
        self.perdant.deck[1].energie = self.perdant.deck[1].energieMax
        self.perdant.deck[2].energie = self.perdant.deck[2].energieMax  
    
    # IA de l'ordinateur de difficulte allant de 1(facile) a 3(difficile)    
    def __AI(self,pokemonAssaillant,pokemonAssailli):
        if self.difficulte == 1: 
            while True:
                if int(pokemonAssaillant.vie) <= 0:
                    for i in range(len(self.__dresseur2.deck)):
                        if self.__dresseur2.deck[i].vie > 0:
                            self.__changePokemon(self.__dresseur2, self.__dresseur2.deck[i])
                            break
                    break 
                # IA utilise une competence quelconque
                rand = np.random.randint(0,len(pokemonAssaillant.Competence)-1)
                self.__utilCompetence(pokemonAssaillant.Competence[rand], pokemonAssaillant, pokemonAssailli)
                break
        
        
        if self.__difficulte == 2:
            while True:
                if int(pokemonAssaillant.vie) <= 0:
                    for i in range(len(self.__dresseur2.deck)):
                        if self.__dresseur2.deck[i].vie > 0:
                            self.__changePokemon(self.__dresseur2, self.__dresseur2.deck[i])
                            break
                    break
                
                if pokemonAssaillant.vie < 0.2*pokemonAssaillant.vieMax:
                    reussi = False
                    for i in range(len(pokemonAssaillant.Competence)):
                        if isinstance(pokemonAssaillant.Competence[i],ComDefense):
                            if pokemonAssaillant.Competence[i].valeurSoin != '':
                                self.__utilCompetence(pokemonAssaillant.Competence[i], pokemonAssaillant, pokemonAssailli)
                                print("soin reussi({})".format(pokemonAssaillant.Competence[i].nom))
                                reussi = True
                    if reussi == True:
                        break
                if pokemonAssaillant.energie < 0.2*pokemonAssaillant.energieMax:
                    for i in range(len(pokemonAssaillant.Competence)):
                        if isinstance(pokemonAssaillant.Competence[i],ComDefense):
                            if pokemonAssaillant.Competence[i].valeurEnergie != '':
                                self.__utilCompetence(pokemonAssaillant.Competence[i], pokemonAssaillant, pokemonAssailli)
                                print("regeneration d'energie reussi({})".format(pokemonAssaillant.Competence[i].nom))
                    break
                
                tableau = []
                for i in range(len(pokemonAssaillant.Competence)):
                    if isinstance(pokemonAssaillant.Competence[i],ComAttaque):
                        # IA cherche la competence qui cause le plus de dégats
                        degat = pokemonAssaillant.Competence[i].utilCompetence(pokemonAssaillant,pokemonAssailli)
                        position = i
                        tableau.append([degat,position])
                maximum = 0
                tag = 0
                for i in range(len(tableau)):
                    if tableau[i][0] > maximum:
                        maximum = tableau[i][0]
                        tag = tableau[i][1]
                self.__utilCompetence(pokemonAssaillant.Competence[tag], pokemonAssaillant, pokemonAssailli)
                break
            
        if self.__difficulte == 3 or self.__difficulte == 0:
            while True:
                if int(pokemonAssaillant.vie) <= 0:
                    for i in range(len(self.__dresseur2.deck)):
                        if self.__dresseur2.deck[i].vie > 0:
                            self.__changePokemon(self.__dresseur2, self.__dresseur2.deck[i])
                            break
                    break
                
                if pokemonAssaillant.vie < 0.4*pokemonAssaillant.vieMax:
                    reussi = False
                    for i in range(len(pokemonAssaillant.Competence)):
                        if isinstance(pokemonAssaillant.Competence[i],ComDefense):
                            if pokemonAssaillant.Competence[i].valeurSoin != '':
                                self.__utilCompetence(pokemonAssaillant.Competence[i], pokemonAssaillant, pokemonAssailli)
                                print("soin reussi({})".format(pokemonAssaillant.Competence[i].nom))
                                reussi = True
                    if reussi == True:
                        break
                if pokemonAssaillant.energie < 0.3*pokemonAssaillant.energieMax:
                    for i in range(len(pokemonAssaillant.Competence)):
                        if isinstance(pokemonAssaillant.Competence[i],ComDefense):
                            if pokemonAssaillant.Competence[i].valeurEnergie != '':
                                self.__utilCompetence(pokemonAssaillant.Competence[i], pokemonAssaillant, pokemonAssailli)
                                print("regeneration d'energie reussi({})".format(pokemonAssaillant.Competence[i].nom))
                    break
                
                tableau = []
                for i in range(len(pokemonAssaillant.Competence)):
                    if isinstance(pokemonAssaillant.Competence[i],ComAttaque):
                        degat = pokemonAssaillant.Competence[i].utilCompetence(pokemonAssaillant,pokemonAssailli)
                        # IA calcul le score pour trouver une competence la plus favorable
                        score = degat * (pokemonAssaillant.Competence[i].precision/100)
                        position = i
                        tableau.append([score,position])
                maximum = 0
                tag = 0
                for i in range(len(tableau)):
                    if tableau[i][0] > maximum:
                        maximum = tableau[i][0]
                        tag = tableau[i][1]
                self.__utilCompetence(pokemonAssaillant.Competence[tag], pokemonAssaillant, pokemonAssailli)
                break

                    
    def combat(self):
        #debut du combat
        if self.__difficulte == 0 :
            self.__dresseur1.afficheDeck()
            self.__pokemonActive1 = self.__dresseur1.deck[0]            
        else:
            print("Combat JcJ entre {} et {}!".format(self.__dresseur1.nom,self.__dresseur2.nom))
            self.__dresseur1.afficheDeck()
            s = input("Quel pokemon voulez vous utiliser? (1-3):")
            if s == "1":
                self.__pokemonActive1 = self.__dresseur1.deck[0]
            elif s == "2":
                self.__pokemonActive1 = self.__dresseur1.deck[1]
            elif s == "3":
                self.__pokemonActive1 = self.__dresseur1.deck[2]
            else:
                print("input error!")
        self.__dresseur2.afficheDeck()
        self.__pokemonActive2 = self.__dresseur2.deck[0]
        

        # tour par tour
        tourMax = 100
        for i in range(tourMax):
            if i%2 == 0:
                pokemonAssaillant = self.__pokemonActive1
                pokemonAssailli = self.__pokemonActive2
                dresseurActive = self.__dresseur1
            else:
                pokemonAssaillant = self.__pokemonActive2
                pokemonAssailli = self.__pokemonActive1
                dresseurActive = self.__dresseur2
            
            # derterminer si le pokemon a été mis KO. Si oui, changer le pokemon avec un autre présent dans le deck. Si tous les pokemons du deck sont ko. Combat terminé.      
            if int(pokemonAssaillant.vie) <= 0:
                print("Votre Pokemon a ete mis KO")
                print(pokemonAssaillant,"\n")
                if dresseurActive.deck[0].vie <= 0 and dresseurActive.deck[1].vie <= 0 and dresseurActive.deck[2].vie <= 0 :
                    if i%2 == 0:
                        self.gagnant = self.__dresseur2
                        self.perdant = self.__dresseur1
                    else:
                        self.gagnant = self.__dresseur1
                        self.perdant = self.__dresseur2
                    break
                
                # Si c'est le tour de joueur
                if (i%2 == 0 and self.__difficulte != 0) or self.__difficulte == -1:
                    ko = True
                    while ko:
                        print("Changement de Pokemon \n1: {} \n2: {} \n3: {}".format(dresseurActive.deck[0].nom,dresseurActive.deck[1].nom,dresseurActive.deck[2].nom))
                        choix = input("Lequel voulez vous choisir? (1-3): ")
                        if choix == "1":    
                            self.__changePokemon(dresseurActive,dresseurActive.deck[0])
                        elif choix == "2":
                            self.__changePokemon(dresseurActive,dresseurActive.deck[1])
                        elif choix == "3":
                            self.__changePokemon(dresseurActive,dresseurActive.deck[2])
                        else:
                            print("Veuillez choisir un chiffre entre 1 et 3")
                            ko = True
                        if i%2 == 0:
                            pokemonAssaillant = self.__pokemonActive1
                            pokemonAssailli = self.__pokemonActive2
                            dresseurActive = self.__dresseur1
                        else:
                            pokemonAssaillant = self.__pokemonActive2
                            pokemonAssailli = self.__pokemonActive1
                            dresseurActive = self.__dresseur2        
                        if pokemonAssaillant.vie <= 0:
                            ko = True
                            print("Vous ne pouvez pas choisir un Pokemon dont la vie est inferieur a 0")
                        else:
                            ko = False
                else:
                    self.__AI(pokemonAssaillant,pokemonAssailli)
                    if i%2 == 0:
                        pokemonAssaillant = self.__pokemonActive1
                    else:    
                        pokemonAssaillant = self.__pokemonActive2

            pokemonAssaillant.energie += pokemonAssaillant.regeEnergie
            if pokemonAssaillant.energie > pokemonAssaillant.energieMax:
                pokemonAssaillant.energie = pokemonAssaillant.energieMax
            print("Tour {}".format(i+1))
            print("c'est a {} de jouer".format(dresseurActive.nom))
            print(pokemonAssaillant,"\n")
            
            if (i%2 == 0 and self.__difficulte != 0) or self.__difficulte == -1:
                print("1: Choisissez une competence de votre Pokemon \n2: Changement de Pokemon avec un autre present dans le Deck \n3: Declarer forfait")
                decision = input("Vous voulez faire? (1-3):")
                if decision == "1":
                    for i in range(len(pokemonAssaillant.Competence)):
                        print("{}: {}".format(i+1,pokemonAssaillant.Competence[i]))
                    numCompetence = int(input("Que voulez vous faire?(1-{})".format(len(pokemonAssaillant.Competence))))
                    if numCompetence > len(pokemonAssaillant.Competence):
                        print("input error!")
                    else:
                        self.__utilCompetence(pokemonAssaillant.Competence[numCompetence-1],pokemonAssaillant,pokemonAssailli)
                elif decision == "2":
                    print("Changement de Pokemon \n1: {} \n2: {} \n3: {}".format(dresseurActive.deck[0].nom,dresseurActive.deck[1].nom,dresseurActive.deck[2].nom))
                    while True:    
                        choix = input("Lequel voulez vous choisir? (1-3): ")
                        if choix == "1":    
                            self.__changePokemon(dresseurActive,dresseurActive.deck[0])
                            break
                        elif choix == "2":
                            self.__changePokemon(dresseurActive,dresseurActive.deck[1])
                            break
                        elif choix == "3":
                            self.__changePokemon(dresseurActive,dresseurActive.deck[2])
                            break
                        else:
                            print("input error!")                
                elif decision == "3":
                    self.__forfait(dresseurActive)
                    if i%2 == 0:
                        self.gagnant = self.__dresseur2
                        self.perdant = self.__dresseur1
                    else:
                        self.gagnant = self.__dresseur1
                        self.perdant = self.__dresseur2     
                    break
                else:
                    print("input error!")
                    i -= 1
                    pokemonAssaillant.energie -= pokemonAssaillant.regeEnergie
            
            # si c'est le tour de l'ordinateur. On donne la decision avec l'IA de l'ordinateur        
            else:
                self.__AI(pokemonAssaillant,pokemonAssailli)
                
                
            # si le combat n'est pas fini apres un certain nombre de tours, le pokemon avec une vie superieure gagne le combat.    
            if i == tourMax-1: # quang i = 99 donc (i%2 != 0)
                if pokemonAssaillant.vie >= pokemonAssailli.vie:
                    self.gagnant = self.__dresseur2
                    self.perdant = self.__dresseur1
                elif pokemonAssaillant.vie < pokemonAssailli.vie:
                    self.gagnant = self.__dresseur1
                    self.perdant = self.__dresseur2      
        
        # on calcul les experiences gagnés par les pokemons du dresseur ayant gagné
        self.__reglement()
        # avant de sortir du combat, on remets la vie et l'energie de tous les pokemons a leur etat maximum
        self.__reinitialisation()                    
                    