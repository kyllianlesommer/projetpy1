# -*- coding: utf-8 -*-
"""
date: 26/11/2020
comment: Projet Python
autor: LARMIER Maxime, LE SOMMER Kyllian
"""

import os            #importation de la bibliothèque OS
from os import chdir #importation de chdir depuis la bibliothèque OS

auto = input("Remplissage automatique des variables par le répetoire courant et 'testEntree.txt' en tant que fichier source ? (O/N) > ")

if auto != "O":
  project_path = input("entrer le repertoire du fichier (ex:/home/ex/project) ou 'ici' pour sélectionner le répertoire courant > ")
  if project_path == "ici":
          project_path = os.getcwd()

#vérification du chemin d'accès
  while not os.path.exists(project_path):
    project_path = input("le repertoire n'existe pas, réessayer > ")

  chdir(project_path)
  print("\nrépertoire courant changé pour: ", project_path,"\n")

  fichierlog = input("entrez le nom du fichier texte (ex: testEntree.txt) > ")

#vérification de l'existence du ficher
  while not os.path.exists(fichierlog):
    fichierlog = input("le fichier n'existe pas, réessayer > ")
  print("\n (", fichierlog, ") Sélectionné\n")
else:
  project_path = os.getcwd()  
  fichierlog = "testEntree.txt"
f=open(fichierlog,'r')      # ouverture de testentree en lecture
g=open('testSortie.txt','w')  # ouverture de testSortie en écriture
for ligne in f :  # boucle de lecture de 'testEntrée' et de création de 'testSortie'
    totalMots=ligne.split(";")  # séparation des mots
    a=(totalMots[0][0])         # sélection des premiers caractères
    b=(totalMots[1])            # sélection du deuxieme mot
    tfinal = a+b                # concaténations des caractèes
    f=open('testSortie.txt','w')  # ouverture de testSortie en écriture
    g.write(tfinal.lower())
f.close()                            # fermeture de testEntree
g.close()                            # fermeture de testSortie
print("Fichier testSortie.txt généré") # affichage final