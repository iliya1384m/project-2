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

#functie om vermijd detectie
def vermijd_detectie():
    print("\nStep 3: Connor finds an alternate route through the ventilation system.")
    print("Step 4: He encounters a locked panel.")
    keuze = input("Do you (1) hack the panel or (2) search for a keycard? ")

    if keuze == "1":
        hack_paneel()
    elif keuze == "2":
        zoek_sleutelkaart()
    else:
        print("Invalid choice. Try again.")
        vermijd_detectie()

#functie om praat met afwijkende
def praat_met_afwijkende():
    print("\nStep 3: The deviant provides valuable intel about the facility.")
    print("Step 4: He warns Connor about increased security.")
    keuze = input("Do you (1) follow the deviant's advice or (2) take a different route? ")

    if keuze == "1":
        volg_advies()
    elif keuze == "2":
        andere_route()
    else:
        print("Invalid choice. Try again.")
        praat_met_afwijkende()

# functie om negeer afwijkende
def negeer_afwijkende():
    print("\nStep 3: Connor ignores the deviant and enters the facility alone.")
    print("Step 4: Security cameras spot him.")
    keuze = input("Do you (1) disable the cameras or (2) proceed quickly? ")

    if keuze == "1":
        schakel_camera_uit()
    elif keuze == "2":
        ga_snel_verder()
    else:
        print("Invalid choice. Try again.")
        negeer_afwijkende()

# functie om bluf bewaker
def bluf_bewaker():
    print("\nStep 5: Connor successfully bluffs the guard and continues.")
    betreed_beveiligde_ruimte()
# functie om gebruiik geweld
def gebruik_geweld():
    print("\nStep 5: Connor uses force to neutralize the guard.")
    print("Step 6: Alarms are triggered.")
    keuze = input("Do you (1) disable the alarms or (2) rush to the objective? ")

    if keuze == "1":
        schakel_alarm_uit()
    elif keuze == "2":
        haast_naar_doel()
    else:
        print("Invalid choice. Try again.")
        gebruik_geweld()
