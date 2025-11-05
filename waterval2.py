import states

def begin():
    print("\n--- WATERVAL (fase 2) ---")
    print(f"Gezondheid: {states.gezondheid}, Honger: {states.honger}, Dorst: {states.dorst}, Items: {states.voorwerpen}")
    print("Je klimt omhoog langs de waterval en vindt wat bessen en een tak.")
    print("Typ 'PAKKEN' of 'NEGEREN'.")

    antwoord = input("> ")

    if antwoord == "PAKKEN":
        print("Je neemt alles mee.")
        print("Je klimt weer naar beneden, hier is niks meer te vinden.")
        states.voorwerpen.append("tak")
        states.voorwerpen.append("bessen")
        states.honger -= 1
        states.locatie = "WATERVAL1"
    else:
        print("Je negeert de spullen en loopt terug naar de jungle.")
        states.locatie = "JUNGLE3"

    if "WATERVAL2" not in states.bezochte_locaties:
        states.bezochte_locaties.append("WATERVAL2")
