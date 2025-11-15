import states

def begin ():
    print(f"Gezondheid: {states.gezondheid}, Honger: {states.honger}, Dorst: {states.dorst}, Items: {states.voorwerpen}")
    print("Je kijkt nog wat rond, maar er is niks meer te vinden hier.")
    print("Je kunt TERUG of nog even UITRUSTEN om te herstellen en daarna terug te gaan")
    
    antwoord = input ("> ")
    
    if antwoord == "TERUG":
        states.honger += 3
        states.dorst += 3
        states.locatie = "JUNGLE1"
    elif antwoord == "UITRUSTEN":
        states.gezondheid += 20
        if states.gezondheid >= 100:
            states.gezondheid = 100
            states.locatie = "JUNGLE1"