import states

def begin():
    print("--- WATERVAL ---")
    print(f"Gezondheid: {states.gezondheid}, Honger: {states.honger}, Dorst: {states.dorst}, Items: {states.voorwerpen}")
    print("Het water is helder en koel.")
    print("Typ 'DRINK', 'BERGTOP' of 'JUNGLE'.")

    antwoord = input("> ")

    if antwoord == "DRINK":
        print("Je drinkt wat water. Dorst neemt af.")
        states.dorst -= 3
        if states.dorst < 0:
            states.dorst = 0
        states.honger +=3
        states.locatie = "WATERVAL2"
    elif antwoord == "BERGTOP":
        states.honger += 3
        states.dorst += 3
        states.locatie = "BERGTOP1"
    elif antwoord == "JUNGLE":
        states.honger += 3
        states.dorst += 3
        states.locatie = "JUNGLE2"

    if "WATERVAL1" not in states.bezochte_locaties:
        states.bezochte_locaties.append("WATERVAL1")
