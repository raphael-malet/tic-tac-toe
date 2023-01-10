import random
#varibale global
grille_depart = ["-","-","-",
                 "-","-","-",
                 "-","-","-",]

grille_placement =["1","2","3",
                   "4","5","6",
                   "7","8","9",]

partie_en_cours = True
gagnant = None

#choix signe joueurs
while True :
    joueur1 = input('Joueur1 veuiller entrer votre signe X ou O : ')
    if joueur1 =='X' or joueur1 =='O':
        break
    else:
        continue
if joueur1 =='X':
    joueur2='O'
    print('Jouer 1 = X et joueur 2 = O.')
else:
    joueur2 ='X'
    print('joueuer 1 = O et joueur 2 = X.')
joueur_actuel = joueur1

#Début du jeu 

def jouer_partie():
    global grille_partie
    grille_partie = grille_depart
    
#boucle tant que la partie n'est pas nul ou gagné
    if '-' in grille_depart:
        while partie_en_cours:
            grille_fonction()#print la grille
            grille_jeu()
            grille_fonction()
            partie_nul()
            winner()
            ia()
            grille_fonction()
            winner()
            partie_nul()
        #tour_joueur()#changement de joueur
    
    #print le signe du gagnant
    if gagnant == joueur1 or gagnant ==joueur2:
        grille_fonction()
        print(gagnant +' est le GRAND GAGNANT !!!!'+'\n')
        rejouer()
    else :
        print('\nMatch nul :(') # print match nul
        rejouer()
        
#fonction affichage grille
def grille_fonction():
    print(grille_partie[0]+' | ' + grille_partie[1]+ ' | ' +grille_partie[2] + '         1 | 2 | 3')
    print(grille_partie[3]+' | ' + grille_partie[4]+ ' | ' +grille_partie[5] + '         4 | 5 | 6')
    print(grille_partie[6]+' | ' + grille_partie[7]+ ' | ' +grille_partie[8] + '         7 | 8 | 9\n')   
print(' ')

#fonction entrer qui permet de jouer + remplacement signe dans la grille de débpart
def grille_jeu():
    while True :
        placement = input('Au tour du joueur '+ joueur_actuel +' de jouer.'+ '\nEntrer emplacement de 1 à 9 :\n')
        if placement in grille_placement:
            placement = int(placement)-1
            if '-' in grille_partie[placement] :
                break
            else:
                print('\ncase déja choisis.\n')
                grille_fonction()
                continue
        else:
            print('\nVotre entré ne correspond a aucune case.\n')
            grille_fonction()
            continue
    grille_partie[placement] = joueur_actuel

  
#changement de joueur  
def tour_joueur():
    global joueur_actuel
    global joueur1
    global joueur2
    if joueur_actuel == 'X':
        joueur_actuel='O'
    elif joueur_actuel == 'O':
        joueur_actuel = 'X'

#vérification match nul
def partie_nul():
    global partie_en_cours
    if '-' not in grille_partie:
        partie_en_cours = False
    else:
        return False

#vérification gagnant
def winner():
    global gagnant
    global partie_en_cours
    if grille_partie[0] == grille_partie[1] == grille_partie[2] !='-':#premiere ligne
        gagnant = grille_partie[0] 
        partie_en_cours = False 
    elif grille_partie[3] == grille_partie[4] == grille_partie[5] !='-' :#deuxieme ligne
        gagnant = grille_partie[3]
        partie_en_cours = False 
    elif grille_partie[6] == grille_partie[7] == grille_partie[8] !='-' :#3eme ligne
        gagnant = grille_partie[6] 
        partie_en_cours = False  
    elif grille_partie[2] == grille_partie[5] == grille_partie[8] !='-' :#3eme colone
        gagnant = grille_partie[2]
        partie_en_cours = False 
    elif grille_partie[0] == grille_partie[3] == grille_partie[6] !='-' :#1ere colone
        gagnant = grille_partie[0]
        partie_en_cours = False  
    elif grille_partie[1] == grille_partie[4] == grille_partie[7] !='-' :#2eme colone
        gagnant = grille_partie[1]
        partie_en_cours = False 
    elif grille_partie[0] == grille_partie[4] == grille_partie[8] !='-' :#premiere diagonal
        gagnant = grille_partie[0]
        partie_en_cours = False 
    elif grille_partie[2] == grille_partie[4] == grille_partie[6] !='-' :#deuxieme diagonal
        gagnant = grille_partie[2]
        partie_en_cours = False 
    else :
        gagnant = None     


def rejouer():
    global grille_depart
    global gagnant
    global partie_en_cours
    while True:
        choix = input('Voulez-vous rejouer (oui/non) ? :\n')
        if choix == 'oui' or choix == 'o' or choix =='y' or choix =='yes' :
            grille_depart = ["-","-","-",
                            "-","-","-",
                            "-","-","-",]
            gagnant = None
            partie_en_cours = True
            print('_______________________________\nUne nouvelle partie commence !!')
            jouer_partie()
        elif choix == 'non' or choix =='n' or choix =='no':
            print('\nAurevoir et a bientot :D')
            quit()
        else:
            print('\nEntrer oui, o, y pour rejouer ou non, n ou non pour quitter. ')
            continue

def ia():
    global partie_en_cours
    global gagnant
    print("\nTour de l'ordinateur\n")
    if gagnant == None and "-" in grille_depart:
        while True:
            placement_ia = int(random.randrange(0, 8))
            if grille_partie[placement_ia] == '-':
                grille_depart[placement_ia] = joueur2
                winner()
                break
            else:
                continue
    else:
        return None
              
jouer_partie()#fin de la fonction partie
