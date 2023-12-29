import pygame
import time
import json


file_path = '' #вставте це /data/data/com.Warknak.Card master/files/app/ у лапки зінної file_path якщо створюєте .apk файл
#newBackground = pygame.transform.scale(background, (WIDTH, HEIGHT))
pygame.init()
button_bake = pygame.image.load(file_path + 'image/Button/Menu/Button _back_.png')
clock = pygame.time.Clock()
screen = pygame.display.set_mode((612, 367)) #flags = pygame.NOFRAME
pygame.display.set_caption("Card master")
icon = pygame.image.load(file_path + 'image/Picture program.png').convert_alpha()
pygame.display.set_icon(icon)
text_game = pygame.font.Font(file_path + 'font/Roboto-Light.ttf', 20)
name_of_game = text_game.render('Card master', True, 'Red')



file = open(file_path + 'progress.json', 'r')
game_info = json.load(file)
file.close()
key_button_down_check = False
key_button_left_check = False

wall_1 = pygame.image.load(file_path + 'image/Walls/Dangeren.png').convert_alpha()
wall_1_y = 100
wall_2_x = 0
wall_3_x = 0
wall_5_x = 0
wall_1_y_check = False
wall_2_x_check = False
wall_3_x_check = False
wall_5_x_check = False
wall_2 = pygame.image.load(file_path + 'image/Walls/Dangeren.png').convert_alpha()
wall_2_y = 150
wall_2_y_check = False
wall_3 = pygame.image.load(file_path + 'image/Walls/Dangeren.png').convert_alpha()
wall_3_y = 200
wall_3_y_check = False
wall_4 = pygame.image.load(file_path + 'image/Walls/Dangeren.png').convert_alpha()
wall_4_y = 250
wall_4_y_check = False

laser_circle = pygame.image.load(file_path + 'image/Walls/Dangeren_1.png').convert_alpha()
laser_circle_1 = laser_circle
laser_circle_2 = laser_circle

key_button_up_check = False

line_laser = pygame.image.load(file_path + 'image/Walls/Lasers/Line_laser.png').convert_alpha()
line_laser_v2 = pygame.image.load(file_path + 'image/Walls/Lasers/Line_laser_2.png').convert_alpha()


common_wall = pygame.image.load(file_path + 'image/Walls/Common_wall_with_K.png').convert_alpha()
common_wall_antibug = pygame.image.load(file_path + 'image/Walls/Common_wall_with_K_antibug.png').convert_alpha()

goal = pygame.image.load(file_path + 'image/Goal.png').convert_alpha()

progress_text = text_game.render('Якщо виходите, виходьте через меню, збережете прогрес.', True, 'black')

pause_icon = pygame.image.load(file_path + 'image/Pause icon.png').convert_alpha()
pause_use = False
pause_icon_use = pygame.image.load(file_path + 'image/Pause icon Use.png').convert_alpha()

button_0 = pygame.image.load(file_path + 'image/Button/Keyboard number/0.png').convert_alpha()
button_1 = pygame.image.load(file_path + 'image/Button/Keyboard number/1.png').convert_alpha()
button_2 = pygame.image.load(file_path + 'image/Button/Keyboard number/2.png').convert_alpha()
button_3 = pygame.image.load(file_path + 'image/Button/Keyboard number/3.png').convert_alpha()
button_4 = pygame.image.load(file_path + 'image/Button/Keyboard number/4.png').convert_alpha()
button_5 = pygame.image.load(file_path + 'image/Button/Keyboard number/5.png').convert_alpha()
button_6 = pygame.image.load(file_path + 'image/Button/Keyboard number/6.png').convert_alpha()
button_7 = pygame.image.load(file_path + 'image/Button/Keyboard number/7.png').convert_alpha()
button_8 = pygame.image.load(file_path + 'image/Button/Keyboard number/8.png').convert_alpha()
button_9 = pygame.image.load(file_path + 'image/Button/Keyboard number/9.png').convert_alpha()
number_canvas = pygame.image.load(file_path + 'image/Button/Keyboard number/Number canvas.png').convert_alpha()
pl_button_up = pygame.image.load(file_path + 'image/Button/Playing butons/Pl._button up.png').convert_alpha()
pl_button_down = pygame.image.load(file_path + 'image/Button/Playing butons/Pl. button down.png').convert_alpha()
pl_button_left = pygame.image.load(file_path + 'image/Button/Playing butons/Pl. button left.png').convert_alpha()
pl_button_right = pygame.image.load(file_path + 'image/Button/Playing butons/Pl. button right.png').convert_alpha()

levels = 'choose'
frame_of_levels = pygame.image.load(file_path + 'image/Background/Levels background/Frame of levels.png').convert_alpha()
level_1_0 = pygame.image.load(file_path + 'image/Background/Levels background/Level 1/Level 1.0.png').convert_alpha()
level_1_1 = pygame.image.load(file_path + 'image/Background/Levels background/Level 1/Level 1.1.png').convert_alpha()
level_1_2 = pygame.image.load(file_path + 'image/Background/Levels background/Level 1/Level 1.2.png').convert_alpha()
level_play = False

level_3_0 = pygame.image.load(file_path + 'image/Background/Levels background/Level 3/3.0.png').convert_alpha()
tool = pygame.image.load(file_path + 'image/Background/Levels background/Tool/example.png')

set_buttons_button = pygame.image.load(file_path + 'image/Button/Playing butons/Settinging x, y of buttons.png').convert_alpha()

if game_info['version button'] == 1:
    variant = '1'
    pl_button_up_x = 450
    pl_button_up_y = 203
    pl_button_down_x = 450
    pl_button_down_y = 280
    pl_button_right_x = 529
    pl_button_right_y = 280
    pl_button_left_x = 371
    pl_button_left_y = 280
elif game_info['version button'] == 2:
    variant = '2'
    pl_button_up_x = 3
    pl_button_up_y = 3
    pl_button_left_x = 450
    pl_button_left_y = 280
    pl_button_right_x = 529
    pl_button_right_y = 280
    pl_button_down_x = 3
    pl_button_down_y = 280
elif game_info['version button'] == 3:
    variant = '3'
    pl_button_left_x = 3
    pl_button_left_y = 280
    pl_button_down_x = 82
    pl_button_down_y = 280
    pl_button_up_x = 82
    pl_button_up_y = 203
    pl_button_right_x = 161
    pl_button_right_y = 280
elif game_info['version button'] == 4:
    variant = '4'
    pl_button_up_x = 3
    pl_button_up_y = 203
    pl_button_down_x = 3
    pl_button_down_y = 280
    pl_button_left_x = 450
    pl_button_left_y = 280
    pl_button_right_x = 529
    pl_button_right_y = 280
elif game_info['version button'] == 5:
    variant = '5'
    pl_button_up_x = 529
    pl_button_up_y = 203
    pl_button_down_x = 529
    pl_button_down_y = 280
    pl_button_left_x = 3
    pl_button_left_y = 280
    pl_button_right_x = 82
    pl_button_right_y = 280
else:
    variant = '1'

button_press = False

keyboard_mode = pygame.image.load(file_path + 'image/Button/Playing buttons set/Button keyboard mode.png').convert_alpha()
touch_mode = pygame.image.load(file_path + 'image/Button/Playing buttons set/Button touch mode.png').convert_alpha()
player_skin = pygame.image.load(file_path + 'image/Player animation/Player up/Player_animation1up.png')

if game_info['skin'] == 'default':
    player_death = pygame.image.load(file_path + 'image/Player animation/Player_animation1up_death.png')
    walk_right = [
        pygame.image.load(file_path + 'image/Player animation/Player right/Player_animation1rignt.png').convert_alpha(),
        pygame.image.load(file_path + 'image/Player animation/Player right/Player_animation2right.png').convert_alpha(),
        pygame.image.load(file_path + 'image/Player animation/Player right/Player_animation3right.png').convert_alpha(),
        pygame.image.load(
            file_path + 'image/Player animation/Player right/Player_animation4right.png').convert_alpha(), ]
    walk_left = [
        pygame.image.load(file_path + 'image/Player animation/Player left/Player_animation1left.png').convert_alpha(),
        pygame.image.load(file_path + 'image/Player animation/Player left/Player_animation2left.png').convert_alpha(),
        pygame.image.load(file_path + 'image/Player animation/Player left/Player_animation3left.png').convert_alpha(),
        pygame.image.load(file_path + 'image/Player animation/Player left/Player_animation4left.png').convert_alpha(), ]
    walk_down = [
        pygame.image.load(file_path + 'image/Player animation/Player up/Player_animation1up.png').convert_alpha(),
        pygame.image.load(file_path + 'image/Player animation/Player up/Player_animation2up.png').convert_alpha(),
        pygame.image.load(file_path + 'image/Player animation/Player up/Player_animation3up.png').convert_alpha(),
        pygame.image.load(file_path + 'image/Player animation/Player up/Player_animation4up.png').convert_alpha(), ]
    walk_up = [
        pygame.image.load(file_path + 'image/Player animation/Player down/Player_animation1down.png').convert_alpha(),
        pygame.image.load(file_path + 'image/Player animation/Player down/Player_animation2down.png').convert_alpha(),
        pygame.image.load(file_path + 'image/Player animation/Player down/Player_animation3down.png').convert_alpha(),
        pygame.image.load(file_path + 'image/Player animation/Player down/Player_animation4down.png').convert_alpha(), ]
    stand = pygame.image.load(file_path + 'image/Player animation/Player up/Player_animation1up.png').convert_alpha()
background = pygame.image.load(file_path + 'image/Background/Menu_background.jpg').convert_alpha()
button_start = pygame.image.load(file_path + 'image/Button/Menu/Button _start_.png').convert_alpha()
button_set = pygame.image.load(file_path + 'image/Button/Menu/Button _Settings_.png').convert_alpha()
button_exit = pygame.image.load(file_path + 'image/Button/Menu/Button _exit_.jpg').convert_alpha()
player_animation_count = 0
screen.fill((71, 158, 230))
author = text_game.render('Card master by Warknak', False, 'black')
my_avatar = pygame.image.load(file_path + 'image/My avatar.png').convert_alpha()
upgrade_icon = pygame.image.load(file_path + 'image/Upgrade player/Upgrade icon.jpg').convert_alpha()
background_x = 0
background_sound = pygame.mixer.Sound(file_path + 'sound/background music.mp3')
background_sound.play(1000)
step_sound = pygame.mixer.Sound(file_path + 'sound/Step sound.mp3')

Icon_skins = pygame.image.load(file_path + 'image/Skins pack/Icon skins.png').convert_alpha()
screen_game = 'menu'

level_version = 0.0
if game_info['mode button'] == 'keyboard':
    key_mode = 'keyboard'
else:
    key_mode = 'touch'

down_set = pygame.image.load(file_path + 'image/Button/Playing buttons set/Pl. button down_set.png') .convert_alpha()
up_set = pygame.image.load(file_path + 'image/Button/Playing buttons set/Pl._button up_set.png').convert_alpha()
left_set = pygame.image.load(file_path + 'image/Button/Playing buttons set/Pl. button left_set.png').convert_alpha()
right_set = pygame.image.load(file_path + 'image/Button/Playing buttons set/Pl. button right_set.png').convert_alpha()
corect_cancel = pygame.image.load(file_path + 'image/Button/Playing buttons set/Cancel corect.png').convert_alpha()

lvl_1_kard = pygame.image.load(file_path + 'image/Level kard/Kard lvl 1.png').convert_alpha()
lvl_2_kard = pygame.image.load(file_path + 'image/Level kard/Kard lvl 2.png').convert_alpha()
lvl_3_kard = pygame.image.load(file_path + 'image/Level kard/Kard lvl 3.png').convert_alpha()
lvl_4_kard = pygame.image.load(file_path + 'image/Level kard/Kard lvl 4.png').convert_alpha()
lvl_5_kard = pygame.image.load(file_path + 'image/Level kard/Kard lvl 5.png').convert_alpha()

level_2_check = False
level_3_check = False
level_4_check = False
level_5_check = False
level_6_check = False

completed_game_screen = pygame.image.load(file_path + 'image/Background/Completed game screen.png').convert_alpha()
if game_info['level open'] >= 2:
    level_2_check = True
if game_info['level open'] >= 3:
    level_3_check = True
if game_info['level open'] >= 4:
    level_4_check = True
if game_info['level open'] >= 5:
    level_5_check = True
if game_info['level open'] >= 6:
    level_6_check = True
key_button_down_rect_1_y_n = False

drone = pygame.image.load(file_path + 'image/Drone.png').convert_alpha()
drone_get = False
drone_ing = False
drone_button = pygame.image.load(file_path + 'image/Drone button.png').convert_alpha()
x_drone = 0
y_drone = 0

tool_1 = pygame.image.load(file_path + 'image/Background/Levels background/Tool/Tool 2.png').convert_alpha()

player_speed = 10
player_x = 150
player_y = 250

table = pygame.image.load(file_path + 'image/Background/Table.png').convert_alpha()

key_button_up = pygame.image.load(file_path + 'image/Key button/up.png').convert_alpha()
key_button_down = pygame.image.load(file_path + 'image/Key button/down.png').convert_alpha()
key_button_left = pygame.image.load(file_path + 'image/Key button/left.png').convert_alpha()
key_button_right = pygame.image.load(file_path + 'image/Key button/right.png').convert_alpha()

slot_1 = pygame.image.load(file_path + 'image/Card slot lvl/1 lvl.png').convert_alpha()
slot_2 = pygame.image.load(file_path + 'image/Card slot lvl/2 lvl.png').convert_alpha()
slot_3 = pygame.image.load(file_path + 'image/Card slot lvl/3 lvl.png').convert_alpha()
slot_4 = pygame.image.load(file_path + 'image/Card slot lvl/4 lvl.png').convert_alpha()
slot_5 = pygame.image.load(file_path + 'image/Card slot lvl/5 lvl.png').convert_alpha()

yes_no = True

lvl_1_kard_location = False
lvl_2_kard_location = False
lvl_3_kard_location = False
lvl_4_kard_location = False
lvl_5_kard_location = False
kard_index = 0

reset_progress = pygame.image.load(file_path + 'image/Reset progress.png').convert_alpha()

def arrows_set(goal, key_x, key_y):
    screen.blit(corect_cancel, (45 + key_x, 124 + key_y))
    if goal == 'y':
        screen.blit(up_set, (45.9 + key_x, 46 + key_y))
        screen.blit(down_set, (45 + key_x, 85 + key_y))
        if event.type == pygame.MOUSEBUTTONDOWN:
            x, y = event.pos
            print(x, y)
            if (45.9 + key_x) < x < (82 + key_x) and (46 + key_y) < y < (82 + key_y):
                return -1
            elif (45 + key_x) < x < (82 + key_x) and (85 + key_y) < y < (120 + key_y):
                return 1
            elif (45 + key_x) < x < (85 + key_x) and (124 + key_y) < y < (160 + key_y):
                return 'cancel'
            else:
                return 0
    elif goal == 'x':
        screen.blit(left_set, (5 + key_x, 85 + key_y))
        screen.blit(right_set, (85 + key_x, 85 + key_y))
        if event.type == pygame.MOUSEBUTTONDOWN:
            x, y = event.pos
            print(x, y)
            if (5 + key_x) < x < (45 + key_x) and (85 + key_y) < y < (120 + key_y):
                return -1
            elif (85 + key_x) < x < (120 + key_x) and (85 + key_y) < y < (120 + key_y):
                return 1
            elif (45 + key_x) < x < (85 + key_x) and (124 + key_y) < y < (160 + key_y):
                return 'cancel'
            else:
                return 0
def blit_slot_1():
    screen.blit(slot_1, (10, 10))
    screen.blit(slot_1, (10, 50))
    screen.blit(slot_1, (10, 90))
    screen.blit(slot_1, (10, 130))
    screen.blit(slot_1, (10, 170))
    screen.blit(slot_1, (10, 210))
    screen.blit(slot_1, (10, 210))
    screen.blit(slot_1, (10, 250))
    screen.blit(slot_1, (10, 290))
    screen.blit(slot_1, (10, 330))
    screen.blit(slot_1, (50, 10))
    screen.blit(slot_1, (50, 50))
    screen.blit(slot_1, (50, 90))
    screen.blit(slot_1, (50, 130))
    screen.blit(slot_1, (50, 170))
    screen.blit(slot_1, (50, 210))
    screen.blit(slot_1, (50, 210))
    screen.blit(slot_1, (50, 250))
    screen.blit(slot_1, (50, 290))
    screen.blit(slot_1, (50, 330))
    screen.blit(slot_1, (90, 10))
    screen.blit(slot_1, (90, 50))
    screen.blit(slot_1, (90, 90))
    screen.blit(slot_1, (90, 130))
    screen.blit(slot_1, (90, 170))
    screen.blit(slot_1, (90, 210))
    screen.blit(slot_1, (90, 210))
    screen.blit(slot_1, (90, 250))
    screen.blit(slot_1, (90, 290))
    screen.blit(slot_1, (90, 330))
    screen.blit(slot_1, (130, 10))
    screen.blit(slot_1, (130, 50))
    screen.blit(slot_1, (130, 90))
    screen.blit(slot_1, (130, 130))
    screen.blit(slot_1, (130, 170))
    screen.blit(slot_1, (130, 210))
    screen.blit(slot_1, (130, 210))
    screen.blit(slot_1, (130, 250))
    screen.blit(slot_1, (130, 290))
    screen.blit(slot_1, (130, 330))
    screen.blit(slot_1, (170, 10))
    screen.blit(slot_1, (170, 50))
    screen.blit(slot_1, (170, 90))
    screen.blit(slot_1, (170, 130))
    screen.blit(slot_1, (170, 170))
    screen.blit(slot_1, (170, 210))
    screen.blit(slot_1, (170, 210))
    screen.blit(slot_1, (170, 250))
    screen.blit(slot_1, (170, 290))
    screen.blit(slot_1, (170, 330))
    screen.blit(slot_1, (210, 10))
    screen.blit(slot_1, (210, 50))
    screen.blit(slot_1, (210, 90))
    screen.blit(slot_1, (210, 130))
    screen.blit(slot_1, (210, 170))
    screen.blit(slot_1, (210, 210))
    screen.blit(slot_1, (210, 210))
    screen.blit(slot_1, (210, 250))
    screen.blit(slot_1, (210, 290))
    screen.blit(slot_1, (210, 330))
    screen.blit(slot_1, (250, 10))
    screen.blit(slot_1, (250, 50))
    screen.blit(slot_1, (250, 90))
    screen.blit(slot_1, (250, 130))
    screen.blit(slot_1, (250, 170))
    screen.blit(slot_1, (250, 210))
    screen.blit(slot_1, (250, 210))
    screen.blit(slot_1, (250, 250))
    screen.blit(slot_1, (250, 290))
    screen.blit(slot_1, (250, 330))
    screen.blit(slot_1, (290, 10))
    screen.blit(slot_1, (290, 50))
    screen.blit(slot_1, (290, 90))
    screen.blit(slot_1, (290, 130))
    screen.blit(slot_1, (290, 170))
    screen.blit(slot_1, (290, 210))
    screen.blit(slot_1, (290, 210))
    screen.blit(slot_1, (290, 250))
    screen.blit(slot_1, (290, 290))
    screen.blit(slot_1, (290, 330))
    screen.blit(slot_1, (330, 10))
    screen.blit(slot_1, (330, 50))
    screen.blit(slot_1, (330, 90))
    screen.blit(slot_1, (330, 130))
    screen.blit(slot_1, (330, 170))
    screen.blit(slot_1, (330, 210))
    screen.blit(slot_1, (330, 210))
    screen.blit(slot_1, (330, 250))
    screen.blit(slot_1, (330, 290))
    screen.blit(slot_1, (330, 330))
    screen.blit(slot_1, (370, 10))
    screen.blit(slot_1, (370, 50))
    screen.blit(slot_1, (370, 90))
    screen.blit(slot_1, (370, 130))
    screen.blit(slot_1, (370, 170))
    screen.blit(slot_1, (370, 210))
    screen.blit(slot_1, (370, 210))
    screen.blit(slot_1, (370, 250))
    screen.blit(slot_1, (370, 290))
    screen.blit(slot_1, (370, 330))
    screen.blit(slot_1, (410, 10))
    screen.blit(slot_1, (410, 50))
    screen.blit(slot_1, (410, 90))
    screen.blit(slot_1, (410, 130))
    screen.blit(slot_1, (410, 170))
    screen.blit(slot_1, (410, 210))
    screen.blit(slot_1, (410, 210))
    screen.blit(slot_1, (410, 250))
    screen.blit(slot_1, (410, 290))
    screen.blit(slot_1, (410, 330))
    screen.blit(slot_1, (450, 10))
    screen.blit(slot_1, (450, 50))
    screen.blit(slot_1, (450, 90))
    screen.blit(slot_1, (450, 130))
    screen.blit(slot_1, (450, 170))
    screen.blit(slot_1, (450, 210))
    screen.blit(slot_1, (450, 210))
    screen.blit(slot_1, (450, 250))
    screen.blit(slot_1, (450, 290))
    screen.blit(slot_1, (450, 330))
    screen.blit(slot_1, (490, 10))
    screen.blit(slot_1, (490, 50))
    screen.blit(slot_1, (490, 90))
    screen.blit(slot_1, (490, 130))
    screen.blit(slot_1, (490, 170))
    screen.blit(slot_1, (490, 210))
    screen.blit(slot_1, (490, 210))
    screen.blit(slot_1, (490, 250))
    screen.blit(slot_1, (490, 290))
    screen.blit(slot_1, (490, 330))
    screen.blit(slot_1, (530, 10))
    screen.blit(slot_1, (530, 50))
    screen.blit(slot_1, (530, 90))
    screen.blit(slot_1, (530, 130))
    screen.blit(slot_1, (530, 170))
    screen.blit(slot_1, (530, 210))
    screen.blit(slot_1, (530, 210))
    screen.blit(slot_1, (530, 250))
    screen.blit(slot_1, (530, 290))
    screen.blit(slot_1, (530, 330))
    screen.blit(slot_1, (570, 10))
    screen.blit(slot_1, (570, 50))
    screen.blit(slot_1, (570, 90))
    screen.blit(slot_1, (570, 130))
    screen.blit(slot_1, (570, 170))
    screen.blit(slot_1, (570, 210))
    screen.blit(slot_1, (570, 210))
    screen.blit(slot_1, (570, 250))
    screen.blit(slot_1, (570, 290))
    screen.blit(slot_1, (570, 330))

def number_keyboard(x_key, y_key): #in development
    screen.blit(button_0, (264+x_key, 281+y_key))
    screen.blit(button_1, (180+x_key, 50+y_key))
    screen.blit(button_2, (264+x_key, 50+y_key))
    screen.blit(button_3, (348+x_key, 50+y_key))
    screen.blit(button_4, (180+x_key, 127+y_key))
    screen.blit(button_5, (264+x_key, 127+y_key))
    screen.blit(button_6, (348+x_key, 127+y_key))
    screen.blit(button_7, (180+x_key, 204+y_key))
    screen.blit(button_8, (264+x_key, 204+y_key))
    screen.blit(button_9, (348+x_key, 204+y_key))
    screen.blit(number_canvas, (180+x_key, 10+y_key))
    if event.type == pygame.MOUSEBUTTONDOWN:
        x, y = event.pos
        if 264 < x < 345 and 281 < y < 355:
            time.sleep(2)
            return 0
        elif 180 < x < 260 and 50 < y < 123:
            time.sleep(2)
            return 1
        elif 264 < x < 345 and 50 < y < 123:
            time.sleep(2)
            return 2
        elif 348 < x < 429 and 50 < y < 123:
            time.sleep(2)
            return 3
        elif 180 < x < 260 and 127 < y < 200:
            time.sleep(2)
            return 4
        elif 264 < x < 345 and 127 < y < 200:
            return 5
        elif 348 < x < 429 and 127 < y < 200:
            time.sleep(2)
            return 6
        elif 180 < x < 260 and 204 < y < 277:
            time.sleep(2)
            return 7
        elif 264 < x < 345 and 204 < y < 277:
            time.sleep(2)
            return 8
        elif 348 < x < 429 and 204 < y < 277:
            time.sleep(2)
            return 9
        else:
            time.sleep(2)

running = True
while running:
    pygame.display.update()
    #show images on canvas
    if screen_game == 'menu': #_________________________
        screen.blit(background, (background_x + 0, 0))
        player_x = 150
        player_y = 250
        screen.blit(background, (background_x + 612, 0))
        screen.blit(walk_right[player_animation_count], (player_x, 250))
        screen.blit(button_start, (225, 75))
        screen.blit(name_of_game, (245, 25))
        screen.blit(button_set, (206.5, 140))
        screen.blit(button_exit, (3, 3))
        # exit meneger
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
                pygame.quit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    pygame.quit()
                    running = False
        if event.type == pygame.MOUSEBUTTONDOWN:
            x, y = event.pos
            if 3<x<53 and 3<y<24:
                #button exit
                if level_2_check == True:
                    game_info['level open'] = 2
                if level_3_check == True:
                    game_info['level open'] = 3
                if level_4_check == True:
                    game_info['level open'] = 4
                if level_5_check == True:
                    game_info['level open'] = 5
                if level_6_check == True:
                    game_info['level open'] = 6
                file = open(file_path + 'progress.json', 'w')
                json.dump(game_info, file)
                file.close()
                pygame.quit()
                running = False
            elif 207<x<394 and 140<y<187:
                screen_game = 'settings'
                time.sleep(0.2)
                #settings
                x, y = 0, 0
            elif 225 < x < 375 and 75 < y < 125:
                screen_game = 'play'
        if player_animation_count >= 3:
            player_animation_count = 0
        else:
            player_animation_count += 1
        if background_x == -612:
            background_x = 0
        else:
            background_x -= 2
    elif screen_game == 'play':
        pygame.display.update()
        screen.fill((5, 250, 250))
        if player_animation_count >= 3:
            player_animation_count = 0
        else:
            player_animation_count += 1
        if levels == 'choose':
            pygame.mixer.Sound.stop(step_sound)
            screen.blit(frame_of_levels, (140, 100))
            screen.blit(frame_of_levels, (290, 140))
            screen.blit(frame_of_levels, (430, 100))
            screen.blit(frame_of_levels, (140, 240))
            screen.blit(frame_of_levels, (430, 240))
            screen.blit(button_bake, (10, 10))
            l_1 = text_game.render('1', True, 'black')
            l_2 = text_game.render('2', True, 'black')
            l_3 = text_game.render('3', True, 'black')
            l_4 = text_game.render('4', True, 'black')
            l_5 = text_game.render('5', True, 'black')
            level_text = text_game.render('Рівень:', True, 'black')
            screen.blit(l_1, (159, 113))
            screen.blit(level_text, (280, 10))
            if level_2_check == True:
                screen.blit(l_2, (308, 153))
            if level_3_check == True:
                screen.blit(l_3, (448, 113))
            if level_4_check == True:
                screen.blit(l_4, (158, 252))
            if level_5_check == True:
                screen.blit(l_5, (448, 252))

            if event.type == pygame.MOUSEBUTTONDOWN:
                x_l_c, y_l_c = event.pos
                if 10 < x_l_c < 25 and 10 < y_l_c < 25:
                    screen_game = 'menu'
                elif 140 < x_l_c < 188 and 100 < y_l_c < 148:
                    kard_index = 0
                    levels = '1'
                    level_play = True
                    level_version = 1.0
                elif 290 < x_l_c < 338 and 140 < y_l_c < 188:
                    if level_2_check == True:
                        levels = '2'
                        kard_index = 1
                        level_play = True
                        level_version = 1.0
                        drone_get = True
                        lvl_1_kard_location = False
                elif 430 < x_l_c < 478 and 100 < y_l_c < 148:
                    if level_3_check == True:
                        levels = '3'
                        level_play = True
                        level_version = 1.0
                        kard_index = 0
                        drone_get = False
                        player_x = 0
                        player_y = 0
                elif 140 < x_l_c < 188 and 240 < y_l_c < 288:
                    if level_4_check == True:
                        levels = '4'
                        level_play = True
                        level_version = 1.0
                        kard_index = 0
                        player_x = 10
                        player_y = 10
                        key_button_down_check = False
                elif 430 < x_l_c < 477 and 240 < y_l_c < 287:
                    if level_5_check == True:
                        levels = '5'
                        level_play = True
                        level_version = 1.0
                        kard_index = 0
                        drone_get = False
                        player_x = 10
                        player_y = 10
                        key_button_left_check = False
        elif levels == '1':
            if level_version == 1.0:
                pygame.mixer.Sound.stop(background_sound)
                screen.blit(level_1_0, (0, 0))
                player_rect = stand.get_rect(topleft=(player_x, player_y))
                slot_1_rect = slot_1.get_rect(topleft=(3, 10))
                screen.blit(slot_1, (3, 10))
                text_level = text_game.render('Недопустима картка', True, 'black')
                drone_rect = drone.get_rect(topleft=(593, 10))
                if drone_get == False:
                    screen.blit(drone, (593, 10))
                    if player_rect.colliderect(drone_rect):
                        drone_get = True
                if lvl_1_kard_location == False:
                    lvl_1_kard_rect = lvl_1_kard.get_rect(topleft=(350, 245))
                    screen.blit(lvl_1_kard, (350, 245))
                    if player_rect.colliderect(lvl_1_kard_rect):
                        lvl_1_kard_location = True
                        if kard_index < 1:
                            kard_index = 1
                if player_rect.colliderect(slot_1_rect):
                    if kard_index >= 1:
                        level_version = 1.1
                    else:
                        screen.blit(text_level, (240, 10))
            elif level_version == 1.1:
                text_level = text_game.render('Недопустима картка', True, 'white')
                player_rect = stand.get_rect(topleft=(player_x, player_y))
                screen.blit(level_1_1, (0, 0))
                screen.blit(table, (246, 220))
                screen.blit(key_button_up, (0, 362))
                key_button_up_rect = key_button_up.get_rect(topleft=(0, 362))
                screen.blit(slot_2, (580, 10))
                slot_2_rect = slot_2.get_rect(topleft=(580, 10))
                if player_rect.colliderect(slot_2_rect):
                    if kard_index >= 2:
                        level_version = 1.2
                    else:
                        screen.blit(text_level, (240, 10))
                if drone_ing == True:
                    drone_rect = drone.get_rect(topleft=(x_drone, y_drone))
                else:
                    drone_rect = drone.get_rect(topleft=(player_x+10, player_y - 13))
                if lvl_2_kard_location == False:
                    if player_rect.colliderect(key_button_up_rect) or key_button_up_rect.colliderect(drone_rect):
                        screen.blit(lvl_2_kard, (280, 300))
                        lvl_2_kard_rect = lvl_2_kard.get_rect(topleft=(280, 300))
                        if player_rect.colliderect(lvl_2_kard_rect):
                            lvl_2_kard_location = True
                            if kard_index < 2:
                                kard_index = 2
                else:
                    lvl_2_kard_rect = lvl_2_kard.get_rect(topleft=(-10000, -10000))
            elif level_version == 1.2:
                screen.blit(level_1_2, (0, 0))
                if drone_ing == True:
                    drone_rect = drone.get_rect(topleft=(x_drone, y_drone))
                else:
                    drone_rect = drone.get_rect(topleft=(player_x+10, player_y - 13))
                lvl_3_kard_rect = lvl_3_kard.get_rect(topleft=(78, 175))
                if lvl_3_kard_rect.colliderect(drone_rect):
                    if lvl_3_kard_location == False:
                        lvl_3_kard_location = True
                        if kard_index < 3:
                            kard_index = 3
                if lvl_3_kard_location == False:
                    screen.blit(lvl_3_kard, (78, 175))
                screen.blit(slot_3, (3, 10))
                slot_3_rect = slot_3.get_rect(topleft=(3, 10))
                player_rect = stand.get_rect(topleft=(player_x, player_y))
                if player_rect.colliderect(slot_3_rect):
                    levels = 'choose'
                    background_sound.play(1000)
                    level_2_check = True
                    kard_index = 0
                    level_play = False
            id_kard_info = text_game.render('Kard ID: ' + str(kard_index), True, 'white')
            screen.blit(id_kard_info, (520, 3))
        elif levels == '2':
            if level_version == 1.0:
                pygame.mixer.Sound.stop(background_sound)
                screen.blit(slot_1, (106, 0))
                screen.blit(slot_1, (306, 0))
                screen.blit(slot_1, (506, 0))
                text_level = text_game.render('Яку геометричну фігуру вивчає покарана дитина?', True, 'white')
                text_level_1 = text_game.render('Квадрат', True, 'white')
                text_level_2 = text_game.render('Трикутник', True, 'white')
                text_level_3 = text_game.render('Кут', True, 'white')
                screen.blit(text_level, (90, 240))
                screen.blit(text_level_1, (106, 30))
                screen.blit(text_level_2, (306, 30))
                screen.blit(text_level_3, (506, 30))
                player_rect = stand.get_rect(topleft=(player_x, player_y))
                slot_1_rect_1 = slot_1.get_rect(topleft=(106, 0))
                slot_1_rect_2 = slot_1.get_rect(topleft=(306, 0))
                slot_1_rect_3 = slot_1.get_rect(topleft=(506, 0))
                if player_rect.colliderect(slot_1_rect_3):
                    level_version = 1.1
                    player_x = 250
                    player_y = 250
                elif player_rect.colliderect(slot_1_rect_1) or player_rect.colliderect(slot_1_rect_1):
                    level_version = 1.0
            elif level_version == 1.1:
                pygame.mixer.Sound.stop(background_sound)
                screen.blit(slot_1, (122.4, 0))
                screen.blit(slot_1, (244.8, 0))
                screen.blit(slot_1, (367.2, 0))
                screen.blit(slot_1, (489.6, 0))
                text_level = text_game.render('Як називається відрізок шляху довжиною 42км 195м?', True, 'white')
                text_level_1 = text_game.render('Орієнтований', True, 'white')
                text_level_2 = text_game.render('Сумірний', True, 'white')
                text_level_3 = text_game.render('Марафонський', True, 'white')
                text_level_4 = text_game.render('Прямий', True, 'white')
                screen.blit(text_level, (90, 240))
                screen.blit(text_level_1, (100.4, 30))
                screen.blit(text_level_2, (244.8, 30))
                screen.blit(text_level_3, (345.2, 30))
                screen.blit(text_level_4, (489.6, 30))
                player_rect = stand.get_rect(topleft=(player_x, player_y))
                slot_1_rect_1 = slot_1.get_rect(topleft=(122.4, 0))
                slot_1_rect_2 = slot_1.get_rect(topleft=(244.8, 0))
                slot_1_rect_3 = slot_1.get_rect(topleft=(367.2, 0))
                slot_1_rect_4 = slot_1.get_rect(topleft=(489.6, 0))
                if player_rect.colliderect(slot_1_rect_3):
                    level_version = 1.2
                    player_x = 250
                    player_y = 250
                elif player_rect.colliderect(slot_1_rect_1) or player_rect.colliderect(slot_1_rect_2) or player_rect.colliderect(slot_1_rect_4):
                    level_version = 1.0
            elif level_version == 1.2:
                pygame.mixer.Sound.stop(background_sound)
                screen.blit(slot_1, (122.4, 0))
                screen.blit(slot_1, (244.8, 0))
                screen.blit(slot_1, (367.2, 0))
                screen.blit(slot_1, (489.6, 0))
                text_level = text_game.render('Віднови ряд: 2, 32, 332, 33332.', True, 'white')
                text_level_1 = text_game.render('33332', True, 'white')
                text_level_2 = text_game.render('3322', True, 'white')
                text_level_3 = text_game.render('3232', True, 'white')
                text_level_4 = text_game.render('322', True, 'white')
                screen.blit(text_level, (90, 240))
                screen.blit(text_level_1, (100.4, 30))
                screen.blit(text_level_2, (244.8, 30))
                screen.blit(text_level_3, (345.2, 30))
                screen.blit(text_level_4, (489.6, 30))
                player_rect = stand.get_rect(topleft=(player_x, player_y))
                slot_1_rect_1 = slot_1.get_rect(topleft=(122.4, 0))
                slot_1_rect_2 = slot_1.get_rect(topleft=(244.8, 0))
                slot_1_rect_3 = slot_1.get_rect(topleft=(367.2, 0))
                slot_1_rect_4 = slot_1.get_rect(topleft=(489.6, 0))
                if player_rect.colliderect(slot_1_rect_1):
                    level_version = 1.3
                    player_x = 250
                    player_y = 250
                elif player_rect.colliderect(slot_1_rect_2) or player_rect.colliderect(
                    slot_1_rect_3) or player_rect.colliderect(slot_1_rect_4):
                    level_version = 1.0
            elif level_version == 1.3:
                pygame.mixer.Sound.stop(background_sound)
                screen.blit(slot_1, (122.4, 0))
                screen.blit(slot_1, (244.8, 0))
                screen.blit(slot_1, (367.2, 0))
                screen.blit(slot_1, (489.6, 0))
                text_level = text_game.render('У готелі 4 поверхи. Що вище поверх, то більше людей там мешкає. ', True, 'white')
                text_level_5 = text_game.render('На який поверх частіше їздить ліфт?', True, 'white')
                text_level_1 = text_game.render('1', True, 'white')
                text_level_2 = text_game.render('2', True, 'white')
                text_level_3 = text_game.render('3', True, 'white')
                text_level_4 = text_game.render('4', True, 'white')
                screen.blit(text_level, (50, 240))
                screen.blit(text_level_1, (100.4, 30))
                screen.blit(text_level_2, (244.8, 30))
                screen.blit(text_level_3, (345.2, 30))
                screen.blit(text_level_4, (489.6, 30))
                screen.blit(text_level_5, (90, 260))
                player_rect = stand.get_rect(topleft=(player_x, player_y))
                slot_1_rect_1 = slot_1.get_rect(topleft=(122.4, 0))
                slot_1_rect_2 = slot_1.get_rect(topleft=(244.8, 0))
                slot_1_rect_3 = slot_1.get_rect(topleft=(367.2, 0))
                slot_1_rect_4 = slot_1.get_rect(topleft=(489.6, 0))
                if player_rect.colliderect(slot_1_rect_1):
                    levels = 'choose'
                    background_sound.play(1000)
                    level_3_check = True
                    kard_index = 0
                    level_play = False
                elif player_rect.colliderect(slot_1_rect_2) or player_rect.colliderect(
                        slot_1_rect_3) or player_rect.colliderect(slot_1_rect_4):
                    level_version = 1.0
            id_kard_info = text_game.render('Kard ID: ' + str(kard_index), True, 'white')
            screen.blit(id_kard_info, (520, 3))
        elif levels == '3':
            pygame.mixer.Sound.stop(background_sound)
            if level_version == 1.0:
                screen.blit(wall_1, (100, wall_1_y))
                screen.blit(goal, (581, 183.5))
                screen.blit(text_game.render('Фініш->', True, 'black'), (510, 186))
                if wall_1_y >= 326:
                    wall_1_y_check = False
                elif wall_1_y <= 0:
                    wall_1_y_check = True
                if wall_1_y_check == True:
                    wall_1_y += 10
                elif wall_1_y_check == False:
                    wall_1_y -= 10

                screen.blit(wall_2, (200, wall_2_y))
                if wall_2_y >= 326:
                    wall_2_y_check = False
                elif wall_2_y <= 0:
                    wall_2_y_check = True
                if wall_2_y_check == True:
                    wall_2_y += 15
                elif wall_2_y_check == False:
                    wall_2_y -= 15

                screen.blit(wall_2, (300, wall_3_y))
                if wall_3_y >= 326:
                    wall_3_y_check = False
                elif wall_3_y <= 0:
                    wall_3_y_check = True
                if wall_3_y_check == True:
                    wall_3_y += 20
                elif wall_3_y_check == False:
                    wall_3_y -= 20

                screen.blit(wall_2, (400, wall_4_y))
                if wall_4_y >= 310:
                    wall_4_y_check = False
                elif wall_4_y <= 0:
                    wall_4_y_check = True
                if wall_4_y_check == True:
                    wall_4_y += 30
                elif wall_3_y_check == False:
                    wall_4_y -= 30
                player_rect = stand.get_rect(topleft=(player_x, player_y))
                wall_1_rect = wall_1.get_rect(topleft=(100, wall_1_y))
                wall_2_rect = wall_2.get_rect(topleft=(200, wall_2_y))
                wall_3_rect = wall_3.get_rect(topleft=(300, wall_3_y))
                wall_4_rect = wall_4.get_rect(topleft=(400, wall_4_y))
                goal_rect = goal.get_rect(topleft=(581, 183.5))
                if player_rect.colliderect(wall_1_rect):
                    screen.blit(player_death, (player_x, player_y))
                    player_x = 0
                    player_y = 0
                if player_rect.colliderect(wall_2_rect):
                    screen.blit(player_death, (player_x, player_y))
                    player_x = 0
                    player_y = 0
                if player_rect.colliderect(wall_3_rect):
                    screen.blit(player_death, (player_x, player_y))
                    player_x = 0
                    player_y = 0
                if player_rect.colliderect(wall_4_rect):
                    screen.blit(player_death, (player_x, player_y))
                    player_x = 0
                    player_y = 0
                if player_rect.colliderect(goal_rect):
                    levels = 'choose'
                    background_sound.play(1000)
                    level_4_check = True
                    kard_index = 0
                    level_play = False
                    pygame.mixer.Sound.stop(step_sound)


        elif levels == '4':
            pygame.mixer.Sound.stop(background_sound)
            if level_version == 1.0:
                screen.blit(common_wall_antibug, (113, 117))
                screen.blit(goal, (581, 0))
                screen.blit(common_wall, (100, 100))
                screen.blit(key_button_down, (380, 0))
                screen.blit(laser_circle, (100, 50))
                screen.blit(laser_circle_1, (185, 8))
                line_laser = pygame.transform.scale(line_laser, (300, 10))
                screen.blit(line_laser, (250, 97))
                line_laser_rect = line_laser.get_rect(topleft=(250, 98))
                line_laser_2 = line_laser
                line_laser_2 = pygame.transform.scale(line_laser_2, (300, 32))
                screen.blit(line_laser_2, (250, 262))
                line_laser_2_rect = line_laser_2.get_rect(topleft=(250, 272))
                line_laser_4 = line_laser
                line_laser_4 = pygame.transform.scale(line_laser_4, (500, 32))
                screen.blit(line_laser_4, (335, 180))
                line_laser_4_rect = line_laser_4.get_rect(topleft=(300, 200))
                line_laser_v2 = pygame.transform.scale(line_laser, (5, 225))
                screen.blit(line_laser_v2, (450, -75))
                line_laser_v2_rect = line_laser_v2.get_rect(topleft=(450, -100))
                laser_circle_rect = laser_circle.get_rect(topleft=(100, 50))
                laser_circle_1_rect = laser_circle_1.get_rect(topleft=(185, 8))
                common_wall_rect = common_wall.get_rect(topleft=(100, 100))
                player_rect = stand.get_rect(topleft=(player_x, player_y))
                common_wall_antibug_rect = common_wall_antibug.get_rect(topleft=(113, 117))
                key_button_down_rect = key_button_down.get_rect(topleft=(380, 0))
                goal_rect = goal.get_rect(topleft=(581, 0))
                if key_button_down_check == False:
                    screen.blit(laser_circle_2, (100, 300))
                    laser_circle_2_rect = laser_circle_2.get_rect(topleft=(100, 300))
                    if player_rect.colliderect(laser_circle_2_rect):
                        screen.blit(player_death, (player_x, player_y))
                        player_x = 10
                        player_y = 10
                        key_button_down_check = False
                if player_rect.colliderect(key_button_down_rect):
                    key_button_down_check = True
                if player_rect.colliderect(common_wall_rect):
                    if up_check == True:
                        player_y += 11
                    if down_check == True:
                        player_y -= 11
                    if right_check == True:
                        player_x -= 11
                    if left_check == True:
                        player_x += 11
                if player_rect.colliderect(line_laser_v2_rect):
                    screen.blit(player_death, (player_x, player_y))
                    player_x = 10
                    player_y = 10
                    key_button_down_check = False
                if player_rect.colliderect(common_wall_antibug_rect):
                    screen.blit(player_death, (player_x, player_y))
                    player_x = 10
                    player_y = 10
                    key_button_down_check = False
                if player_rect.colliderect(laser_circle_rect):
                    screen.blit(player_death, (player_x, player_y))
                    player_x = 10
                    player_y = 10
                    key_button_down_check = False
                if player_rect.colliderect(laser_circle_1_rect):
                    screen.blit(player_death, (player_x, player_y))
                    player_x = 10
                    player_y = 10
                    key_button_down_check = False
                if player_rect.colliderect(line_laser_rect):
                    screen.blit(player_death, (player_x, player_y))
                    player_x = 10
                    player_y = 10
                    key_button_down_check = False
                if player_rect.colliderect(line_laser_2_rect):
                    screen.blit(player_death, (player_x, player_y))
                    player_x = 10
                    player_y = 10
                    key_button_down_check = False
                if player_rect.colliderect(goal_rect) and key_button_down_check == True:
                    levels = 'choose'
                    background_sound.play(1000)
                    level_5_check = True
                    kard_index = 0
                    level_play = False
                    pygame.mixer.Sound.stop(step_sound)


        elif levels == '5':
            pygame.mixer.Sound.stop(background_sound)
            if level_version == 1.0:
                screen.blit(wall_1, (100, wall_1_y))
                wall_1_rect = wall_1.get_rect(topleft=(100, wall_1_y))
                wall_2 = wall_1
                screen.blit(wall_2, (wall_2_x, 100))
                wall_2_rect = wall_2.get_rect(topleft=(wall_2_x, 100))
                wall_3 = wall_1
                screen.blit(wall_3, (wall_3_x, 240))
                wall_3_rect = wall_3.get_rect(topleft=(wall_3_x, 240))
                wall_4 = wall_1
                screen.blit(wall_3, (270, wall_4_y))
                wall_4_rect = wall_4.get_rect(topleft=(270, wall_4_y))
                screen.blit(common_wall_antibug, (113, 117))
                screen.blit(common_wall, (100, 100))
                common_wall_rect = common_wall.get_rect(topleft=(100, 100))
                common_wall_2 = common_wall
                common_wall_antibug_2 = common_wall_antibug
                screen.blit(common_wall_antibug_2, (257, 117))
                screen.blit(common_wall_2, (244, 100))
                player_rect = stand.get_rect(topleft=(player_x, player_y))
                common_wall_antibug_rect = common_wall_antibug.get_rect(topleft=(113, 117))
                common_wall_2_rect = common_wall_2.get_rect(topleft=(244, 100))
                common_wall_antibug_2_rect = common_wall_antibug.get_rect(topleft=(257, 117))
                screen.blit(goal, (581, 0))
                goal_rect = goal.get_rect(topleft=(581, 0))
                line_laser = pygame.transform.scale(line_laser, (300, 10))
                screen.blit(line_laser, (320, 97))
                line_laser_rect = line_laser.get_rect(topleft=(320, 98))
                line_laser_2 = line_laser
                line_laser_2 = pygame.transform.scale(line_laser_2, (300, 10))
                screen.blit(line_laser_2, (470, 197))
                line_laser_2_rect = line_laser_2.get_rect(topleft=(470, 197))
                line_laser_3 = line_laser
                line_laser_3 = pygame.transform.scale(line_laser_3, (180, 10))
                screen.blit(line_laser_3, (370, 272))
                line_laser_3_rect = line_laser_3.get_rect(topleft=(370, 272))
                if key_button_left_check == False:
                    screen.blit(laser_circle, (100, 25))
                    laser_circle_rect = laser_circle.get_rect(topleft=(100, 25))
                    if player_rect.colliderect(laser_circle_rect):
                        screen.blit(player_death, (player_x, player_y))
                        player_x = 10
                        player_y = 10
                        key_button_up_check = False
                screen.blit(key_button_left, (600, 150))
                key_button_left_rect = key_button_left.get_rect(topleft=(600, 150))
                if wall_1_y >= 326:
                    wall_1_y_check = False
                elif wall_1_y <= 200:
                    wall_1_y_check = True
                if wall_1_y_check == True:
                    wall_1_y += 10
                elif wall_1_y_check == False:
                    wall_1_y -= 10
                if wall_2_x >= 125:
                    wall_2_x_check = False
                elif wall_2_x <= 0:
                    wall_2_x_check = True
                if wall_2_x_check == True:
                    wall_2_x += 10
                elif wall_2_x_check == False:
                    wall_2_x -= 10
                if wall_3_x >= 125:
                    wall_3_x_check = False
                elif wall_3_x <= 0:
                    wall_3_x_check = True
                if wall_3_x_check == True:
                    wall_3_x += 10
                elif wall_3_x_check == False:
                    wall_3_x -= 10
                if wall_4_y >= 326:
                    wall_4_y_check = False
                elif wall_4_y <= 200:
                    wall_4_y_check = True
                if wall_4_y_check == True:
                    wall_4_y += 10
                elif wall_4_y_check == False:
                    wall_4_y -= 10
                if key_button_left_check == True:
                    wall_5 = wall_1
                    wall_5 = pygame.transform.scale(wall_5, (100, 80))
                    screen.blit(wall_5, (wall_5_x, 10))
                    wall_5_rect = wall_5.get_rect(topleft=(wall_5_x, 10))
                    if wall_5_x >= 405:
                        wall_5_x_check = False
                    elif wall_5_x <= -175:
                        wall_5_x_check = True
                    if wall_5_x_check == True:
                        wall_5_x += 11
                    elif wall_5_x_check == False:
                        wall_5_x -= 11
                    if player_rect.colliderect(wall_5_rect):
                        screen.blit(player_death, (player_x, player_y))
                        player_x = 10
                        player_y = 10
                        key_button_left_check = False
                if player_rect.colliderect(key_button_left_rect):
                    key_button_left_check = True
                if player_rect.colliderect(wall_2_rect):
                    screen.blit(player_death, (player_x, player_y))
                    player_x = 10
                    player_y = 10
                    key_button_left_check = False
                if player_rect.colliderect(wall_4_rect):
                    screen.blit(player_death, (player_x, player_y))
                    player_x = 10
                    player_y = 10
                    key_button_left_check = False
                if player_rect.colliderect(line_laser_2_rect):
                    screen.blit(player_death, (player_x, player_y))
                    player_x = 10
                    player_y = 10
                    key_button_left_check = False
                if player_rect.colliderect(line_laser_3_rect):
                    screen.blit(player_death, (player_x, player_y))
                    player_x = 10
                    player_y = 10
                    key_button_left_check = False
                if player_rect.colliderect(wall_3_rect):
                    screen.blit(player_death, (player_x, player_y))
                    player_x = 10
                    player_y = 10
                    key_button_left_check = False
                if player_rect.colliderect(common_wall_antibug_rect):
                    screen.blit(player_death, (player_x, player_y))
                    player_x = 10
                    player_y = 10
                    key_button_left_check = False
                if player_rect.colliderect(common_wall_2_rect) or player_rect.colliderect(common_wall_rect):
                    if up_check == True:
                        player_y += 11
                    if down_check == True:
                        player_y -= 11
                    if right_check == True:
                        player_x -= 11
                    if left_check == True:
                        player_x += 11
                    player_speed = 10
                if player_rect.colliderect(wall_1_rect):
                    screen.blit(player_death, (player_x, player_y))
                    player_x = 10
                    player_y = 10
                    key_button_left_check = False
                if player_rect.colliderect(line_laser_rect):
                    screen.blit(player_death, (player_x, player_y))
                    player_x = 10
                    player_y = 10
                    key_button_left_check = False
                if player_rect.colliderect(common_wall_antibug_2_rect):
                    screen.blit(player_death, (player_x, player_y))
                    player_x = 10
                    player_y = 10
                    key_button_left_check = False
                if player_rect.colliderect(goal_rect) and key_button_left_check == True:
                    screen.blit(completed_game_screen, (0, 0))
                    screen.blit(button_exit, (548, 3))
                    drone_get = False
                    level_play = False
                    game_info['level open'] = 5
                    background_sound.play(1000)
                    kard_index = 0
                    pygame.mixer.Sound.stop(step_sound)
                    if event.type == pygame.MOUSEBUTTONDOWN:
                        x_com, y_com = event.pos
                        if 548 < x_com < 598 and 3 < y_com < 24:
                            screen_game = 'menu'
                            level_play = True

        if pause_use == True:
            screen.blit(pause_icon_use, (300, 0))
            if event.type == pygame.MOUSEBUTTONDOWN:
                x_pause, y_pause = event.pos
                if 300 < x_pause < 320 and 0 < y_pause < 18:
                    pause_use = False
                    player_x = player_x_pause
                    player_y = player_y_pause
                    level_version = level_version_pause
                    level_play = True
                    levels = levels_pause
                    pygame.mixer.Sound.stop(background_sound)
        if level_play == True:
            keys = pygame.key.get_pressed()
            if key_mode == 'touch':
                if event.type == pygame.MOUSEBUTTONDOWN:
                    x, y = event.pos
                    if variant == '1':
                        if 450 < x < 525 and 205 < y < 275 and player_y >= 4:
                            screen.blit(walk_up[player_animation_count], (player_x, player_y))
                            player_y -= player_speed
                            step_sound.play()
                            button_press = False
                            up_check = True
                        elif 450 < x < 525 and 280 < y < 355 and player_y < 315:
                            screen.blit(walk_down[player_animation_count], (player_x, player_y))
                            player_y += player_speed
                            step_sound.play()
                            button_press = False
                            down_check = True
                        elif 530 < x < 605 and 280 < y < 355 and player_x < 575:
                            screen.blit(walk_right[player_animation_count], (player_x, player_y))
                            player_x += player_speed
                            step_sound.play()
                            button_press = False
                            right_check = True
                        elif 370 < x < 445 and 280 < y < 355 and player_x > 0:
                            screen.blit(walk_left[player_animation_count], (player_x, player_y))
                            player_x -= player_speed
                            step_sound.play()
                            button_press = False
                            left_check = True
                        else:
                            screen.blit(stand, (player_x, player_y))
                            pygame.mixer.Sound.stop(step_sound)
                            button_press = True
                            up_check = False
                            down_check = False
                            right_check = False
                            left_check = False
                    elif variant == '2':
                        if 530 < x < 605 and 280 < y < 355 and player_x < 575:
                            screen.blit(walk_right[player_animation_count], (player_x, player_y))
                            player_x += player_speed
                            step_sound.play()
                            button_press = False
                            right_check = True
                        elif 450 < x < 525 and 280 < y < 355 and player_x > 0:
                            screen.blit(walk_left[player_animation_count], (player_x, player_y))
                            player_x -= player_speed
                            step_sound.play()
                            button_press = False
                            left_check = True
                        elif 3 < x < 78 and 3 < y < 77 and player_y >= 4:
                            screen.blit(walk_up[player_animation_count], (player_x, player_y))
                            player_y -= player_speed
                            step_sound.play()
                            button_press = False
                            up_check = True
                        elif 3 < x < 80 and 280 < y < 355 and player_y < 315:
                            screen.blit(walk_down[player_animation_count], (player_x, player_y))
                            player_y += player_speed
                            step_sound.play()
                            button_press = False
                            down_check = True
                        else:
                            screen.blit(stand, (player_x, player_y))
                            pygame.mixer.Sound.stop(step_sound)
                            button_press = True
                            up_check = False
                            down_check = False
                            right_check = False
                            left_check = False

                    elif variant == '3':
                        if 82 < x < 157 and 203 < y < 277 and player_y >= 4:
                            screen.blit(walk_up[player_animation_count], (player_x, player_y))
                            player_y -= player_speed
                            step_sound.play()
                            button_press = False
                            up_check = True
                        elif 82 < x < 158 and 280 < y < 355 and player_y < 315:
                            screen.blit(walk_down[player_animation_count], (player_x, player_y))
                            player_y += player_speed
                            step_sound.play()
                            button_press = False
                            down_check = True
                        elif 3 < x < 80 and 280 < y < 355 and player_x > 0:
                            screen.blit(walk_left[player_animation_count], (player_x, player_y))
                            player_x -= player_speed
                            step_sound.play()
                            button_press = False
                            left_check = True
                        elif 161 < x < 235 and 280 < y < 355 and player_x < 575:
                            screen.blit(walk_right[player_animation_count], (player_x, player_y))
                            player_x += player_speed
                            step_sound.play()
                            button_press = False
                            right_check = True
                        else:
                            screen.blit(stand, (player_x, player_y))
                            pygame.mixer.Sound.stop(step_sound)
                            button_press = True
                            up_check = False
                            down_check = False
                            right_check = False
                            left_check = False
                    elif variant == '4':
                        if 530 < x < 605 and 280 < y < 355 and player_x < 575:
                            screen.blit(walk_right[player_animation_count], (player_x, player_y))
                            player_x += player_speed
                            step_sound.play()
                            button_press = False
                            right_check = True
                        elif 450 < x < 525 and 280 < y < 355 and player_x > 0:
                            screen.blit(walk_left[player_animation_count], (player_x, player_y))
                            player_x -= player_speed
                            step_sound.play()
                            button_press = False
                            left_check = True
                        elif 3 < x < 80 and 280 < y < 355 and player_y < 315:
                            screen.blit(walk_down[player_animation_count], (player_x, player_y))
                            player_y += player_speed
                            step_sound.play()
                            button_press = False
                            down_check = True
                        elif 3 < x < 78 and 203 < y < 277 and player_y >= 4:
                            screen.blit(walk_up[player_animation_count], (player_x, player_y))
                            player_y -= player_speed
                            step_sound.play()
                            button_press = False
                            up_check = True
                        else:
                            screen.blit(stand, (player_x, player_y))
                            pygame.mixer.Sound.stop(step_sound)
                            button_press = True
                            up_check = False
                            down_check = False
                            right_check = False
                            left_check = False
                    elif variant == '5':
                        if 3 < x < 80 and 280 < y < 355 and player_x > 0:
                            screen.blit(walk_left[player_animation_count], (player_x, player_y))
                            player_x -= player_speed
                            step_sound.play()
                            button_press = False
                            left_check = True
                        elif 530 < x < 605 and 280 < y < 355 and player_y < 315:
                            screen.blit(walk_down[player_animation_count], (player_x, player_y))
                            player_y += player_speed
                            step_sound.play()
                            button_press = False
                            down_check = True
                        elif 529 < x < 604 and 203 < y < 278 and player_y >= 4:
                            screen.blit(walk_up[player_animation_count], (player_x, player_y))
                            player_y -= player_speed
                            step_sound.play()
                            button_press = False
                            up_check = True
                        elif 82 < x < 155 and 280 < y < 354 and player_x < 575:
                            screen.blit(walk_right[player_animation_count], (player_x, player_y))
                            player_x += player_speed
                            step_sound.play()
                            button_press = False
                            right_check = True
                        else:
                            screen.blit(stand, (player_x, player_y))
                            pygame.mixer.Sound.stop(step_sound)
                            button_press = True
                            up_check = False
                            down_check = False
                            right_check = False
                            left_check = False

                else:
                    screen.blit(stand, (player_x, player_y))
                    pygame.mixer.Sound.stop(step_sound)
                    up_check = False
                    down_check = False
                    right_check = False
                    left_check = False

                screen.blit(pl_button_up, (pl_button_up_x, pl_button_up_y))
                screen.blit(pl_button_down, (pl_button_down_x, pl_button_down_y))
                screen.blit(pl_button_right, (pl_button_right_x, pl_button_right_y))
                screen.blit(pl_button_left, (pl_button_left_x, pl_button_left_y))
            elif key_mode == 'keyboard':
                if keys[pygame.K_a] and player_x > 0:
                    screen.blit(walk_left[player_animation_count], (player_x, player_y))
                    player_x -= player_speed
                    step_sound.play()
                    left_check = True
                elif keys[pygame.K_d] and player_x < 575:
                    screen.blit(walk_right[player_animation_count], (player_x, player_y))
                    player_x += player_speed
                    step_sound.play()
                    right_check = True
                elif keys[pygame.K_w] and player_y >= 4:
                    screen.blit(walk_up[player_animation_count], (player_x, player_y))
                    player_y -= player_speed
                    step_sound.play()
                    up_check = True
                elif keys[pygame.K_s] and player_y < 315:
                    screen.blit(walk_down[player_animation_count], (player_x, player_y))
                    player_y += player_speed
                    step_sound.play()
                    down_check = True
                else:
                    screen.blit(stand, (player_x, player_y))
                    pygame.mixer.Sound.stop(step_sound)
                    up_check = False
                    down_check = False
                    right_check = False
                    left_check = False
            if level_play == True:
                if pause_use == False:
                    screen.blit(pause_icon, (320, 340))
                    if event.type == pygame.MOUSEBUTTONDOWN:
                        x_pause, y_pause = event.pos
                        if 320 < x_pause < 341 and 340 < y_pause < 359:
                            pause_use = True
                            player_x_pause = player_x
                            player_y_pause = player_x
                            level_version_pause = level_version
                            level_play_pause = level_play
                            level_play = False
                            levels_pause = levels
                            levels = 'choose'
                            pygame.mixer.Sound.play(background_sound, 10000000)
            if drone_get == True:
                    if key_mode == 'keyboard':
                        if keys[pygame.K_f]:
                            if drone_ing == False:
                                if event.type == pygame.MOUSEBUTTONDOWN:
                                    x_drone, y_drone = event.pos
                                    drone_ing = True
                            elif drone_ing == True:
                                if keys[pygame.K_SPACE]:
                                    drone_ing = False
                        if drone_ing == False:
                            screen.blit(drone, (player_x + 10, player_y - 13))
                        elif drone_ing == True:
                            screen.blit(drone, (x_drone, y_drone))
                    elif key_mode == 'touch':
                        if drone_ing == True:
                            if event.type == pygame.MOUSEBUTTONDOWN:
                                if button_press == True:
                                    x_drone, y_drone = event.pos
                            screen.blit(drone, (x_drone, y_drone))
                        elif drone_ing == False:
                            screen.blit(drone, (player_x + 10, player_y - 13))
                            screen.blit(drone_button, (280, 340))
                        if event.type == pygame.MOUSEBUTTONDOWN:
                            x_1drone, y_1drone = event.pos
                            if drone_ing == False:
                                if 280 < x_1drone < 304 and 340 < y_1drone < 362:
                                    drone_ing = True
                            elif drone_ing == True:
                                if player_x < x_1drone < player_x + 32 and player_y < y_1drone < player_y + 48:
                                    drone_ing = False

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
                pygame.quit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    pygame.quit()
                    running = False


    elif screen_game == 'settings': #_____________________
        pygame.display.update()
        screen.fill(('white'))
        #screen.blit(upgrade_icon, (6, 125))
        screen.blit(button_bake, (580, 10))
        #screen.blit(Icon_skins, (3, 200))
        screen.blit(my_avatar, (3, 300))
        screen.blit(author, (70, 321))
        screen.blit(set_buttons_button, (190, 100))
        screen.blit(progress_text, (40, 3))
        screen.blit(reset_progress, (535, 294))
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
                pygame.quit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    pygame.quit()
                    running = False
        if event.type == pygame.MOUSEBUTTONDOWN:
            x, y = event.pos
            if 580 < x < 596 and 10 < y < 23:
                time.sleep(0.2)
                screen_game = 'menu'
            elif 535 < x < 610 and 294 < y < 363:
                game_info['level open'] = 1
                game_info['version button'] = 1
                game_info['mode button'] = 'touch'
                file = open('progress.json', 'w')
                json.dump(game_info, file)
                file.close()
                running = False
                pygame.quit()
            elif 191 < x < 421 and 100 < y < 132:
                time.sleep(0.2)
                walk_button_up = True
                walk_button_down = 0
                walk_button_left = 0
                walk_button_right = 0
                screen_game = 'settings_buttons'
                variant_buttons = 'None'
                x, y = 0, 0
            #elif 10 < x < 58 and 127 < y < 175:
                #time.sleep(0.2)
                #screen_game = 'upgrade_player'
            #elif 10 < x < 61 and 210 < y < 255:
                #time.sleep(0.2)
                #screen_game = 'set_skin_player'
    elif screen_game == 'settings_buttons':
        x, y = 0, 0
        pygame.display.update()
        v_1 = text_game.render('1', True, 'black')
        v_2 = text_game.render('2', True, 'black')
        v_3 = text_game.render('3', True, 'black')
        v_4 = text_game.render('4', True, 'black')
        v_5 = text_game.render('5', True, 'black')
        variant_text = text_game.render('Варіант:', True, 'black')
        screen.fill((87, 206, 230))
        if key_mode == 'touch':
            screen.blit(keyboard_mode, (220, 200))
            pidkaska_4 = text_game.render('Щоб забрати дрон нажміть по персонажу', True, 'black')
            screen.blit(pidkaska_4, (100, 100))
            screen.blit(pl_button_down, (pl_button_down_x, pl_button_down_y))
            screen.blit(pl_button_left, (pl_button_left_x, pl_button_left_y))
            screen.blit(pl_button_right, (pl_button_right_x, pl_button_right_y))
            screen.blit(pl_button_up, (pl_button_up_x, pl_button_up_y))
            screen.blit(v_1, (240, 10))
            screen.blit(v_2, (280, 10))
            screen.blit(v_3, (320, 10))
            screen.blit(v_4, (360, 10))
            screen.blit(v_5, (400, 10))
            screen.blit(variant_text, (150, 10))
            if event.type == pygame.MOUSEBUTTONDOWN:
                x, y = event.pos
                if 10 < x < 25 and 10 < y < 25:
                    screen_game = 'settings'
                elif 240 < x < 250 and 10 < y < 30:
                    variant = '1'
                elif 280 < x < 295 and 10 < y < 30:
                    variant = '2'
                elif 320 < x < 335 and 10 < y < 30:
                    variant = '3'
                elif 360 < x < 380 and 10 < y < 30:
                    variant = '4'
                elif 400 < x < 415 and 10 < y < 30:
                    variant = '5'
                elif 220 < x < 390 and 200 < y < 220:
                    key_mode = 'keyboard'
                    game_info['mode button'] = 'keyboard'
                if variant == '1':
                    game_info['version button'] = 1
                    pl_button_up_x = 450
                    pl_button_up_y = 203
                    pl_button_down_x = 450
                    pl_button_down_y = 280
                    pl_button_right_x = 529
                    pl_button_right_y = 280
                    pl_button_left_x = 371
                    pl_button_left_y = 280
                elif variant == '2':
                    game_info['version button'] = 2
                    pl_button_up_x = 3
                    pl_button_up_y = 3
                    pl_button_left_x = 450
                    pl_button_left_y = 280
                    pl_button_right_x = 529
                    pl_button_right_y = 280
                    pl_button_down_x = 3
                    pl_button_down_y = 280
                elif variant == '3':
                    game_info['version button'] = 3
                    pl_button_left_x = 3
                    pl_button_left_y = 280
                    pl_button_down_x = 82
                    pl_button_down_y = 280
                    pl_button_up_x = 82
                    pl_button_up_y = 203
                    pl_button_right_x = 161
                    pl_button_right_y = 280
                elif variant == '4':
                    game_info['version button'] = 4
                    pl_button_up_x = 3
                    pl_button_up_y = 203
                    pl_button_down_x = 3
                    pl_button_down_y = 280
                    pl_button_left_x = 450
                    pl_button_left_y = 280
                    pl_button_right_x = 529
                    pl_button_right_y = 280
                elif variant == '5':
                    game_info['version button'] = 5
                    pl_button_up_x = 529
                    pl_button_up_y = 203
                    pl_button_down_x = 529
                    pl_button_down_y = 280
                    pl_button_left_x = 3
                    pl_button_left_y = 280
                    pl_button_right_x = 82
                    pl_button_right_y = 280
        elif key_mode == 'keyboard':
            pidkaska = text_game.render('Клавіши W,S,D,A - для руху', True, 'black')
            pidkaska_1 = text_game.render('Для керуванням дроном нажміть F', True, 'black')
            pidkaska_2 = text_game.render('Потім клацніть де хочете', True, 'black')
            pidkaska_3 = text_game.render('Щоб забрати дрон нажміть F і пробіл', True, 'black')
            screen.blit(touch_mode, (220, 330))
            screen.blit(pidkaska, (0, 20))
            screen.blit(pidkaska_1, (0, 40))
            screen.blit(pidkaska_2, (0, 65))
            screen.blit(pidkaska_3, (0, 85))
            if event.type == pygame.MOUSEBUTTONDOWN:
                x, y = event.pos
                if 10 < x < 25 and 10 < y < 25:
                    screen_game = 'settings'
                elif 220 < x < 390 and 330 < y < 350:
                    key_mode = 'touch'
                    game_info['mode button'] = 'touch'
        screen.blit(button_bake, (10, 10))
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
                pygame.quit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    pygame.quit()
                    running = False
    #elif screen_game == 'upgrade_player':
        #pygame.display.update()
        #screen.fill((87, 206, 230))
        #for event in pygame.event.get():
            #if event.type == pygame.QUIT:
                #running = False
                #pygame.quit()
            #if event.type == pygame.KEYDOWN:
                #if event.key == pygame.K_ESCAPE:
                    #pygame.quit()
                    #running = False
    #elif screen_game == 'set_skin_player':
        #pygame.display.update()
        #screen.fill((87, 206, 230))
        #screen.blit(player_skin, (10, 10))
        #screen.blit(button_bake, (10, 340))
        #for event in pygame.event.get():
            #if event.type == pygame.QUIT:
                #running = False
                #pygame.quit()
            #if event.type == pygame.KEYDOWN:
                #if event.key == pygame.K_ESCAPE:
                    #pygame.quit()
                    #running = False
        #if event.type == pygame.MOUSEBUTTONDOWN:
            #x, y = event.pos
            #if 10 < x < 25 and 340 < y < 353:
                #screen_game = 'settings'
    clock.tick(10)