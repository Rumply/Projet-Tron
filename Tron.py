#! /usr/bin/env python3.4
# -*- coding: utf-8 -*-
'''
###########################################################################
#                                                                         #
#                      Fichier: Tron.py                                   #
#                  Fait par: Guillaume Hamel-Gagné                        #
#                Travail Finale: (Tron light cycle)                       #
#               Dernière fois modifier: 28 May 2015                       #
#                                                                         #
###########################################################################
'''
import pygame, random, math
import FonctionFichier, DictVariable


pygame.init()


infoResolution = pygame.display.Info()

couleur = DictVariable.dictCouleur()
fenetre = DictVariable.dictFenetre(infoResolution)
terrain = DictVariable.dictTerrain(fenetre)
info = DictVariable.dictInfo(terrain)
sprite = DictVariable.dictSprite(info)

gameDisplay = pygame.display.set_mode((fenetre["display_width"],
                                       fenetre["display_height"]), 
                                       pygame.constants.FULLSCREEN)
pygame.display.set_caption("Tron")

arrierePlan = pygame.image.load("./images/tron.jpg").convert()
arrierePlan = pygame.transform.scale(
                                arrierePlan, 
                                (fenetre["display_width"],
                                 fenetre["display_height"]))
arrierePlanIntro = pygame.image.load("./images/intro.jpg").convert()
arrierePlanIntro = pygame.transform.scale(
                                arrierePlanIntro, 
                                (fenetre["display_width"],
                                 fenetre["display_height"]))
icon = pygame.image.load("./images/icon.png")
pygame.display.set_icon(icon)


"""

    Choix couleur (Joueur)

"""
config ={}
FonctionFichier.genererConfig(config)
couleur1 = config["couleurJ1"]
couleur2 = config["couleurJ2"]


if config["multi"].upper() == "TRUE":
    multiJoueur = True
elif config["multi"].upper() == "FALSE":
    multiJoueur = False

clock = pygame.time.Clock()

FPS = 20
vitesseJeu = FPS

direction = "gauche"

smallfont = pygame.font.SysFont("Terminal", 50)
medfont = pygame.font.SysFont("Terminal", 100)
largefont = pygame.font.SysFont("Terminal", 160)


"""

    Musique

"""

main = ["./son/Main1.mp3","./son/Main2.mp3","./son/Main3.mp3"]
game = ["./son/Game1.mp3"]
mort = "./son/Mort.mp3"



main_Theme = lambda : pygame.mixer.music.load("./son/Main"+str(random.randint(1,3))+".mp3")
game_Theme = lambda : pygame.mixer.music.load(game[random.randint(0,(len(game)-1))]) 
mort_Sound = lambda : pygame.mixer.music.load(mort)

def orienterImage(img, direction):
    """Cette fonction prend un sprite et le retourne
    avec une nouvelle orientation dépendament de la direction."""
    # Gauche
    if direction == "gauche":
        img = pygame.transform.rotate(img, 90)
    # Bas
    elif direction == "bas":
        img = pygame.transform.rotate(img, 180)
    # Droite
    elif direction == "droite":
        img = pygame.transform.rotate(img, 270)
    # Haut
    elif direction == "haut":
        img = img
    return img

def ChoixCouleur(couleur):
    """Cette fonction prend en argument une couleur
    et retrourne les sprites de cette couleur."""
    ligne = sprite[couleur]["ligne"]
    coin = sprite[couleur]["coin"]
    spriteJoueur = {"ligne":ligne,
                    "coin":coin}
    return spriteJoueur


def pause():
    """Cette procédure 'loop' jusqu'à ce que le joueur
    appui sur 'P' ou 'Q'."""
    paused = True
    message_to_screen("Pause",
                      couleur["blanc"], -125, size="large")
    message_to_screen("Appuyer sur 'P' afin de continuer ou 'Q' pour quitter.", 
                      couleur["blanc"], 50)
    pygame.display.update()
    
    while paused:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()
            
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_p:
                    paused = False
                elif event.key == pygame.K_q:
                    pygame.quit()
                    quit()
        
        clock.tick(5)
        pygame.display.update()
                    
def memeDiviseur(donner, base):
    """Cette fonction prend en argument un chiffre
    qui va mettre le chiffre sur la même base que l'argument base"""
    donner = (donner//base)*base
    return donner

def randMapCoordGen():
    """Cette fonction retourne une liste de coordonner
    randome dans le terrain de jeu"""
    randX = round(random.randrange(
                            terrain["margin"]["largeur"], 
                            terrain["largeur"] - info["objet"]["largeur"]))
    randX = memeDiviseur(
                    randX, info["joueur"]["largeur"])
    
    randY = round(random.randrange(
                            terrain["margin"]["hauteur"], 
                            terrain["hauteur"] - info["objet"]["hauteur"]))
    randY = memeDiviseur(
                    randY, info["joueur"]["hauteur"])
    
    return [randX, randY]

def affichageTemps(minutes,seconds):
    """Cette procédure affiche le temps du jeu"""
    text = smallfont.render("Temps: " + str(minutes) +\
                            ":"+ str(seconds), True, couleur["bleu"])
    gameDisplay.blit(text, [(terrain["largeur"]/2) -\
                            ( 2*terrain["margin"]["largeur"]),0])


       

def game_intro():
    """Cette fonction est lancé au début du lancement
    du jeu elle affiche les instructions aussi."""
    intro = True
    main_Theme()
    pygame.mixer.music.play(loops = -1)
    
    while intro:
        
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_c:
                    intro = False
                elif event.key == pygame.K_q:
                    pygame.quit()
                    quit()
        gameDisplay.blit(arrierePlanIntro, [0,0])
        message_to_screen("Bienvenu sur Tron!", 
                          couleur["cyan"], -350, size = "large")
        message_to_screen("L'objectif est de piéger", 
                          couleur["blanc"], -200, size = "small")
        message_to_screen("votre ennemi dans votre lumière.", 
                          couleur["blanc"], -100, size = "small")
        message_to_screen("Appuyer sur 'C' afin de jouer ou 'Q' pour quitter.", 
                          couleur["blanc"], 20, size = "small")
        
        pygame.display.update()
        clock.tick(4)
    pygame.mixer.music.stop()

def sortieMap(positionX, positionY):
    """Cette fonction retourne un boolean qui
    informera la fonction principale si elle"""
    mort = False
    if positionX + info["joueur"]["largeur"] >= terrain["largeur"] + \
    terrain["margin"]["largeur"] \
    or positionX < terrain["margin"]["largeur"] \
    or positionY + info["joueur"]["hauteur"] >= terrain["hauteur"] + \
    terrain["margin"]["hauteur"] \
    or positionY < terrain["margin"]["hauteur"]:
        mort = True
    return mort

def collisionJoueur(tabJoueur1, tabJoueur2):
    """Cette fonction compare deux tableaux afin
    de trouver qui à toucher qui."""
    collision = ""
    for eachSegment in tabJoueur1[:-2]:
        if eachSegment[0] == tabJoueur1[-1][0]:
            if eachSegment[1] == tabJoueur1[-1][1]:
                collision = "joueur"
        if eachSegment[0] == tabJoueur2[-1][0]:
            if eachSegment[1] == tabJoueur2[-1][1]:
                collision = "autre"
    if tabJoueur1[-1][0] == tabJoueur2[-1][0] \
    and tabJoueur1[-1][1] == tabJoueur2[-1][1]:
        collision = "null"
    return collision

def gestionCollisionJoueur(moto1Tab,moto2Tab):
    """Cette fonction prend en argument 2 tableaux
    la fonction retourne qui à toucher qui avec
    la fonction 'collisionJoueur'."""
    gameOver = False
    vivant = ""
    
    collision1 = collisionJoueur(moto1Tab, moto2Tab)
    collision2 = collisionJoueur(moto2Tab, moto1Tab)
    if collision1 == "joueur" or collision2 == "autre":
        vivant = couleur2
        gameOver = True
    elif collision1 == "autre" or collision2 == "joueur":
        vivant = couleur1
        gameOver = True
    elif collision1 == "null":
        vivant = "aucun"
        gameOver = True
    if sortieMap(moto1Tab[-1][0], moto1Tab[-1][1]):
            vivant = couleur2
            gameOver = True
            
    elif sortieMap(moto2Tab[-1][0], moto2Tab[-1][1]):
            vivant = couleur1
            gameOver = True
    return vivant, gameOver



def toucheJoueur(event, direction,position_change, diminution, joueur):
    """Cette fonction gère les touches des joueurs."""
    virage = ""
    touche = [[],
              [pygame.K_LEFT,pygame.K_RIGHT,pygame.K_UP,pygame.K_DOWN,pygame.K_KP0],
              [pygame.K_a,pygame.K_d,pygame.K_w,pygame.K_s,pygame.K_LSHIFT]
              ]
    if event.type == pygame.KEYDOWN:
        if event.key == touche[joueur][0]:
            if direction != "droite" and direction != "gauche":
                virage = direction
                direction = "gauche"
                position_change[0] = -info["joueur"]["largeur"]
                position_change[1] = 0
        if event.key == touche[joueur][1]:
            if direction != "gauche" and direction != "droite":
                virage = direction
                direction = "droite"
                position_change[0] = info["joueur"]["largeur"]
                position_change[1] = 0
        if event.key == touche[joueur][2]:
            if direction != "bas" and direction != "haut":
                virage = direction
                direction = "haut"
                position_change[0] = 0
                position_change[1] = -info["joueur"]["hauteur"]
        if event.key == touche[joueur][3]:
            if direction != "bas" and direction != "haut":
                virage = direction
                direction = "bas"
                position_change[0] = 0
                position_change[1] = info["joueur"]["hauteur"]
        if event.key == touche[joueur][4]:
            diminution = -1
        if event.key == pygame.K_p and joueur == 1:
            pause()
    if event.type == pygame.KEYUP:
        if event.key == touche[joueur][0] \
        or event.key == touche[joueur][1] \
        or event.key == touche[joueur][2] \
        or event.key == touche[joueur][3]:
            virage = ""
        if event.key == touche[joueur][4]:
            diminution = 1
    return virage, direction, position_change, diminution

def prochainePosition(position_change,position):
    """Cette fonction prend en argument un nombre
    qui ce résume à être la largeur ou hauteur de la moto
    qui sera additionné avec la position."""
    position[0] += int(position_change[0])
    position[1] += int(position_change[1])
    return position

def ajoutPosition(position,direction,virage):
    """Cette fonction ajoute les nouvelles
    informations dans une nouvelle liste."""
    moto = []
    moto.append(int(position[0]))
    moto.append(int(position[1]))
    moto.append(str(direction))
    moto.append(str(virage))
    return moto

def collisionObjet(position,objet):
    """Cette fonction à pour but de
    tester si une position ce trouve dans un objet"""
    collision = False
    if position[0] > objet[0] and position[0] < objet[0] + \
    info["objet"]["largeur"] or position[0] + \
    info["joueur"]["largeur"] > objet[0] and position[0] + \
    info["joueur"]["largeur"] < objet[0] + info["objet"]["largeur"]:
        if position[1] > objet[1] and position[1] < objet[1] + \
        info["objet"]["hauteur"]:
            collision = True
        elif position[1] + info["joueur"]["hauteur"] > objet[1] \
        and position[1] + info["joueur"]["hauteur"] < objet[1] +\
         info["objet"]["hauteur"]:
            collision = True
    return collision

def gestionCollisionObjet(motoTab,position,randPortail1,randPortail2):
    """Cette fonction gère les collisions des objets qui
    peuvent être dans le terrain de jeux"""
    if collisionObjet(position,randPortail1):
        position = [randPortail2[0],randPortail2[1]]
        motoTab.append(ajoutPosition(position,motoTab[-1][2],motoTab[-1][3]))
        randPortail1[0], randPortail1[1] = randMapCoordGen()
        randPortail2[0], randPortail2[1] = randMapCoordGen()

    elif collisionObjet(position,randPortail2):
        position = [randPortail1[0],randPortail1[1]]
        motoTab.append(ajoutPosition(position,motoTab[-1][2],motoTab[-1][3]))
        randPortail1[0],randPortail1[1] = randMapCoordGen()
        randPortail2[0],randPortail2[1] = randMapCoordGen()
    
    return motoTab,position,randPortail1, randPortail2

def prochainMouvement(position_change,direction, NouvelleDirection):
    """Cette à pour but de donner une nouvelle direction au joueur robot."""
    virage = ""
    if NouvelleDirection == "haut" and direction != "bas":
        virage += direction
        direction = "haut"
        position_change = [0,-info["joueur"]["hauteur"]]
    elif NouvelleDirection == "bas" and direction != "haut":
        virage += direction
        direction = "bas"
        position_change = [0,info["joueur"]["hauteur"]]
    elif NouvelleDirection == "droite" and direction != "gauche":
        virage += direction
        direction = "droite"
        position_change = [info["joueur"]["largeur"],0]
    elif NouvelleDirection == "gauche" and direction != "droite":
        virage += direction
        direction = "gauche"
        position_change = [-info["joueur"]["largeur"],0]
    if virage == NouvelleDirection:
        virage = ""
    return position_change, direction, virage


def robotJoueur(motoTab1,motoTab2,direction,position_change):
    """(Version incomplete Version Alpha)
    Cette fonction ce comporte comme un joueur en trouvant
    qu'elle action il lui est possible d'accomplir 
    et d'exécuter par la suite"""
    motoTabTemp = []
    liste = ["haut","bas","droite","gauche", "", ""]
    positionJoueur = [motoTab1[-1][0],motoTab1[-1][1]]
    positionRobot = [motoTab2[-1][0],motoTab2[-1][1]]
    distanceJoueurX = motoTab1[-1][0] - motoTab2[-1][0]
    if distanceJoueurX < 0:
        distanceJoueurX = distanceJoueurX*-1
    distanceJoueurY = motoTab1[-1][1] - motoTab2[-1][1]
    if distanceJoueurY < 0:
        distanceJoueurY = distanceJoueurY*-1
    if direction[0] == " ":
        direction = direction[0:]
    NouvelleDirection = liste[random.randrange(0,5)]
    while NouvelleDirection == direction:
        NouvelleDirection = liste[random.randrange(0,5)]
    position_change, direction, virage = prochainMouvement(
                                                position_change,
                                                direction, NouvelleDirection)
    motoTabTemp += motoTab2 + [[positionRobot[0] + position_change[0],
                                positionRobot[1] + position_change[1], 
                                direction, virage]]
    if sortieMap(positionRobot[0] + position_change[0], positionRobot[1] + \
                 position_change[1]) or sortieMap(positionRobot[0] + \
                2*position_change[0], positionRobot[1] + \
                2*position_change[1]) or (gestionCollisionJoueur(
                                                            motoTab2, 
                                                            motoTabTemp)[1]):
        test = ""
        test += direction
        if test == "droite":
            motoTabTemp[-1][0] = 0
            motoTabTemp[-1][1] = -info["joueur"]["hauteur"]
            if (gestionCollisionJoueur(motoTab2, motoTabTemp)[1]):
                motoTabTemp[-1][0] = 0
                motoTabTemp[-1][1] = info["joueur"]["hauteur"]
        if test == "gauche":
            motoTabTemp[-1][0] = 0
            motoTabTemp[-1][1] = info["joueur"]["hauteur"]
            if (gestionCollisionJoueur(motoTab2, motoTabTemp)[1]):
                motoTabTemp[-1][0] = 0
                motoTabTemp[-1][1] = -info["joueur"]["hauteur"]
        if test == "haut":
            motoTabTemp[-1][0] = -info["joueur"]["largeur"]
            motoTabTemp[-1][1] = 0
            if (gestionCollisionJoueur(motoTab2, motoTabTemp)[1]):
                motoTabTemp[-1][0] = info["joueur"]["largeur"]
                motoTabTemp[-1][1] = 0    
        if test == "bas":
            motoTabTemp[-1][0] = info["joueur"]["largeur"]
            motoTabTemp[-1][1] = 0
            if (gestionCollisionJoueur(motoTab2, motoTabTemp)[1]):
                motoTabTemp[-1][0] = -info["joueur"]["largeur"]
                motoTabTemp[-1][1] = 0
    return virage, direction, position_change


def GestionJoueur(motoTab,spriteJoueur):
    """Cette fonction gère les images du joueurs
    dépendament son virage et sa nouvelle direction"""
    direction = motoTab[-1][2]
    head = orienterImage(sprite["joueur2"]["devant"], direction)
    arriere = orienterImage(sprite["joueur2"]["arriere"], direction)
    ligneVertical = pygame.transform.rotate(spriteJoueur["ligne"], 90)
    for position, element in enumerate(motoTab[:-2]):
        coordonner = (element[0],element[1])
        if element[2] == element[3]:   
            element[3] = ""
        
        if element[2] == element[3]:
                element[3] = ""
        if motoTab[position][1] == motoTab[position + 2][1]:
            if motoTab[position][0] != motoTab[position + 2][0]:
                motoTab[position + 1][3] = ""
        
        elif motoTab[position][1] < motoTab[position + 1][1]:
            if motoTab[position + 1][0] != motoTab[position + 1][0]:
                element[3] = "haut"
        elif motoTab[position][1] > motoTab[position + 1][1]:
            if motoTab[position][0] != motoTab[position + 1][0]:
                element[3] = "bas"
        if motoTab[position][0] == motoTab[position + 2][0]:
            if motoTab[position][1] != motoTab[position + 2][1]:
                motoTab[position + 1][3] = ""
        
        if element[3] == "":
            if element[2] == "droite" or element[2] == "gauche":
                gameDisplay.blit(ligneVertical, coordonner)
            elif element[2] == "haut" or element[2] == "bas":
                gameDisplay.blit(spriteJoueur["ligne"], coordonner)
        else:
            if element[2] == "gauche" or element[2] == "bas":
                if element[3] == "haut" or element[3] == "droite":
                    gameDisplay.blit(spriteJoueur["coin"]["DH"],coordonner)
                elif element[3] == "bas":
                    gameDisplay.blit(spriteJoueur["coin"]["DB"],coordonner)
                elif element[3] == "gauche":
                    gameDisplay.blit(spriteJoueur["coin"]["GH"],coordonner)
                        
            elif element[2] == "droite" or element[2] == "haut":
                if element[3] == "bas" or element[3] == "gauche":
                    gameDisplay.blit(spriteJoueur["coin"]["GB"],coordonner) 
                elif element[3] == "haut":
                    gameDisplay.blit(spriteJoueur["coin"]["GH"],coordonner)
                elif element[3] == "droite":
                    gameDisplay.blit(spriteJoueur["coin"]["DB"],coordonner)
    gameDisplay.blit(head, (motoTab[-1][0],motoTab[-1][1]))
    gameDisplay.blit(arriere, (motoTab[-2][0],motoTab[-2][1]))


def restreindreLongueur(motoTab, longueurMoto):
    """Cette procédure diminue la longueur de la tracer
    de la moto"""
    while longueurMoto != len(motoTab):
        del motoTab[0]
        
def gestionLongueur(motoTab,longueurMoto, diminution):
    """Cette fonction gère la longueur de la tracer 
    si c'est plus grand que la longueur qu'il est
    supposer avoir. Le tableau sera envoyer à
    la procédure 'restreindreLongueur'."""
    longueurMoto += int(diminution)
    if len(motoTab) > int(longueurMoto):
        restreindreLongueur(motoTab, longueurMoto)
    return motoTab, longueurMoto
   
def text_object(text, color, size):
    """Cette fonction prend en argument un texte,
    une couleur et une grandeur de texte afin de
    retourner une surface avec du texte."""
    if size == "small":
        textSurface = smallfont.render(text, True, color)
    elif size == "medium":
        textSurface = medfont.render(text, True, color)
    elif size == "large":
        textSurface = largefont.render(text, True, color)
    elif size == "test":
        textSurface = pygame.font.SysFont("Terminal",
                                          630).render(text, True, color)
    return textSurface, textSurface.get_rect()


def message_to_screen(msg,color, y_displace=0, x_displace=0, size= "small"):
    """Cette procédure affiche un texte à une position et une
    grandeur par rapport au centre de l'écran."""
    textSurf, textRect = text_object(msg, color, size)
    textRect.center = (fenetre["display_width"] / 2) + x_displace, \
                        (fenetre["display_height"] / 2) + y_displace
    gameDisplay.blit(textSurf, textRect)


def debutJeux():
    spriteJ1 = ChoixCouleur(couleur1)
    spriteJ2 = ChoixCouleur(couleur2)
    
    direction1 = "droite"
    virage1 = ""

    direction2 = "gauche"
    virage2 = ""

    milieuX = terrain["largeur"]/2 + terrain["margin"]["largeur"]
    milieuY = terrain["hauteur"]/2 + terrain["margin"]["hauteur"]
    
    position1_change = [info["joueur"]["largeur"],0]
    
    position2_change = [-info["joueur"]["largeur"],0]
    
    positionX1 = memeDiviseur((milieuX + (3*info["joueur"]["largeur"])),
                              info["joueur"]["largeur"])
    positionY1 = memeDiviseur(milieuY, 
                              info["joueur"]["hauteur"])
    
    position1 = [positionX1, positionY1]
        
    positionX2 = memeDiviseur((milieuX - (3*info["joueur"]["largeur"])),
                              info["joueur"]["largeur"])
    positionY2 = memeDiviseur(milieuY, 
                              info["joueur"]["hauteur"])
    
    position2 = [positionX2, positionY2]
    
    moto1Tab = [[position1[0] - info["joueur"]["largeur"],
                    position1[1], direction1, virage1],
                [position1[0],position1[1], direction1, virage1]]
    moto2Tab = [[position2[0] + info["joueur"]["largeur"],
                    position2[1], direction2, virage2],
                [position2[0],position2[1], direction2, virage2]]
    
    randPortail1 = randMapCoordGen()
    randPortail2 = randMapCoordGen()
    
    milliseconds = 0
    seconds = 0
    
    count = 0
    
    decompte = 3
    temps = pygame.time.Clock()
    game_Theme()
    pygame.mixer.music.play(loops = -1)
    while seconds < 4:
        gameDisplay.blit(arrierePlan,[0,0])
        pygame.draw.rect(gameDisplay, couleur["cyan"], 
                        (int(fenetre["display_width"]*0.02),
                        int(fenetre["display_height"]*0.03),
                        terrain["largeur"],terrain["hauteur"]),
                        5)
        pygame.draw.rect(gameDisplay, 
                        couleur["blanc"], 
                        (int(fenetre["display_width"]*0.02),
                        int(fenetre["display_height"]*0.03),
                        terrain["largeur"],terrain["hauteur"]),
                        1)
        GestionJoueur(moto1Tab,spriteJ1)
        GestionJoueur(moto2Tab,spriteJ2)
        
        count += 1
        if milliseconds > 1000:
                seconds += 1
                decompte -= 1
                milliseconds -= 1000
        if seconds > 60:
            seconds -= 60
        if count > 7:
            count = 0
        if milliseconds >= 0:
            gameDisplay.blit(sprite["portail"][count],
                            (randPortail1[0],
                            randPortail1[1]))
            gameDisplay.blit(sprite["portail"][count],
                            (randPortail2[0],
                            randPortail2[1]))
        if decompte > 0:
            message_to_screen(str(decompte), couleur["rouge"], 
                              0, size = "test")
        else:
            message_to_screen("GO", couleur["cyan"], 
                              0, size = "test")
            
        
        pygame.display.update()
        milliseconds += temps.tick_busy_loop(FPS)
    return spriteJ1, spriteJ2, position1, position2, randPortail1, randPortail2
        
def gameloop(gameDisplay):
    """Cette fonction va 'looper' tant que l'on ne quitte pas le jeu
    Les méthodes pour quitter sont d'appuyer sur la lettre 'Q' ou
    d'appuyer sur le 'X' de la fenêtre. Par contre, cela est impossible,
    puisque le mode plein écran est activer et seul la modification 
    du code peu changer cela.
    """
    
    spriteJ1, spriteJ2, position1, \
    position2, randPortail1, randPortail2 = debutJeux()
    
    direction1 = "droite"
    virage1 = ""

    direction2 = "gauche"
    virage2 = ""
    
    gameExit = False
    gameOver = False
    
    diminution1 = 1
    diminution2 = 1

    vivant = ""
    
    position1_change = [info["joueur"]["largeur"],0]
    
    position2_change = [-info["joueur"]["largeur"],0]
    

    moto1Tab = [[position1[0] - info["joueur"]["largeur"],
                    position1[1], direction1, virage1],
                [position1[0],position1[1], direction1, virage1]]
    moto2Tab = [[position2[0] + info["joueur"]["largeur"],
                    position2[1], direction2, virage2],
                [position2[0],position2[1], direction2, virage2]]
    
    longueurMoto1 = 2
    longueurMoto2 = 2
    
    
    milliseconds = 0
    seconds = 0
    minutes = 0
    FPS = vitesseJeu
    count = 0
    while not gameExit:
        
        virage1 = ""
        virage2 = ""
        
        if gameOver == True:
            if vivant != "aucun":   
                couleurVivant = vivant
            else:
                couleurVivant = "blanc"
            vivant = vivant[0].upper() + vivant[1:]
            message_to_screen("Partie terminée", couleur["rouge"], 
                              -50, size = "large")
            message_to_screen(vivant + " a gagné!", couleur[couleurVivant], 
                              60, size="medium")
            message_to_screen("Appuyer sur 'C' afin de continuer et 'Q' pour quitter.", 
                              couleur["blanc"], 150, size="medium")
            pygame.display.update()
    
        while gameOver == True:
            milliseconds = 0
            seconds = 0
            minutes = 0
            
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    gameOver = False
                    gameExit = True
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_q:
                        gameExit = True
                        gameOver = False
                    if event.key== pygame.K_c:
                        gameloop(gameDisplay)
 
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                gameExit = True
                gameOver = False
                
            virage1, direction1, \
            position1_change, diminution1 = toucheJoueur(
                                                    event, 
                                                    direction1,
                                                    position1_change,
                                                    diminution1,
                                                    1)
            if multiJoueur:
                virage2, direction2, \
                position2_change, diminution2 = toucheJoueur(
                                                        event, 
                                                        direction2,
                                                        position2_change,
                                                        diminution2,
                                                        2)
        
        if not multiJoueur and ((count % 4) == 0) and gameOver == False:
            virage2, direction2, position2_change = robotJoueur(
                                                            moto1Tab,
                                                            moto2Tab,
                                                            direction2,
                                                            position2_change)
        if virage1 != "" and moto1Tab[-1][-1] != virage1: 
            moto1Tab[-1][-1] =  virage1
            
        if virage2 != "" and moto2Tab[-1][-1] != virage2: 
            moto2Tab[-1][-1] =  virage2 
        
        moto1Tab.append(ajoutPosition(position1,direction1,virage1))
        moto2Tab.append(ajoutPosition(position2,direction2,virage2))    
        
        moto1Tab, longueurMoto1 = gestionLongueur(moto1Tab,
                                                  diminution1,
                                                  longueurMoto1)
        moto2Tab, longueurMoto2 = gestionLongueur(moto2Tab,
                                                  diminution2,
                                                  longueurMoto2)
        gameDisplay.blit(arrierePlan,[0,0])
        pygame.draw.rect(gameDisplay, couleur["cyan"], 
                        (int(fenetre["display_width"]*0.02),
                        int(fenetre["display_height"]*0.03),
                        terrain["largeur"],terrain["hauteur"]),
                        5)
        pygame.draw.rect(gameDisplay, 
                        couleur["blanc"], 
                        (int(fenetre["display_width"]*0.02),
                        int(fenetre["display_height"]*0.03),
                        terrain["largeur"],terrain["hauteur"]),
                        1)
        GestionJoueur(moto1Tab,spriteJ1)
        GestionJoueur(moto2Tab,spriteJ2)
        
        position2 = prochainePosition(position2_change,position2)
        position1 = prochainePosition(position1_change,position1)
        
        if longueurMoto1 < info["joueur"]["longueurMin"]:
            longueurMoto1 = info["joueur"]["longueurMin"]
        if longueurMoto2 < info["joueur"]["longueurMin"]:
            longueurMoto2 = info["joueur"]["longueurMin"]
        
        count += 1
        if milliseconds > 1000:
                FPS += 0.5
                seconds += 1
                milliseconds -= 1000
        if seconds > 60:
            minutes += 1
            seconds -= 60
        if count > 7:
            count = 0
        if milliseconds >= 0:
            gameDisplay.blit(sprite["portail"][count],
                            (randPortail1[0],
                            randPortail1[1]))
            gameDisplay.blit(sprite["portail"][count],
                            (randPortail2[0],
                            randPortail2[1]))
        
        vivant, gameOver = gestionCollisionJoueur(moto1Tab,moto2Tab)
        
        if gameOver:
					
            mort_Sound()
            
            pygame.mixer.music.play(loops = 0)
        
        moto1Tab,position1,\
        randPortail1, randPortail2 = gestionCollisionObjet(
                                                    moto1Tab,position1,
                                                    randPortail1, randPortail2)
        moto2Tab,position2,\
        randPortail1, randPortail2 = gestionCollisionObjet(
                                                    moto2Tab,position2,
                                                    randPortail1, randPortail2)

        affichageTemps(math.floor(minutes),math.floor(seconds))
        
        pygame.display.update()
        milliseconds += clock.tick_busy_loop(int(FPS))
    
    pygame.mixer.music.stop()
    gameDisplay.fill(couleur["noir"]) 
    pygame.display.update()
    pygame.time.wait(500)
    pygame.quit()
    quit()
    
game_intro()
gameloop(gameDisplay)
