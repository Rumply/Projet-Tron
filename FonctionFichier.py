'''
###########################################################################
#                                                                         #
#                    Fichier: FonctionFichier.py                          #
#                  Fait par: Guillaume Hamel-Gagné                        #
#                Travail Finale: (Tron light cycle)                       #
#               Dernière fois modifier: 27 May 2015                       #
#                                                                         #
#               Utilité: Sert a générer les configurations                #
#               du jeu et les resets quand il y a problème                #
#                                                                         #
###########################################################################
'''
import os
import sys

dossierUsers = "C:/Users/" + os.getlogin()
couleurDispo = ["orange","magenta","cyan","vert"]

if sys.platform.startswith("win"):
    fichierPerm = dossierUsers
if sys.platform.startswith("linux"):
    fichierPerm = os.path.expanduser("~")

fichierPerm += "/config"

def gestionErreurFichier():
    """Cette fonction à pour but de tester si le fichier existe"""
    fonctionnelle = True
    if sys.platform.startswith("win"):
        if not os.access(fichierPerm, os.W_OK):
            print("Le fichier: " + fichierPerm + " est introuvable")
            fonctionnelle = False
    if sys.platform.startswith("linux"):
        if not os.access(os.path.expanduser("~/config"), os.W_OK):
            print("Le fichier: " + "config" + " est introuvable.")
            fonctionnelle = False
    return fonctionnelle



def resetConfigFile():
    """Cette procédure réinitialise le fichier de configuration
    avec les données de défaut"""
    fichier = ["couleurJ1=orange\n","couleurJ2=magenta\n","multi=TRUE"]
    if sys.platform.startswith("win"):
        with open(fichierPerm, "w") as fichierConfig:
            for ligne in fichier:
                fichierConfig.write(ligne)
    elif sys.platform.startswith("linux"):
        os.system("cp config ~")


def genererConfig(config):
    """Cette"""
    teste = []
    if not gestionErreurFichier():
        resetConfigFile()
    with open(fichierPerm, "r") as document:
        for ligne in document:
            if ligne != "\n" and ligne.count("=") == 1:
                teste.append(ligne)
                (cle,val) = ligne.split("=")
                if val[-1:] == "\n":
                    config[cle] = val[:-1]
                else:
                    config[cle] = val
    if not config["couleurJ1"].lower() in couleurDispo \
    or not config["couleurJ2"].lower() in couleurDispo:
        print("Erreur: couleur invalide. Reset du fichier")
        resetConfigFile()
        genererConfig()
    elif config["multi"].upper() != "TRUE" \
   and config["multi"].upper() != "FALSE":
        print("Erreur: couleur invalide. Reset du fichier")
        resetConfigFile()
        config = {}
        genererConfig()

