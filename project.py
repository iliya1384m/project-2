# functie om de game te starten
def start_missie():

    print("Connor arrives at the CyberLife facility.")
    print("Mission: Investigate deviant activities inside the facility.")
    keuze = input("Do you follow orders (1) or deviate from your mission (2)? ")
# hier wordt gecontroleerd 
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
# hier wordt gecontroleerd 
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
# hier wordt gecontroleerd 
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
# hier wordt gecontroleerd 
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
# hier wordt gecontroleerd 
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
# hier wordt gecontroleerd 
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
# hier wordt gecontroleerd
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
# hier wordt gecontroleerd
    if keuze == "1":
        schakel_alarm_uit()
    elif keuze == "2":
        haast_naar_doel()
    else:
        print("Invalid choice. Try again.")
        gebruik_geweld()

# functie om hack baneel
def hack_paneel():
    print("\nStep 5: Connor hacks the panel and gains access to a restricted area.")
    betreed_beveiligde_ruimte()
# functie om zoek sleutelkaart
def zoek_sleutelkaart():
    print("\nStep 5: Connor searches for a keycard and finds one in a guard's locker.")
    print("Step 6: The guard returns unexpectedly.")
    keuze = input("Do you (1) hide or (2) confront the guard? ")
# hier wordt gecontroleerd
    if keuze == "1":
        verberg()
    elif keuze == "2":
        confronteer_bewaker()
    else:
        print("Invalid choice. Try again.")
        zoek_sleutelkaart()

# functie om volg advies
def volg_advies():
    print("\nStep 5: Connor avoids detection by following the deviant's advice.")
    betreed_beveiligde_ruimte()
# functie om andere route
def andere_route():
    print("\nStep 5: Connor takes a different route but faces a security checkpoint.")
    keuze = input("Do you (1) sneak past or (2) use your badge to bypass? ")
# hier wordt gecontroleerd
    if keuze == "1":
        sluip_langs()
    elif keuze == "2":
        gebruik_pas()
    else:
        print("Invalid choice. Try again.")
        andere_route()

# functie om schakel camera uit
def schakel_camera_uit():
    print("\nStep 5: Connor disables the cameras and avoids detection.")
    betreed_beveiligde_ruimte()

# functie om ga snel verder
def ga_snel_verder():
    print("\nStep 5: Connor proceeds quickly but leaves evidence of his presence.")
    betreed_beveiligde_ruimte()

# functie om betreed beveiligde ruimte
def betreed_beveiligde_ruimte():
    print("\nStep 7: Connor enters the restricted area.")
    print("Step 8: He finds the CyberLife database.")

# functie om schakel alarm uit
def schakel_alarm_uit():
    print("\nStep 7: Connor disables the alarms and continues.")
    betreed_beveiligde_ruimte()

# functie om haast naar doel
def haast_naar_doel():
    print("\nStep 7: Connor rushes to the objective but leaves security on high alert.")
    print("Security has been alerted! The mission is over.")
    print("Game Over. Security is too tight, and the mission has failed.")
# game over
    exit()