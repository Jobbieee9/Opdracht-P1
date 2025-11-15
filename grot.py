import states

def begin():
    if "grot" not in states.kennis:
        print("Je weet nog niet hoe je de grot binnen moet komen... Je moet eerst meer kennis krijgen...")
        states.locatie = "JUNGLE1"
        return

    print("--- GROT ---")
    print(f"Gezondheid: {states.gezondheid}, Honger: {states.honger}, Dorst: {states.dorst}, Items: {states.voorwerpen}")
    print("Het is donker en koel. Je hoort druppelend water.")
    print("Typ 'RUST' , 'VERKEN of 'TERUG'.")

    antwoord = input("> ")

    if antwoord == "RUST":
        states.gezondheid += 20
        if states.gezondheid > 100:
            states.gezondheid = 100
        print("Je rust uit en je gezondheid neemt toe.")
        states.locatie = "GROT1"
    elif antwoord == "VERKEN":
        states.honger += 3
        states.dorst += 3
        states.locatie = "GROT2"
    elif antwoord == "TERUG":
        states.honger += 3
        states.dorst += 3
        states.locatie = "JUNGLE3"

    if "GROT1" not in states.bezochte_locaties:
        states.bezochte_locaties.append("GROT1")
