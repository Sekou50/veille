class Humain :
    def __init__(self,nom,age):
        self.nom=nom
        self.age =age
    def parler(self):
        print("bonjour python")

h1=Humain("Togo",21)
print("nom est :",h1.nom)
print("age est",h1.age)
h1.parler( )