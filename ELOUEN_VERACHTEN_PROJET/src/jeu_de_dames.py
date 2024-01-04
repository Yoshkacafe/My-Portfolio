import time
from tkinter import *
from tkinter import ttk
from tkinter import messagebox
from random import randrange

# DEFINITION DE LA FENETRE TKINTER #

WIDTH = 500
HEIGHT = 700
root = Tk()
canva = Canvas(root, width=WIDTH, height=HEIGHT)
root.configure(padx=25, pady=25) 
root.title("Jeu de dames multijoueur - Jouez avec vos amis !")
root.resizable(width=False, height=False) 
canva.pack()

# Définition des variables et images #

piont_mange_equipe_noir = 0
piont_mange_equipe_blanc = 0
noirRempli = PhotoImage(file="DamesNoirRempliFondNoir.png")
blancRempli = PhotoImage(file="Dames-Blanc-Rempli-Fond-Noir.png")
blanc = PhotoImage(file="Dames-Blanc_Vide.png")
noir = PhotoImage(file="Dames-Noir_Vide.png")
demi_Blanc = PhotoImage(file="demi_Blanc.png")
demi_Noir = PhotoImage(file="demi_Noir.png")
reine_blanc = PhotoImage(file="Reine-Blanche.png")
reine_noir = PhotoImage(file="Reine-Noir.png")
demi_reine_blanc = PhotoImage(file="demi_Reine_Blanc.png")
demi_reine_noir = PhotoImage(file="demi_Reine_Noir.png")
zero = PhotoImage(file="0(1).png")
un = PhotoImage(file="1(1).png")
deux = PhotoImage(file="2(1).png")
trois = PhotoImage(file="3(2).png")
quatre = PhotoImage(file="4(2).png")
cinq = PhotoImage(file="5(1).png")
six = PhotoImage(file="6(1).png")
sept = PhotoImage(file="7(1).png")
huit = PhotoImage(file="8(1).png")
seuf = PhotoImage(file="9(1).png")
dix = PhotoImage(file="10(1).png")
onze = PhotoImage(file="11(1).png")
douze = PhotoImage(file="12(1).png")
treize = PhotoImage(file="13(1).png")
quatorze = PhotoImage(file="14(1).png")
quinze = PhotoImage(file="15(1).png")
seize = PhotoImage(file="16(1).png")
dix_sept = PhotoImage(file="17(1).png")
dix_huit = PhotoImage(file="18(1).png")
dix_seuf = PhotoImage(file="19(1).png")
vingt = PhotoImage(file="20(1).png")
gagnant_blanc = PhotoImage(file="gagnant_blanc.png")
gagnant_noir = PhotoImage(file="gagnant_noir.png")

# Définition de la liste des pions et de la listes des points representants des images #

listee = [blanc, noirRempli, blanc, noirRempli, blanc, noirRempli, blanc, noirRempli, blanc, noirRempli, 
        noirRempli, blanc, noirRempli, blanc, noirRempli, blanc, noirRempli, blanc, noirRempli, blanc,
        blanc, noirRempli, blanc, noirRempli, blanc, noirRempli, blanc, noirRempli, blanc, noirRempli, 
        noirRempli, blanc, noirRempli, blanc, noirRempli, blanc, noirRempli, blanc, noirRempli, blanc,
        blanc, noir, blanc, noir, blanc, noir, blanc, noir, blanc, noir,
        noir, blanc, noir, blanc, noir, blanc, noir, blanc, noir, blanc,
        blanc, blancRempli, blanc, blancRempli, blanc, blancRempli, blanc, blancRempli, blanc, blancRempli,
        blancRempli, blanc, blancRempli, blanc, blancRempli, blanc, blancRempli, blanc, blancRempli, blanc,
        blanc, blancRempli, blanc, blancRempli, blanc, blancRempli, blanc, blancRempli, blanc, blancRempli,
        blancRempli, blanc, blancRempli, blanc, blancRempli, blanc, blancRempli, blanc, blancRempli, blanc]

list_numero = [zero, un, deux, trois, quatre, cinq, six, sept, huit, seuf, dix,
               onze, douze, treize, quatorze, quinze, seize, dix_sept, dix_huit, dix_seuf, vingt]

#Création de la fonction affichage() qui permet d'afficher grâce à Tkinter un damier #
def affichage():
    """
    Cette fonction permet d'afficher le tableau et de supprimer l'ancien quand un clic a lieu.  
    """
    canva.delete('all')
    # Définition des variables pour l'axe X et Y de la fenêtre Tkinter #
    x, y = 25, 25
    x2 = 25
    x3 = 25
    x4 = 25
    x5 = 25
    x6 = 25
    x7 = 25
    x8 = 25
    x9 = 25
    x10 = 25
    # Boucles pour création du damiers #
    for i in range(100):
        if i < 10:
            id_pion = canva.create_image(x, y, image=listee[i])
            x += 50
        elif i >= 10 and i < 20:
            id_pion = canva.create_image(x2, y + 50, image=listee[i])
            x2 += 50
        elif i >= 20 and i < 30:
            id_pion = canva.create_image(x3, y + 100, image=listee[i])
            x3 += 50
        elif i >= 30 and i < 40:
            id_pion = canva.create_image(x4, y + 150, image=listee[i])
            x4 += 50
        elif i >= 40 and i < 50:
            id_pion = canva.create_image(x5, y + 200, image=listee[i])
            x5 += 50
        elif i >= 50 and i < 60:
            id_pion = canva.create_image(x6, y + 250, image=listee[i])
            x6 += 50
        elif i >= 60 and i < 70:
            id_pion = canva.create_image(x7, y + 300, image=listee[i])
            x7 += 50
        elif i >= 70 and i < 80:
            id_pion = canva.create_image(x8, y + 350, image=listee[i])
            x8 += 50
        elif i >= 80 and i < 90:
            id_pion = canva.create_image(x9, y + 400, image=listee[i])
            x9 += 50
        elif i >= 90 and i < 100:
            id_pion = canva.create_image(x10, y + 450, image=listee[i])
            x10 += 50
    
    # Affichage des points
    score_blanc = canva.create_image(175, 600, image=list_numero[piont_mange_equipe_blanc])
    score_noir = canva.create_image(325, 600, image=list_numero[piont_mange_equipe_noir])

    # Vérification du gagnant à chaque clique

    if piont_mange_equipe_blanc == 20:
        gagnant = canva.create_image(250, 250, image=gagnant_blanc)
        score = open('scores.txt', 'w')
        score.write(piont_mange_equipe_noir, piont_mange_equipe_blanc)
        score.close()
    if piont_mange_equipe_noir == 20:
        gagnant = canva.create_image(250, 250, image=gagnant_noir)
        score = open('scores.txt', 'w')
        score.write(piont_mange_equipe_noir, piont_mange_equipe_blanc)
        score.close()

affichage()

white = True
# Fonction principal regroupant tous les déplacements lors d'un clic #
def clique(event):
    """
    Cette fonction permet de déplacer les pions lors d'un clic sur une case si possible.
    """
    global piont_mange_equipe_blanc
    global piont_mange_equipe_noir
    global white
    global x, y
    x, y = event.x, event.y
 
    # X et Y representent ici les coordonées du numero de la case cliqué #
    x = x // 50 + 1
    y = y // 50 + 1

    # Numero de la case touché dans la liste #
    numero_case_touched = (10 * (y - 1) + x) - 1

    # Vérification de la case, et si vérification ok, affichage des possibilités de déplacements et déplacement du pion (pion normal seulement) #
    if numero_case_touched >= 12 and numero_case_touched < 89:
        canMove = False
        first_diagonal = listee[numero_case_touched - 11]
        second_diagonal = listee[numero_case_touched - 9]
        third_diagonal = listee[numero_case_touched + 9]
        fourth_diagonal = listee[numero_case_touched + 11]

        if first_diagonal == noir or second_diagonal == noir or third_diagonal == noir or fourth_diagonal == noir:
            canMove = True
        else:
            canMove = False
        if white == True:
            if listee[numero_case_touched] == blancRempli:
                for i in range(len(listee)):
                    if listee[i] == demi_Blanc and (i != numero_case_touched - 11 and i != numero_case_touched - 9 and i != numero_case_touched + 11 and i != numero_case_touched + 9):
                        listee[i] = noir
            if listee[numero_case_touched] == blancRempli:
                global a_supprimer 
                a_supprimer = numero_case_touched
            if first_diagonal == noir and listee[numero_case_touched] == blancRempli:
                listee[numero_case_touched - 11] = demi_Blanc
            if second_diagonal == noir and listee[numero_case_touched] == blancRempli:
                listee[numero_case_touched - 9] = demi_Blanc
            if first_diagonal == noirRempli and listee[numero_case_touched] == blancRempli and listee[numero_case_touched - 22] == noir:
                listee[numero_case_touched - 22] = demi_Blanc
            if second_diagonal == noirRempli and listee[numero_case_touched] == blancRempli and listee[numero_case_touched - 18] == noir:
                listee[numero_case_touched - 18] = demi_Blanc
            if third_diagonal == noirRempli and listee[numero_case_touched] == blancRempli and listee[numero_case_touched + 18] == noir:
                listee[numero_case_touched + 18] = demi_Blanc
            if fourth_diagonal == noirRempli and listee[numero_case_touched] == blancRempli and listee[numero_case_touched + 22] == noir:
                listee[numero_case_touched + 22] = demi_Blanc
            if listee[numero_case_touched] == demi_Blanc:
                listee[numero_case_touched] = blancRempli
                for i in range(len(listee)):
                    if listee[i] == demi_Blanc:
                        listee[i] = noir
                if a_supprimer - numero_case_touched == 18:
                    listee[numero_case_touched + 9] = noir
                    piont_mange_equipe_blanc += 1
                if a_supprimer - numero_case_touched == 22:
                    listee[numero_case_touched + 11] = noir
                    piont_mange_equipe_blanc += 1
                if numero_case_touched - a_supprimer == 22:
                    listee[numero_case_touched - 11] = noir
                    piont_mange_equipe_blanc += 1
                if numero_case_touched - a_supprimer == 18:
                    listee[numero_case_touched - 9] = noir
                    piont_mange_equipe_blanc += 1
                listee[a_supprimer] = noir
                white = False
        else:
            if listee[numero_case_touched] == noirRempli:
                for i in range(len(listee)):
                    if listee[i] == demi_Noir and (i != numero_case_touched - 11 and i != numero_case_touched - 9 and i != numero_case_touched + 11 and i != numero_case_touched + 9):
                        listee[i] = noir
             
            if listee[numero_case_touched] == noirRempli:
                a_supprimer = numero_case_touched
            if listee[numero_case_touched] == noirRempli and (numero_case_touched == 1 or numero_case_touched == 11 or numero_case_touched == 21 or numero_case_touched == 31 or numero_case_touched == 41 or numero_case_touched == 51 or numero_case_touched == 61 or numero_case_touched == 71 or numero_case_touched == 81 or numero_case_touched == 91):
                listee[numero_case_touched + 18] = blanc
                print("Bug")
            if third_diagonal == noir and listee[numero_case_touched] == noirRempli:
                listee[numero_case_touched + 9] = demi_Noir
            if fourth_diagonal == noir and listee[numero_case_touched] == noirRempli:
                listee[numero_case_touched + 11] = demi_Noir
            if first_diagonal == blancRempli and listee[numero_case_touched] == noirRempli and listee[numero_case_touched - 22] == noir:
                listee[numero_case_touched - 22] = demi_Noir
            if second_diagonal == blancRempli and listee[numero_case_touched] == noirRempli and listee[numero_case_touched - 18] == noir:
                listee[numero_case_touched - 18] = demi_Noir
            if third_diagonal == blancRempli and listee[numero_case_touched] == noirRempli and listee[numero_case_touched + 18] == noir:
                listee[numero_case_touched + 18] = demi_Noir
            if fourth_diagonal == blancRempli and listee[numero_case_touched] == noirRempli and listee[numero_case_touched + 22] == noir:
                listee[numero_case_touched + 22] = demi_Noir
            if listee[numero_case_touched] == demi_Noir:
                listee[numero_case_touched] = noirRempli
                for i in range(len(listee)):
                    if listee[i] == demi_Noir:
                        listee[i] = noir
                if a_supprimer - numero_case_touched == 18:
                    listee[numero_case_touched + 9] = noir
                    piont_mange_equipe_noir += 1
                if a_supprimer - numero_case_touched == 22:
                    listee[numero_case_touched + 11] = noir
                    piont_mange_equipe_noir += 1
                if numero_case_touched - a_supprimer == 22:
                    listee[numero_case_touched - 11] = noir
                    piont_mange_equipe_noir += 1
                if numero_case_touched - a_supprimer == 18:
                    listee[numero_case_touched - 9] = noir
                    piont_mange_equipe_noir += 1
                listee[a_supprimer] = noir
                white = True
    elif numero_case_touched <= 7 and numero_case_touched > 0:
        canMove = False
        third_diagonal = listee[numero_case_touched + 9] 
        fourth_diagonal = listee[numero_case_touched + 11]

        if third_diagonal == noir or fourth_diagonal == noir:
            canMove = True
        else:
            canMove = False
        if white == True:
            if listee[numero_case_touched] == blancRempli:
                for i in range(len(listee)):
                    if listee[i] == demi_Blanc and (i != numero_case_touched + 11 and i != numero_case_touched + 9):
                        listee[i] = noir
            if listee[numero_case_touched] == blancRempli:
                a_supprimer = numero_case_touched
            if third_diagonal == noirRempli and listee[numero_case_touched] == blancRempli and listee[numero_case_touched + 18] == noir:
                listee[numero_case_touched + 18] = demi_Blanc
            if fourth_diagonal == noirRempli and listee[numero_case_touched] == blancRempli and listee[numero_case_touched + 22] == noir:
                listee[numero_case_touched + 22] = demi_Blanc
            if listee[numero_case_touched] == demi_Blanc:
                listee[numero_case_touched] = blancRempli
                for i in range(len(listee)):
                    if listee[i] == demi_Blanc:
                        listee[i] = noir
                if a_supprimer - numero_case_touched == 18:
                    listee[numero_case_touched + 9] = noir
                    piont_mange_equipe_blanc += 1
                if a_supprimer - numero_case_touched == 22:
                    listee[numero_case_touched + 11] = noir
                    piont_mange_equipe_blanc += 1
                if numero_case_touched - a_supprimer == 22:
                    listee[numero_case_touched - 11] = noir
                    piont_mange_equipe_blanc += 1
                if numero_case_touched - a_supprimer == 18:
                    listee[numero_case_touched - 9] = noir
                    piont_mange_equipe_blanc += 1
                listee[a_supprimer] = noir
                white = False
        else:
            if listee[numero_case_touched] == noirRempli:
                for i in range(len(listee)):
                    if listee[i] == demi_Noir and (i != numero_case_touched - 11 and i != numero_case_touched - 9 and i != numero_case_touched + 11 and i != numero_case_touched + 9):
                        listee[i] = noir
            if listee[numero_case_touched] == noirRempli:
                a_supprimer = numero_case_touched
            if third_diagonal == noir and listee[numero_case_touched] == noirRempli:
                listee[numero_case_touched + 9] = demi_Noir
            if fourth_diagonal == noir and listee[numero_case_touched] == noirRempli:
                listee[numero_case_touched + 11] = demi_Noir
            if third_diagonal == blancRempli and listee[numero_case_touched] == noirRempli and listee[numero_case_touched + 18] == noir:
                listee[numero_case_touched + 18] = demi_Noir
            if fourth_diagonal == blancRempli and listee[numero_case_touched] == noirRempli and listee[numero_case_touched + 22] == noir:
                listee[numero_case_touched + 22] = demi_Noir
            if listee[numero_case_touched] == demi_Noir:
                listee[numero_case_touched] = noirRempli
                for i in range(len(listee)):
                    if listee[i] == demi_Noir:
                        listee[i] = noir
                if a_supprimer - numero_case_touched == 18:
                    listee[numero_case_touched + 9] = noir
                    piont_mange_equipe_noir += 1
                if a_supprimer - numero_case_touched == 22:
                    listee[numero_case_touched + 11] = noir
                    piont_mange_equipe_noir += 1
                if numero_case_touched - a_supprimer == 22:
                    listee[numero_case_touched - 11] = noir
                    piont_mange_equipe_noir += 1
                if numero_case_touched - a_supprimer == 18:
                    listee[numero_case_touched - 9] = noir
                    piont_mange_equipe_noir += 1
                listee[a_supprimer] = noir
                white = True
    elif numero_case_touched == 9:
        canMove = False
        third_diagonal = listee[numero_case_touched + 9]

        if third_diagonal == noir:
            canMove = True
        else:
            canMove = False
        if white == True:
            if listee[numero_case_touched] == blancRempli:
                for i in range(len(listee)):
                    if listee[i] == demi_Blanc and (i != numero_case_touched + 9):
                        listee[i] = noir
            if listee[numero_case_touched] == blancRempli:
                a_supprimer = numero_case_touched
             
            if third_diagonal == noirRempli and listee[numero_case_touched] == blancRempli and listee[numero_case_touched + 18] == noir:
                listee[numero_case_touched + 18] = demi_Blanc
            if listee[numero_case_touched] == demi_Blanc:
                listee[numero_case_touched] = blancRempli
                for i in range(len(listee)):
                    if listee[i] == demi_Blanc:
                        listee[i] = noir
                if a_supprimer - numero_case_touched == 18:
                    listee[numero_case_touched + 9] = noir
                    piont_mange_equipe_blanc += 1
                if a_supprimer - numero_case_touched == 22:
                    listee[numero_case_touched + 11] = noir
                    piont_mange_equipe_blanc += 1
                if numero_case_touched - a_supprimer == 22:
                    listee[numero_case_touched - 11] = noir
                    piont_mange_equipe_blanc += 1
                if numero_case_touched - a_supprimer == 18:
                    listee[numero_case_touched - 9] = noir
                    piont_mange_equipe_blanc += 1
                listee[numero_case_touched] = blancRempli
                listee[numero_case_touched + 9] = noir
                listee[a_supprimer] = noir
                white = False
        else:
            if listee[numero_case_touched] == noirRempli:
                for i in range(len(listee)):
                    if listee[i] == demi_Noir and (i != numero_case_touched + 9):
                        listee[i] = noir
             
            if listee[numero_case_touched] == noirRempli:
                a_supprimer = numero_case_touched
            if third_diagonal == noir and listee[numero_case_touched] == noirRempli:
                listee[numero_case_touched + 9] = demi_Noir
            if third_diagonal == blancRempli and listee[numero_case_touched] == noirRempli and listee[numero_case_touched + 18] == noir:
                listee[numero_case_touched + 18] = demi_Noir
            if listee[numero_case_touched] == demi_Noir:
                listee[numero_case_touched] = noirRempli
                for i in range(len(listee)):
                    if listee[i] == demi_Noir:
                        listee[i] = noir
                if numero_case_touched - a_supprimer == 18:
                    listee[numero_case_touched - 9] = noir
                    piont_mange_equipe_noir += 1
                listee[a_supprimer] = noir
                white = True
    elif numero_case_touched == 90:
        canMove = False
        second_diagonal = listee[numero_case_touched - 9]

        if second_diagonal == noir:
            canMove = True
        else:
            canMove = False
        if white == True:
            if listee[numero_case_touched] == blancRempli:
                for i in range(len(listee)):
                    if listee[i] == demi_Blanc and (i != numero_case_touched - 11 and i != numero_case_touched - 9 and i != numero_case_touched + 11 and i != numero_case_touched + 9):
                        listee[i] = noir
             
            if listee[numero_case_touched] == blancRempli:
                a_supprimer = numero_case_touched
            if second_diagonal == noir and listee[numero_case_touched] == blancRempli:
                    listee[numero_case_touched - 9] = demi_Blanc
            if second_diagonal == noirRempli and listee[numero_case_touched] == blancRempli and listee[numero_case_touched - 18] == noir:
                listee[numero_case_touched - 18] = demi_Blanc
            if listee[numero_case_touched] == demi_Blanc:
                listee[numero_case_touched] = blancRempli
                for i in range(len(listee)):
                    if listee[i] == demi_Blanc:
                        listee[i] = noir
                if a_supprimer - numero_case_touched == 18:
                    listee[numero_case_touched + 9] = noir
                    piont_mange_equipe_blanc += 1
                listee[a_supprimer] = noir
                white = False
        else:
            if listee[numero_case_touched] == noirRempli:
                for i in range(len(listee)):
                    if listee[i] == demi_Noir and (i != numero_case_touched - 9):
                        listee[i] = noir
             
            if listee[numero_case_touched] == noirRempli:
                a_supprimer = numero_case_touched
            if second_diagonal == blancRempli and listee[numero_case_touched] == noirRempli:
                listee[numero_case_touched - 18] = demi_Noir
            if listee[numero_case_touched] == demi_Noir:
                listee[numero_case_touched] = noirRempli
                for i in range(len(listee)):
                    if listee[i] == demi_Noir:
                        listee[i] = noir
                if a_supprimer - numero_case_touched == 18:
                    listee[numero_case_touched + 9] = noir
                    piont_mange_equipe_noir += 1
                listee[a_supprimer] = noir
                white = True
    elif numero_case_touched < 99 and numero_case_touched >= 92:
        canMove = False
        first_diagonal = listee[numero_case_touched - 11]
        second_diagonal = listee[numero_case_touched - 9]

        if first_diagonal == noir or second_diagonal == noir:
            canMove = True
        else:
            canMove = False
        if white == True:
            if listee[numero_case_touched] == blancRempli:
                for i in range(len(listee)):
                    if listee[i] == demi_Blanc and (i != numero_case_touched - 11 and i != numero_case_touched - 9):
                        listee[i] = noir
             
            if listee[numero_case_touched] == blancRempli:
                a_supprimer = numero_case_touched
            if first_diagonal == noir and listee[numero_case_touched] == blancRempli:
                    listee[numero_case_touched - 11] = demi_Blanc
            if second_diagonal == noir and listee[numero_case_touched] == blancRempli:
                    listee[numero_case_touched - 9] = demi_Blanc
            if first_diagonal == noirRempli and listee[numero_case_touched] == blancRempli and listee[numero_case_touched - 22] == noir:
                listee[numero_case_touched - 22] = demi_Blanc
            if second_diagonal == noirRempli and listee[numero_case_touched] == blancRempli and listee[numero_case_touched - 18] == noir:
                listee[numero_case_touched - 18] = demi_Blanc
            if listee[numero_case_touched] == demi_Blanc:
                listee[numero_case_touched] = blancRempli
                for i in range(len(listee)):
                    if listee[i] == demi_Blanc:
                        listee[i] = noir
                if numero_case_touched - a_supprimer == 22:
                    listee[numero_case_touched - 11] = noir
                    piont_mange_equipe_blanc += 1
                if numero_case_touched - a_supprimer == 18:
                    listee[numero_case_touched - 9] = noir
                    piont_mange_equipe_blanc += 1
                listee[a_supprimer] = noir
                white = False
        else:
            if listee[numero_case_touched] == blancRempli:
                for i in range(len(listee)):
                    if listee[i] == demi_Blanc and (i != numero_case_touched - 11 and i != numero_case_touched - 9):
                        listee[i] = noir
             
            if listee[numero_case_touched] == noirRempli:
                a_supprimer = numero_case_touched
            if first_diagonal == blancRempli and listee[numero_case_touched] == noirRempli and listee[numero_case_touched - 22] == noir:
                listee[numero_case_touched - 22] = demi_Noir
            if second_diagonal == blancRempli and listee[numero_case_touched] == noirRempli and listee[numero_case_touched - 18] == noir:
                listee[numero_case_touched - 18] = demi_Noir
            if listee[numero_case_touched] == demi_Noir:
                listee[numero_case_touched] = noirRempli
                for i in range(len(listee)):
                    if listee[i] == demi_Noir:
                        listee[i] = noir
                if a_supprimer - numero_case_touched == 18:
                    listee[numero_case_touched + 9] = noir
                    piont_mange_equipe_noir += 1
                if a_supprimer - numero_case_touched == 22:
                    listee[numero_case_touched + 11] = noir
                    piont_mange_equipe_noir += 1
                if numero_case_touched - a_supprimer == 22:
                    listee[numero_case_touched - 11] = noir
                    piont_mange_equipe_noir += 1
                if numero_case_touched - a_supprimer == 18:
                    listee[numero_case_touched - 9] = noir
                    piont_mange_equipe_noir += 1
                listee[a_supprimer] = noir
                white = True
    elif numero_case_touched == 10:
        canMove = False
        second_diagonal = listee[numero_case_touched - 9]
        fourth_diagonal = listee[numero_case_touched + 11]

        if second_diagonal == noir or fourth_diagonal == noir:
            canMove = True
        else:
            canMove = False
        if white == True:
            if listee[numero_case_touched] == blancRempli:
                for i in range(len(listee)):
                    if listee[i] == demi_Blanc and (i != numero_case_touched + 11 and i != numero_case_touched - 9):
                        listee[i] = noir
             
            if listee[numero_case_touched] == blancRempli: 
                a_supprimer = numero_case_touched
            if second_diagonal == noir and listee[numero_case_touched] == blancRempli:
                    listee[numero_case_touched - 9] = demi_Blanc
            if second_diagonal == noirRempli and listee[numero_case_touched] == blancRempli and listee[numero_case_touched - 18] == noir:
                listee[numero_case_touched - 18] = demi_Blanc
            if fourth_diagonal == noirRempli and listee[numero_case_touched] == blancRempli and listee[numero_case_touched + 22] == noir:
                listee[numero_case_touched + 22] = demi_Blanc
            if listee[numero_case_touched] == demi_Blanc:
                listee[numero_case_touched] = blancRempli
                for i in range(len(listee)):
                    if listee[i] == demi_Blanc:
                        listee[i] = noir
                if numero_case_touched - a_supprimer == 22:
                    listee[numero_case_touched - 11] = noir
                    piont_mange_equipe_blanc += 1
                listee[a_supprimer] = noir
                white = False
        else:
            if listee[numero_case_touched] == noirRempli:
                for i in range(len(listee)):
                    if listee[i] == demi_Noir and (i != numero_case_touched + 11 and i != numero_case_touched - 9):
                        listee[i] = noir
             
            if listee[numero_case_touched] == noirRempli:
                a_supprimer = numero_case_touched
            if listee[numero_case_touched] == noirRempli and (numero_case_touched == 1 or numero_case_touched == 11 or numero_case_touched == 21 or numero_case_touched == 31 or numero_case_touched == 41 or numero_case_touched == 51 or numero_case_touched == 61 or numero_case_touched == 71 or numero_case_touched == 81 or numero_case_touched == 91):
                listee[numero_case_touched + 18] = blanc
                print("Bug")
            if fourth_diagonal == noir and listee[numero_case_touched] == noirRempli:
                listee[numero_case_touched + 11] = demi_Noir
            if second_diagonal == blancRempli and listee[numero_case_touched] == noirRempli and listee[numero_case_touched - 18] == noir:
                listee[numero_case_touched - 18] = demi_Noir
            if fourth_diagonal == blancRempli and listee[numero_case_touched] == noirRempli and listee[numero_case_touched + 22] == noir:
                listee[numero_case_touched + 22] = demi_Noir
            if listee[numero_case_touched] == demi_Noir:
                listee[numero_case_touched] = noirRempli
                for i in range(len(listee)):
                    if listee[i] == demi_Noir:
                        listee[i] = noir
                if numero_case_touched - a_supprimer == 22:
                    listee[numero_case_touched - 11] = noir
                    piont_mange_equipe_noir += 1
                listee[a_supprimer] = noir
                white = True
    elif numero_case_touched == 89:
        canMove = False
        first_diagonal = listee[numero_case_touched - 11]
        third_diagonal = listee[numero_case_touched + 9]

        if first_diagonal == noir or third_diagonal == noir:
            canMove = True
        else:
            canMove = False
        if white == True:
            if listee[numero_case_touched] == blancRempli:
                for i in range(len(listee)):
                    if listee[i] == demi_Blanc and (i != numero_case_touched - 11 and i != numero_case_touched + 9):
                        listee[i] = noir
            if listee[numero_case_touched] == blancRempli:
                a_supprimer = numero_case_touched
            if first_diagonal == noir and listee[numero_case_touched] == blancRempli:
                    listee[numero_case_touched - 11] = demi_Blanc
            if first_diagonal == noirRempli and listee[numero_case_touched] == blancRempli and listee[numero_case_touched - 22] == noir:
                listee[numero_case_touched - 22] = demi_Blanc
            if third_diagonal == noirRempli and listee[numero_case_touched] == blancRempli and listee[numero_case_touched + 18] == noir:
                listee[numero_case_touched + 18] = demi_Blanc
            if listee[numero_case_touched] == demi_Blanc:
                listee[numero_case_touched] = blancRempli
                for i in range(len(listee)):
                    if listee[i] == demi_Blanc:
                        listee[i] = noir
                if a_supprimer - numero_case_touched == 22:
                    listee[numero_case_touched + 11] = noir
                    piont_mange_equipe_blanc += 1
                listee[a_supprimer] = noir
                white = False
        else:
            if listee[numero_case_touched] == noirRempli:
                for i in range(len(listee)):
                    if listee[i] == demi_Noir and (i != numero_case_touched - 11 and i != numero_case_touched + 9):
                        listee[i] = noir
             
            if listee[numero_case_touched] == noirRempli:
                a_supprimer = numero_case_touched
            if listee[numero_case_touched] == noirRempli and (numero_case_touched == 1 or numero_case_touched == 11 or numero_case_touched == 21 or numero_case_touched == 31 or numero_case_touched == 41 or numero_case_touched == 51 or numero_case_touched == 61 or numero_case_touched == 71 or numero_case_touched == 81 or numero_case_touched == 91):
                listee[numero_case_touched + 18] = blanc
                print("Bug")
            if third_diagonal == noir and listee[numero_case_touched] == noirRempli:
                listee[numero_case_touched + 9] = demi_Noir
            if first_diagonal == blancRempli and listee[numero_case_touched] == noirRempli and listee[numero_case_touched - 22] == noir:
                listee[numero_case_touched - 22] = demi_Noir
            if third_diagonal == blancRempli and listee[numero_case_touched] == noirRempli and listee[numero_case_touched + 18] == noir:
                listee[numero_case_touched + 18] = demi_Noir
            if listee[numero_case_touched] == demi_Noir:
                listee[numero_case_touched] = noirRempli
                for i in range(len(listee)):
                    if listee[i] == demi_Noir:
                        listee[i] = noir
                if a_supprimer - numero_case_touched == 18:
                    listee[numero_case_touched + 9] = noir
                    piont_mange_equipe_noir += 1
                if a_supprimer - numero_case_touched == 22:
                    listee[numero_case_touched + 11] = noir
                    piont_mange_equipe_noir += 1
                if numero_case_touched - a_supprimer == 22:
                    listee[numero_case_touched - 11] = noir
                    piont_mange_equipe_noir += 1
                if numero_case_touched - a_supprimer == 18:
                    listee[numero_case_touched - 9] = noir
                    piont_mange_equipe_noir += 1
                listee[a_supprimer] = noir
                white = True
    
    # Déplacement des reines
    if white == True:
        if listee[numero_case_touched] == reine_blanc:
            global a_supprimer_for_reine
            a_supprimer_for_reine = numero_case_touched
        for i in range(1, 100):
            if ((i - numero_case_touched) % 9 == 0 or (i - numero_case_touched) % 11 == 0) and listee[numero_case_touched] == reine_blanc and listee[i] == noir:
                listee[i] = demi_reine_blanc
                print(listee[numero_case_touched], x, y, white, numero_case_touched, i)
        if listee[numero_case_touched] == demi_reine_blanc:
            piont_mange_equipe_blanc += 1
            for i in range(1, 100):
                if listee[i] == noirRempli and (((i - a_supprimer_for_reine) % 9 == 0) or ((i - a_supprimer_for_reine) % 11 == 0)) and ((i > a_supprimer_for_reine and numero_case_touched > i) or (i < a_supprimer_for_reine and numero_case_touched < i)):
                    print("Bug")
                    listee[i] = noir
            listee[numero_case_touched] = reine_blanc
            for i in range(len(listee)):
                if listee[i] == demi_reine_blanc:
                    listee[i] = noir
            listee[a_supprimer_for_reine] = noir
            white = False
    else:
        if listee[numero_case_touched] == reine_noir:
            global a_supprimer_for_reine_noir
            a_supprimer_for_reine_noir = numero_case_touched
        for i in range(1, 100):
            if ((i - numero_case_touched) % 9 == 0 or (i - numero_case_touched) % 11 == 0) and listee[numero_case_touched] == reine_noir and listee[i] == noir:
                listee[i] = demi_reine_noir
                print(listee[numero_case_touched], x, y, white, numero_case_touched, i)
        if listee[numero_case_touched] == demi_reine_noir:
            piont_mange_equipe_noir += 1
            for i in range(1, 100):
                if listee[i] == blancRempli and (((i - a_supprimer_for_reine_noir) % 9 == 0) or ((i - a_supprimer_for_reine_noir) % 11 == 0)) and ((i > a_supprimer_for_reine_noir and numero_case_touched > i) or (i < a_supprimer_for_reine_noir and numero_case_touched < i)):
                    print("Bug")
                    listee[i] = noir
            listee[numero_case_touched] = reine_noir
            for i in range(len(listee)):
                if listee[i] == demi_reine_noir:
                    listee[i] = noir
            listee[a_supprimer_for_reine_noir] = noir
            white = True
    
    for i in range(10):
        if listee[i] == blancRempli:
            listee[i] = reine_blanc

    for i in range(90, 100):
        if listee[i] == noirRempli:
            listee[i] = reine_noir

    affichage()

canva.bind("<Button-1>", clique)

## FIN DE LA BOUCLE PRINCIPAL ##
root.mainloop()