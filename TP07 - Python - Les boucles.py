#Exercice 1
i=1
while i<=10:
    i+=1
    print(i)

print("------------------")

#Exercice 2
i=10
while i>=1:
    print(i)
    i-=1


print("------------------")
#Exercice 3
n=int(input("Entrez un nombre : "))
somme=0
i=1
while i<=n:
    somme+=i
    i+=1
print("Résultat :", somme, f"({n}+{n-1}+...+1)") 
print("------------------")
#Exercice 4
mot_de_passe="python"
while True:
    tentative = input("Entrez le mot de passe : ")
    if tentative == mot_de_passe:
        print("accès autorisé")
        break
    else:
        print("Mot de passe incorrect. Veuillez réessayer.")

print("------------------")
#Exercice 5
def afficher_nombres(n):
    for i in range(n + 1):
        print(i)

afficher_nombres(5)
print("------------------")
#Exercice 6
def table_mult(nombre):
    for i in range(1, 11):
        print(f"{nombre} x {i} = {nombre * i}")

table_mult(3)
print("------------------")
#Exercice 7 
def somme_nombres(n):
    total = 0
    for i in range(1, n + 1):
        total += i
    return total
print(somme_nombres(10))  
print("------------------")
#Exercice 8
def afficher_lettres(mot):
    for lettre in mot:
        print(lettre)


afficher_lettres("python")
print("------------------")
#Exercice 9
def compter_voyelles(texte):
    voyelles = "aeiouyAEIOUY"
    compteur = 0
    for caractere in texte:
        if caractere in voyelles:
            compteur += 1
    return compteur
       
print(compter_voyelles("AEIOUY"))    
print("------------------")
#Exercice 10
def notes_valides(liste_notes):
    for note in liste_notes:
        if note >= 10:
            print(note)

notes_valides([12, 15, 9, 17, 8, 14])