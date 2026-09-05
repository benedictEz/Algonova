import pygame

back = (200, 255, 255)
win_width = 600
win_height = 500
window = pygame.display.set_mode((win_width, win_height))
window.fill(back)
game = True
finish = False
clock = pygame.time.Clock()
FPS = 60




while game:
    for e in pygame.event.get():
        if e.type == pygame.QUIT:
            break

    pygame.display.update()
    clock.tick(FPS)
