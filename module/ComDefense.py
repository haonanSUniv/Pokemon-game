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
from module.Competence import Competence
# In[3]

class ComDefense(Competence):
    def __init__(self,nom,description,element,valeurSoin,valeurEnergie,cout):
        super().__init__(nom,description,element,cout)
        self.__valeurSoin = valeurSoin
        self.__valeurEnergie = valeurEnergie
        
    @property
    def valeurSoin(self):
        return self.__valeurSoin
    @valeurSoin.setter
    def valeurSoin(self,valeurSoin):
        self.__valeurSoin = valeurSoin
        
    @property
    def valeurEnergie(self):
        return self.__valeurEnergie
    @valeurEnergie.setter
    def valeurEnergie(self,valeurEnergie):
        self.__valeurEnergie = valeurEnergie
        
    def __str__(self):
        sum = '{} (Soin, {}, Cout: {}, Soin: {}, Energie: {}): {}'.format(self.nom,self.element,self.cout,self.__valeurSoin,self.valeurEnergie,self.description)
        return sum
    
    def utilCompetence(self,Pokemon):
    # different que la methode portant le même nom dans la classe ComAttaque, cette methode n'a aucun retour mais l'effet sera appliqué directement aux données du pokemon(la vie ou l'energie actuelles)
        if self.__valeurSoin != '':
            Pokemon.vie += np.random.randint(self.__valeurSoin[0],self.__valeurSoin[1]+1)
            if Pokemon.vie > Pokemon.vieMax:
                Pokemon.vie = Pokemon.vieMax                
        elif self.__valeurEnergie != '':
            Pokemon.energie += np.random.randint(self.__valeurEnergie[0],self.__valeurEnergie[1]+1)
            if Pokemon.energie > Pokemon.energieMax:
                Pokemon.energie = Pokemon.energieMax
        

