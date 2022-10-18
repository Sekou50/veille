class Pet:
    def __init__(self,nom,tpye,age):

        self.__nom=nom
        self.__type=type
        self.__age=age
    def getage(self):
        return self.__age
    def gettype(self):
        return self.__type
    def getnom(self):
        return self.__nom
    def setnom(self,nom):
        self.__nom= nom
    def settype(self,animalType):
        self.__type=animalType
    def setage(self,age):
        self.__age=age
    def afficher(self):
        print("Nom : ",self.__nom)
        print("Type : ", self.__type)
        print("Age : ", self.__age)
try:
    nom = input("Donner le nom de l'animal : ")
    age = int(input("Donner le age de l'animal : "))
    type = input("Donner le type de l'animal : ")
except ValueError:
    print("Vous devez entrer un entier au niveau de lage !!!")
p=Pet(nom,type,age)
p.afficher()
