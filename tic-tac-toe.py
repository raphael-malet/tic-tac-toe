#varibale global
grille_depart = ["-","-","-",
                 "-","-","-",
                 "-","-","-",]

gagnant = None
partie_en_cours = True

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

#impression de la grille vide 
def jouer_partie():

    while partie_en_cours:
        grille_fonction()
        grille_jeu()
        partie_nul()
        winner()
        tour_joueur()
    if gagnant == 'X' or gagnant =='O':
        grille_fonction()
        print('le gagnat est ' + gagnant +'\n')
    else :
        print('\nMatch nul')
        

def grille_fonction():
    print(grille_depart[0]+' | ' + grille_depart[1]+ ' | ' +grille_depart[2] + '         1 | 2 | 3')
    print(grille_depart[3]+' | ' + grille_depart[4]+ ' | ' +grille_depart[5] + '         4 | 5 | 6')
    print(grille_depart[6]+' | ' + grille_depart[7]+ ' | ' +grille_depart[8] + '         7 | 8 | 9\n')   

print(' ')

def grille_jeu():
    while True:
        placement = int(input('entrer  votre emplacement de 1 à 9 : \n'))-1
        if  placement < 9:
            if '-' in grille_depart[placement] :
                break
            else:
                print('case déja choisis\n')
                continue
        else:
            print('Votre entré ne correspond a aucune case\n')
            continue
    grille_depart[placement] = joueur_actuel
    
def tour_joueur():
    global joueur_actuel
    global joueur1
    global joueur2
    if joueur_actuel == 'X':
        joueur_actuel='O'
    elif joueur_actuel == 'O':
        joueur_actuel = 'X'

def partie_nul():
    global partie_en_cours
    if '-' not in grille_depart:
        partie_en_cours = False
    else:
        return False

def winner():
    global gagnant
    global partie_en_cours
    if grille_depart[0] == grille_depart[1] == grille_depart[2] !='-':
        gagnant = grille_depart[0] 
        partie_en_cours = False 
    elif grille_depart[3] == grille_depart[4] == grille_depart[5] !='-' :
        gagnant = grille_depart[3]
        partie_en_cours = False 
    elif grille_depart[6] == grille_depart[7] == grille_depart[8] !='-' :
        gagnant = grille_depart[6] 
        partie_en_cours = False  
    elif grille_depart[0] == grille_depart[3] == grille_depart[6] !='-' :
        gagnant = grille_depart[0]
        partie_en_cours = False 
    elif grille_depart[1] == grille_depart[4] == grille_depart[5] !='-' :
        gagnant = grille_depart[1]
        partie_en_cours = False  
    elif grille_depart[2] == grille_depart[5] == grille_depart[8] !='-' :
        gagnant = grille_depart[2]
        partie_en_cours = False 
    elif grille_depart[0] == grille_depart[4] == grille_depart[8] !='-' :
        gagnant = grille_depart[0]
        partie_en_cours = False 
    elif grille_depart[2] == grille_depart[4] == grille_depart[6] !='-' :
        gagnant = grille_depart[0]
        partie_en_cours = False 
    else :
        gagnant = None
        
jouer_partie()