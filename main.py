# main.py - Onni's Alleyway Tycoon

import time
import modules.inventory as inventory
import modules.save_load as save_load
import modules.events as events
import modules.actions as actions

def main():
    # 1. Alustetaan muuttujat ENNEN try-lohkoa, jotta ne ovat olemassa lopussa
    start_time = time.time()
    choices_made = []

    # Luetaan pelin asetukset ulkoisesta tiedostosta
    # Pelin muuttujat ovat siellä
    GAME_MATH = save_load.load_settings()
    if GAME_MATH == None:
        return # Lopetetaan peli heti, jos asetukset puuttuvat
    
    print("🐾 Welcome to Onni's Black Market Tycoon! 🐾\n")
    print("Would you like to load an existing game or start a new one?")
    
    load_or_not = input("Press L to load and N for a new game!\n").upper()

    if load_or_not == "L":
        # Lataa vanha peli
        day, cash, heat = save_load.load_game()

        # Tarkistetaan onko tallennettu peli jo päättynyt
        if cash >= 1000:
            print("\n✨ This save file is already completed! Onni is enjoying his Golden Tuna.")
            print("🆕 Starting a fresh new business venture instead!")
            day = 1
            cash = 100
            heat = 0
        elif heat >= 100:
            print("\n🚨 This save file is busted! Onni is currently in jail.")
            print("🆕 Starting a fresh new business venture instead!")
            day = 1
            cash = 100
            heat = 0
        else:
            print(f"\n💾 Welcome back! Resuming from Day {day}.")
    
    else:
        cash = 100
        heat = 0
        day = 1
        print("\n🆕 Starting a fresh new business venture.")
       
    print("Goal: Reach 1000€ to buy the Golden Tuna without hitting 100% Heat.\n")
    

    # TODO 2: Pelin pääsilmukka (The Game Loop)
    # Kirjoita 'while'-silmukka, joka on käynnissä NIIN KAUAN KUIN cash on alle 1000 JA heat on alle 100.
    try:
        while cash < 1000 and heat < 100:   
            
            # TODO 3: Tulosta päivän otsikko
            # Tulosta teksti "--- DAY X ---" käyttämällä 'day'-muuttujaasi.
            print(f"--- DAY {day} ---") 
            print(f"Cash: {cash} 🔸 Heat: {heat}%")
            time.sleep(4)
            # Tulosta nykyiset tilastot (stats), jotta pelaaja tietää missä mennään.
            
            # Toimintovalikko (Action Menu)
            print("\nWhat should Onni do today?")
            print("1. Send mules to sell contraband (+Cash, +Heat)")
            print("2. Bribe the alleyway guards (-Heat)")
            print("3. Hide in the Jimm's box (Do nothing)")
            print("4. Check inventory stock")
            print("5. Send a mule to sell a specific item")

            # Luo muuttuja nimeltä 'choice', joka ottaa pelaajalta syötteen input()-funktiolla.
            choice = input()

            # Toteuta toiminto
            # Kirjoita if/elif/else-rakenne 'choice'-muuttujan perusteella.
            # - Jos choice on "1", lisää 75 cash-muuttujaan ja 20 heat-muuttujaan.
            # - Jos choice on "2", vähennä 25 heat-muuttujasta (Lisähaaste: varmista, ettei heat mene alle nollan!)
            # - Jos choice on "3", tulosta "Onni naps safely. Heat drops by 5." ja vähennä 5 heat-muuttujasta.
            # - Else (muussa tapauksessa), tulosta "Invalid choice, the mules are confused!"

            # TARKISTETAAN ONKO VALINTA SALLITTU (1, 2 tai 3)
            if choice in ["1", "2", "3", "4", "5"]:
                choices_made.append(choice)
                if choice == "4":
                    inventory.show_inventory()
                    print("Returning to alleyway...\n")
                    continue # 🛑 TÄMÄ ON TAIKASANA! Ohittaa kaiken alla olevan ja hyppää silmukan alkuun.

                elif choice == "1":
                    # 1. TARKISTETAAN ONKO VARASTO TYHJÄ ENNEN KUIN TEHDÄÄN MITÄÄN
                    if inventory.is_inventory_empty():
                        print("\n⚠️ The warehouse is completely empty! Mules have nothing to sell.")
                        # Täydennetään varasto
                        inventory.restock_inventory()
                        continue # Hypätään takaisin valikkoon

                    # Jos varastossa on tavaraa, tehdään tavallinen myyntilooppi
                    success = False # Suksee on aluksi tyhjä

                    
                    while success == False:
                        random_item = inventory.get_random_item()
                        hype = inventory.get_sold_out_multiplier()
                        # Lähetetään esine ja tiedot funktiolle, ja otetaan uudet arvot vastaan!
                        cash, heat, success = actions.sell_item(random_item, cash, heat, GAME_MATH, 0, hype)
                
                   # Tuodaan cash ja heat takaisin eventseistä... (Tämä rivi on hyvä pitää silmukan ulkopuolella!)
                    cash, heat = events.run_events(cash, heat, GAME_MATH)

                elif choice == "2":
                    heat -= GAME_MATH["choices"]["bribe_heat_drop"]
                    print(f"\nHeat decreased by {GAME_MATH["choices"]["bribe_heat_drop"]}.\n")
                    if heat < 0:
                        heat = 0

                elif choice == "3":
                    print(f"\nOnni naps safely. Heat drops by {GAME_MATH["choices"]["nap_heat_drop"]}.")
                    heat -= GAME_MATH["choices"]["nap_heat_drop"]
                    print(f"\nHeat decreased by {GAME_MATH["choices"]["nap_heat_drop"]}.\n")
                    if heat < 0:
                        heat = 0

                elif choice == "5":
                    inventory.show_inventory()
                    print("Sending a mule to sell a specific item is potentially dangerous to the mule and adds increased risk to add heat to Onni's operation! \n")
                    print("This action requires a hazard fee of 5€ and potentially increases heat from 5 to 10%.")
                    print(f"\nEnter the number of the item you wish to sell or type exit to cancel:")
                    item_choice = input()
                    if item_choice == 'exit':
                        continue

                    chosen_item = None
                    for item in inventory.items:
                        if item["number"] == item_choice:
                            chosen_item = item
                            break # Lopeta kuluva silmukka heti kun oikea numero mätsää ja hyppää pois.
                                  # Muuten se looppaisi kaikki numerot putkeen
                    
                    if chosen_item != None:

                        old_cash = cash # Varmuuskopiot, jos tuote onkin loppu
                        old_heat = heat

                        heat = events.hazard_risk(heat)
                        cash -= GAME_MATH["choices"]["hazard_fee"]
                        print(f"💸  Hazard fee of {GAME_MATH["choices"]["hazard_fee"]}€ has been deducted!")
                        cash, heat, success = actions.sell_item(chosen_item, cash, heat, GAME_MATH, GAME_MATH["choices"]["hazard_fee"])

                        # ROLLBACK: Jos myynti epäonnistui (esine loppu)
                        if success == False:
                            cash = old_cash
                            heat = old_heat
                            print("🔄 Hazard fee refunded and heat cancelled (Item out of stock).")
                            continue

                    else:
                        # Jos laatikko jäi tyhjäksi, pelaaja antoi huonon numeron!
                        print("\nInvalid item number! The mules don't know what to sell.")
                        continue

            # Päivä vaihtuu VAIN jos tehtiin oikea siirto
                day += 1
            else:
                print("Invalid choice, the mules are confused!")

    except KeyboardInterrupt:
        # Tämä suoritetaan VAIN jos painat Ctrl + C
        print("\n\n⚠️ Game interrupted by user (Ctrl+C). Saving progress anyway...")  

    finally:
        # TÄMÄ AJETAAN AINA: loppuipa peli voittoon, häviöön tai keskeytykseen!
        # Tallennetaan kesto
        end_time = time.time()
        duration_seconds = round(end_time - start_time, 2)
        
        # Tallennetaan vain, jos pelaaja ehti tehdä edes jotain
        # "a" tarkoittaa 'append' eli uusi rivi lisätään vanhojen perään
        if len(choices_made) > 0:
            # Tallenna peli
            save_load.save_game(day, cash, heat)
            # Tallenna tiedot lokiin
            save_load.log_session(choices_made, day, duration_seconds)

         
        # TODO 7: Päivän päätös
        time.sleep(2) # Tämä tekee 2 sekunnin tauon, jotta teksti ei vilise silmissä liian nopeasti!
        
    # --- PELI ON PÄÄTTYNYT --- 
    # TODO 8: Lopputulos (The Aftermath)
    # While-silmukka päättyi! Kirjoita if/else-rakenne, joka selvittää MIKSI peli päättyi.
    # - Jos heat >= 100, tulosta Game Over -viesti siitä, että Onni jäi kiinni.
    # - Jos cash >= 1000, tulosta Voittoviesti siitä, että Onni ostaa Golden Tunan ja jää eläkkeelle.
    if heat >= 100:
        print("Onni got busted! 🚨")
    elif cash >= 1000:
        print("\n" + "="*50)
        print("🏆 VICTORY: THE FINAL PIECE OF THE PUZZLE! 🏆")
        print("="*50)
        print("Onni adds the final 1,000€ to his hidden million-euro stash.")
        print("He heads to the secret auction and outbids everyone...")
        print("\n✨ ONNI HAS ACQUIRED THE GOLDEN TUNA STATUE! ✨")
        print("The criminal underworld's Holy Grail is finally in his paws.")
        print("\nOnni purrs contentedly as he retires to his private island.")
        print("="*50 + "\n")
    

# Tämä on koodin "aloituspiste" (Entry Point), joka käynnistää pelin. Jätä tämä juuri näin!
if __name__ == "__main__":
    main()