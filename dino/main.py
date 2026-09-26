import pygame
pygame.init()

window_width = 750
window_height = 600

background = pygame.image.load('track.png')

window = pygame.display.set_mode((window_width, window_height))
pygame.display.set_caption("chrome dinosaur game")
clock = pygame.time.Clock()

class GameSprite(pygame.sprite.Sprite):
    def __init__(self, image, x, y, width, height, speed):
        super().__init__()
        self.image = image
        self.rect = pygame.Rect(x, y, width, height)
        self.speed = speed

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            exit()
    window.blit(background, (0, 300))
    pygame.display.update()
    clock.tick(60)