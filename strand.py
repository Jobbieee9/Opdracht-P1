import states

def begin():
    print("--- STRAND ---")
    print(f"Gezondheid: {states.gezondheid}, Honger: {states.honger}, Dorst: {states.dorst}, Items: {states.voorwerpen}")
    print("Je staat op het strand. Je ziet de jungle in de verte en een klein kampvuur.")
    print("Je kunt spullen zoeken in het zand of naar de jungle lopen.")
    print("Typ 'ZOEK' of 'JUNGLE'.")

    antwoord = input("> ")

    if antwoord == "ZOEK":
        print("Je vindt een stuk touw!")
        states.voorwerpen.append("touw")
        states.honger += 3
        states.dorst += 3
        states.locatie = "STRAND2"
    elif antwoord == "JUNGLE":
        print("Je loopt de jungle in.")
        states.honger += 3
        states.dorst += 3
        states.locatie = "JUNGLE1"

    if "STRAND" not in states.bezochte_locaties:
        states.bezochte_locaties.append("STRAND")

