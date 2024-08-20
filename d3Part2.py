#nom: Samuel Prevost
#numero d'etudiant: 300355439
# Jeu de cartes appelé "Pouilleux" 

# L'ordinateur est le donneur des cartes.

# Une carte est une chaine de 2 caractères. 
# Le premier caractère représente une valeur et le deuxième une couleur.
# Les valeurs sont des caractères comme '2','3','4','5','6','7','8','9','10','J','Q','K', et 'A'.
# Les couleurs sont des caractères comme : ♠, ♡, ♣, et ♢.
# On utilise 4 symboles Unicode pour représenter les 4 couleurs: pique, coeur, trèfle et carreau.
# Pour les cartes de 10 on utilise 3 caractères, parce que la valeur '10' utilise deux caractères.

import random

def attend_le_joueur():
    '''()->None
    Pause le programme jusqu'au l'usager appui Enter
    '''
    try:
         input("Appuyez Enter pour continuer. ")
    except SyntaxError:
         pass


def prepare_paquet(): #premiere chose que le programme fait
    '''()->list of str
        Retourne une liste des chaines de caractères qui représente tous les cartes,
        sauf le valet noir.
    '''
    paquet=[]
    couleurs = ['\u2660', '\u2661', '\u2662', '\u2663']
    valeurs = ['2','3','4','5','6','7','8','9','10','J','Q','K','A']
    for val in valeurs:
        for couleur in couleurs:
            paquet.append(val+couleur)
    paquet.remove('J\u2663') # élimine le valet noir (le valet de trèfle)
    return paquet

def melange_paquet(p): #deuxieme chose que le programme fait
    '''(list of str)->None
       Melange la liste des chaines des caractères qui représente le paquet des cartes    
    '''
    random.shuffle(p)

def donne_cartes(p): #troisieme chose que le programme fait
     '''(list of str)-> tuple of (list of str,list of str)

     Retournes deux listes qui représentent les deux mains des cartes.  
     Le donneur donne une carte à l'autre joueur, une à lui-même,
     et ça continue jusqu'à la fin du paquet p.
     '''
     
     donneur=[]
     autre=[]


     # COMPLETEZ CETTE FONCTION EN CONFORMITE AVEC LA DESCRIPTION CI-DESSUS
     # AJOUTEZ VOTRE CODE ICI

    #le paquet est deja melanger
     choix = 0
     for i in range(len(p)):
         if choix == 1:
                donneur.append(p[i])
                choix = 0

         elif choix == 0:
                autre.append(p[i])
                choix = 1

     
     return (donneur, autre)


def elimine_paires(l):
    '''
     (list of str)->list of str

     Retourne une copy de la liste l avec tous les paires éliminées 
     et mélange les éléments qui restent.

     Test:
     (Notez que l’ordre des éléments dans le résultat pourrait être différent)
     
     >>> elimine_paires(['9♠', '5♠', 'K♢', 'A♣', 'K♣', 'K♡', '2♠', 'Q♠', 'K♠', 'Q♢', 'J♠', 'A♡', '4♣', '5♣', '7♡', 'A♠', '10♣', 'Q♡', '8♡', '9♢', '10♢', 'J♡', '10♡', 'J♣', '3♡'])
     ['10♣', '2♠', '3♡', '4♣', '7♡', '8♡', 'A♣', 'J♣', 'Q♢']
     >>> elimine_paires(['10♣', '2♣', '5♢', '6♣', '9♣', 'A♢', '10♢'])
     ['2♣', '5♢', '6♣', '9♣', 'A♢']
    '''

    resultat=[]


    # COMPLETEZ CETTE FONCTION EN CONFORMITE AVEC LA DESCRIPTION CI-DESSUS
    # AJOUTEZ VOTRE CODE ICI

    if len(l) < 2:
        return l
        
    l.sort()  
    i = 1
    derniere = l[len(l)-1]
    
    while i < len(l):
        if l[i-1][:-1] != l[i][:-1]: #[:-1 enleve le symbole de la carte]
            resultat.append(l[i-1])
            i+=1
        else:
            i+=2
    resultat.append(derniere)
    random.shuffle(resultat)
    return resultat


def affiche_cartes(p):
    '''
    (list)-None
    Affiche les éléments de la liste p séparées par d'espaces
    '''


    # COMPLETEZ CETTE FONCTION EN CONFORMITE AVEC LA DESCRIPTION CI-DESSUS
    # AJOUTEZ VOTRE CODE ICI
    
    print(*p)

    

def entrez_position_valide(n):
     '''
     (int)->int
     Retourne un entier du clavier, de 1 à n (1 et n inclus).
     Continue à demander si l'usager entre un entier qui n'est pas dans l'intervalle [1,n]
     
     Précondition: n>=1
     '''

     # COMPLETEZ CETTE FONCTION EN CONFORMITE AVEC LA DESCRIPTION CI-DESSUS
     # AJOUTEZ VOTRE CODE ICI


     val = int(input("Entrez un chiffre entre 1 et " + str(n) + ": "))
     if n >= 1 and val >= 1:
          return val
     else: 
          erreur = True
          while(erreur == True):
                val = int(input("Erreur, entrez un chiffre entre 1 et " + str(n) + ": "))
                if n >= 1 and val >= 1:
                    return val

def joue():
     '''()->None
     Cette fonction joue le jeu'''
    
     p=prepare_paquet()
     melange_paquet(p)
     tmp=donne_cartes(p)
     donneur=tmp[0]
     humain=tmp[1]

     print("Bonjour. Je m'appelle Robot et je distribue les cartes.")
     print("Votre main est:")
     affiche_cartes(humain)
     print("Ne vous inquiétez pas, je ne peux pas voir vos cartes ni leur ordre.")
     print("Maintenant défaussez toutes les paires de votre main. Je vais le faire moi aussi.")
     attend_le_joueur()
     
     donneur=elimine_paires(donneur)
     humain=elimine_paires(humain)
    
     # COMPLETEZ CETTE FONCTION EN CONFORMITE AVEC LA DESCRIPTION CI-DESSUS
     # AJOUTEZ VOTRE CODE ICI
    
     tour = 1
        #tour == 1 -> tour au joueur
        #tour == 0 -> tour a l'ordi

     while(True):
            if len(humain) == 0:
               print("Il vous reste aucune cartes ")
               print("Felicitations, vous avez gagner ")
               break

            elif len(donneur) == 0:
                print("Bouhou, vous avez perdu ")
                break

            else:
                 if tour == 1:
                        tour = 0

                        print("C'est a votre tour, voici vos cartes")
                        affiche_cartes(humain)
                        print("Il me reste " + str(len(donneur)) + " cartes, laquelle voulez vous?")
                        choix = entrez_position_valide(len(donneur))

                        print("")
                        print("Vous avez choisis ma " + str(choix) + "e carte qui etait " + donneur[int(choix)-1])

                        humain.append(donneur[int(choix)-1])
                        donneur.remove(donneur[int(choix)-1])

                        print("Votre nouvelle main sans paires est: " )

                        humain = elimine_paires(humain)
                        print(*humain)

                        attend_le_joueur()

                 elif tour == 0:
                      tour = 1
                      print("")
                      print("Tour au robot...")
                      print("")
                      choix = random.randint(1,len(humain))

                      print("Je prend ta " + str(choix) + "e carte qui etait " + humain[int(choix)-1])
                      
                      donneur.append(humain[int(choix)-1])
                      humain.remove(humain[int(choix)-1])
                      donneur = elimine_paires(donneur)
                      attend_le_joueur()


# programme principale
joue()

