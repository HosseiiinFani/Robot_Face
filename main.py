import pygame
from serial import Serial

PORT="/dev/cu.usbserial-14330"

def main():
    pygame.init()
    ARDUINO = False
    try:
        arduino = Serial(PORT, 9600)
        ARDUINO = True
    except: pass
    BG = (255,255,255)

    happy = pygame.image.load("lib/happy.png")
    angry = pygame.image.load("lib/angry.png")
    sleepy = pygame.image.load("lib/sleepy.png")
    excited = pygame.image.load("lib/excited.png")

    moods = {'happy': happy, 'angry': angry, 'sleepy': sleepy, 'excited': excited}

    current_mood = 'sleepy'

    happy_button = pygame.transform.scale(pygame.image.load("lib/assets/happy.png"), (100,40))
    angry_button = pygame.transform.scale(pygame.image.load("lib/assets/angry.png"), (100,40))
    sleepy_button = pygame.transform.scale(pygame.image.load("lib/assets/sleepy.png"), (100,40))
    excited_button = pygame.transform.scale(pygame.image.load("lib/assets/excited.png"), (100,40))

    screen = pygame.display.set_mode((480,800))
    clock = pygame.time.Clock()

    base_font = pygame.font.Font(None, 32)

    run = True

    screen.fill(BG)

    while run:
        data = arduino.readline()
        value = int(data.decode(encoding='UTF-8'))
        screen.fill(BG)
        mood_text = base_font.render(f"Current mood: {current_mood}", False, (0,0,0))
        sleepy_rect = screen.blit(sleepy_button, (50, screen.get_height() - 100))
        happy_rect = screen.blit(happy_button, (150, screen.get_height() - 100))
        excited_rect = screen.blit(excited_button, (250, screen.get_height() - 100))
        angry_rect = screen.blit(angry_button, (350, screen.get_height() - 100))

        if ARDUINO:
            if value < 60: current_mood = "sleepy"
            if (value >= 60 and value < 120): current_mood = "happy"
            if (value >= 120 and value < 200): current_mood = "excited"
            if value >= 200: current_mood = "angry"
 
        events = pygame.event.get()
        for event in events:
            if event.type == pygame.QUIT: run = False
            if event.type == pygame.MOUSEBUTTONDOWN:
                if sleepy_rect.collidepoint(event.pos): current_mood = "sleepy"
                if happy_rect.collidepoint(event.pos): current_mood = "happy"
                if excited_rect.collidepoint(event.pos): current_mood = "excited"
                if angry_rect.collidepoint(event.pos): current_mood = "angry"
        screen.blit(moods[current_mood], (100,100))
        screen.blit(mood_text, (100, 20))
        pygame.display.update()
        clock.tick(60)

if __name__ == "__main__":
    main()