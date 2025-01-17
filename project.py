# functie om de game te starten
def start_missie():

    print("Connor arrives at the CyberLife facility.")
    print("Mission: Investigate deviant activities inside the facility.")
    keuze = input("Do you follow orders (1) or deviate from your mission (2)? ")

    if keuze == "1":
        volg_bevelen()
    elif keuze == "2":
        afwijk()
    else:
        print("Invalid choice. Try again.")
        start_missie()

