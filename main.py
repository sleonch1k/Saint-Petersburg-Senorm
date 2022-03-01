import pygame



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
pygame.mixer.init()
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption('Start')
pygame.mixer.music.load("John Williams, London Symphony Orchestra - Star Wars Main Title and the Arrival at Naboo.mp3")
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
target1_rect = pygame.Rect
target2 = pygame.image.load('target.png')
target2_dr = pygame.transform.scale(target2, (100, 100))
target2_rect = pygame.Rect
target3 = pygame.image.load('target.png')
target3_dr = pygame.transform.scale(target3, (100, 100))
target3_rect = pygame.Rect

target21 = pygame.image.load('target.png')
target21_dr = pygame.transform.scale(target21, (50, 50))
target21_rect = pygame.Rect
target22 = pygame.image.load('target.png')
target22_dr = pygame.transform.scale(target22, (50, 50))
target22_rect = pygame.Rect
target23 = pygame.image.load('target.png')
target23_dr = pygame.transform.scale(target23, (50, 50))
target23_rect = pygame.Rect


# laser_group = pygame.sprite.Group()
# targetss = pygame.sprite.Group()
# laser1 = pygame.sprite.Sprite()
# target11 = pygame.sprite.Sprite()
# target21 = pygame.sprite.Sprite()
# target31 = pygame.sprite.Sprite()


def menu():  # создание окна основного меню
    pygame.init()
    global is_start
    run = True
    font = pygame.font.Font(None, 50)
    text1 = font.render('SAVE THE WORLD', True, (255, 255, 255))


    while run:
        screen.fill((202, 0, 100))
        screen.blit(back, (0, 0))
        screen.blit(text1, (200, 100))
        if start_button.draw(screen):
            is_start = True
            pygame.mixer.music.play(1)
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
        if self.rect.y < 100:
            self.rect.y = 440
            self.change_y = 0
        if self.rect.y >= 950:
            self.rect.y = 440
            self.change_y = 0

    def stop(self):
        self.change_y = 0

    def jump(self):  # механика движения персонажа
        self.change_y = 7

    def player_down(self):
        self.change_y = -9

    def shot(self):
        laser_rect.y = self.rect.y
        return laser_rect.y


class Bullet(Player):
    global laser_rect, image_laser, laser_group

    def __init__(self, x, y):
        self.rect_y = rect_y
        self.x = x
        self.y = y
        self.rect = pygame.Rect

    def move(self):
        return screen.blit(image_laser, (self.x, self.y))

    def rect(self):
        return self.rect


class Target(pygame.sprite.Sprite):
    global target1_rect, target2_rect, target3_rect, target1, target2, target3, target1_dr, target2_dr, target3_dr

    def firstTarget(self):
        global target1_rect
        target1_rect = screen.blit(target1_dr, (1300, 156))

    def secondTarget(self):
        global target2_rect
        target2_rect = screen.blit(target2_dr, (1300, 456))

    def trihrdTarget(self):
        global target3_rect
        target3_rect = screen.blit(target3_dr, (1300, 756))

    def firstTarget_secondLevel(self):
        global target21_rect
        target21_rect = screen.blit(target21_dr, (1300, 156))

    def secondTarget_secondLevel(self):
        global target22_rect
        target22_rect = screen.blit(target22_dr, (1300, 456))

    def trihrdTarget_secondLevel(self):
        global target23_rect
        target23_rect = screen.blit(target23_dr, (1300, 756))


level = 1


class Level(object):  # класс уровней, их основа
    global score, screen, level, mas

    def __init__(self, player):

        self.player = player

    def draw(self, screen):
        global arrow

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
pygame.display.set_caption("save the world")
player = Player()
level_list = [Level_01(player)]

current_level_no = 0
current_level = level_list[current_level_no]

active_sprite_list = pygame.sprite.Group()
player.level = current_level

player.rect.x = 340
player.rect.y = SCREEN_HEIGHT // 2

active_sprite_list.add(player)

done = False
clock = pygame.time.Clock()

score = 0
count_of_bullets = 11


def level2():
    global score, level, count_of_bullets
    level = 3


    running2 = True

    while running2:
        Level(object)
        pygame.mouse.set_visible(False)
        font = pygame.font.Font(None, 50)
        text = font.render('your bullets: ' + str(count_of_bullets), True, (255, 0, 0))
        current_level.draw(screen)
        first_shoted = 0
        second_shoted = 0
        trihrd_shoted = 0
        if first_shoted == 0:
            Target().firstTarget_secondLevel()
        if second_shoted == 0:
            Target().secondTarget_secondLevel()
        if trihrd_shoted == 0:
            Target().trihrdTarget_secondLevel()
        active_sprite_list.draw(screen)
        screen.blit(text, (250, 250))

        pygame.display.update()


        for event in pygame.event.get():

            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_1:
                    running2 = False

                if event.key == pygame.K_s:
                    player.jump()

                if event.key == pygame.K_w:
                    player.player_down()

                if event.key == pygame.K_f:
                    player.stop()

                if event.key == pygame.K_e:
                    count_of_bullets -= 1

                    active_sprite_list.update()

                    bullet_rect = Bullet(player.rect.right, player.rect.centery).move()

                    if bullet_rect.colliderect(target22_rect):

                        score += 1


                    elif bullet_rect.colliderect(target21_rect):
                        score += 1


                    elif bullet_rect.colliderect(target23_rect):
                        score += 1



                    if score == 6:
                        print('you won')
                        running2 = False
                    if count_of_bullets < 1:
                        print('you lose')
                        running2 = False

                        # print(target1_rect.y)
                        # print(laser_rect.y)

                    pygame.display.flip()

        active_sprite_list.update()

        if player.rect.right > SCREEN_WIDTH:
            player.rect.right = SCREEN_WIDTH

        if player.rect.left < 0:
            player.rect.left = 0

        clock.tick(30)

        pygame.display.flip()


font = pygame.font.Font(None, 50)

while not done:
    Level(object)
    text = font.render('your bullets: ' + str(count_of_bullets), True, (255, 0, 0))
    pygame.mouse.set_visible(False)


    current_level.draw(screen)
    Target().firstTarget()
    Target().secondTarget()
    Target().trihrdTarget()
    screen.blit(text, (250, 250))
    active_sprite_list.draw(screen)

    pygame.display.update()

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

            if event.key == pygame.K_e:
                count_of_bullets -= 1
                active_sprite_list.update()

                bullet_rect = Bullet(player.rect.right, player.rect.centery).move()

                if bullet_rect.colliderect(target2_rect):

                    score += 1


                elif bullet_rect.colliderect(target1_rect):
                    score += 1



                elif bullet_rect.colliderect(target3_rect):
                    score += 1


                if count_of_bullets < 1:
                    done = True
                    print('you lose')

                if score == 3:
                    print('new level')
                    level2()
                    level = 2

                    done = True

                    # print(target1_rect.y)
                    # print(laser_rect.y)

                pygame.display.flip()

    active_sprite_list.update()

    if player.rect.right > SCREEN_WIDTH:
        player.rect.right = SCREEN_WIDTH

    if player.rect.left < 0:
        player.rect.left = 0

    clock.tick(30)

    pygame.display.flip()

# class ButtonsEnd: #кнопки при окончании игры
#
#     def __init__(self, x, y, image, scale):
#         width = image.get_width()
#         height = image.get_height()
#         self.image = pygame.transform.scale(image, (int(width * scale),
#         int(height * scale)))
#         self.rect = self.image.get_rect()
#         self.rect.topleft = (x, y)
#         self.clicked = false
#
#     def draw(self, surface):
#         action = false
#         pygame.init()
#         pos = pygame.mouse.get_pos()
#         if self.rect.collidepoint(pos):
#         if pygame.mouse.get_pressed()[0] == 1 and not self.clicked:
#             self.clicked = true
#             action = true
#         if pygame.mouse.get_pressed()[0] == 0:
#             self.clicked = false
#             surface.blit(self.image, (self.rect.x, self.rect.y))
#             return action


# pygame.font.init()
# GAME_OVER_FONT = pygame.freetype.Font("orecrusherrotal.ttf", 75)
# textsurface = GAME_OVER_FONT.render('Some Text', False, (100, 100, 100))
# exit_button1 = Button(300, 300, exit_img, 0.8)
# class ButtonsEnd: #кнопки при окончаии игры
#     def __init__(self, x, y, image, scale):
#         width = image.get_width()
#         height = image.get_height()
#         self.image = pygame.transform.scale(image, (int(width * scale), int(height * scale)))
#         self.rect = self.image.get_rect()
#         self.rect.topleft = (x, y)
#         self.clicked = False
#
#     def draw(self, surface):
#         action = False
#         pygame.init()
#         pos = pygame.mouse.get_pos()
#
#         if self.rect.collidepoint(pos):
#             if pygame.mouse.get_pressed()[0] == 1 and not self.clicked:
#                 self.clicked = True
#                 action = True
#
#         if pygame.mouse.get_pressed()[0] == 0:
#             self.clicked = False
#         surface.blit(self.image, (self.rect.x, self.rect.y))
#         return action
#
#
# SCREEN_WIDTH1, SCREEN_HEIGHT1 = 800, 500
#
# screen1 = pygame.display.set_mode((SCREEN_WIDTH1, SCREEN_HEIGHT1), pygame.FULLSCREEN)
# pygame.display.set_caption('Button Demo')
# backgr = pygame.image.load('osnPfut.jpg')
# backgr = pygame.transform.scale(backgr, (800, 500))
#
# exit_img = pygame.image.load('exit_btn.png').convert_alpha()
#
# pygame.font.init()
#
# GAME_OVER_FONT = pygame.freetype.Font("orecrusherrotal.ttf", 75)
# textsurface = GAME_OVER_FONT.render('Some Text', False, (100, 100, 100))
# exit_button1 = Button(300, 300, exit_img, 0.8)
# is_finish1 = True
#
#
# def konec(): #окно поражения
#     global is_finish1, exit_button1
#     run = True
#     while run:
#         screen.fill((0, 0, 0))
#         screen.blit(backgr, (0, 0))
#         if exit_button1.draw(screen):
#             return None
#         text_surface, rect = GAME_OVER_FONT.render("GAME OVER!", (0, 255, 0))
#         screen.blit(text_surface, (200, 100))
#
#         for event in pygame.event.get():
#             if event.type == pygame.QUIT:
#                 run = False
#
#         pygame.display.update()

# def konec(): #окно поражения
#     global is_finish1
#     run = true
#     while run:
#         screen.fill((0, 0, 0))
#         screen.blit(backgro, (0, 0))
#         if exit_button2.draw(screen):
#             return None
#     text_surface, rect = GAME_OVER_FONT.render("Вы проиграли", (0, 255, 0))
#     screen.blit(text_surface, (200, 100))
#     for event in pygame.event.get():
#     if event.type == pygame.QUIT:
#         run = false
#     pygame.display.update()


if __name__ == '__main__':
    pygame.quit()
