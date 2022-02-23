import pygame, pygame.freetype


class Button:  # создание кнопок основного меню
    def __init__(self, x, y, image, scale):
        width = image.get_width()
        height = image.get_height()
        self.image = pygame.transform.scale(image, (int(width * scale), int(height * scale)))
        self.rect = self.image.get_rect()
        self.rect.topleft = (x, y)
        self.clicked = False

    def draw(self, surface):
        action = False
        pygame.init()
        pos = pygame.mouse.get_pos()

        if self.rect.collidepoint(pos):
            if pygame.mouse.get_pressed()[0] == 1 and not self.clicked:
                self.clicked = True
                action = True

        if pygame.mouse.get_pressed()[0] == 0:
            self.clicked = False
        surface.blit(self.image, (self.rect.x, self.rect.y))
        return action


SCREEN_HEIGHT = 500
SCREEN_WIDTH = 800

screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption('Start')
back = pygame.image.load('osnPfut.jpg')
back = pygame.transform.scale(back, (800, 500))
start_img = pygame.image.load('start_btn.png').convert_alpha()
exit_img = pygame.image.load('exit_btn.png').convert_alpha()
rect_x = 1920 // 3
rect_y = 1080 - 200
rect_width = 100
rect_height = 100
is_start = False
is_finish = False
# laser_im = pygame.image.load('Laser.png')
laser = pygame.image.load('Laser.png')
image_laser = pygame.transform.scale(laser, (150, 30))
laser_rect = image_laser.get_rect()
image = pygame.image.load('player.png')
image = pygame.transform.scale(image, (100, 100))
rect = image.get_rect()
start_button = Button(100, 200, start_img, 0.8)
exit_button = Button(450, 200, exit_img, 0.8)


def menu():  # создание окна основного меню
    global is_start
    run = True

    text1 = 'SEASON RIDER', 500, (192, 255, 192)
    while run:
        screen.fill((202, 0, 100))
        screen.blit(back, (0, 0))
        if start_button.draw(screen):
            is_start = True
            return is_start
        if exit_button.draw(screen):
            pygame.quit()
            exit(0)
            return None

        for event in pygame.event.get():
            if event.type == pygame.K_1:
                run = False
                exit(0)
                return
            pygame.display.update()


menu()
level = 1
SCREEN_HEIGHT = 1920
SCREEN_WIDTH = 1080


class Player(pygame.sprite.Sprite):  # создание модели персонажа
    global rect

    def __init__(self):
        super().__init__()
        self.level = None
        self.image = pygame.image.load('player.png')
        self.image = pygame.transform.scale(self.image, (100, 100))
        self.rect = self.image.get_rect()

        self.change_y = 0

    def update(self):
        self.rect.y += self.change_y
        if self.rect.y < 0:
            self.rect.y = 440
            self.change_y = 0
        if self.rect.y >= 900:
            self.rect.y = 440
            self.change_y = 0

    def stop(self):
        self.change_y = 0

    def jump(self):  # механика движения персонажа
        self.change_y = 7

    def player_down(self):
        self.change_y = -9

    # def shot(self):
    #     self.x = 340
    #     self.y = self.rect.y
    #     pygame.draw.rect(screen, (255, 0, 0),
    #                      (340, 500, 100, 100), 0)
    #     print(self.y)

class Bullet():
    global laser_rect, rect

    def __init__(self, x, y):
        # super().__init__()
        # self.rect = rect
        # self.laser_rect = laser_rect
        self.x = 340
        self.y = y
        # if self.y == self.rect.y:
        #     print(self.y)

    def move(self):
        self.x += 15
        if self.x <= 1920:
            screen.blit(image_laser, (self.x, self.y))
            print(self.y)
            return True
        else:
            return False


# class Bullet():
#     global laser_rect, rect
#
#     def __init__(self, x, y):
#         # super().__init__()
#         self.rect = rect
#         self.laser_rect = laser_rect
#         self.x = 340
#         self.y = self.rect.y
#         if self.y == self.rect.y:
#             print(self.y)
#
#     def move(self):
#         self.x += 15
#         if self.x <= 1920:
#             screen.blit(self.laser_rect, (self.x, self.y))
#             return True
#         else:
#             return False
#

# class Bullet(pygame.sprite.Sprite):
# def __init__(self, x, y, radius, color):
#     self.x = x
#     self.y = y
#     self.radius = radius
#     self.color = color
#     self.facing = 1
#     self.vel = 8 * self.facing
#
# def draw(self):
#
# def update(self):
#     self.rect.y += self.speedy
#     # убить, если он заходит за верхнюю часть экрана
#     if self.rect.bottom < 0:
#         self.kill()


class Level(object):  # класс уровней, их основа
    global score, screen, level, mas

    def __init__(self, player):
        # self.platform_list = pygame.sprite.Group()
        self.player = player

    def draw(self, screen):
        level = 1
        if level == 1:
            bg = pygame.image.load('planeta1_fon.jpg')
            bg = pygame.transform.scale(bg, (1920, 1080))
        elif level == 2:
            bg = pygame.image.load('planeta2_fon.jpeg')
            bg = pygame.transform.scale(bg, (1920, 1080))
        elif level == 3:
            bg = pygame.image.load('planeta3_fon.jpg')
            bg = pygame.transform.scale(bg, (1920, 1080))
        elif level == 4:
            bg = pygame.image.load('planeta_final_fon.jpg')
            bg = pygame.transform.scale(bg, (1920, 1080))
        screen.blit(bg, (0, 0))


class Level_01(Level):  # остальные механики первого уровня
    def __init__(self, player):
        Level.__init__(self, player)


score = 0

SCREEN_WIDTH, SCREEN_HEIGHT = 1920, 1080
size = [SCREEN_WIDTH, SCREEN_HEIGHT]
screen = pygame.display.set_mode(size, pygame.FULLSCREEN)
pygame.display.set_caption("побежать из тюрьмы")
player = Player()
level_list = [Level_01(player)]

current_level_no = 0
current_level = level_list[current_level_no]

active_sprite_list = pygame.sprite.Group()
player.level = current_level

player.rect.x = 340
player.rect.y = SCREEN_HEIGHT // 2

# target = pygame.image.load('target.png')
# target = pygame.transform.scale(target, (100, 100))
# target_rect = target.get_rect()
# target_rect.x = 1700
# target_rect.y = 350
# active_sprite_list.add(target)
active_sprite_list.add(player)
done = False
clock = pygame.time.Clock()
all_btn_bullets = []

while not done:
    Level(object)

    for event in pygame.event.get():
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_1:
                done = True
            if event.key == pygame.K_s:
                player.jump()

            if event.key == pygame.K_w:
                player.player_down()
            if event.key == pygame.K_f:
                player.stop()
            #
            # if event.key == pygame.K_SPACE:
            #     player.shot()
            if event.key == pygame.K_e:
                print(player.rect.x)
                # player.stop()
                # h = (rect_x + rect_width, rect_y)
                all_btn_bullets.append(Bullet(rect_x + rect_width, rect_y))

                for bullet in all_btn_bullets:
                    if not bullet.move():
                        all_btn_bullets.remove(bullet)

    active_sprite_list.update()

    if player.rect.right > SCREEN_WIDTH:
        player.rect.right = SCREEN_WIDTH

    if player.rect.left < 0:
        player.rect.left = 0

    current_level.draw(screen)
    active_sprite_list.draw(screen)

    clock.tick(30)

    pygame.display.flip()

if __name__ == '__main__':
    pygame.quit()
