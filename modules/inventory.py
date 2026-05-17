# inventory.py
import random

# TODO 1: Luo lista nimeltä 'items'. 
# Jokainen esine on sanakirja {}, jolla on 'name' ja 'price'.
# Keksi vähintään 5 hauskaa mustan pörssin esinettä!

item_names= [
    "Baby Pacifier (Pink)",
    "Untouched Pizza Slice",
    "Slightly Chewed Tennis Ball",
    "Beautiful Oak Tree Leaf",
    "Pristine Cat Toy",
    "Broken Gardening Glove",
    "Cute Frog Plushie", 
    "Dirty Microfiber Cloth",
    "Spiderman Figurine",
    "Pink Crocs Size 37"   
]

items = []

for i, esineen_nimi in enumerate(item_names, 1): # 1 ja i On laskurin numero, ei indeksinumero
    new_item = {
        "number": str(i),
        "name": esineen_nimi,
        "price": random.randint(1, 100), # Arvotaan hinta
        "stock": random.randint(1, 10) # Arvotaan varastomäärä
    }
    items.append(new_item)

def show_inventory():
    """Tulostaa Onnin varaston sisällön tyylikkäästi."""
    print("\n--- 📦 ONNI'S BLACK MARKET STOCK ---")
    
    # TODO 2: Kirjoita for-silmukka, joka käy läpi 'items'-listan.
    # Tulosta jokainen esine muodossa: "- Esineen nimi: 50€"
    # Vinkki: käytä item["name"] ja item["price"]
    for item in items:
        if item["stock"] == 0:
            # Tulostetaan ANSI-koodeilla yliviivattuna!
            print(f'\033[9m{item["number"]} - {item["name"]}: {item["price"]} € (Stock: 0)\033[0m')
        else:
            print(f'{item["number"]} - {item["name"]}: {item["price"]} €🔹 Current Stock: {item["stock"]} ')
    
    print("------------------------------------\n")

def get_random_item():
    """Hakee satunnaisen esineen koko varastosta."""
    # TODO 3: Käytä random.choice(items) funktiota hakeaksesi yhden sanakirjan.
    # Palauta (return) tuo koko sanakirja.
    random_item = random.choice(items)
    return random_item
    
def is_inventory_empty():
    """Tarkistaa, onko kaikki tuotteet myyty loppuun"""
    for item in items:
        if item["stock"] > 0: # Löytyi ainakin yksi tuote! Varasto ei ole tyhjä.
            return False
    return True # Silmukka meni loppuun saakka eikä löytänyt tuotteita, joten varasto on tyhjä.

def restock_inventory():
    """Täyttää varaston uudelleen uusilla tuotteilla."""
    print("\n📦 The mules raided a shipping container! Inventory completely restocked!")
    # Arvotaan jokaiselle tuotteelle uusi varastosaldo
    for item in items:
        item["stock"] = random.randint(3, 10)

# Hype-funktiot, mitä enemmän myyty loppuun, sitä enemmän saa bonusta!
def get_sold_out_count():
    """Laskee kuinka monta uniikkia tuotetta on täysin loppu."""
    count = 0
    for item in items:
        if item["stock"] <= 0:
            count += 1
    return count

def get_sold_out_multiplier():
    """Laskee kertoimen sen mukaan, kuinka moni tuote on loppu."""
    count = get_sold_out_count()
    
    if count >= 9:
        return 2.0  # 100% bonus (tuplahinta!)
    
    # 5% lisäys per loppunut tuote (1->1.05, 2->1.10 jne.)
    return 1.0 + (count * 0.05)