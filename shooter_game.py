#Create your own shooter

from pygame import *
from random import randint

win_width = 700
win_height = 500
display.set_caption('Shooter')
window = display.set_mode((win_width, win_height))
background = transform.scale(image.load('galaxy.jpg'), (win_width, win_height))

font.init()
text = font.Font(None, 36)

score = 0
lost = 10

class GameSprite(sprite.Sprite):
    def __init__(self, player_image, player_x, player_y, size_x, size_y, player_speed):
        sprite.Sprite.__init__(self)
        self.image = transform.scale(image.load(player_image), (size_x, size_y))
        self.speed = player_speed
        self.rect = self.image.get_rect()
        self.rect.x = player_x
        self.rect.y = player_y
    def reset(self):
        window.blit(self.image, (self.rect.x, self.rect.y))

class Player(GameSprite):

    def update(self):
        keys = key.get_pressed()
        if keys[K_LEFT] and self.rect.x > 5:
            self.rect.x -= self.speed
        if keys[K_RIGHT] and self.rect.x < win_width - 80:
            self.rect.x += self.speed

    def fire(self):
        bullet = Bullet('bullet.png', self.rect.centerx, self.rect.top, 15, 20, -15)
        bullets.add(bullet)

class Enemy(GameSprite):
    def update(self):
        self.rect.y += self.speed
        if self.rect.y > win_height:
            self.rect.x = randint(80, win_width - 80)
            self.rect.y = 0

class Bullet(GameSprite):
    def update(self):
        self.rect.y += self.speed
        if self.rect.y < 0:
            self.kill()
            

game_over = False

player = Player('rocket.png', 450, 400, 65, 65, 5)

enemies = sprite.Group()
bullets = sprite.Group()

for i in range(3):
    enemy = Enemy('ufo.png', randint(0, 700), 0, 65, 65, randint(1, 4))
    asteroid = Enemy('asteroid.png', randint(0, 700), 0, 65, 65, randint(1, 4))
    enemies.add(enemy)
    enemies.add(asteroid)

text_lose = text.render('You lose!', 1, (255, 255, 255))
text_win = text.render('You win!', 1, (255, 255, 255))

clock = time.Clock()
run = True
while run:
    for e in event.get():
        if e.type == QUIT:
            run = False
        elif e.type == KEYDOWN:
            if e.key == K_SPACE:
                player.fire()
    if not game_over:
        
        window.blit(background, (0, 0))
        enemies.draw(window)
        enemies.update()
        player.reset()
        player.update()
        bullets.update()
        bullets.draw(window)
        score_text = text.render("Score:"+str(score), 1, (255, 255, 255))
        window.blit(score_text, (10, 20))
        health_text = text.render("Health:"+str(lost), 1, (255, 255, 255))
        window.blit(health_text, (10, 60))

        collides = sprite.groupcollide(enemies, bullets, True, True)
        for c in collides:
            score += 1
            random_choice = randint(0, 1)
            if random_choice == 0:
                asteroid = Enemy('asteroid.png', randint(0, 700), 0, 65, 65, randint(1, 4))
                enemies.add(asteroid)
            else:
                enemy = Enemy('ufo.png', randint(0, 700), 0, 65, 65, randint(1, 4))
                enemies.add(enemy)

        collides2 = sprite.spritecollide(player, enemies, True)
        for c in collides2:
            lost -= 1
            random_choice = randint(0, 1)
            if random_choice == 0:
                asteroid = Enemy('asteroid.png', randint(0, 700), 0, 65, 65, randint(1, 4))
                enemies.add(asteroid)
            else:
                enemy = Enemy('ufo.png', randint(0, 700), 0, 65, 65, randint(1, 4))
                enemies.add(enemy)
            window.blit(text_lose, (350, 250))
            game_over = True
        if score > 10:
            window.blit(text_win, (350, 250))
            game_over = True
    display.update()
    clock.tick(60)