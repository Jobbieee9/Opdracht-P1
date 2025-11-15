import states

def begin():
    print("--- STRAND (fase 3) ---")
    print(f"Gezondheid: {states.gezondheid}, Honger: {states.honger}, Dorst: {states.dorst}, Items: {states.voorwerpen}")
    print("Het strand is rustig en leeg. Er is verder niets te vinden.")
    print("Je kunt terug naar de jungle gaan of het spel opgeven.")
    print("Typ 'JUNGLE' of 'OPGEVEN'.")

    antwoord = input("> ")

    if antwoord == "JUNGLE":
        print("Je loopt terug naar de jungle.")
        states.dorst +=3
        states.honger +=3
        states.locatie = "JUNGLE1"
    elif antwoord == "OPGEVEN":
        print("Je geeft het op en verdinkt jezelf in zee, zwakkeling! Game over.")
        states.locatie = "GAMEOVER"

    if "STRAND3" not in states.bezochte_locaties:
        states.bezochte_locaties.append("STRAND3")
