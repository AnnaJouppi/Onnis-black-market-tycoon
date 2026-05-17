import json
import csv
import os

def load_settings():
    """Lataa pelin asetukset (GAME_MATH)."""
    try:
        with open("config/settings.json", "r") as file:
            return json.load(file)
    except FileNotFoundError:
        print("❌ CRITICAL ERROR: 'settings.json' is missing!")
        return None
    except json.JSONDecodeError:
        print("❌ CRITICAL ERROR: 'settings.json' is corrupted!")
        return None

def load_game():
    """Lataa tallennetun pelin tilan, jos sellainen on olemassa."""
    if os.path.exists("data/game_state.csv"):
        with open("data/game_state.csv", "r", encoding='utf-8') as f:
            reader = csv.reader(f)
            for row in reader:
                if len(row) == 3:
                    return int(row[0]), int(row[1]), int(row[2]) # Palauttaa: day, cash, heat
    
    return 1, 100, 0 # Jos ei tallennusta, palauta aloitusarvot!

def save_game(day, cash, heat):
    """Tallentaa pelin tilan ylikirjoittamalla vanhan."""
    with open("data/game_state.csv", "w", encoding="utf-8", newline="") as f:
        writer = csv.writer(f)
        writer.writerow([day, cash, heat])
    print("💾 Game progress saved successfully!")

def log_session(choices_made, day, duration_seconds):
    """Tallentaa analytiikan lokitiedostoon."""
    if len(choices_made) > 0:
        with open("data/game_logs.csv", "a", encoding="utf-8", newline="") as f:
            writer = csv.writer(f)
            choices_str = "-".join(choices_made)
            writer.writerow([choices_str, day, duration_seconds])
        print(f"📊 Logged: {len(choices_made)} moves, reached Day {day}.")
    else:
         print("📊 No moves made, nothing to log.")