import pygame
pygame.init()


back = (200, 255, 255)
win_width = 600
win_height = 500
window = pygame.display.set_mode((win_width, win_height))
window.fill(back)
game = True
finish = False
clock = pygame.time.Clock()
FPS = 60

class GameSprite(pygame.sprite.Sprite):
    def __init__(self, player_image, player_x, player_y, player_speed, width, height):
        super().__init__()
        self.image = pygame.transform.scale(pygame.image.load(player_image), (width, height))
        self.speed = player_speed
        self.rect = self.image.get_rect()
        self.rect.x = player_x
        self.rect.y = player_y

    def reset(self):
        window.blit(self.image, (self.rect.x, self.rect.y))

player_l = GameSprite('racket.png', 5, 200, 4, 50, 150)
player_r = GameSprite('racket.png', 550, 200, 4, 50, 150)
ball = GameSprite('tenis_ball.png', 100, 200, 4, 50, 50)


while game:
    for e in pygame.event.get():
        if e.type == pygame.QUIT:
            game = False
    window.fill(back)
    player_l.reset()
    player_r.reset()
    ball.reset()
    pygame.display.update()
    clock.tick(FPS)
