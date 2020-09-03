# python game with pygame : Jumping dino
# by. BlockDMask
import pygame
import sys

# step1 : set screen, fps

pygame.init()
pygame.display.set_caption('Jumping dino')
MAX_WIDTH = 800
MAX_HEIGHT = 400


def main():
    # set screen, fps
    screen = pygame.display.set_mode((MAX_WIDTH, MAX_HEIGHT))
    fps = pygame.time.Clock()

    while True:
        screen.fill((255, 255, 255))

        # event check
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

        # draw tree
        pygame.display.update()
        fps.tick(30)


if __name__ == '__main__':
    main()
