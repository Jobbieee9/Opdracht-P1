import states

def begin():
    print("--- JUNGLE (fase 2) ---")
    print(f"Gezondheid: {states.gezondheid}, Honger: {states.honger}, Dorst: {states.dorst}, Items: {states.voorwerpen}")
    print("Dieper in de jungle zie je een riviertje en een oude boom.")
    print("Je kunt het riviertje volgen of naar de boom gaan.")
    print("het wordt steeds dichter en donkerder, je kunt ook teruggaan!")
    print("Typ 'RIVIER' , 'BOOM' of 'TERUG'.")

    antwoord = input("> ")

    if antwoord == "RIVIER":
        print("Je volgt het riviertje en vindt bessen. Je honger neemt af.")
        print("ook zie je een sjamaan bij een vuurtje op een open plek zitten.")
        print("Je loopt snel naar hem toe!")
        states.honger += 3
        states.dorst += 3
        states.locatie = "JUNGLE3"
    elif antwoord == "BOOM":
        print("Je klimt in de boom ")
        print("Je kijkt de omgeving rond en ziet een sjamaan in de verte.")
        print("Je klimt snel naar bendeden en loopt naar de sjamaan.")
        states.honger += 3
        states.dorst += 3
        states.locatie = "JUNGLE3"
    elif antwoord == "TERUG":
        print("je loopt terug... lafaard.")
        states.honger += 3
        states.dorst += 3
        states.locatie = "JUNGLE1"

    if "JUNGLE2" not in states.bezochte_locaties:
        states.bezochte_locaties.append("JUNGLE2")
