def calculatrice():
    try:
        
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
            
            if nombre2 == 0:
                print("Erreur : Division par zéro impossible.")
                return
            resultat = nombre1 / nombre2
        else:
            print("Erreur : Opération non valide.")
            return
        
        print(f"Résultat : {resultat}")

    except ValueError:
        print("Erreur : Veuillez entrer des nombres valides.")
    except Exception as e:
        print(f"Erreur : Une erreur inattendue s'est produite - {e}")

calculatrice()