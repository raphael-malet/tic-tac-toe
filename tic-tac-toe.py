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

#Début du jeu 
def jouer_partie():
#boucle tant que la partie n'est pas nul ou gagné
    while partie_en_cours:
        grille_fonction()#print la grille
        grille_jeu()#permet au joeur de jouer
        winner()#vérification si il y a un gagnat
        partie_nul()#vérification match nul
        tour_joueur()#changement de joueur
    #print le signe du gagnant
    if gagnant == 'X' or gagnant =='O':
        grille_fonction()
        print('le gagnat est ' + gagnant +'\n')
    else :
        print('\nMatch nul') # print match nul
        
#fonction affichage grille
def grille_fonction():
    print(grille_depart[0]+' | ' + grille_depart[1]+ ' | ' +grille_depart[2] + '         1 | 2 | 3')
    print(grille_depart[3]+' | ' + grille_depart[4]+ ' | ' +grille_depart[5] + '         4 | 5 | 6')
    print(grille_depart[6]+' | ' + grille_depart[7]+ ' | ' +grille_depart[8] + '         7 | 8 | 9\n')   
print(' ')

#fonction entrer qui permet de jouer + remplacement signe dans la grille de débpart
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
    if '-' not in grille_depart:
        partie_en_cours = False
    else:
        return False

#vérification gagnant
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
        
jouer_partie() #fin de la fonction partie
