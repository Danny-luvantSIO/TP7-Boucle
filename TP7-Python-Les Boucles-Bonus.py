#Excercice 1*
def afficher_carre(n):
    for i in range(1, n + 1):
        print(i ** 2)
afficher_carre(5)
print("------------------")
#Exercice 2
def dessiner_carre(taille):

    for i in range(taille):
        
        for j in range(taille):
            print("∎", end="")
        
        print()
dessiner_carre(4)
print("------------------")
#Exercice 3
def plus_grand_nombre():
    try:
        num1 = float(input("Entrez le premier nombre : "))
        num2 = float(input("Entrez le deuxième nombre : "))
        num3 = float(input("Entrez le troisième nombre : "))
        max_num = max(num1, num2, num3)
        print(f"LA PLUS GRANDE VALEURS parmi{num1}, {num2} et {num3} est : {max_num}")
        
    except ValueError:
        print("Veuillez entrer des nombres valides.")
plus_grand_nombre()
print("------------------")
#Exercice 4
def trier_liste(liste):
    
    n = len(liste)
   
    for i in range(n):
        
        for j in range(0, n - i - 1):
            
            if liste[j] > liste[j + 1]:
                liste[j], liste[j + 1] = liste[j + 1], liste[j]
    
    print(liste)
ma_liste = [7, 2, 9, 1, 5]
trier_liste(ma_liste)


