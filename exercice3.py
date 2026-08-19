import random

# Générer un nombre mystère au hasard entre 1 et 10
nombre_mystere = random.randint(1, 10)
tentatives = 0
trouve = False

print("=== JEU DU NOMBRE MYSTÈRE ===")
print("J'ai choisi un nombre entre 1 et 10. À toi de deviner !")

# La boucle 'while' répète le code TANT QUE 'trouve' reste Faux
while not trouve:
    choix = int(input("Propose un nombre : "))
        tentatives += 1  # Compte le nombre d'essais

            if choix < nombre_mystere:
                    print("C'est PLUS GRAND ! Essaye encore.\n")
                        elif choix > nombre_mystere:
                                print("C'est PLUS PETIT ! Essaye encore.\n")
                                    else:
                                            print(f"Bravo ! Tu as trouvé le nombre {nombre_mystere} en {tentatives} essai(s) ! 🎉")
                                                    trouve = True  # Arrête la boucle
                                                    ")
