import pygame

def main():
    pygame.init()

    BG = (255,255,255)

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