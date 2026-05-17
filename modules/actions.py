# Lisätään 'multiplier' parametriksi (oletus on 1.0)
def sell_item(item, current_cash, current_heat, GAME_MATH, hazard_fee=0, multiplier=1.0):
        
        """Käsittelee yhden esineen myynnin ja palauttaa uudet rahat ja heatin"""
        if item["stock"] <= 0:
        # 1. Tarkistetaan, onko tavara loppu
            print(f"\n❌ {item['name']} is already sold out!")
            # Palautetaan vanhat rahat ja heat, sekä 'False' (myynti epäonnistui)
            return current_cash, current_heat, False
        
        # LASKETAAN LOPULLINEN MYYNTIHINTA KERTOIMELLA
        # round() pitää huolen, ettei tule senttejä (esim. 46.234€)
        final_price = round(item["price"] * multiplier)

        # 2, Tehdään myynti
        item["stock"] -= 1
        current_cash += final_price
        print(f"\n🔥 SOLD OUT BONUS: Market is empty! Prices increased by {round((multiplier-1)*100)}%!")
        current_heat += GAME_MATH["choices"]["sell_heat_gain"]

            # 3. Tulostetaan tyylikkäät tekstit
        print(f"\nOnni's mules sold: {item['name']} for {item['price']} €!")

        if item["stock"] == 0:
            print(f"✏️ Onni crosses '{item['name']}' out from his ledger.")
        else:
            print(f"Remaining stock: {item['stock']}")
        # Lasketaan vain tulostetta varten! Hazard fee on jo vähennetty main.py:ssä
        net_profit= final_price - hazard_fee
        print(f"Cash increased by {net_profit}. Heat increased by {GAME_MATH['choices']['sell_heat_gain']}.\n")

        # 4. Palautetaan uudet rahat, uusi heat, ja 'True' (myynti onnistui)
        return current_cash, current_heat, True