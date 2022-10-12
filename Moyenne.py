note1 = float(input("entrez la note1 : "))
note2 = float(input("entrez la note2 : "))
note3 = float(input("entrez la note3 : "))
moyenne = (note1+note2+note3)/3
print("votre moyenne est : ",format(moyenne,".2f"))
if moyenne < 10:
    print("mention insufissant")
elif  10 >= moyenne < 12:
    print("mention passable")
elif 12 < moyenne < 14:
    print("mention Assez bien")
elif 14 < moyenne < 16 :
    print("mention  bien ")
else :
    print("mention tres bien ")
