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

pygame.font.init()
font = pygame.font.Font(None, 35)
win_right = font.render('PLAYER RIGHT WINS!', True, (180, 0, 0))
win_left = font.render('PLAYER LEFT WINS!', True, (180, 0, 0))
score_left = 0
score_right = 0

score_left_text = font.render(f'Score Left: {score_left}', True, (0, 0, 0))
score_right_text = font.render(f'Score Right: {score_right}', True, (0 ,0, 0))

player_l = GameSprite('racket.png', 5, 200, 4, 50, 150)
player_r = GameSprite('racket.png', 550, 200, 4, 50, 150)
ball = GameSprite('tenis_ball.png', 100, 200, 4, 50, 50)
speed_x = 4
speed_y = 4

finish = False

while game:
    for e in pygame.event.get():
        if e.type == pygame.QUIT:
            game = False

    if not finish:
        window.fill(back)
        

        player_l.reset()
        player_r.reset()
        player_l.update_l()
        player_r.update_r()
        if pygame.sprite.collide_rect(player_r, ball) or pygame.sprite.collide_rect(player_l, ball):
            speed_x *= -1
        ball.reset()
        ball.rect.x += speed_x
        ball.rect.y += speed_y
        if ball.rect.x < 0:
            score_right += 1
            ball.rect.x = 250
            ball.rect.y = 250
        if ball.rect.x > 600:
            score_left += 1
            ball.rect.x = 250
            ball.rect.y = 250

        if ball.rect.y >= 500 or ball.rect.y < 0:
            speed_y*= -1
        
        if score_right == 10:
            window.blit(win_right, (150, 150))

            finish = True
        if score_left == 10:
            window.blit(win_left, (150, 150))
            finish = True

        score_left_text = font.render(f'Score Left: {score_left}', True, (0, 0, 0))
        score_right_text = font.render(f'Score Right: {score_right}', True, (0 ,0, 0))
        window.blit(score_left_text, (10, 10))
        window.blit(score_right_text, (410, 10))
    pygame.display.update()
    clock.tick(FPS)
