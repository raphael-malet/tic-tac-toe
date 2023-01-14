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
joueur_actuel =''
utlisateur = ''
utilisateur_login = ''
nom_utilisateur =''
nom_utilisateur2 =''
joueur1 =''
joueur2=''
fichier_utilisateur =''
score =''
score2=''

#fonction ouverture du ficher utilisateur.txt
def ouverture_fichier_utilisateur():
    global fichier_utilisateur
    fichier_utilisateur = open('utilisateur.txt','r')
    fichier_utilisateur = fichier_utilisateur.read()
    fichier_utilisateur = fichier_utilisateur.split(',')
  
#choix signe joueurs
def choix_signe():
    global joueur_actuel
    global joueur1
    global joueur2
    while True :
        joueur1 = input('Joueur1 veuiller entrer votre signe X ou O : ')
        joueur1 = joueur1.upper()
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

#fonciton partie JVJ
def jouer_partie():
    global grille_partie
    grille_partie = grille_depart   
#boucle tant que la partie n'est pas nul ou gagné
    while partie_en_cours:
        winner()#vérification si il y a un gagnat
        partie_nul()#vérification match nul
        grille_fonction()#print la grille
        grille_jeu()#permet au joeur de jouer
        winner()
        partie_nul()
        tour_joueur()#changement de joueur
        
    #print le signe du gagnant
    if gagnant == joueur1 :
        
        if nom_utilisateur =='':
            grille_fonction()
            print(gagnant +' est le GRAND GAGNANT !!!!\n')
            stockage_histotique()
            rejouer()
            
        else:
            grille_fonction()
            print(nom_utilisateur +' est le GRAND GAGNANT !!!!'+'\n')
            ajout_score_utilisateur()
            add_score_utilisateur_fichier()
            stockage_histotique()
            rejouer()
            
    elif gagnant == joueur2:
        
        if nom_utilisateur =='':
            grille_fonction()
            print(gagnant +' est le GRAND GAGNANT !!!!\n')
            stockage_histotique()
            rejouer()
  
        else:
            grille_fonction()
            print(nom_utilisateur2 +' est le GRAND GAGNANT !!!!'+'\n')
            ajout_score_utilisateur()
            add_score_utilisateur_fichier()
            stockage_histotique()
            rejouer()
   
    else :
        print('\nMatch nul :(') # print match nul
        rejouer()

#fonction partie jVC
def jouer_partie_jVC():
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
            winner()
            partie_nul()
        #tour_joueur()#changement de joueur
    
    #print le signe du gagnant
    if gagnant == joueur1 :
        
        if nom_utilisateur =='':
            grille_fonction()
            print(gagnant +' est le GRAND GAGNANT !!!!\n')
            stockage_histotique()
            rejouer()
            
        else:
            grille_fonction()
            print(nom_utilisateur +' est le GRAND GAGNANT !!!!'+'\n')
            stockage_histotique()
            rejouer()
            
    elif gagnant == joueur2:
        
        if nom_utilisateur =='':
            grille_fonction()
            print(gagnant +' est le GRAND GAGNANT !!!!\n')
            stockage_histotique()
            rejouer()
  
        else:
            grille_fonction()
            print(nom_utilisateur2 +' est le GRAND GAGNANT !!!!'+'\n')
            stockage_histotique()
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

#fonction pour rejouer
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
            while True:
                retour_menu = input('\n1:Retour menu.\n2:Quitter le jeu.\nEntre 1 ou 2 : ')
                if retour_menu == '1':
                    grille_depart = ["-","-","-",
                            "-","-","-",
                            "-","-","-",]
                    gagnant = None
                    partie_en_cours = True
                    menu()
                elif retour_menu =='2':
                    print('\nAurevoir et a bientot :D')
                    quit()
        else:
            print('\nEntrer oui, o, y pour rejouer ou non, n ou non pour quitter. ')
            continue

#fonction ia bas niveau
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

#fonction qui prend la score du joueur 1
def user_score():
    global nom_utilisateur
    global fichier_utilisateur
    global score
    nom_utilisateur = input("\nPour retourner au menu taper menu \nEntrer votre nom d'utilisateur : ")
    for i in range (len(fichier_utilisateur)):
        if fichier_utilisateur[i] == nom_utilisateur:
            score = fichier_utilisateur[i+1]
        elif nom_utilisateur == 'menu':
            menu()

#fonction qui prend de lscore de l'utilisateur 2
def user_score_joueur2():
    global nom_utilisateur2
    global fichier_utilisateur
    global score2
    nom_utilisateur2 = input("Entrer votre nom d'utilisateur")
    for i in range (len(fichier_utilisateur)):
        if fichier_utilisateur[i] == nom_utilisateur2:
            score2 = fichier_utilisateur[i+1]
        elif nom_utilisateur2 =='menu':
            menu()
    return

#fonction qui jaoute le score a l'utilisateur qui a gagner            
def ajout_score_utilisateur():
    global fichier_utilisateur
    global nom_utilisateur
    global nom_utilisateur2
    global score
    global score2
    global gagnant
    global joueur1 
    global joueur2
    if gagnant == joueur1 :
        if nom_utilisateur == '':
            pass
        else:
            i = 0
            while i <= len(fichier_utilisateur) :
                if fichier_utilisateur[i] == nom_utilisateur:
                    score = int(score)
                    score = score +1
                    score = str(score)
                    fichier_utilisateur[i+1] = score
                    i=0
                    break
                else:
                    i = i+1
    
    elif gagnant == joueur2 :
        if nom_utilisateur2 == '':
            pass
        else:
            i = 0
            print(i)
            while i <= len(fichier_utilisateur) :
                if fichier_utilisateur[i] == nom_utilisateur2:
                    score2 = int(score2) + 1
                    score2 = str(score2)
                    fichier_utilisateur[i+1] = score2
                    i=0
                    break
                else:
                    i=i+1
            
#fonction qui actualise la dossier utilisateur.txt avec les scores
def add_score_utilisateur_fichier():
    global fichier_utilisateur
    fichier_utilisateur = ','.join(fichier_utilisateur)
    ajout_score_fichier_utilisateur = open('utilisateur.txt','w')
    ajout_score_fichier_utilisateur.write(fichier_utilisateur)
    ajout_score_fichier_utilisateur.close()
    ouverture_fichier_utilisateur()
    
#permet d'afficher le score de l'utilisateur
def afficher_score():
    print('\n'+nom_utilisateur +' ton score est de '+score+' victoire \n')
    while True:
        continuer = input('Appuyer sur ENTRER pour revenir au menu de sélection : ')
        if continuer == '':
            break
    
#permet d'afficher l'historique des parties
def afficher_historique():
    historique = open('historique.txt' , 'r')
    historique = historique.read()
    print('\n' + historique +'\n')
    while True:
        continuer = input('Appuyer sur ENTRER pour revenir au menu de sélection : ')
        if continuer == '':
            break

#permet de stocker le resultat d'une partie dans l'historique
def stockage_histotique():
    global gagnant
    global nom_utilisateur
    global nom_utilisateur2
    if gagnant == joueur1:
        if nom_utilisateur == '' and nom_utilisateur2 =='':
            stockage_resultat = 'joueur 1 a gagné contre joueur2\n'
        
        elif nom_utilisateur != '' and nom_utilisateur2 =='':
            stockage_resultat = nom_utilisateur +' a gagné contre joueur2\n'
        
        elif nom_utilisateur == '' and nom_utilisateur2 !='':
            stockage_resultat = 'Joueur 1 a gagné contre '+nom_utilisateur2+'\n'
        else:
            stockage_resultat = nom_utilisateur + ' a gagné contre '+nom_utilisateur2 + '\n'
    
    elif gagnant == joueur2:
        if nom_utilisateur == '' and nom_utilisateur2 =='':
            stockage_resultat = 'Joueur 2 a gagné contre joueur1\n'
        
        elif nom_utilisateur == '' and nom_utilisateur2 !='':
            stockage_resultat = nom_utilisateur2 +' a gagné contre joueur 1\n'
        
        elif nom_utilisateur != '' and nom_utilisateur2 =='':
            stockage_resultat = 'Joueur 2 a gagné contre '+nom_utilisateur+'\n'
        else:
            stockage_resultat = nom_utilisateur + ' a gagné contre '+nom_utilisateur2 + '\n'
    
    stockage_resultat_historique = open('historique.txt','a')
    stockage_resultat_historique.write(stockage_resultat)
    stockage_resultat_historique.close()

#création d'un nouvelle utilisateur
def creation_utilisateur():
    while True:
        new_utilisateur = input("Entrer votre nom d'utilisateur : ")
        confirmation = input('confirmer vous que votre nom est : '+new_utilisateur +' : \n')
        if confirmation == 'oui' or confirmation =='':
            break
        else:
            continue
    creation_user_file = open('utilisateur.txt' ,'a')
    creation_user_file.write(','+new_utilisateur+',0')
    creation_user_file.close()

#fonction de menu 
def menu():
    global utilisateur_login
    global nom_utilisateur
    while True:
        menu_entrer = input('Vous êtes dans le menu appuyer sur ENTRER pour continuer : ')
        if menu_entrer =="":
            break
        else:
            continue

    utilisateur_login = input('Voulez-vous vous enregistrer ? oui/non: ')
    if utilisateur_login == 'oui' or utilisateur_login =='o'or utilisateur_login == 'yes' or utilisateur_login =='y' : 
        choix = input('voulez-vous créer un nouvelle utilisateur ')
        if choix == 'oui' or choix == 'o' or choix == 'y' or choix == 'yes' :
            creation_utilisateur()
            user_score()
        else:
            user_score()           
    
    while True:
        entrer_choix = input('1:jouer joueur vs joueur.\n2:Jouer contre ordinateur.\n3:afficher historique.\n4:afficher score. \n5:quitter.\nEntrer le numéro qui correspond : ')
        if entrer_choix =='1':
            while True:
                choix_utilisateur2 = input("Voulez-vous enregistrer un deuxieme utilisateur ? ")
                if choix_utilisateur2 == 'oui':
                    user_score_joueur2()
                    choix_signe()
                    jouer_partie()
                else:
                    break
            choix_signe()
            jouer_partie()   
        
        elif entrer_choix =='2':
            choix_signe()
            jouer_partie_jVC()
            
        elif entrer_choix =='3':
            afficher_historique()
            
        elif entrer_choix =='4':
            afficher_score()
            
        elif entrer_choix =='5':
            print('Aurevoir et a bientot :D')
            quit() 
        else:
            continue

ouverture_fichier_utilisateur()
menu()