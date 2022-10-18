class Table:
    def __init__(self,prixDeFabrication,tableEnStock,reference,matiere,longueur,largeur,hauteur,poids,prix):
         self.__prixDeFabrication = prixDeFabrication
         self.__tableEnStock = tableEnStock
         self.reference = reference
         self.matiere = matiere
         self.longueur = longueur
         self.largeur = largeur
         self.hauteur = hauteur
         self.poids = poids
         self.prix = prix
    def getTable(self):
        return self._prixDeFabrication
    def getTable(self):
        return self._tableEnStock
    def setTable(self,prixDeFabrication):
        self.__prixDeFabrication= prixDeFabrication
    def setTable(self,tableEnStock):
        self.__tableEnStock=tableEnStock
    def affichage (self):
        print(self.reference,self.matiere,self.longueur,self.largeur,self.hauteur,self.poids,self.prix)
T=Table("gs","bois","hjh",45,16,48,45,34,34)
T.affichage()
