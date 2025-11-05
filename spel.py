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
        print("\n🎉 Je bent gered! Goed gedaan!")
        break
    if states.locatie == "GAMEOVER":
        print("\n💀 Je hebt het spel opgegeven. Game over.")
        break
    if states.gezondheid <= 0:
        print("\n💀 Je bent te zwak geworden... Game over.")
        break


    if states.honger > 5 or states.dorst > 5:
        states.gezondheid -= 5
        print("\nJe voelt je zwakker door honger of dorst. Gezondheid daalt!")


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