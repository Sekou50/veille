#coding :utf-8
class Humain :
    def __init__(self,cnom,cage):
        print("en cours de realistion")
        self.nom= cnom
        self.age=cage
    def parler(self,message):
        print("{}  a dit {}".format(self.nom, message))
    def definition():
        print("l'humain est le premier jhgkjhqg")
print("en cours de fabrication")
h1=Humain("Karambe", 13)

""""print("age est {}".format(h1.age))
h2 = Humain("Niass", 23)
print("nom est : {}".format(h2.nom))
print("age est {}".format(h2.age))"""
h1.parler("bonjour à vous")
h1.parler("bienvenue")
Humain.definition()