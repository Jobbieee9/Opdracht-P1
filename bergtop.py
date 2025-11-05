import states

def begin():
    print("\n--- BERGTOP ---")
    print(f"Gezondheid: {states.gezondheid}, Honger: {states.honger}, Dorst: {states.dorst}, Items: {states.voorwerpen}")

    verplicht = ["STRAND", "JUNGLE1", 
                 "WATERVAL1", "GROT1", "GROT2"]
    if not all(loc in states.bezochte_locaties for loc in verplicht):
        print("Je hebt nog niet de benodigde spullen verzameld om boven te komen, zoek alle locaties eerst af!")
        states.locatie = "WATERVAL2"
        return

    print("Je ziet een schip in de verte. Je kunt een groot vuur maken of wachten.")
    print("Typ 'VUUR' of 'WACHT'.")

    antwoord = input("> ")

    if antwoord == "VUUR" and "touw" in states.voorwerpen and "tak" in states.voorwerpen:
        print("Je maakt een groot vuur. Het schip ziet de rook! Je bent gered!")
        states.locatie = "GERED"
    else:
        print("Je hebt niet genoeg materialen of kiest te wachten. Morgen probeer je het opnieuw.")
        states.locatie = "BERGTOP2"

    if "BERGTOP1" not in states.bezochte_locaties:
        states.bezochte_locaties.append("BERGTOP1")