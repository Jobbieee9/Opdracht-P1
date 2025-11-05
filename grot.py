import states

def begin():
    if "grot" not in states.kennis:
        print("\nJe weet nog niet hoe je de grot binnen moet komen... Je moet eerst meer kennis krijgen...")
        states.locatie = "JUNGLE1"
        return

    print("\n--- GROT ---")
    print(f"Gezondheid: {states.gezondheid}, Honger: {states.honger}, Dorst: {states.dorst}, Items: {states.voorwerpen}")
    print("Het is donker en koel. Je hoort druppelend water.")
    print("Typ 'RUST' , 'VERKEN of 'TERUG'.")

    antwoord = input("> ")

    if antwoord == "RUST":
        states.gezondheid += 5
        if states.gezondheid > 100:
            states.gezondheid = 100
        print("Je rust uit en je gezondheid neemt toe.")
        states.locatie = "GROT1"
    elif antwoord == "VERKEN":
        states.locatie = "GROT2"
    else:
        states.locatie = "JUNGLE3"

    if "GROT1" not in states.bezochte_locaties:
        states.bezochte_locaties.append("GROT1")
