import math
import pygame
import sys

# 1. PELIN ALUSTUS
pygame.init()

# 2. IKKUNAN ASETUKSET
# Luodaan Onnin päämajalle sopiva moderni HD-ikkuna (1280x720)
SCREEN_WIDTH = 1280
SCREEN_HEIGHT = 720
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption("Onni's Black Market Tycoon - Graphical Version")

# 3. KELLO (Rajoitetaan pelin pyörimisnopeus, ettei prosessori laula hoosiannaa)
clock = pygame.time.Clock()
# Käytetään Pygamen oletusfonttia, 32
font = pygame.font.Font(None, 32)
small_font = pygame.font.Font(None, 22) # Pienempi fontti tooltipeille

# Pelin oletusarvot
day = 1
cash = 100
heat = 0
game_state = "PLAYING"  # Mahdolliset tilat: "PLAYING", "VICTORY", "GAMEOVER"

# Määritetään Onnin päämajan (HQ) paikka kartalla (X, Y)
HQ_X = 200
HQ_Y = 400

# Määritetään ensimmäisen myyntipisteen (Route 1 päätepiste) paikka
ROUTE1_X = 600
ROUTE1_Y = 250

# Alapalkin asetukset
BOTTOM_BAR_HEIGHT = 60
BOTTOM_BAR_Y = SCREEN_HEIGHT - BOTTOM_BAR_HEIGHT

# Alapalkin painikkeiden asetukset
btn_y = BOTTOM_BAR_Y + 30  # Keskikohta pystysuunnassa alapalkissa
radius = 20                # Ympyrän säde (suurempi, jotta numerot mahtuvat nätisti)

# Määritetään 5 painiketta: (X-koordinaatti, Numero, Aputeksti)
buttons = [
    (213, "1", "Send mules to sell contraband (+Cash, +Heat)"),
    (426, "2", "Bribe the alleyway guards (-Heat)"),
    (640, "3", "Hide in the Jimm's box (Do nothing)"),
    (853, "4", "Check inventory stock"),
    (1066, "5", "Send a mule to sell a specific item")
    ]

# VÄRIT
# Kartta ja HQ
line_color = (100, 110, 125) # Tyylikäs sateenharmaa reittiviiva
hq_color = (78, 154, 241) # Onnin päämajan sininen loisto
shop_color = (230, 126, 34)

# Yläpalkki ja alapalkki
# Painikkeiden värit
btn_bg_color = (55, 61, 72) # Hieman vaaleampi harmaa painikkeille
btn_border_color = (100, 110, 125)
hover_color = (78, 154, 241) # Muuttuu siniseksi, kun hiiri on päällä!
text_color = (230, 235, 245) # Tyylikäs vaalea teksti

# 4. PELISILMUKKA (Game Loop)
# Tämä silmukka pyörii niin kauan kuin peli on käynnissä
running = True
while running:
    
    # --- A. TAPAHTUMIEN KÄSITTELY (Event Handling) ---
    # Kuunnellaan käyttäjän syötteitä (hiiri, näppäimistö, ikkunan sulkeminen)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False  # Sulkee pelisilmukan, kun painat ruksia
        
        # UUTTA: Kuunnellaan hiiren klikkauksia
        elif event.type == pygame.MOUSEBUTTONDOWN:
            if event.button == 1 and game_state == "PLAYING":  # 1 = Hiiren vasen painike, klikkaukset toimivat vain pelatessa
                click_x, click_y = event.pos  # Otetaan talteen kohta, johon klikattiin

                # Käydään kaikki 5 painiketta läpi ja katsotaan, osuiko klikkaus johonkin niistä
                for x, number, tooltip_text in buttons:
                    # Käytetään tuttua hypotenuusamatematiikkaa klikkauskohdan ja ympyrän välillä
                    distance = math.hypot(click_x - x, click_y - btn_y)

                    # Jos klikkaus osui ympyrän sisälle (etäisyys pienempi kuin säde)
                    if distance < radius:
                        print(f"Klikkasit painiketta {number}!")  # Debug-tulostus VS Coden konsoliin

                        # REAGOIDAAN KLIKKAUKSEEN TEKSTIPELIN SÄÄNTÖJEN MUKAAN:
                        
                        if number == "1":
                            # MVP-vaihe: Lisätään suoraan Cash/Heat (Tulevaisuudessa haetaan inventory-moduulista!)
                            cash += 75
                            heat += 10
                            day += 1  # Päivä vaihtuu onnistuneesta toiminnosta

                        elif number == "2":
                            # Bribe: Heat tippuu 25, ei maksa mitään tekstiversion mukaan!
                            heat -= 25
                            if heat < 0:
                                heat = 0
                            day += 1

                        elif number == "3":
                            # Hide in Jimm's box: Heat tippuu 5
                            heat -= 5
                            if heat < 0:
                                heat = 0
                            day += 1

                        elif number == "4":
                            # Logiikka työn alle myöhemmin (Inventory)
                            print("Inventory-toiminnallisuus työn alla...")

                        elif number == "5":
                            # Logiikka työn alle myöhemmin (Specific item sale)
                            print("Tietyn tuotteen myynti-toiminnallisuus työn alla...")

    # --- B. PELILOGIIKAN PÄIVITYS (Update) ---
    # Haetaan hiiren nykyiset X- ja Y-koordinaatit joka kierroksella
    mouse_x, mouse_y = pygame.mouse.get_pos()

    # Tarkistetaan loppuehdot vain, jos peli on vielä käynnissä
    if game_state == "PLAYING":
        if cash >= 1000:
            game_state = "VICTORY"
        elif heat >= 100:
            game_state = "GAMEOVER"

    # --- C. PIIRTÄMINEN (Render / Draw) ---
    # Täytetään ruutu pimeiden kujien tunnelmaan sopivalla tummanharmaalla (RGB-värit)
    screen.fill((40, 44, 52))
    if game_state == "PLAYING":
        # 1. KARTTA JA HQ

        # 1.1 Piirretään reittiviiva HQ:sta myyntipisteeseen
        # pygame.draw.line(pinta, väri_RGB, (alku_x, alku_y), (loppu_x, loppu_y), viivan_paksuus)
        pygame.draw.line(screen, line_color, (HQ_X, HQ_Y), (ROUTE1_X, ROUTE1_Y), 4)

        # 1.2. Piirretään Onnin päämaja (HQ) hienona ympyränä
        # pygame.draw.circle(pinta, väri_RGB, (keskipiste_x, keskipiste_y), säde_pikseleinä)
        pygame.draw.circle(screen, hq_color, (HQ_X, HQ_Y), 25)

        # 1.3. Piirretään ensimmäinen myyntipiste (oranssi ympyrä)
        pygame.draw.circle(screen, shop_color, (ROUTE1_X, ROUTE1_Y), 15)

        # Laitetaan vielä pienet tekstit solmujen kohdalle, jotta pelaaja tajuaa mitä ne ovat
        hq_label = font.render("Onni's HQ", True, hq_color)
        shop_label = font.render("Route 1 (Drop-off)", True, shop_color)

        # Siirretään tekstejä hieman sivuun ympyröistä, etteivät ne ole päällekkäin
        screen.blit(hq_label, (HQ_X - 45, HQ_Y + 35))
        screen.blit(shop_label, (ROUTE1_X - 80, ROUTE1_Y - 45))

        # 2. YLÄPALKKI JA ALAPALKKI
        
        # Piirretään yläpalkin taustalaatikko: (x, y, leveys, korkeus)
        # Väri on hieman tummempi harmaa (28, 30, 34)
        TOP_BAR_HEIGHT = 60
        pygame.draw.rect(screen, (28, 30, 34), (0, 0, SCREEN_WIDTH, TOP_BAR_HEIGHT))

        # Luodaan tekstipinnat statsille
        # font.render("teksti", antialiasing, väri_RGB)
        day_text = font.render(f"DAY: {day}", True, text_color)
        cash_text = font.render(f"CASH: {cash}€", True, (100, 220, 110)) # Vihreä raha!
        heat_text = font.render(f"HEAT: {heat}%", True, (240, 90, 90))    # Punainen riski!

        # Liimataan tekstipinnat ruudulle yläpalkin sisään (blit)
        # x-koordinaatit jaettu tasaisesti (100, 500, 900), y-koordinaatti keskittää tekstin korkeussuunnassa
        screen.blit(day_text, (100, 18))
        screen.blit(cash_text, (500, 18))
        screen.blit(heat_text, (900, 18))

        # Piirretään alapalkin taustalaatikko: (x, y, leveys, korkeus)
        # Väri on hieman tummempi harmaa (28, 30, 34)
        pygame.draw.rect(screen, (28, 30, 34), (0, BOTTOM_BAR_Y, SCREEN_WIDTH, TOP_BAR_HEIGHT))

        # Muuttuja, johon tallennetaan parhaillaan hoverattavan painikkeen aputeksti
        active_tooltip = None
        tooltip_x, tooltip_y = 0, 0

        # Piirretään painikkeet silmukassa ja katsotaan onko hiiri painikkeen päällä
        for x, number, tooltip_text in buttons:
            # Lasketaan etäisyys hiiren ja ympyrän keskipisteen välillä (Pythagoraan lause)
            distance = math.hypot(mouse_x - x, mouse_y - btn_y)
            
            # Jos etäisyys on pienempi kuin säde, hiiri on ympyrän SILLÄ PUOLELLA (Hover!)
            is_hovered = distance < radius
            
            # Valitaan väri sen mukaan, onko hiiri päällä vai ei
            current_border = hover_color if is_hovered else btn_border_color
            current_bg = (45, 50, 60) if is_hovered else btn_bg_color

            # 1. Piirretään ulkoreuna (isompi ympyrä)
            pygame.draw.circle(screen, current_border, (x, btn_y), radius)
            # 2. Piirretään sisus (hieman pienempi ympyrä, jolloin väliin jää reuna)
            pygame.draw.circle(screen, current_bg, (x, btn_y), radius - 3)

            # 3. Piirretään numero keskelle ympyrää
            num_surface = font.render(number, True, text_color)
            # Keskihifistely tekstille: vähennetään puolet tekstin koosta, jotta se on tismalleen keskellä
            screen.blit(num_surface, (x - num_surface.get_width()//2, btn_y - num_surface.get_height()//2))

            # 4. Jos hiiri on päällä, otetaan aputeksti talteen piirtoa varten
            if is_hovered:
                active_tooltip = tooltip_text
                tooltip_x = x
                tooltip_y = btn_y - 65 # Piirretään laatikko painikkeen yläpuolelle

    

        # 3. --- APUTEKSTILAATIKON (TOOLTIP) PIIRTÄMINEN ---
        # Piirretään tämä vasta silmukan jälkeen, jotta se kerrostuu kaikkien muiden asioiden päälle
        if active_tooltip:
            tooltip_surface = small_font.render(active_tooltip, True, (255, 255, 255))
            pad_x, pad_y = 10, 6 # Tyhjää tilaa tekstin ympärille laatikkoon
            
            # Laatikon mitat tekstin mukaan
            box_w = tooltip_surface.get_width() + (pad_x * 2)
            box_h = tooltip_surface.get_height() + (pad_y * 2)
            box_x = tooltip_x - box_w // 2
            box_y = tooltip_y
        
            # Piirretään musta taustalaatikko pyöristetyillä kulmilla ja harmaalla reunalla
            pygame.draw.rect(screen, (20, 22, 26), (box_x, box_y, box_w, box_h), 0, 4)
            pygame.draw.rect(screen, hover_color, (box_x, box_y, box_w, box_h), 1, 4)
            
            # Liimataan teksti laatikon sisään
            screen.blit(tooltip_surface, (box_x + pad_x, box_y + pad_y))
    elif game_state == "VICTORY":

        # ------------ VOITTO-RUUTU ------------
        # Värjätään tausta upealla tummanvihreällä
        # render luo tarran
        # blit liimaa tarran annettuihin koordinaatteihin: (SCREEN_WIDTH//2 - win_title.get_width()//2, SCREEN_HEIGHT//2 - 80))
        screen.fill((20, 50, 30))
        win_title = font.render("🏆 VICTORY: THE GOLDEN TUNA IS YOURS! 🏆", True, (100, 255, 120))
        story_text1 = small_font.render("Onni bought the mythical Golden Tuna Statue and retired to a private island.", True, text_color)
        story_text2 = small_font.render(f"Business completed successfully in {day} days!", True, text_color)
        
        screen.blit(win_title, (SCREEN_WIDTH//2 - win_title.get_width()//2, SCREEN_HEIGHT//2 - 80))
        screen.blit(story_text1, (SCREEN_WIDTH//2 - story_text1.get_width()//2, SCREEN_HEIGHT//2))
        screen.blit(story_text2, (SCREEN_WIDTH//2 - story_text2.get_width()//2, SCREEN_HEIGHT//2 + 40))
    
    elif game_state == "GAMEOVER":
        # ------------ HÄVIÖ-RUUTU ------------
        # Värjätään tausta dramaattisella tummanpunaisella
        screen.fill((60, 20, 20))
        loss_title = font.render("🚨 GAME OVER: BUSTED! 🚨", True, (255, 90, 90))
        loss_text = small_font.render("The Heat reached 100%. Onni's black market operation was busted by the guards!", True, text_color)
        
        screen.blit(loss_title, (SCREEN_WIDTH//2 - loss_title.get_width()//2, SCREEN_HEIGHT//2 - 40))
        screen.blit(loss_text, (SCREEN_WIDTH//2 - loss_text.get_width()//2, SCREEN_HEIGHT//2 + 10))

    # Päivitetään ruutu näyttämään kaikki uudet piirrokset
    pygame.display.flip()

    # Rajoitetaan peli pyörimään tasan 60 kertaa sekunnissa (60 FPS)
    clock.tick(60)

# 5. PELISTÄ POISTUMINEN
# Kun silmukka päättyy, suljetaan Pygame ja vapautetaan muisti siististi
pygame.quit()
sys.exit()