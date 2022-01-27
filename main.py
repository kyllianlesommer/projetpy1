# -*- coding: utf-8 -*-
"""
date: 26/11/2020
comment: Projet Python 1SIOA
autor: LARMIER Maxime, LE SOMMER Kyllian
"""

#librairies
import os
from os import chdir
import enquiries

#global variables
logfile_path = "?"
project_path = "?"


def readfile():
  #open the file selected \ ouverture du fichier selectinné
  global logfile_path
  global project_path
  openlog = open(project_path+'/'+logfile_path, 'r')
  print(openlog.read())
  openlog.close()
  return 0



#path initialization \ initialisation du chemin d'accès
def ppath():
  project_path = input("enter project path (ex:/home/ex/project) or 'here' for current dir > ")
  if project_path == "here":
    project_path = os.getcwd()

  #path existence verification \ vérification du chemin d'accès
  while not os.path.exists(project_path):
    project_path = input("path doesn't exist, please reenter the path > ")

  chdir(project_path)
  print("\ncurrent path changed to: ", project_path,"\n")
  return project_path




def lpath():
  logfile_path = input("enter log file name (log.txt) > ")

  #file existence verification \ vérification de l'existence du ficher
  while not os.path.exists(logfile_path):
    logfile_path = input("file doesn't exist, please reenter the file name > ")
  return logfile_path




def gensqlfile():
  global project_path
  global logfile_path
  xlog = open(project_path+'/'+logfile_path, 'r')
  xdate = input('enter the date in the format:"yyyy-mm-dd" > ')
  ligne=xlog.readline()
  #les noms des fichiers de log sont 'log_proxy_'+date+'.txt'
  #fichiersql= #variable de nom fichier de fichier
  try:
    for ligne in xlog:
      #début insert
      ligne=ligne.lower()
      ligne=ligne.split(" ")
      fichiersql = open(project_path+'/'+'insert_'+xdate+'.sql', "a")
      fichiersql.write(" INSERT INTO PROXY(ID, ADRESSEIP, DATEHEURE, URL) VALUES (SEQ_ID2.nextVal, "+chr(39)+ligne[1]+chr(39)+", "+chr(39)+xdate+chr(39)+ ", "+chr(39)+ligne[4]+chr(39)+");\n")
      fichiersql.close() # close the logfile reading
  except Exception as error:
    print("\nerreur:\n")
    print(error)
    print("\n")
  xlog.close()
  if os.path.exists(project_path+"/insert_"+xdate+".sql"):
      print("\n Fichier sql géneré !")
  else:
      print("\n Fichier sql n'as pas été géneré !")


def line_count():
    global logfile_path
    global project_path
    try:
        file = open(project_path+"/"+logfile_path, 'r')
        line_number = len(file.readline())
        file.close()
        return line_number
    except:
        line_number = 0
        return line_number

#menu
def menu():
  global project_path
  global logfile_path
  os.system('clear')
  xline ="no"
  choice = ""
  while choice != "exit":
    if project_path != "?" and logfile_path != "?":
        xline = str(line_count())
    print("current directory: [", project_path, "]")
    print("selected file: [", logfile_path, "] ("+xline+" line)")
    options = ['select path', 'select file', 'read logfile', 'generate sql file', 'exit']
    choice = enquiries.choose('Choose one of these options: ', options)

    if choice == "select path":
      project_path = ppath()

    elif choice == "select file":
      logfile_path = lpath()

    elif choice == "read logfile":
      readfile()

    elif choice == "generate sql file":
      gensqlfile()

menu()
