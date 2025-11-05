import states

def begin():
    print("\n--- BERGTOP (fase 2) ---")
    print(f"Gezondheid: {states.gezondheid}, Honger: {states.honger}, Dorst: {states.dorst}, Items: {states.voorwerpen}")
    print("Je krijgt nog een kans om een groot vuur te maken.")
    print("Typ 'VUUR' om het vuur te maken of 'WACHT' om het de volgende dag te proberen.")

    antwoord = input("> ")

    if antwoord == "VUUR":
        if "touw" in states.voorwerpen and "tak" in states.voorwerpen:
            print("Je maakt een groot vuur. Het schip ziet de rook! Je bent gered!")
            states.locatie = "GERED"
        else:
            print("Je hebt niet genoeg spullen. Je moet terug naar het strand om nieuwe materialen te zoeken.")
            states.locatie = "STRAND"
    elif antwoord == "WACHT":
        print("Je hebt nog steeds niet genoeg spullen. Je moet terug naar het strand om nieuwe materialen te zoeken.")
        states.locatie = "STRAND"

    if "BERGTOP2" not in states.bezochte_locaties:
        states.bezochte_locaties.append("BERGTOP2")
