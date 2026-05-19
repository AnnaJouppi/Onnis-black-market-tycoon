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

    # Tähän väliin piirretään myöhemmin yläpalkki, kartta ja napit

    # Päivitetään ruutu näyttämään kaikki uudet piirrokset
    pygame.display.flip()

    # Rajoitetaan peli pyörimään tasan 60 kertaa sekunnissa (60 FPS)
    clock.tick(60)

# 5. PELISTÄ POISTUMINEN
# Kun silmukka päättyy, suljetaan Pygame ja vapautetaan muisti siististi
pygame.quit()
sys.exit()