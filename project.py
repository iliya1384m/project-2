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
# functie om afwijken van je missie
def afwijk():
    print("\nConnor decides to deviate from his mission.")
    print("Step 1: Connor bypasses the main entrance.")
    print("Step 2: He encounters a deviant android outside.")
    keuze = input("Do you (1) talk to the deviant or (2) ignore and move on? ")

    if keuze == "1":
        praat_met_afwijkende()
    elif keuze == "2":
        negeer_afwijkende()
    else:
        print("Invalid choice. Try again.")
        afwijk()
        
#functie om kalm verder gaan
def kalm_verder():
    print("\nStep 3: Connor walks confidently through the checkpoint.")
    print("Step 4: A guard stops him for questioning.")
    keuze = input("Do you (1) bluff your way through or (2) use force? ")

    if keuze == "1":
        bluf_bewaker()
    elif keuze == "2":
        gebruik_geweld()
    else:
        print("Invalid choice. Try again.")
        kalm_verder()
