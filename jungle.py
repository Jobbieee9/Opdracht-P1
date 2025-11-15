import states

def begin():
    print("--- JUNGLE ---")
    print(f"Gezondheid: {states.gezondheid}, Honger: {states.honger}, Dorst: {states.dorst}, Items: {states.voorwerpen}")
    print("Je staat in de jungle. Er is een pad naar de waterval en een donkere grot.")
    print("Je kunt ook vruchten zoeken.")
    print("Typ 'WATERVAL', 'GROT' of 'VRUCHTEN'.")

    antwoord = input("> ")

    if antwoord == "WATERVAL":
        print("Je loopt naar de waterval.")
        states.honger += 3
        states.dorst += 3
        states.locatie = "WATERVAL1"
    elif antwoord == "GROT":
        print("Je loopt naar de grot.")
        states.honger += 3
        states.dorst += 3
        states.locatie = "GROT1"
    elif antwoord == "VRUCHTEN":
        print("Je vindt wat vruchten. Je honger neemt af.")
        print("Je loopt wat verder de jungle in.")
        states.honger -= 3
        if states.honger < 0:
            states.honger = 0
        states.locatie = "JUNGLE2"

    if "JUNGLE1" not in states.bezochte_locaties:
        states.bezochte_locaties.append("JUNGLE1")
