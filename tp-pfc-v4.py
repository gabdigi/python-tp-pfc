#TP PIERRE FEUILLE CISEAUX
#library
import random
import time

##########################################################################################

# liste pour pierre feuille ciseaux
# pfc veut dire pierre feuille ciseaux
pfc = ['pierre', 'feuille', 'ciseaux']

#variable pour afficher les scores du joueur et ordinateur
scoreJoueur = 0
scoreOrdi   = 0

##########################################################################################

#création de la variable pour la boucle infinie

choix = "o"

while choix == "o":

##########################################################################################

        #information visible pour le joueur
        print("bonjour joueur bienvenue")

        print("pour jouer veuillez choisir un chiffre")

        print(" 0 - pierre")
        print(" 1 - feuille")
        print(" 2 - ciseaux")

##########################################################################################

        #création aléatoire d'un chiffre pour l'ordi et cherche dans la liste avec le nombre creer
        ordi   = random.choice(pfc)
        #joueur choisit 1 chiffre
        joueur = input("veuillez taper un chiffre entre 0 et 2 s'il vous plait --- ")
        #transforme la chaine de caractère en chiffre
        joueur = int(joueur)
        
##########################################################################################

        # lancement du jeux pierre feuille ciseaux

        if joueur > 3:
            print("j'ai dit entre 0 et 2")
        else:
            joueur = pfc[joueur]

            time.sleep(3)
            print("très bien alors c'est partit")
            #temps different pour afficher le texte
            time.sleep(1)
            print("pierre")
            time.sleep(1)
            print("feuille")
            time.sleep(1)   
            print("ciseaux")

##########################################################################################

            # condition en fonction du gagnant, perdant et égaliter

            time.sleep(2)
            if joueur == pfc[0] and ordi == pfc[0]:
                print("égaliter")
                print("joueur: " + str(scoreJoueur) + " ordinateur " + str(scoreOrdi))
            elif joueur == pfc[0] and ordi == pfc[1]:
                print("perdu")
                scoreOrdi += 1
                print("joueur: " + str(scoreJoueur) + " ordinateur " + str(scoreOrdi))
            elif joueur == pfc[0] and ordi == pfc[2]:
                print("gagner")
                scoreJoueur += 1
                print("joueur: " + str(scoreJoueur) + " ordinateur " + str(scoreOrdi))
            elif joueur == pfc[1] and ordi == pfc[0]:
                print("gagner")
                scoreJoueur += 1
                print("joueur: " + str(scoreJoueur) + " ordinateur " + str(scoreOrdi))
            elif joueur == pfc[1] and ordi == pfc[1]:
                print("égaliter")
                print("joueur: " + str(scoreJoueur) + " ordinateur " + str(scoreOrdi))
            elif joueur == pfc[1] and ordi == pfc[2]:
                print("perdu")
                scoreOrdi += 1
                print("joueur: " + str(scoreJoueur) + " ordinateur " + str(scoreOrdi))
            elif joueur == pfc[2] and ordi == pfc[0]:
                print("perdu")
                scoreOrdi += 1
                print("joueur: " + str(scoreJoueur) + " ordinateur " + str(scoreOrdi))
            elif joueur == pfc[2] and ordi == pfc[1]:
                print("gagner")
                scoreJoueur += 1
                print("joueur: " + str(scoreJoueur) + " ordinateur " + str(scoreOrdi))
            elif joueur == pfc[2] and ordi == pfc[2]:
                print("égaliter")
                print("joueur: " + str(scoreJoueur) + " ordinateur " + str(scoreOrdi))
            else:
                print("erreur veuillez recommencer")     


##########################################################################################

        # pour relancer une partit ou sortir de la boucle et du jeux

        question = input("voulez vous refaire une partit o/n ? --- ")

        if question == "o":
            print("très bien")
        else:
            print("au revoir")
            break
