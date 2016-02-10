'''
###########################################################################
#                                                                         #
#                        Fichier: Teste.py                                #
#                  Fait par: Guillaume Hamel-Gagné                        #
#                Travail Finale: (Tron light cycle)                       #
#               Dernière fois modifier: 28 May 2015                       #
#                                                                         #
#               Afin de faire les testes il faut mettre                   #
#               en commentaire game_intro() et                            #
#               gameloop(gameDisplay) dans le fichier                     #
#               Tron.py sinon le jeu sera lancé                           #
#                                                                         #
###########################################################################
'''
import Tron
"""Les fonctions ci-dessous
    n'on pas été tester, car il est difficile de
    tester quand ce que sa retourne est une
    classe comme une surface ou une image ou
    un dictionnaire ayant besoin de variable
    que l'on a automatiquement avec des fonctions
    de pygame en lanceant le jeu.

orienterImage(img, direction)
toucheJoueur(event, direction,position_change, diminution, joueur)
text_object(text, color, size)    
dictSprite(info)    
dictTerrain(fenetre)
dictInfo(terrain)

-Tron.py

gestionLongueur(motoTab,longueurMoto, diminution)
"""

def testeChoixCouleur():
    fonctionnel = True
    chiffre = 1
    cleInconnu = "abcdfz"
    liste = [1]
    couleurFonctionnel = "cyan"
    try:
        Tron.ChoixCouleur(chiffre)
    except KeyError:
        print("Fonctionnel")
    else:
        print("La fonction ChoixCouleur accepte les chiffres")
        fonctionnel = False
    try:
        Tron.ChoixCouleur(cleInconnu)
    except KeyError:
        print("Fonctionnel")
    else:
        print("La fonction ChoixCouleur accepte une clé inconnu")
        fonctionnel = False
    try:
        Tron.ChoixCouleur(liste)
    except TypeError:
        print("Fonctionnel")
    else:
        print("La fonction ChoixCouleur accepte les listes.")
        fonctionnel = False
    if fonctionnel:
        try:
            Tron.ChoixCouleur(couleurFonctionnel)
        except KeyError:
            print("La fonction ChoixCouleur ne fonctionne pas.")
        else:
            print("La fonction ChoixCouleur fonctionne entièrement.")
            
def testeMemeDiviseur():
    fonctionnel = True
    lettre = "a"
    liste = ["a"]
    donner = 418
    base = 20
    try:
        Tron.memeDiviseur(lettre,base)
    except TypeError:
        print("Fonctionnel")
    else:
        print("La fonction memeDiviseur prend des strings pour la donner")
        fonctionnel = False
    try:
        Tron.memeDiviseur(donner,lettre)
    except TypeError:
        print("Fonctionnel")
    else:
        print("La fonction memeDiviseur prend des strings pour la base")
        fonctionnel = False
    try:
        Tron.memeDiviseur(liste,base)
    except TypeError:
        print("Fonctionnel")
    else:
        print("La fonction memeDiviseur prend des listes")
        fonctionnel = False
    if fonctionnel:
        bonneRep = 400
        if Tron.memeDiviseur(donner,base) == bonneRep:
            print("La fonction memeDiviseur fonctionne entièrement.")
        else:
            print("La fonction memeDiviseur ne donne pas ce qu'elle doit.")
        

def testeSortieMap():
    fonctionnel = True
    positionX = 100
    positionY = 200
    lettre = "a"
    liste = ["a"]
    try:
        Tron.sortieMap(lettre,positionY)
    except TypeError:
        print("Fonctionnel")
    else:
        print("""La fonction sortieMap prend des strings 
        pour l'une des positions""")
        fonctionnel = False
    try:
        Tron.sortieMap(liste,positionY)
    except TypeError:
        print("Fonctionnel")
    else:
        print("La fonction sortieMap prend des listes")
        fonctionnel = False
    if fonctionnel:
        if not Tron.sortieMap(positionX,positionY) and Tron.sortieMap(-40,0):
            print("La fonction sortieMap fonctionne entièrement.")
        else:
            print("""La fonction sortieMap ne voit pas si 
            les coordonners sont hors ou dans la zone de jeu.""")
    

def testeCollisionJoueur():
    fonctionnel = True
    tabJoueur1 = [[999.0, 570.0, 'gauche', ''], [990.0, 570.0, 'gauche', ''], 
                  [990, 570, 'haut', ''], [990, 560, 'haut', ''], 
                  [990, 550, 'haut', ''], [990, 540, 'haut', ''], 
                  [990, 530, 'haut', ''], [990, 520, 'haut', ''], 
                  [990, 510, 'haut', ''], [990, 500, 'haut', ''], 
                  [990, 490, 'droite', 'haut'], [999, 490, 'droite', ''], 
                  [1008, 490, 'droite', ''], [1017, 490, 'droite', ''], 
                  [1026, 490, 'droite', ''], [1035, 490, 'droite', ''], 
                  [1044, 490, 'droite', ''], [1053, 490, 'droite', ''], 
                  [1062, 490, 'haut', 'droite'], [1062, 480, 'haut', '']]
    tabJoueur2 = [[1035.0, 570.0, 'droite', ''], [1044.0, 570.0, 'droite', ''],
                   [1044, 570, 'droite', ''], [1053, 570, 'droite', ''],
                    [1062, 570, 'droite', ''], [1071, 570, 'droite', ''],
                    [1080, 570, 'haut', 'droite'], [1080, 560, 'haut', ''],
                    [1080, 550, 'haut', ''], [1080, 540, 'gauche', ''],
                    [1071, 540, 'gauche', ''], [1062, 540, 'gauche', ''],
                    [1053, 540, 'gauche', ''], [1044, 540, 'gauche', ''], 
                    [1035, 540, 'gauche', ''], [1026, 540, 'gauche', ''], 
                    [1017, 540, 'gauche', ''], [1008, 540, 'gauche', ''], 
                    [999, 540, 'gauche', ''], [990, 540, 'gauche', '']]
    chiffre = 1
    lettre = "a"
    try:
        Tron.collisionJoueur(chiffre,tabJoueur2)
    except TypeError:
        print("Fonctionnel")
    else:
        print("""La fonction collisionJoueur ne fonctionne pas.
Elle prend des chiffres.""")
        fonctionnel = False
    if fonctionnel:
        if Tron.collisionJoueur(tabJoueur1,tabJoueur2) == "autre" \
        and Tron.collisionJoueur(tabJoueur2,tabJoueur1) == "joueur": 
            print("La fonction collisionJoueur fonctionne entièrement.")
        else:
            print("La fonction ne donne pas les bonnes valeurs.")

def testeGestionCollisionJoueur():
    fonctionnel = True
    tabJoueur1 = [[999.0, 570.0, 'gauche', ''], [990.0, 570.0, 'gauche', ''], 
                    [990, 570, 'haut', ''], [990, 560, 'haut', ''], 
                    [990, 550, 'haut', ''], [990, 540, 'haut', ''], 
                    [990, 530, 'haut', ''], [990, 520, 'haut', ''], 
                    [990, 510, 'haut', ''], [990, 500, 'haut', ''], 
                    [990, 490, 'droite', 'haut'], [999, 490, 'droite', ''], 
                    [1008, 490, 'droite', ''], [1017, 490, 'droite', ''], 
                    [1026, 490, 'droite', ''], [1035, 490, 'droite', ''], 
                    [1044, 490, 'droite', ''], [1053, 490, 'droite', ''], 
                    [1062, 490, 'haut', 'droite'], [1062, 480, 'haut', '']]
    tabJoueur2 = [[1035.0, 570.0, 'droite', ''], [1044.0, 570.0, 'droite', ''],
                    [1044, 570, 'droite', ''], [1053, 570, 'droite', ''],
                    [1062, 570, 'droite', ''], [1071, 570, 'droite', ''],
                    [1080, 570, 'haut', 'droite'], [1080, 560, 'haut', ''],
                    [1080, 550, 'haut', ''], [1080, 540, 'gauche', ''],
                    [1071, 540, 'gauche', ''], [1062, 540, 'gauche', ''],
                    [1053, 540, 'gauche', ''], [1044, 540, 'gauche', ''], 
                    [1035, 540, 'gauche', ''], [1026, 540, 'gauche', ''], 
                    [1017, 540, 'gauche', ''], [1008, 540, 'gauche', ''], 
                    [999, 540, 'gauche', ''], [990, 540, 'gauche', '']]
    chiffre = 1
    lettre = "a"
    try:
        Tron.gestionCollisionJoueur(chiffre,tabJoueur2)
    except TypeError:
        print("Fonctionnel")
    else:
        print("""La fonction gestionCollisionJoueur ne fonctionne pas.
        Elle prend des chiffres.""")
        fonctionnel = False
    try:
        Tron.gestionCollisionJoueur(lettre,tabJoueur2)
    except (TypeError, IndexError):
        print("Fonctionnel")
    else:
        print("""La fonction gestionCollisionJoueur ne fonctionne pas.
        Elle prend des strings.""")
        fonctionnel = False
    if fonctionnel:
        if Tron.gestionCollisionJoueur(tabJoueur1,tabJoueur2)[1]:
            print("La fonction gestionCollisionJoueur fonctionne entièrement")
        else:
            print("""La fonction gestionCollisionJoueur ne donne pas
ce qu'elle devrait.""")
            

            

def testeGestionLongueur():
    fonctionnel = True
    motoTab = [[1035.0, 570.0, 'droite', ''], [1044.0, 570.0, 'droite', ''],
                [1044, 570, 'droite', ''], [1053, 570, 'droite', ''],
                [1062, 570, 'droite', ''], [1071, 570, 'droite', ''],
                [1080, 570, 'haut', 'droite'], [1080, 560, 'haut', ''],
                [1080, 550, 'haut', ''], [1080, 540, 'gauche', ''],
                [1071, 540, 'gauche', ''], [1062, 540, 'gauche', ''],
                [1053, 540, 'gauche', ''], [1044, 540, 'gauche', ''], 
                [1035, 540, 'gauche', ''], [1026, 540, 'gauche', ''], 
                [1017, 540, 'gauche', ''], [1008, 540, 'gauche', ''], 
                [999, 540, 'gauche', ''], [990, 540, 'gauche', '']]
    longueurMoto = 5
    diminution = 1
    lettre = "a"
    try:
        Tron.gestionLongueur(motoTab,longueurMoto,lettre)
    except ValueError:
        print("Fonctionnel")
    else:
        print("""La fonction gestionLongueur ne fonctionne pas.
Elle prend un string en troisième argument.""")
        fonctionnel = False
    try:
        Tron.gestionLongueur(motoTab,lettre,diminution)
    except TypeError:
        print("Fonctionnel")
    else:
        print("""La fonction gestionLongueur ne fonctionne pas.
Elle prend un string en deuxième argument.""")
        fonctionnel = False
    if fonctionnel:
        motoTab, longueur = Tron.gestionLongueur(motoTab,
                                                 longueurMoto,
                                                 diminution)
        if len(motoTab) == longueur:
            print("La fonction gestionLongueur fonctionne entièrement.")
        else:
            print("""La fonction gestionLongueur ne donne pas
la réponse attendu""")
        
        
testeChoixCouleur()
testeMemeDiviseur()
testeSortieMap()
testeCollisionJoueur()
testeGestionCollisionJoueur()
testeGestionLongueur()