#coding:utf-8
class Humain :
    def __init__(self,prenom):
        self.__prenom = prenom
    def getHumain(self):
        return self.__prenom
    def setHumain(self,prenom):
         self.__prenom=prenom
h1= Humain("Moussa")
print(h1.getHumain())
h1.setHumain("SEKOU")
print(h1.getHumain())
