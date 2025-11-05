import states

def begin():
    print("\n--- GROT (fase 2) ---")
    print(f"Gezondheid: {states.gezondheid}, Honger: {states.honger}, Dorst: {states.dorst}, Items: {states.voorwerpen}")
    print("Je gaat dieper de grot in en vindt een kleine schuilplaats.")
    print("Typ 'VERKEN' of 'TERUG'.")

    antwoord = input("> ")

    if antwoord == "VERKEN":
        print("Je vindt voedsel en water. Je honger en dorst nemen af.")
        states.voorwerpen.append("voedsel")
        states.honger -= 2
        states.dorst -= 2
        states.locatie = "GROT1"
    else:
        states.locatie = "JUNGLE3"

    if "GROT2" not in states.bezochte_locaties:
        states.bezochte_locaties.append("GROT2")
