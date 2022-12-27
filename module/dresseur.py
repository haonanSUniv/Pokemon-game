# -*- coding: utf-8 -*-
"""
Created on Wed Jan 12 22:09:55 2022

@author: 

Haonan Yuan
Valentin Cointrel
Sonia Slimi

"""

# import


import os
 
# In[5]

class dresseur:
    def __init__(self,nom,pokemon,deck):
        self.__nom = nom
        self.__pokemon = pokemon
        self.__deck = deck
        
    @property
    def nom(self):
        return self.__nom
    @nom.setter
    def nom(self,nom):
        self.__nom = nom
        
    @property
    def pokemon(self):
        return self.__pokemon
    @pokemon.setter
    def pokemon(self,pokemon):
        self.__pokemon = pokemon 
        
    @property
    def deck(self):
        return self.__deck
    @deck.setter
    def deck(self,deck):
        self.__deck = deck 
        
    def afficheDeck(self):
        for i in range(3):
            print(i+1,'/ ',str(self.__deck[i]),'\n')
            
    def affichePokemon(self):
        for i in range(len(self.__pokemon)):
            print(i+1,'/ ',str(self.__pokemon[i]),'\n')
    def changeDeck(self):
        self.affichePokemon()
        notdone = True
        while notdone:
            for i in range(3):
                s = input("Lesquels voulez vous choisir: (1-{}) ({}eme choix)".format(len(self.__pokemon),i+1))
                self.__deck[i] = self.__pokemon[int(s)-1]
            if self.__deck[0] == self.__deck[1] or self.__deck[0] == self.__deck[2] or self.__deck[1] == self.__deck[2]:
                print("Le deck ne peut pas contenir plusieurs fois le meme Pokemon")
            else:
                notdone = False

    def sauvegarder(self): 
        chemin = os.getcwd()
        if os.path.exists(chemin + "/save") :
            editeur1 = open(chemin + "/save/" + self.__nom + ".txt","w")
            for i in range(len(self.__deck)):
                editeur1.write(self.__deck[i].nom+'\n')
            editeur2 = open(chemin + "/save/" + self.__nom + ".txt","a")
            for i in range(len(self.__pokemon)): 
                editeur2.write(self.__pokemon[i].nom+' '+str(self.__pokemon[i].niveau)+' ' +str(self.__pokemon[i].experience)+'\n')
        else:
            os.mkdir(chemin + "/save")  
            editeur1 = open(chemin + "/save/" + self.__nom + ".txt","w")  
            for i in range(len(self.__deck)):
                editeur1.write(self.__deck[i].nom+'\n')
            editeur2 = open(chemin + "/save/" + self.__nom + ".txt","a")
            for i in range(len(self.__pokemons)):
                editeur2.write(self.__pokemons[i].nom+' '+str(self.__pokemons[i].niveau)+' '+str(self.__pokemon[i].experience)+'\n')
       
        
