import pygame
pygame.init()

window_width = 750
window_height = 600

background = pygame.image.load('track.png')

window = pygame.display.set_mode((window_width, window_height))
pygame.display.set_caption("chrome dinosaur game")
clock = pygame.time.Clock()

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            exit()
    window.blit(background, (0, 300))
    pygame.display.update()
    clock.tick(60)