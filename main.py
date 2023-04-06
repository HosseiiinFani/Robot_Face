import pygame

def main():
    pygame.init()

    BG = (255,255,255)

    happy = pygame.image.load("lib/happy.png")
    angry = pygame.image.load("lib/angry.png")
    sleepy = pygame.image.load("lib/sleepy.png")
    excited = pygame.image.load("lib/excited.png")

    moods = {'happy': happy, 'angry': angry, 'sleepy': sleepy, 'excited': excited}

    happy_button = pygame.transform.scale(pygame.image.load("lib/assets/happy.png"), (100,40))
    angry_button = pygame.transform.scale(pygame.image.load("lib/assets/angry.png"), (100,40))
    sleepy_button = pygame.transform.scale(pygame.image.load("lib/assets/sleepy.png"), (100,40))
    excited_button = pygame.transform.scale(pygame.image.load("lib/assets/excited.png"), (100,40))

    screen = pygame.display.set_mode((480,800))
    clock = pygame.time.Clock()

    run = True

    screen.fill(BG)

    while run:
        events = pygame.event.get()
        for event in events:
            if event.type == pygame.QUIT: run = False

        screen.blit(sleepy_button, (50, screen.get_height() - 100))
        screen.blit(happy_button, (150, screen.get_height() - 100))
        screen.blit(excited_button, (250, screen.get_height() - 100))
        screen.blit(angry_button, (350, screen.get_height() - 100))
        pygame.display.update()
        clock.tick(60)

if __name__ == "__main__":
    main()