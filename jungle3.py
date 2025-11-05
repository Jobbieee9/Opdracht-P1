import states

def begin():
    print("\n--- JUNGLE (fase 3) ---")
    print(f"Gezondheid: {states.gezondheid}, Honger: {states.honger}, Dorst: {states.dorst}, Items: {states.voorwerpen}, Kennis: {states.kennis}")
    print("Diep in de jungle zie je een oude sjamaan bij een kampvuur.")
    print("Je kunt met hem praten of teruggaan.")
    print("Typ 'PRATEN' of 'TERUG'.")

    antwoord = input("> ")

    if antwoord == "PRATEN":
        print("De sjamaan leert je over de geheimen van het eiland. Je weet nu hoe je de grot binnen moet komen!")
        if "grot" not in states.kennis:
            states.kennis.append("grot")
        states.locatie = "GROT1"
    elif antwoord == "TERUG":
        print("Je gaat terug naar Jungle2.")
        states.locatie = "JUNGLE2"

    if "JUNGLE3" not in states.bezochte_locaties:
        states.bezochte_locaties.append("JUNGLE3")
