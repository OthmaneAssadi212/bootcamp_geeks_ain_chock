# ------ Exercise 1
# p = True
# q = False
# m = 5
# n = 10
# print("p is", p)
# print("q is", q)
# print("m:", m)
# print("n:", n)

# ------ Exercise 2
mot_saisi = input("Entrez un mot : ")
ancien = mot_saisi
precedent = ""
while "a" not in ancien.lower() and len(ancien) > len(precedent):
    print("félicitations", end=" ")
    precedent = ancien
    ancien = input("Entrez un mot : ")
    print()

# ------ Exercise 3
texte = ("La programmation est une compétence pratique et créative. "
         "Avec un peu de logique et beaucoup d’entraînement, on peut résoudre "
         "des problèmes réels et construire des applications utiles au quotidien. "
         "Même les débutants progressent rapidement en écrivant du code chaque jour!")

compteur_car = 0
for ch in texte:
    if ch in ' .,:;!?\'"’«»()-–—\n\t':
        continue
    compteur_car += 1
print("Nombre de caractères :", compteur_car)

import re
phrases = [s for s in re.split(r"[.!?]+", texte) if s.strip() != ""]
print("Nombre de phrases :", len(phrases))

mots = texte.split()
print("Nombre de mots :", len(mots))

mots_nettoyes = []
for w in mots:
    w2 = w.strip('.,:;!?\'"’«»()-–—')
    if w2:
        mots_nettoyes.append(w2.lower())
ensemble_mots = set(mots_nettoyes)
print("Nombre de mots uniques :", len(ensemble_mots))
