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

    def update_r(self):
        keys = pygame.key.get_pressed()
        if keys[pygame.K_UP] and self.rect.y > 5:
            self.rect.y -= self.speed
        if keys[pygame.K_DOWN] and self.rect.y < win_height - 80:
            self.rect.y += self.speed

    def update_l(self):
        keys = pygame.key.get_pressed()
        if keys[pygame.K_w] and self.rect.y > 5:
            self.rect.y -= self.speed
        if keys[pygame.K_s] and self.rect.y < win_height - 80:
            self.rect.y += self.speed


    def reset(self):
        window.blit(self.image, (self.rect.x, self.rect.y))

player_l = GameSprite('racket.png', 5, 200, 4, 50, 150)
player_r = GameSprite('racket.png', 550, 200, 4, 50, 150)
ball = GameSprite('tenis_ball.png', 100, 200, 4, 50, 50)
speed_x = 1
speed_y = 1

while game:
    for e in pygame.event.get():
        if e.type == pygame.QUIT:
            game = False
    window.fill(back)\
    
    player_l.reset()
    player_r.reset()
    player_l.update_l()
    player_r.update_r()

    ball.reset()
    ball.rect.x += speed_x
    ball.rect.y += speed_y

    if ball.rect.y >= 500 or ball.rect.y < 0:
        speed_y*= -1
    pygame.display.update()
    clock.tick(FPS)
