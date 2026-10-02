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
        self.image = pygame.transform.scale(pygame.image.load(image), (width, height))        
        self.rect = pygame.Rect(x, y, width, height)
        self.speed = speed

class Dino(GameSprite):
    def __init__(self, image, x, y, width, height, speed, jump_velocity, duck_velocity, animation):
        super().__init__(image, x, y, width, height, speed)
        self.jump_velocity = jump_velocity
        self.duck_velocity = duck_velocity
        self.animation = animation
        self.is_jumping = False
        self.start_y = y
        self.duck_velocity_y = 0
        self.run_images = [
            pygame.transform.scale(pygame.image.load('dino-run1.png'), (width, height)),
            pygame.transform.scale(pygame.image.load('dino-run2.png'), (width, height))
        ]
        self.jump_img = pygame.transform.scale(pygame.image.load('dino-jump.png'), (width, height))
        self.anim_step = 0
        self.gravity = 0.6

    def jump(self):
        if not self.is_jumping:
            self.is_jumping =  True
            self.duck_velocity_y = -self.jump_velocity
    def update(self):
        if self.is_jumping:
            self.velocity_y += self.gravity
            self.rect.y += self.velocity_y
            self.image = self.jump_img

        if self.rect.y >= self.start_y:
            self.rect.y = self.start_y
            self.velocity_y = 0
            self.is_jumping = False

        else:
            self.anim_step += False
            frame = int(self.anim_step)% len(self.run_images)
            self.image = self.run_images[frame]
    def show(self):
        window.blit(self.image, (self.rect.x, self.rect.y))

dinoasur = Dino('dino.png', 100, 300, 50, 50, 5, 10, 5, 'jump')
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            exit()
        if event.type == pygame.KEYDOWN:
            if event.key in (pygame.K_SPACE, pygame.K_UP):
                dinoasur.jump()
    window.blit(background, (0, 300))
    dinoasur.show()
    dinoasur.update()
    pygame.display.update()
    clock.tick(60)