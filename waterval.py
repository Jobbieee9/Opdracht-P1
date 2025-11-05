import states

def begin():
    print("\n--- WATERVAL ---")
    print(f"Gezondheid: {states.gezondheid}, Honger: {states.honger}, Dorst: {states.dorst}, Items: {states.voorwerpen}")
    print("Het water is helder en koel.")
    print("Typ 'DRINK', 'BERGTOP' of 'JUNGLE'.")

    antwoord = input("> ")

    if antwoord == "DRINK":
        print("Je drinkt wat water. Dorst neemt af.")
        states.dorst -= 2
        if states.dorst < 0:
            states.dorst = 0
        states.locatie = "WATERVAL1"
    elif antwoord == "BERGTOP":
        states.locatie = "BERGTOP1"
    elif antwoord == "JUNGLE":
        states.locatie = "JUNGLE2"

    if "WATERVALL1" not in states.bezochte_locaties:
        states.bezochte_locaties.append("WATERVAL1")
