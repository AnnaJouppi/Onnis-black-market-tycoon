# 🐈‍⬛ Onni's Black Market Tycoon

Welcome to the underground empire of **Onni**, the neighborhood's most feared feline Don. Onni has already stashed away a cool million euros, but he is missing the final piece of the puzzle: **1,000€** to win the secret auction for **The Golden Tuna Statue**—the Holy Grail of the criminal underworld. 

Your mission is to help Onni clean that final grand through black market street deals without getting busted by the police.

---

## 🎮 Gameplay Features

* **Dynamic Black Market Economy:** Trade 10 unique, highly illegal items (ranging from *Untouched Pizza Slices* to *Pink Crocs*). Prices and starting stock are completely randomized every session.
* **Market Scarcity Multiplier:** Smart supply and demand mechanics! As you sell items out, the remaining goods become rare collectibles. Prices increase by 5% per sold-out item, scaling up to a **100% price double** when 9 or more items are out of stock.
* **Risk vs. Reward System:** Send mules on random runs or pay a 5€ hazard fee to dispatch a target delivery. Watch your **Heat meter**—if it hits 100%, Onni gets busted and it's Game Over!
* **Fail-Safe Rollback Engine:** Advanced code logic ensures that if a high-risk hazard delivery fails due to a warehouse shortage, your cash and heat are automatically rolled back to their previous states.
* **Persistent World Saves:** Includes automated progress saving (`game_state.csv`) and session logging (`game_logs.csv`) that tracks your duration, days survived, and choices made.

---

## 📁 Architecture & File Structure

The project follows clean, production-grade modular programming principles:

```text
Onnis-black-market-tycoon/
│
├── main.py              # Game Entry Point & Main Control Loop
│
├── data/                # Persistent Storage
│   ├── game_state.csv   # Saved Game Variables (Day, Cash, Heat)
│   └── game_logs.csv    # Analytics & Session Telemetry Logs
│
├── config/              # Game Configuration
│   └── settings.json    # Balancing Math & Variable Constants
│
└── modules/             # Core Logic Subsystems
    ├── actions.py       # Transaction & Sales Processing Engine
    ├── events.py        # Random Police Patrols & Encounters
    ├── inventory.py     # Warehouse Management & Scarcity Calculations
    └── save_load.py     # File I/O Management (CSV/JSON Parser)
```

## 🚀 How to Run

Make sure you have Python 3.10 or newer installed.

1. Clone this repository to your local machine:
   ```bash
   git clone https://github.com/your-username/Onnis-black-market-tycoon.git

2. Navigate into the project folder:
   ```bash
   cd Onni-Tycoon

3. Boot up the tycoon:
   ```bash
   python main.py
