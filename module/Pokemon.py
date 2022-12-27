# -*- coding: utf-8 -*-
"""
Created on Wed Jan 12 22:09:55 2022

@author: 

Haonan Yuan
Valentin Cointrel
Sonia Slimi

"""

# In[1]

class Pokemon:
    def __init__(self,nom,element,niveau,experience,niveauRange,vieRange,energieRange,regeneRange,resistanceRange,Competence):
        self.__nom = nom
        self.__element = element
        self.__niveau = niveau
        self.__experience = experience 
        self.__niveauRange = niveauRange # pour stocker le niveau maximum et minimum de ce type de pokemon
        self.__vieRange = vieRange # pour stocker la vie maximum et minimum de ce type de pokemon
        self.__energieRange = energieRange # pour stocker l'energie maximum et minimum de ce type de pokemon
        self.__regeneRange = regeneRange # pour stocker la regeneration maximum et minimum de ce type de pokemon
        self.__resistanceRange = resistanceRange # pour stocker le resistance maximum et minimum de ce type de pokemon
        self.__vieMax = self.__vieRange[0] + (self.__niveau - self.__niveauRange[0]) * (self.__vieRange[1]-self.__vieRange[0])/(self.__niveauRange[1]-self.__niveauRange[0])
        self.__energieMax = self.__energieRange[0] + (self.__niveau - self.__niveauRange[0]) * (self.__energieRange[1]-self.__energieRange[0])/(self.__niveauRange[1]-self.__niveauRange[0])
        self.__regeEnergie = self.__regeneRange[0] + (self.__niveau - self.__niveauRange[0]) * (self.__regeneRange[1]-self.__regeneRange[0])/(self.__niveauRange[1]-self.__niveauRange[0])
        self.__resistance = self.__resistanceRange[0] + (self.__niveau - self.__niveauRange[0]) * (self.__resistanceRange[1]-self.__resistanceRange[0])/(self.__niveauRange[1]-self.__niveauRange[0])
        self.__Competence = Competence
        self.__vie = self.__vieMax
        self.__energie = self.__energieMax

#-----------------------les setters et les getters pour tous les donnees de pokemon----------------------------

    @property
    def nom(self):
        return self.__nom
    @nom.setter
    def nom(self,nom):
        self.__nom = nom
        
    @property
    def element(self):
        return self.__element
    @element.setter
    def element(self,element):
        self.__element = element
        
    @property
    def niveau(self):
        return self.__niveau
    @niveau.setter
    def niveau(self,niveau):
        self.__niveau = niveau 
        
    @property
    def experience(self):
        return self.__experience
    @experience.setter
    def experience(self,experience):
        self.__experience = experience  
        
    @property
    def vieMax(self):
        return self.__vieMax
    @vieMax.setter
    def vieMax(self,vieMax):
        self.__vieMax = vieMax  
        
    @property
    def energieMax(self):
        return self.__energieMax
    @energieMax.setter
    def energieMax(self,energieMax):
        self.__energieMax = energieMax  
        
    @property
    def regeEnergie(self):
        return self.__regeEnergie
    @regeEnergie.setter
    def regeEnergie(self,regeEnergie):
        self.__regeEnergie = regeEnergie  
        
    @property
    def Competence(self):
        return self.__Competence
    @Competence.setter
    def Competence(self,Competence):
        self.__Competence = Competence  
        
    @property
    def resistance(self):
        return self.__resistance
    @resistance.setter
    def resistance(self,resistance):
        self.__resistance = resistance  
        
    @property
    def vie(self):
        return self.__vie
    @vie.setter
    def vie(self,vie):
        self.__vie = vie 
    
    @property
    def energie(self):
        return self.__energie
    @energie.setter
    def energie(self,energie):
        self.__energie = energie  
        
    @property
    def niveauRange(self):
        return self.__niveauRange
    @niveauRange.setter
    def niveauRange(self,niveauRange):
        self.__niveauRange = niveauRange  
        
    @property
    def vieRange(self):
        return self.__vieRange
    @vieRange.setter
    def vieRange(self,vieRange):
        self.__vieRange = vieRange 
             
    @property
    def energieRange(self):
        return self.__energieRange
    @energieRange.setter
    def energieRange(self,energieRange):
        self.__energieRange = energieRange          
        
    @property
    def regeneRange(self):
        return self.__regeneRange
    @regeneRange.setter
    def regeneRange(self,regeneRange):
        self.__regeneRange = regeneRange          
        
    @property
    def resistanceRange(self):
        return self.__resistanceRange
    @resistanceRange.setter
    def resistanceRange(self,resistanceRange):
        self.__resistanceRange = resistanceRange      

        
    def __str__(self):
        sum = '{}(Lv {}, {}/{},{}): Vie {}/{}, Energie {}/{} (+{}), Resistance {}'.format(self.__nom,self.__niveau,self.__experience,100*(self.__niveau+1),self.__element,self.__vie,self.__vieMax,self.__energie,self.__energieMax,self.__regeEnergie,self.__resistance)    
        sum += '\n'
        for i in range(len(self.__Competence)):
            sum += '{}'.format(self.__Competence[i].nom)
            if i != len(self.__Competence)-1:
                sum += ','
        return sum
    
    def renewLevel(self):
    # on calcule les donnees de pokemons a partir de son niveau actuel
    # plus le niveau montre, plus les donnees de pokemon sont elevees
        self.__vieMax = self.__vieRange[0] + (self.__niveau - self.__niveauRange[0]) * (self.__vieRange[1]-self.__vieRange[0])/(self.__niveauRange[1]-self.__niveauRange[0])
        self.__energieMax = self.__energieRange[0] + (self.__niveau - self.__niveauRange[0]) * (self.__energieRange[1]-self.__energieRange[0])/(self.__niveauRange[1]-self.__niveauRange[0])
        self.__regeEnergie = self.__regeneRange[0] + (self.__niveau - self.__niveauRange[0]) * (self.__regeneRange[1]-self.__regeneRange[0])/(self.__niveauRange[1]-self.__niveauRange[0])
        self.__resistance = self.__resistanceRange[0] + (self.__niveau - self.__niveauRange[0]) * (self.__resistanceRange[1]-self.__resistanceRange[0])/(self.__niveauRange[1]-self.__niveauRange[0])
  