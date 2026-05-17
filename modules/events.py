import random

# Luo muuttuja nimeltä 'event_roll' ja aseta siihen satunnainen numero väliltä 1-6.
def run_events(cash, heat, GAME_MATH):
    event_roll = random.randint(1, 6)
    # Kirjoita 'if'-lause: Jos heitto on 1, tulosta "🚨 POLICE PATROL! +15 Heat" ja lisää 15 heat-muuttujaan.
    if event_roll == 1:
        heat += GAME_MATH["events"]["police_heat_penalty"]
        print(f"BONUS EVENT 🚨 POLICE PATROL! + {GAME_MATH["events"]["police_heat_penalty"]} Heat\n")
    elif event_roll == 2:
        cash += GAME_MATH["events"]["stash_cash_gain"]
        print(f"BONUS EVENT 💰 An undercover mule found a location of a rival gang's secret stash! +{GAME_MATH["events"]["stash_cash_gain"]} Cash\n")
    
    return cash, heat

def hazard_risk(heat):
    risk_chance = random.randint(1, 6)
    if risk_chance == 1:
        heat_increase = random.randint(5, 10)
        heat += heat_increase
        print(f"Mules ran into cops! Heat increased by {heat_increase}")
    return heat