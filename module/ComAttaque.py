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
# In[2]
class ComAttaque(Competence):
    def __init__(self,nom,description,element,puissance,precision,cout):
    # on peut construire les parametres commun avec la classe mere avec la fonction "super().__init__()"
        super().__init__(nom,description,element,cout)
        self.__puissance = puissance
        self.__precision = precision
    
    @property
    def puissance(self):
        return self.__puissance
    @puissance.setter
    def puissance(self,puissance):
        self.__puissance = puissance 
        
    @property
    def precision(self):
        return self.__precision
    @precision.setter
    def precision(self,precision):
        self.__precision = precision  
    
    def __str__(self):
        res = '{} (Attaque, {}, Cout: {}, Puissance: {}, Precision: {}): {}'.format(self.nom,self.element,self.cout,self.__puissance,self.precision,self.description)
        return res
    
    def utilCompetence(self,pokemonAssaillant,pokemonAssailli):
        if np.random.randint(0,100) > self.__precision:
        # on fait un tirage et si le chiffre est plus grand que la precision, l'attaque aura echoue
            return 0
        
        # on analyse l'element de la competence et du pokemon pour calculer la valeur de "b"
        if self.element == 'Air':
            if pokemonAssaillant.element == 'Air':
                b = 1
            elif pokemonAssaillant.element == 'Eau':
                b = 1.5
            elif pokemonAssaillant.element == 'Feu':
                b = 0.5
            elif pokemonAssaillant.element == 'Terre':
                b = 1
                
        if self.element == 'Eau':
            if pokemonAssaillant.element == 'Air':
                b = 1
            elif pokemonAssaillant.element == 'Eau':
                b = 1
            elif pokemonAssaillant.element == 'Feu':
                b = 1.5
            elif pokemonAssaillant.element == 'Terre':
                b = 0.5
                
        if self.element == 'Feu':
            if pokemonAssaillant.element == 'Air':
                b = 0.5
            elif pokemonAssaillant.element == 'Eau':
                b = 1
            elif pokemonAssaillant.element == 'Feu':
                b = 1
            elif pokemonAssaillant.element == 'Terre':
                b = 1.5
                
        if self.element == 'Terre':
            if pokemonAssaillant.element == 'Air':
                b = 1.5
            elif pokemonAssaillant.element == 'Eau':
                b = 0.5
            elif pokemonAssaillant.element == 'Feu':
                b = 1
            elif pokemonAssaillant.element == 'Terre':
                b = 1     
        
        # On calcule les degats a partir de la formule qu'on a donne dans le sujet, cette methode retourne la valeur des degats
        return round(b*np.random.uniform(0.85,1)*(self.__puissance*(4*pokemonAssaillant.niveau+2)/pokemonAssailli.resistance+2))

