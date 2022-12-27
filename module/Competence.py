# -*- coding: utf-8 -*-
"""
Created on Wed Jan 12 22:09:55 2022

@author: 

Haonan Yuan
Valentin Cointrel
Sonia Slimi

"""

# import

from abc import ABC,abstractmethod

# In[1]

class Competence(ABC):
    def __init__(self,nom,description,element,cout): 
    # tous les parametres sont prives parce qu'on ne veut pas qu'ils soient modifies a l'exterieur de la classe
        self.__nom = nom
        self.__description = description
        self.__element = element
        self.__cout = cout

#--------------------------------les getters et les setters--------------------------------------
    
    @property
    def nom(self):
        return self.__nom
    @nom.setter
    def nom(self,nom):
        self.__nom = nom
        
    @property
    def description(self):
        return self.__description
    @description.setter
    def description(self,description):
        self.__description = description
        
    @property
    def element(self):
        return self.__element
    @element.setter
    def element(self,element):
        self.__element = element
        
    @property
    def cout(self):
        return self.__cout
    @cout.setter
    def cout(self,cout):
        self.__cout = cout  
        
    @abstractmethod
    def utilCompetence(self):pass
    # une methode abstrait qui va etre implemente dans les classes filles
