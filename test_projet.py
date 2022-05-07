import sys

def add_hero(annuaire) :
    hero_info_list = []
    reference = ['telephone','super-pouvoir','niveau de puissance']
    print('Comment s’appelle votre super-héro ?')
    hero = input(str())
    print('Dans quelle ville habite-t-il ? ')
    ville = input(str())
    print('Quel est son numéro de téléphone ?')
    hero_info_list.append(input(str()))
    print('Quels sont ses super-pouvoirs ? (Entrez 0 pour arrêter l’enregistrement) ')
    superpouvoir = []
    pouvoir = ""
    while pouvoir != "0" :
        if pouvoir.strip() :
            superpouvoir.append(pouvoir)
        pouvoir = (input(str()))
    hero_info_list.append(superpouvoir)
    print('Quelle est sa puissance ? ')
    hero_info_list.append(input(str()))
    hero_info_list = zip(reference,hero_info_list)
    hero_info = dict(hero_info_list)
    if ville in annuaire :
        annuaire[ville][hero] = hero_info
    else :
        annuaire[ville] = {hero : hero_info}
    print('Votre super-héro a été ajouté à l’annuaire !')
    return annuaire
def filter_hero(annuaire) :
    print("Ok, dans quelle ville vous trouvez-vous ?")
    ville = input(str())
    if ville in annuaire :
        print("Il y a "+str(len(annuaire[ville]))+" super_hero dans cette ville.")
        print("Quel niveau de puissance minimum avez-vous besoin ? ")
        puissance = input(str())
        test = False
        #while not test and i < len(annuaire[ville]) :
        for hero in annuaire[ville] :
            if annuaire[ville][hero]["niveau de puissance"] >= puissance :
                test = True
        if test :
            print("voici le super-hero que vous pouvez contacter :")
            for hero in annuaire[ville] :
                if annuaire[ville][hero]["niveau de puissance"] >= puissance :
                    print(hero+", possedant une puissance de "\
                          +annuaire[ville][hero]["niveau de puissance"]\
                          +'\n'+"      son/ses super-pouvoir :")
                    for pouvoir in annuaire[ville][hero]['super-pouvoir']:
                        print("         -"+pouvoir)
                    print("Numéro de téléphone : "+annuaire[ville][hero]['telephone'])
        else :
            print("Aucun des super-héros n’est suffisamment puissant... Bonne chance ")
        print("Bon courage avec votre problème !")
    else :
        print("Aucun super-héro ne se trouve dans cette ville... Bonne chance !")

def read_data(filename) :
    try :
        with open(filename, encoding = 'utf8') as f : 
            reference = ['telephone','super-pouvoir', 'niveau de puissance']
            annuaire = {}
            test_file = False
            for line in  f :
                test_file = True
                hero = line.strip().split(';')
                hero_info_list = zip(reference,[hero[2], hero[3].split(','),hero[4]])
                hero_info = dict(hero_info_list)
                if hero[1] in annuaire :
                    annuaire[hero[1]][hero[0]] = hero_info
                else :
                    annuaire[hero[1]] = {hero[0] : hero_info}
            if not test_file :
                print("Vous n’avez pas de super-héros actuellement dans l’annuaire,"\
                      " veuillez effectuer")
                print("au moins une entrée :")
                annuaire = add_hero(annuaire)
            return annuaire
    except FileNotFoundError :
        print("file not found")
        sys.exit()

def write_data(annuaire):
    print("Comment voulez-vous appeler le fichier où sauvegarder l’annuaire ? ")
    choix = input(str())
    while (choix[-4]+choix[-3]+choix[-2]+choix[-1]) != ('.txt') :
        print("Votre nom de fichier doit finir par '.txt'")
        print("Comment voulez-vous appeler le fichier où sauvegarder l’annuaire ?")
        choix = input(str())
    with open(choix,'w',encoding = 'utf8') as f :
        for ville in annuaire :
            f.write(ville+";")
            for hero in annuaire[ville] :
                f.write(hero+";")
                f.write(annuaire[ville][hero][reference[0]]+";")
                f.write(",".join(annuaire[ville][hero][reference[1]])+";")
                f.write(annuaire[ville][hero][reference[2]]) 
            
    return
def menu(fichier) :
    dic = {'1' : add_hero,
           '2' : filter_hero,
           '3' : print,
           '4': write_data,
           '5' : exit}
    print("Bienvenue dans le programme de contact des super-héros !")
    print("Que voulez-vous faire ?")
    print("1) Ajouter un nouveau super-héro à l’annuaire")
    print("2) Contacter un super-héro, je suis en danger !")
    print("3) Voir l’annuaire")
    print("4) Sauvegarder l’annuaire")
    print("5) Quitter le programme")
    choix = input(str())
    while int(choix) not in range(1,6) :
        print("Vous devez choisir 1, 2, 3, 4 ou 5 !")
        choix = input(str())
    dic[choix](annuaire)
    return 
annuaire = read_data("example_annuaire.txt")

while True :
    menu(annuaire)
