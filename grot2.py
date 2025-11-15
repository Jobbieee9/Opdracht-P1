import states

def begin():
    print("--- GROT (fase 2) ---")
    print(f"Gezondheid: {states.gezondheid}, Honger: {states.honger}, Dorst: {states.dorst}, Items: {states.voorwerpen}")
    print("Je gaat dieper de grot in en vindt een kleine schuilplaats.")
    print("Typ 'VERKEN' of 'TERUG'.")

    antwoord = input("> ")

    if antwoord == "VERKEN":
        print("Je vindt voedsel en water. Je honger en dorst nemen af.")
        states.honger -= 5
        states.dorst -= 5
        states.locatie = "GROT3"
    elif antwoord == "TERUG":
        print("je loopt naar terug naar buiten en krijgt een zenuwinzinking doordat je bijna struikelt over een steen.")
        states.gezondheid -= 5
        states.locatie = "JUNGLE3"

    if "GROT2" not in states.bezochte_locaties:
        states.bezochte_locaties.append("GROT2")
