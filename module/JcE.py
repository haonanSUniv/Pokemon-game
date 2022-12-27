# -*- coding: utf-8 -*-
"""
Created on Wed Jan 12 22:09:55 2022

@author: 

Haonan Yuan
Valentin Cointrel
Sonia Slimi

"""

# import
from donnees import biblioComAttaque,biblioComDefense,data_pokemon
import numpy as np
from module.ComAttaque import ComAttaque
from module.ComDefense import ComDefense
# In[7]
class JcE:
    # les methodes sont similaires a la classe JcJ
    def __init__(self,dresseur,pokemon):
        self.__dresseur = dresseur
        self.__pokemon = pokemon

        
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
            print("soin reussi({})".format(competence.nom))
    def __changePokemon(self,dresseurActive,Pokemon):
            self.__pokemonActive1 = Pokemon
        
    def __forfait(self,dresseur):
        print("{} a perdu le combat!".format(dresseur.nom))
    
    # la methode pour capturer le pokemon
    def __capturer(self):
        if self.__pokemon.vie < 0.2*self.__pokemon.vieMax:
            probability = 4 * (0.2 - self.__pokemon.vie / self.__pokemon.vieMax)
            tirage = np.random.random()
            if tirage <= probability:
                return True
            else:
                return False

#-------------------------------la partie d'evolution des pokemons----------------------------------------------

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
                      
    def __reglement(self):
        print("{} a gagne le combat!".format(self.gagnant.nom))
        if self.gagnant == self.__dresseur:
            niveauMoyen = self.perdant.niveau
            self.gagnant.deck[0].experience += 10 + niveauMoyen - self.gagnant.deck[0].niveau
            print("{} a gagne {} experiences".format(self.gagnant.deck[0].nom,10 + niveauMoyen - self.gagnant.deck[0].niveau))
            if self.gagnant.deck[0].experience >= 100*(self.gagnant.deck[0].niveau + 1):
                self.gagnant.deck[0].niveau += 1
            self.gagnant.deck[1].experience += 10 + niveauMoyen - self.gagnant.deck[1].niveau
            print("{} a gagne {} experiences".format(self.gagnant.deck[1].nom,10 + niveauMoyen - self.gagnant.deck[1].niveau))
            if self.gagnant.deck[1].experience >= 100*(self.gagnant.deck[1].niveau + 1):
                self.gagnant.deck[1].niveau += 1
            self.gagnant.deck[2].experience += 10 + niveauMoyen - self.gagnant.deck[2].niveau
            print("{} a gagne {} experiences".format(self.gagnant.deck[2].nom,10 + niveauMoyen - self.gagnant.deck[2].niveau))
            if self.gagnant.deck[2].experience >= 100*(self.gagnant.deck[2].niveau + 1):
                self.gagnant.deck[2].niveau += 1
            self.__evolution()
            
    def __reinitialisation(self):
        self.__dresseur.deck[0].vie = self.__dresseur.deck[0].vieMax
        self.__dresseur.deck[1].vie = self.__dresseur.deck[1].vieMax
        self.__dresseur.deck[2].vie = self.__dresseur.deck[2].vieMax
        self.__pokemon.vie = self.__pokemon.vieMax

        self.__dresseur.deck[0].energie = self.__dresseur.deck[0].energieMax
        self.__dresseur.deck[1].energie = self.__dresseur.deck[1].energieMax
        self.__dresseur.deck[2].energie = self.__dresseur.deck[2].energieMax
        self.__pokemon.energie = self.__pokemon.energieMax


    def combat(self):
        #debut du combat
        print("Combat JcJ entre {} et {}!".format(self.__dresseur.nom,self.__pokemon.nom))
        self.__dresseur.afficheDeck()
        while True:
            s = input("Quel pokemon voulez vous utiliser? (1-3):")
            if s == "1":
                self.__pokemonActive1 = self.__dresseur.deck[0]
                break
            elif s == "2":
                self.__pokemonActive1 = self.__dresseur.deck[1]
                break
            elif s == "3":
                self.__pokemonActive1 = self.__dresseur.deck[2]
                break
            else:
                print("input error!")
        
        tourMax = 100
        for i in range(tourMax):
            if i%2 == 0:
                pokemonAssaillant = self.__pokemonActive1
                pokemonAssailli = self.__pokemon
                dresseurActive = self.__dresseur
            else:
                pokemonAssaillant = self.__pokemon
                pokemonAssailli = self.__pokemonActive1
                dresseurActive = self.__pokemon     
                
            if self.__pokemon.vie <= 0:
                print("Vous avez gagne le combat!")
                self.gagnant = self.__dresseur
                self.perdant = self.__pokemon
                break
                
            if int(pokemonAssaillant.vie) <= 0:
                print("Votre Pokemon a ete mis KO")
                print(pokemonAssaillant,"\n")
                if dresseurActive.deck[0].vie <= 0 and dresseurActive.deck[1].vie <= 0 and dresseurActive.deck[2].vie <= 0 :
                    self.gagnant = self.__pokemon
                    self.perdant = self.__dresseur
                    break
                ko = True
                while ko:
                    print("Changement de Pokemon \n1: {} \n2: {} \n3: {}".format(self.__dresseur.deck[0].nom,self.__dresseur.deck[1].nom,self.__dresseur.deck[2].nom))
                    choix = input("Lequel voulez vous choisir? (1-3): ")
                    if choix == "1":    
                        self.__changePokemon(self.__dresseur,self.__dresseur.deck[0])
                    elif choix == "2":
                        self.__changePokemon(self.__dresseur,self.__dresseur.deck[1])
                    elif choix == "3":
                        self.__changePokemon(self.__dresseur,self.__dresseur.deck[2])
                    else:
                        print("Veuillez choisir un chiffre entre 1 et 3")
                        ko = True
                    if i%2 == 0:
                        pokemonAssaillant = self.__pokemonActive1
                        pokemonAssailli = self.__pokemon
                        dresseurActive = self.__dresseur
                    else:
                        pokemonAssaillant = self.__pokemon
                        pokemonAssailli = self.__pokemonActive1
                        dresseurActive = self.__pokemon        
                    if pokemonAssaillant.vie <= 0:
                        ko = True
                        print("Vous ne pouvez pas choisir un Pokemon dont la vie est inferieur a 0")
                    else:
                        ko = False       
                        
            pokemonAssaillant.energie += pokemonAssaillant.regeEnergie
            if pokemonAssaillant.energie > pokemonAssaillant.energieMax:
                pokemonAssaillant.energie = pokemonAssaillant.energieMax  
                         
            if i%2 == 0: 
                print("Tour {}".format(i+1))
                print("c'est a {} de jouer".format(dresseurActive.nom))
                print(pokemonAssaillant,"\n")
                print("1: Choisissez une competence de votre Pokemon \n2: Changement de Pokemon avec un autre present dans le Deck \n3: Capturer le pokemon \n4: Declarer forfait")
                decision = input("Vous voulez faire? (1-4):")
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
                    if self.__capturer() == True:
                        self.__dresseur.pokemon.append(self.__pokemon)
                        print("Vous avez reussi a capturer le pokemon!")
                        self.gagnant = self.__dresseur
                        self.perdant = self.__pokemon  
                        break
                    else:
                        print("Vous n'avez pas reussi a capturer le pokemon...Le combat continue!")      
                elif decision == "4":
                    self.__forfait(dresseurActive)
                    self.gagnant = self.__pokemon
                    self.perdant = self.__dresseur
                    break
                else:
                    print("input error!")
                    i -= 1 
                    pokemonAssaillant.energie -= pokemonAssaillant.regeEnergie
            
            # La decision du pokemon: il ne peut qu'effectuer une competence. Il ne peut pas changer de Pokemon ou declarer forfait
            else:
                print("Tour {}".format(i+1))
                n = np.random.randint(1,len(self.__pokemon.Competence)-1)
                print(self.__pokemon)
                self.__utilCompetence(pokemonAssaillant.Competence[n],pokemonAssaillant,pokemonAssailli)

            if i == tourMax-1: 
                self.perdant = self.__dresseur
                self.gagnant = self.__pokemon    
                    
        self.__reglement()
        self.__reinitialisation()    
