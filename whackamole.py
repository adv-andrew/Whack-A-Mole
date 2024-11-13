import pygame
import random

def grid(x, y):
    return x * 32, y * 32

def main():
    try:
        pygame.init()
        # You can draw the mole with this snippet:
        # screen.blit(mole_image, mole_image.get_rect(topleft=(x,y)))
        # BELLOOOOOOO
        mole_image = pygame.image.load("minion_mole.png")
        screen = pygame.display.set_mode((640, 512))
        clock = pygame.time.Clock()
        running = True
        moleCords = 0,0
        while running:
            for event in pygame.event.get():
                if event.type == pygame.MOUSEBUTTONDOWN:
                    mousePos = event.pos
                    if moleCords[0]*32 <= mousePos[0] <= moleCords[0]*32+32 and moleCords[1]*32 <= mousePos[1] <= moleCords[1]*32+32:
                        moleCords = random.randrange(0,20), random.randrange(0,16)

                if event.type == pygame.QUIT:
                    running = False
            screen.fill("light blue")
            screen.blit(pygame.image.load("minion_background.png"), pygame.image.load(
                "minion_background.png").get_rect(topleft=(0, 0)))
            screen.blit(mole_image, mole_image.get_rect(topleft=(grid(moleCords[0], moleCords[1]))))
            for i in range(20):
                pygame.draw.line(screen, "white", (32*i, 0), (32*i, 512))
            for i in range(16):
                pygame.draw.line(screen, "white", (0, 32*i), (640, 32*i))
            pygame.display.flip()
            clock.tick(60)
    finally:
        pygame.quit()


if __name__ == "__main__":
    main()
