n = int(input("Entrez un nombre entier n : "))
somme = 0
i = 1

while i <= n:
    somme += i
    i += 1

print("La somme des nombres de 1 à", n, "est :", somme)