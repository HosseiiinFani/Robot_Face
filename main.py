import pygame

def main():
    pygame.init()

    BG = (255,255,255)

    happy = pygame.image.load("lib/happy.png")
    angry = pygame.image.load("lib/angry.png")
    sleepy = pygame.image.load("lib/sleepy.png")
    excited = pygame.image.load("lib/excited.png")

    moods = {'happy': happy, 'angry': angry, 'sleepy': sleepy, 'excited': excited}

    screen = pygame.display.set_mode((480,800))
    clock = pygame.time.Clock()

    run = True

    screen.fill(BG)

    while run:
        events = pygame.event.get()
        for event in events:
            if event.type == pygame.QUIT: run = False
        pygame.display.update()
        clock.tick(60)

if __name__ == "__main__":
    main()