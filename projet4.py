# python3
# INFO-F101 : programmation
# projet4.py : Annuaire de super-Héros
# Servais Nikita

import sys


############
# fonction #
############

def read_data(fichier):
    """
    Lis un fichier et renvoie un annuaire
    """
    try:
        with open(fichier, encoding='utf8') as f:
            annuaire = {}
            test_file = False
            for line in f:
                test_file = True
                hero = line.strip().split(';')
                hero_info_list = [('telephone', hero[2]),
                                  ('super-pouvoir', hero[3].split(',')),
                                  ('puissance', int(hero[4]))]
                hero_info = dict(hero_info_list)
                if hero[1] in annuaire:
                    annuaire[hero[1]][hero[0]] = hero_info
                else:
                    annuaire[hero[1]] = {hero[0]: hero_info}
            if not test_file:
                print("Vous n’avez pas de super-héro actuellement dans l’annuaire, veuillez effectuer")
                print("au moins une entrée :")
                annuaire = add_hero(annuaire)
            return annuaire
    except FileNotFoundError:
        print("fichier introuvable")
        sys.exit()


def write_data(annuaire):
    """
    Enregistre l'annuaire sur un fichier au choix
    """
    print("Comment voulez-vous appeler le fichier "
          "où sauvegarder l’annuaire ? ")
    choix = str(input())
    while (choix[-4] + choix[-3] + choix[-2] + choix[-1]) != '.txt':
        print("Votre nom de fichier doit finir par '.txt'")
        print("Comment voulez-vous appeler le fichier où sauvegarder l’annuaire ?")
        choix = str(input())
    with open(choix, 'w', encoding='utf8') as f:
        for ville in annuaire:
            for hero in annuaire[ville]:
                f.write(hero + ";")
                f.write(ville + ";")
                f.write(annuaire[ville][hero]['telephone'] + ";")
                f.write(",".join(annuaire[ville][hero]['super-pouvoir']) + ";")
                f.write(str(annuaire[ville][hero]['puissance']))
                f.write('\n')
    return annuaire


def add_hero(annuaire):
    """
    Ajoute un nouveau hero à l'annuaire
    """
    hero_info_list = []
    print("Comment s’appelle votre super-héro ?")
    hero = str(input())
    print("Dans quelle ville habite-t-il ?")
    ville = str(input())
    print("Quel est son numéro de téléphone ?")
    tel = str(input())
    while (len(tel) != 14 or ((tel[0] + tel[4] + tel[5] + tel[9] != '()--')
    if len(tel) >= 10 else True)) and tel != "":
        print("Votre numéro de téléphone doit être composé de 3 entiers séparés par ’-’")
        print("dans le format (CCC)-CCC-CCCC.")
        print("Veuillez réessayer d’entrer le numéro.")
        print("Quel est son numéro de téléphone ?")
        tel = str(input())
    hero_info_list.append(('telephone', tel))
    print("Quels sont ses super-pouvoirs ? (Entrez 0 pour arrêter l’enregistrement)")
    superpouvoir = []
    pouvoir = ""
    while pouvoir != "0":
        if pouvoir.strip():
            superpouvoir.append(pouvoir)
        pouvoir = (str(input()))
    hero_info_list.append(('super-pouvoir', superpouvoir))
    print("Quelle est sa puissance ?")
    puissance = str(input())

    while puissance != "" and not int(puissance) <= 100:
        print("Vous devez rentrer un nombre entier entre 0 et 100 !")
        print("Quelle est sa puissance ?")
        puissance = str(input())
    hero_info_list.append(('puissance', puissance))
    hero_info = dict(hero_info_list)
    if ville in annuaire:
        annuaire[ville][hero] = hero_info
    else:
        annuaire[ville] = {hero: hero_info}
    print("Votre super-héro a été ajouté à l’annuaire !")
    return annuaire


def filter_hero(annuaire):
    """
    Permet de trouver un hero adapter au besoin de l'utilisateur
    """
    print("Ok, dans quelle ville vous trouvez-vous ?")
    ville = str(input())
    if ville in annuaire:
        print("Il y a " + str(len(annuaire[ville])) + " super-hero" + (
            "s" if len(annuaire[ville]) > 1 else "") + " dans cette ville.")
        print("Quel niveau de puissance minimum avez-vous besoin ? ")
        puissance = int(input())
        test = False
        # while not test and i < len(annuaire[ville]) :
        for hero in annuaire[ville]:
            if annuaire[ville][hero]["puissance"] \
                    >= int(puissance):
                test = True
        if test:
            print("voici " + ("le super-hero" if len(annuaire[ville]) == 1
                              else "les super-héros") +
                  " que vous pouvez contacter :")
            for hero in annuaire[ville]:
                if annuaire[ville][hero]["puissance"] >= puissance:
                    print(hero + ", possédant une puissance de " + str(annuaire[ville][hero]["puissance"]))
                    print("    son/ses super-pouvoir :")
                    for pouvoir in annuaire[ville][hero]['super-pouvoir']:
                        print("        -" + pouvoir)
                    print("    Numéro de téléphone : " + annuaire[ville][hero]['telephone'])
        else:
            print("Aucun des super-héros n’est suffisamment puissant... Bonne chance ")
        print("Bon courage avec votre problème !" + '\n')
    else:
        print("Aucun super-héro ne se trouve dans cette ville... Bonne chance !")
    return annuaire


def show_hero(annuaire):
    """
    Permet de naviguer dans l'annuaire
    """
    sortir = False
    while not sortir:
        dic = {}
        print("Veuillez choisir une ville pour y voir les héros disponibleS")
        for i, ville in enumerate(annuaire, 1):
            print(str(i) + ") " + ville)
            dic[str(i)] = ville
        test = False
        while not test:
            try:
                choix_ville = dic[str(input())]
                test = True
            except:
                print("Vous devez choisir entre " +
                      ', '.join(str(i) for i in range(1, len(dic))) + " ou " +
                      str(len(dic)) + " !")
                test = False
        dic = {}
        print("Veuillez choisir un hero pour y voir les informations disponibles")
        for i, hero in enumerate(annuaire[choix_ville], 1):
            print(str(i) + ") " + hero)
            dic[str(i)] = hero
        test = False
        while not test:
            try:
                choix_hero = dic[str(input())]
                test = True
            except:
                print("Vous devez choisir entre " +
                      ', '.join(str(i) for i in range(1, len(dic))) +
                      " ou " + str(len(dic)) + " !")
                test = False
        print(choix_hero + " possède une puissance de " + str(annuaire[choix_ville][choix_hero]["puissance"]))
        print("    son/ses super-pouvoir :")
        for pouvoir in annuaire[choix_ville][choix_hero]['super-pouvoir']:
            print("        -" + pouvoir)
        print("    Numéro de téléphone : " +
              annuaire[choix_ville][choix_hero]['telephone'])
        print("Que voulez-vous faire ?")
        print("1) revenir au menu")
        print("2) continuer à naviguer dans l'annuaire")
        choix = str(input())
        while not choix in ('1', '2'):
            print("veuillez choisir 1 ou 2 !")
            choix = str(input())
        sortir = True if choix == '1' else False
    return annuaire


def menu(fichier):
    """
    Permet d'accéder aux différentes fonctionnalités du programme
    """
    sortir = False
    annuaire = read_data(fichier)
    print("Bienvenue dans le programme de contact des super-héros !")
    while not sortir:
        dic = {'1': add_hero,
               '2': filter_hero,
               '3': show_hero,
               '4': write_data}
        print("Que voulez-vous faire ?")
        print("1) Ajouter un nouveau super-héro à l’annuaire")
        print("2) Contacter un super-héro, je suis en danger !")
        print("3) Voir l’annuaire")
        print("4) Sauvegarder l’annuaire")
        print("5) Quitter le programme")
        try:
            choix = str(input())
            while int(choix) not in range(1, 6):
                print("Vous devez choisir 1, 2, 3, 4 ou 5 !")
                choix = str(input())
            if int(choix) < 5:
                annuaire = dic[choix](annuaire)
            else:
                sortir = True
        except ValueError:
            print("Vous devez choisir 1, 2, 3, 4 ou 5 !")
    return


# code principal

try:
    menu(sys.argv[1])
    print("Merci d’avoir utilisé notre programme de contact !")
except IndexError:
    print('vous devez entrer un fichier valide comme argument')
finally:
    sys.exit()
