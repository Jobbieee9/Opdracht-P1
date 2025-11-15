import states

def begin():
    print("--- STRAND (fase 2) ---")
    print(f"Gezondheid: {states.gezondheid}, Honger: {states.honger}, Dorst: {states.dorst}, Items: {states.voorwerpen}")
    print("Je loopt verder op het strand en ziet een wrak van een boot.")
    print("Je kunt de boot onderzoeken of naar de jungle lopen.")
    print("Typ 'BOOT' of 'JUNGLE'.")

    antwoord = input("> ")

    if antwoord == "BOOT":
        print("Je vindt een oude waterfles en wat eten!")
        states.honger -= 3
        states.dorst -= 3
        states.locatie = "STRAND3"
    elif antwoord == "JUNGLE":
        print("Je loopt naar de jungle.")
        states.dorst +=3
        states.honger +=3
        states.locatie = "JUNGLE1"

    if "STRAND2" not in states.bezochte_locaties:
        states.bezochte_locaties.append("STRAND2")
