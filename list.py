
"""import os

files = os.listdir(".");
liste = [file for file in files if file.endswith(".py")]

for file in liste:
    print(file)"""
from typing import TextIO

"""import glob
res = [f for f in glob.glob("*") if "ab" in f or "1" in f or "a1b" in f]
for f in res:
    print (f)"""
"""import os
import fnmatch

for root, dir, files in os.walk("."):
        print (root)
        print ("")
        for files in fnmatch.filter(files, "*"):
                print ("..." + files)
        print ("")"""
"""set="Mohamed","ibrahim",12,12.23
print(set)"""

"""fichier= open("jouer.png", "wb")
fichier.write(0)
#print(a)
fichier.close()"""
"""rnd = 42


class exemple_classe:
    def methode1(self, n):
        simule la génération d'un nombre aléatoire
           compris entre 0 et n-1 inclus
        global rnd
        rnd = 397204094 * rnd % 2147483647
        return int(rnd % n)


nb = exemple_classe()
l1 = [nb.methode1(100) for i in range(0, 10)]
print(l1)   # affiche [19, 46, 26, 88, 44, 56, 56, 26, 0, 8]

nb2 = exemple_classe()
l2 = [nb2.methode1(100) for i in range(0, 10)]
print(l2)   # affiche [46, 42, 89, 66, 48, 12, 61, 84, 71, 41]"""
class Voiture:
    def __int__(self, cmarque, cannee):
        print("creation de voiture")
        self.marque =cmarque
        self.annee=cannee
print("en cours de traitement")
v1= Voiture("Rav4")
print("Marque du voiture : {}".format(v1.marque))
print("annee est {} :".format(v1.annee))
v2= Voiture("Rav4",2008)
print("marque de voiture : {}".format(v2.marque))
print("annee est : {}".format(v2.annee))






