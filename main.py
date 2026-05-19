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

# Pelin oletusarvot
day = 1
cash = 100
heat = 0

# 4. PELISILMUKKA (Game Loop)
# Tämä silmukka pyörii niin kauan kuin peli on käynnissä
running = True
while running:
    
    # --- A. TAPAHTUMIEN KÄSITTELY (Event Handling) ---
    # Kuunnellaan käyttäjän syötteitä (hiiri, näppäimistö, ikkunan sulkeminen)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False  # Sulkee pelisilmukan, kun painat ruksia

    # --- B. PELILOGIIKAN PÄIVITYS (Update) ---
    # Tähän väliin koodataan myöhemmin muulien liikkuminen ja ajan kuluminen

    # --- C. PIIRTÄMINEN (Render / Draw) ---
    # Täytetään ruutu pimeiden kujien tunnelmaan sopivalla tummanharmaalla (RGB-värit)
    screen.fill((40, 44, 52))

    # --- UUTTA: YLÄPALKIN (TOP BAR) PIIRTÄMINEN ---
    # Piirretään yläpalkin taustalaatikko: (x, y, leveys, korkeus)
    # Väri on hieman tummempi harmaa (28, 30, 34)
    TOP_BAR_HEIGHT = 60
    pygame.draw.rect(screen, (28, 30, 34), (0, 0, SCREEN_WIDTH, TOP_BAR_HEIGHT))

    # Luodaan tekstipinnat statsille
    # font.render("teksti", antialiasing, väri_RGB)
    text_color = (230, 235, 245) # Tyylikäs vaalea teksti

    day_text = font.render(f"DAY: {day}", True, text_color)
    cash_text = font.render(f"CASH: {cash}€", True, (100, 220, 110)) # Vihreä raha!
    heat_text = font.render(f"HEAT: {heat}%", True, (240, 90, 90))    # Punainen riski!

    # Liimataan tekstipinnat ruudulle yläpalkin sisään (blit)
    # x-koordinaatit jaettu tasaisesti (100, 500, 900), y-koordinaatti keskittää tekstin korkeussuunnassa
    screen.blit(day_text, (100, 18))
    screen.blit(cash_text, (500, 18))
    screen.blit(heat_text, (900, 18))

    # Päivitetään ruutu näyttämään kaikki uudet piirrokset
    pygame.display.flip()

    # Rajoitetaan peli pyörimään tasan 60 kertaa sekunnissa (60 FPS)
    clock.tick(60)

# 5. PELISTÄ POISTUMINEN
# Kun silmukka päättyy, suljetaan Pygame ja vapautetaan muisti siististi
pygame.quit()
sys.exit()