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

is_start = False
is_finish = False
start_button = Button(100, 200, start_img, 0.8)
exit_button = Button(450, 200, exit_img, 0.8)

rect_x = 1920 // 3
rect_y = 1080 - 200
rect_width = 100
rect_height = 100

# laser_im = pygame.image.load('Laser.png')
laser = pygame.image.load('Laser.png')
image_laser = pygame.transform.scale(laser, (1700, 20))
laser_rect = image_laser.get_rect()
image = pygame.image.load('player.png')
image = pygame.transform.scale(image, (100, 100))
rect = image.get_rect()

target1 = pygame.image.load('target.png')
target1_dr = pygame.transform.scale(target1, (100, 100))
target1 = target1_dr.get_rect()
target2 = pygame.image.load('target.png')
target2_dr = pygame.transform.scale(target2, (100, 100))
target2 = target2_dr.get_rect()
target3 = pygame.image.load('target.png')
target3_dr = pygame.transform.scale(target3, (100, 100))
target3 = target3_dr.get_rect()
laser_group = pygame.sprite.Group()
targetss = pygame.sprite.Group()
laser1 = pygame.sprite.Sprite()
target11 = pygame.sprite.Sprite()
target21 = pygame.sprite.Sprite()
target31 = pygame.sprite.Sprite()



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


class Bullet():
    global laser_rect, image_laser, laser_group

    def __init__(self, x, y):
        self.rect_y = rect_y
        self.x = x
        self.y = y

    def move(self):
        screen.blit(image_laser, (self.x, self.y))
        print(90)

        return True




        # else:
        #     return False


class Target(pygame.sprite.Sprite):
    global target1, target2, target3, tagetss, target1_dr, target2_dr, target3_dr

    def firstTarget(self):
        screen.blit(target1_dr, (1300, 156))

    def secondTarget(self):
        screen.blit(target2_dr, (1300, 456))

    def trihrdTarget(self):
        screen.blit(target3_dr, (1300, 756))

    # def targets(self):
    #     bullet = Bullet(self.rect.centerx, self.rect.top)
    #     all_sprites.add(bullet)
    #     bullets.add(bullet)
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
        global arrow
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
# laser_group = pygame.sprite.Group()
# targets = pygame.sprite.Group()
player.level = current_level

player.rect.x = 340
player.rect.y = SCREEN_HEIGHT // 2

# target = pygame.image.load('target.png')
# target = pygame.transform.scale(target, (100, 100))
# target_rect = target.get_rect()
# target_rect.x = 1700
# target_rect.y = 350
# active_sprite_list.add(target)
# active_sprite_list.add(target_rect)
active_sprite_list.add(player)
# laser_group.add(laser_rect)
# targets.add(target_rect)
done = False
clock = pygame.time.Clock()

score = 0
while not done:
    Level(object)
    pygame.mouse.set_visible(False)

    current_level.draw(screen)
    Target().firstTarget()
    Target().secondTarget()
    Target().trihrdTarget()
    active_sprite_list.draw(screen)

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
            #     player.shot( )
            if event.key == pygame.K_e:
                # print(player.rect.x)
                # player.stop()
                # h = (rect_x + rect_width, rect_y)
                # Bullet(340, 500).move()
                active_sprite_list.update()

                # active_sprite_list.add(laser1)
                # laser_group.add(laser1)
                # targetss.add(target11)
                # targetss.add(target21)
                # targetss.add(target31)
                # hits = pygame.sprite.groupcollide(targetss, laser_group, True, True)

                bul = Bullet(player.rect.right, player.rect.centery).move()
                # hits = laser_rect.colliderect(Target().firstTarget())

                # all_sprites.update()
                # hits = pygame.sprite.spritecollide(laser_rect, target1, False)
                # if hits:
                #     score += 1
                #     print (score)

                if target1.colliderect(laser_rect):
                    score += 1
                    print (score)
                #

                # if target_rect1.collidepoint(laser_rect.center):
                # hits = pygame.sprite.spritecollide(laser_rect, target_rect1, False)
                # if hits:
                #     print(28)

                # collide = rect1.colliderect(rect2)

                # if laser_rect.y >= target_rect.bottom and laser_rect.y <= target_rect.top:
                #     score += 1
                #     print(score)
                #     if score == 3:
                #         pass
                pygame.display.flip()

                # for bullet in all_btn_bullets:
                #     if not bullet.move():
                #         all_btn_bullets.remove(bullet)

    active_sprite_list.update()

    if player.rect.right > SCREEN_WIDTH:
        player.rect.right = SCREEN_WIDTH

    if player.rect.left < 0:
        player.rect.left = 0

    # current_level.draw(screen)
    # Target().firstTarget()
    # Target().secondTarget()
    # Target().trihrdTarget()
    # active_sprite_list.draw(screen)

    clock.tick(30)

    pygame.display.flip()

if __name__ == '__main__':
    pygame.quit()
