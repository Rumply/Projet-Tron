'''
###########################################################################
#                                                                         #
#                      Fichier: DictVariable.py                           #
#                  Fait par: Guillaume Hamel-Gagné                        #
#                Travail Finale: (Tron light cycle)                       #
#               Dernière fois modifier: 27 May 2015                       #
#                                                                         #
#               Utilité: Si l'on veut rajouter des                        #
#               couleurs de lumière quelque ligne de                      #
#               code seulement suffise afin de généré                     #
#               une nouvelle couleur. Sinon ici sont                      #
#               placé les dictionnaires les plus utiliser                 #
#                                                                         #
###########################################################################
'''
import pygame


def dictFenetre(infoResolution):
    fenetre = {"display_width": infoResolution.current_w,
           "display_height" : infoResolution.current_h}
    return fenetre

def dictCouleur():
    """Cette fonction retourne un dictionnaire de couleur. """
    couleur = {"blanc":(255,255,255),
               "noir":(0,0,0),
               "rouge":(255,0,0),
               "vert":(0,255,0),
               "bleu":(0,0,255),
               "cyan":(0,255,255),
               "magenta":(255,0,255),
               "orange":(255,165,0)}
    return couleur



def dictTerrain(fenetre):
    """Cette fonction retourne le dictionnaire terrain. """
    terrain = {"largeur":int(fenetre["display_width"]*0.96),
                "hauteur":int(fenetre["display_height"]*0.94),
                "margin":{"largeur":int(fenetre["display_width"]*0.02),
                          "hauteur":int(fenetre["display_height"]*0.03)}
               }
    terrain["milieu"] = {"X":(terrain["largeur"]/2 + \
                              terrain["margin"]["largeur"]),
                         "Y":(terrain["hauteur"]/2 + \
                              terrain["margin"]["hauteur"])}
    return terrain
    

    
def dictInfo(terrain):
    """Cette fonction retourne le dictionnaire info"""
    info = {"joueur":{"largeur":int(terrain["largeur"]*0.005),
                        "hauteur":int(terrain["hauteur"]*0.01),
                        "longueurMin":20},
            "objet":{"largeur":int(terrain["largeur"]*0.012),
                     "hauteur":int(terrain["hauteur"]*0.024)},
            "portail":{"largeur":int(terrain["largeur"]*0.012),
                     "hauteur":int(terrain["hauteur"]*0.024)}
              }
    return info

def autoDictSprite(sprite, info, couleur, nomFichier):
    """Cette procédure génère un dictionnaire de sprite pour
    un joueur"""
    sprite[couleur] = {"ligne":pygame.image.load(nomFichier[0]),
                        "coin":{"GB":pygame.image.load(nomFichier[1])}}
    sprite[couleur] = {"ligne":pygame.transform.scale(
                                                sprite[couleur]["ligne"], 
                                                (info["joueur"]["largeur"], 
                                                 info["joueur"]["hauteur"])),
                        "coin":{"GB":pygame.transform.scale(
                                                sprite[couleur]["coin"]["GB"], 
                                                (info["joueur"]["largeur"], 
                                                 info["joueur"]["hauteur"]))}
                        }
    
    sprite[couleur]["coin"] = {"GB":sprite[couleur]["coin"]["GB"],
                                 "DB":pygame.transform.rotate(
                                    sprite[couleur]["coin"]["GB"], 90),
                                 "DH":pygame.transform.rotate(
                                    sprite[couleur]["coin"]["GB"], 180),
                                 "GH":pygame.transform.rotate(
                                    sprite[couleur]["coin"]["GB"], 270)}



def dictSpritePortail(sprite,info):
    """Cette procédure ajoute au dictionnaire 'sprite'
    le sprite portail"""
    sprite["portail"] = {0:pygame.image.load("./images/portail.png")}
    sprite["portail"][0] = pygame.transform.scale(
                                                sprite["portail"][0], 
                                                (info["portail"]["largeur"], 
                                                 info["portail"]["hauteur"]))
    
    sprite["portail"] = {0:sprite["portail"][0],
                        1:pygame.transform.rotate(sprite["portail"][0], 45),
                        2:pygame.transform.rotate(sprite["portail"][0], 90),
                        3:pygame.transform.rotate(sprite["portail"][0], 135),
                        4:pygame.transform.rotate(sprite["portail"][0], 180),
                        5:pygame.transform.rotate(sprite["portail"][0], 225),
                        6:pygame.transform.rotate(sprite["portail"][0], 270),
                        7:pygame.transform.rotate(sprite["portail"][0], 315)}
    

def dictSprite(info):
    """Cette fonction génère des dictionnaires de sprite."""
    sprite = {"joueur1":{"devant":pygame.image.load(
                                                "./images/devantOrange.png"),
                         "arriere":pygame.image.load(
                                                "./images/arriereOrange.png")}}
    sprite["joueur1"]["devant"] = pygame.transform.scale(
                                                sprite["joueur1"]["devant"], 
                                                (info["joueur"]["largeur"], 
                                                 info["joueur"]["hauteur"]))
    sprite["joueur1"]["arriere"] = pygame.transform.scale(
                                                sprite["joueur1"]["arriere"], 
                                                (info["joueur"]["largeur"], 
                                                 info["joueur"]["hauteur"]))
    sprite = {"joueur2":{"devant":pygame.image.load(
                                            "./images/devantMagenta.png"),
                     "arriere":pygame.image.load(
                                            "./images/arriereMagenta.png")}}
    sprite["joueur2"]["devant"] = pygame.transform.scale(
                                                sprite["joueur2"]["devant"], 
                                                (info["joueur"]["largeur"], 
                                                 info["joueur"]["hauteur"]))
    sprite["joueur2"]["arriere"] = pygame.transform.scale(
                                                sprite["joueur2"]["arriere"], 
                                                (info["joueur"]["largeur"], 
                                                 info["joueur"]["hauteur"]))
    """    Portail   """
    dictSpritePortail(sprite,info)
    
    """    Tracer    """
    autoDictSprite(sprite, info, "orange", ["./images/ligneOrange.png",
                                            "./images/ligneOrangeCoin.png"])
    
    autoDictSprite(sprite, info, "magenta", ["./images/ligneMagenta.png",
                                             "./images/ligneMagentaCoin.png"])
    
    autoDictSprite(sprite, info, "cyan", ["./images/ligneCyan.png",
                                          "./images/ligneCyanCoin.png"])
    
    """ Tracer Vert    """
    autoDictSprite(sprite, info, "vert", ["./images/ligneVert.png",
                                          "./images/ligneVertCoin.png"])
    return sprite
    
    
    