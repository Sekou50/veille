class Personne :
    def __init__(self,nom,prenom,cin):
        self.nom=nom
        self.prenom=prenom
        self.cin=cin
    def ToString(self):
        return "Nom: "+self.nom+"\nPrenom: "+self.prenom+"\nCin: "+self.cin
class Vaccine(Personne):
    def __init__(self,nom,prenom,cin,code=int,date=str,):
        super().__init__(nom,prenom,cin)
        self.__code=code
        self.__date=date
    def getcode(self):
        return self.__code
    def getdate(self):
        return self.date
    def ToString(self):
        return super().ToString()+"\nCode: "+self.code+"\nDate: "+self.date

class Vaccin(Personne):
    def __init__(self,nom,prenom,cin,codev=int,nomv=str,duree=int):
        super().__init__(nom,prenom,cin)
        self.codev=codev
        self.nomv=nomv
        self.duree=duree
    def ToString(self):
        return super().ToString()+"\nNomv: "+self.nomv+"\nCodev: "+self.codev+"\nDuree: "+self.duree
