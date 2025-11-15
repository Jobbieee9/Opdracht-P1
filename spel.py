import states
import strand
import strand2
import strand3
import jungle
import jungle2
import jungle3
import waterval
import waterval2
import grot
import grot2
import bergtop
import bergtop2

while True:
    
    if states.locatie == "GERED":
        print("🎉 Je bent gered! Goed gedaan!")
        break
    if states.locatie == "GAMEOVER":
        print("💀 Je hebt het spel opgegeven. Game over.")
        break
    if states.gezondheid <= 0:
        print("💀 Je bent te zwak geworden... Game over.")
        break
    if states.honger <= 0 :
        states.honger = 0
    if states.dorst <= 0 :
        states.dorst = 0

    if states.honger >= 5:
        if not states.honger_schade_actief:
            states.gezondheid -= 5
            states.honger_schade_actief = True
            print("Je voelt je zwakker door honger. Gezondheid daalt!")
    else:
        states.honger_schade_actief = False

    if states.dorst >= 5:
        if not states.dorst_schade_actief:
            states.gezondheid -= 5
            states.dorst_schade_actief = True
            print("Je voelt je zwakker door dorst. Gezondheid daalt!")
    else:
        states.dorst_schade_actief = False
    
    honger_level = states.honger // 5 

    if honger_level > states.laatste_honger_schade:
        states.gezondheid -= 5
        print("Je krijgt schade door honger!")
        states.laatste_honger_schade = honger_level

    elif honger_level < states.laatste_honger_schade:
        states.laatste_honger_schade = honger_level


    dorst_level = states.dorst // 5  

    if dorst_level > states.laatste_dorst_schade:
        states.gezondheid -= 5
        print("Je krijgt schade door dorst!")
        states.laatste_dorst_schade = dorst_level

    elif dorst_level < states.laatste_dorst_schade:
        states.laatste_dorst_schade = dorst_level

  

    if states.locatie == "STRAND":
        strand.begin()
    elif states.locatie == "STRAND2":
        strand2.begin()
    elif states.locatie == "STRAND3":
        strand3.begin()
    elif states.locatie == "JUNGLE1":
        jungle.begin()
    elif states.locatie == "JUNGLE2":
        jungle2.begin()
    elif states.locatie == "JUNGLE3":
        jungle3.begin()
    elif states.locatie == "WATERVAL1":
        waterval.begin()
    elif states.locatie == "WATERVAL2":
        waterval2.begin()
    elif states.locatie == "GROT1":
        grot.begin()
    elif states.locatie == "GROT2":
        grot2.begin()
    elif states.locatie == "BERGTOP1":
        bergtop.begin()
    elif states.locatie == "BERGTOP2":
        bergtop2.begin()
    