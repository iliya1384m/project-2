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

# functie om order te volgen
def volg_bevelen():
    print("\nConnor decides to follow CyberLife's orders.")
    print("Step 1: Connor enters the facility through the main entrance.")
    print("Step 2: Security scans detect his presence.")
    keuze = input("Do you (1) proceed calmly or (2) avoid detection? ")

    if keuze == "1":
        kalm_verder()
    elif keuze == "2":
        vermijd_detectie()
    else:
        print("Invalid choice. Try again.")
        volg_bevelen()

