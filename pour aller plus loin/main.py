def calculatrice():
    historique = []

    def afficher_historique():
        if historique:
            print("Historique des calculs:")
            for i, calcul in enumerate(historique, start=1):
                print(f"{i}. {calcul}")
        else:
            print("L'historique est vide.")

    try:
        while True:
            nombre1 = float(input("Entrez le premier nombre : "))
            operation = input("Entrez l'opération (+, -, *, /) : ")
            nombre2 = float(input("Entrez le deuxième nombre : "))

            if operation == "+":
                resultat = nombre1 + nombre2
            elif operation == "-":
                resultat = nombre1 - nombre2
            elif operation == "*":
                resultat = nombre1 * nombre2
            elif operation == "/":
                # Gérer la division par zéro
                if nombre2 == 0:
                    print("Erreur : Division par zéro impossible.")
                    continue
                resultat = nombre1 / nombre2
            else:
                print("Erreur : Opération non valide.")
                continue

            calcul = f"{nombre1} {operation} {nombre2} = {resultat}"
            historique.append(calcul)

            print(f"Résultat : {resultat}")

            voir_historique = input("Voulez-vous voir l'historique des calculs? (o/n): ").lower()
            if voir_historique == "o":
                afficher_historique()

            effacer_historique = input("Voulez-vous effacer l'historique des calculs? (o/n): ").lower()
            if effacer_historique == "o":
                historique.clear()

            continuer_calcul = input("Voulez-vous faire un autre calcul? (o/n): ").lower()
            if continuer_calcul != "o":
                break

    except ValueError:
        print("Erreur : Veuillez entrer des nombres valides.")
    except Exception as e:
        print(f"Erreur : Une erreur inattendue s'est produite - {e}")


calculatrice()