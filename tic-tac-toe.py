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
else:
    joueur2 ='X'
joueur_actuel = joueur1

#Début du jeu 

def jouer_partie():
    global grille_partie
    grille_partie = grille_depart
    
#boucle tant que la partie n'est pas nul ou gagné
    while partie_en_cours:
        grille_fonction()#print la grille
        grille_jeu()#permet au joeur de jouer
        winner()#vérification si il y a un gagnat
        partie_nul()#vérification match nul
        tour_joueur()#changement de joueur
    
    #print le signe du gagnant
    if gagnant == joueur1 or gagnant ==joueur2:
        grille_fonction()
        print(gagnant +' est le GRAND GAGNANT !!!!'+'\n')
        rejouer()
    else :
        print('\nMatch nul') # print match nul
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
        placement = input('Entrer emplacement de 1 à 9 :\n')
        if placement in grille_placement:
            placement = int(placement)-1
            if '-' in grille_partie[placement] :
                break
            else:
                print('case déja choisis\n')
                continue
        else:
            print('Votre entré ne correspond a aucune case\n')
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
    choix= input('Voulez-vous rejouer ? oui = 1 Non = 2 :\n')
    if choix == '1' :
        jouer_partie()
    else:
        quit()
jouer_partie()#fin de la fonction partie
