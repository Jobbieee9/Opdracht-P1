import states

def begin():
    print("\n--- JUNGLE ---")
    print(f"Gezondheid: {states.gezondheid}, Honger: {states.honger}, Dorst: {states.dorst}, Items: {states.voorwerpen}")
    print("Je staat in de jungle. Er is een pad naar de waterval en een donkere grot.")
    print("Je kunt ook vruchten zoeken.")
    print("Typ 'WATERVAL', 'GROT' of 'VRUCHTEN'.")

    antwoord = input("> ")

    if antwoord == "WATERVAL":
        print("Je loopt naar de waterval.")
        states.locatie = "WATERVAL1"
    elif antwoord == "GROT":
        print("Je loopt naar de grot.")
        states.locatie = "GROT1"
    elif antwoord == "VRUCHTEN":
        print("Je vindt wat vruchten. Je honger neemt af.")
        states.honger -= 1
        if states.honger < 0:
            states.honger = 0
        states.locatie = "JUNGLE2"

    if "JUNGLE1" not in states.bezochte_locaties:
        states.bezochte_locaties.append("JUNGLE1")
