import pygame
import math
from pygame.locals import *
pygame.init()
pygame.mixer.music.set_volume(0.1)
# GÁN BIẾN MÀN HÌNH
WIDTH, HEIGHT = 600, 800 
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("EcoHero")
# MÀU SẮC
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
BROWN = (139, 69, 19) 
#CHỈNH FONT
font = pygame.font.Font(None, 36) 
score = 0
#UPLOAD SOUND
pop = pygame.mixer.Sound("pop.mp3")
winsound = pygame.mixer.Sound("winsound.mp3")
failedsound = pygame.mixer.Sound("failedsound.wav")
water = pygame.mixer.Sound("watersound.wav")
thunder = pygame.mixer.Sound("thunder.wav")
rainbow = pygame.mixer.Sound("rainbow.wav")
main_menu_sound = pygame.mixer.Sound("main_menu.mp3")
#UPLOAD NHÂN VẬT
zeen = pygame.image.load('zeencau.png')
zeen = pygame.transform.scale(zeen, (125, 147))
#UPLOAD MÀN HÌNH
bg_default = pygame.image.load('default.png')
bg_default = pygame.transform.scale(bg_default, (WIDTH, HEIGHT))
lose = pygame.image.load('lose.png')
win = pygame.image.load('win.png')
main_menu = pygame.image.load('mainmenu.JPG')
main_menu = pygame.transform.scale(main_menu, (WIDTH, HEIGHT))
end_game = pygame.image.load('overallscore.JPG')
end_game = pygame.transform.scale(end_game, (WIDTH, HEIGHT))
#UPLOAD VẬT PHẨM
ao = pygame.image.load('ao.png')
ao = pygame.transform.scale(ao, (60,60))
ca1 = pygame.image.load('ca1.png')
ca1 = pygame.transform.scale(ca1, (50, 50))
caheo = pygame.image.load('caheo.png')
caheo = pygame.transform.scale(caheo, (100, 90))
chainhua = pygame.image.load('chainhua.png')
chainhua = pygame.transform.scale(chainhua, (70, 70))
chuoi = pygame.image.load('chuoi.png')
chuoi = pygame.transform.scale(chuoi, (50, 50))
ca2 = pygame.image.load('ca2.png')
ca2 = pygame.transform.scale(ca2, (70, 70))
rua = pygame.image.load('rua.png')
rua = pygame.transform.scale(rua, (70, 70))
tao = pygame.image.load('tao.png')
tao = pygame.transform.scale(tao, (50, 50))
kimtiem = pygame.image.load('kimtiem.png')
kimtiem = pygame.transform.scale(kimtiem, (100, 70))
kimtiem = pygame.transform.rotate(kimtiem, -60)
#UPLOAD POSTER
postercabien = pygame.image.load('postercabien.png')
postercaheo = pygame.image.load('postercaheo.png')
posterchainhua = pygame.image.load('posterchainhua.png')
posterkimtiem = pygame.image.load('posterkimtiem.png')
posterquanao = pygame.image.load('posterquanao.png')
posterruabien = pygame.image.load('posterruabien.png')
postertraicay = pygame.image.load('postertraicay.png')
#UPLOAD BUTTON
rachuuco = pygame.image.load('rachuuco.png')
rachuuco = pygame.transform.scale(rachuuco, (142, 50))
ractaiche = pygame.image.load('ractaiche.png')
ractaiche = pygame.transform.scale(ractaiche, (132, 45))
rackhac = pygame.image.load('racconlai.png')
rackhac = pygame.transform.scale(rackhac, (135, 45))
back = pygame.image.load('back.png') # Adding a back button for cua, rua, caheo
back = pygame.transform.scale(back, (90,90))
#GAME STATE
GAME_RUNNING = "GAME_RUNNING"
POSTER_RAC = "POSTER_RAC"
POSTER_DONGVAT = "POSTER_DONGVAT"
MAIN_MENU = "MAIN_MENU"
GAME_END = "GAME_END"
game_state = MAIN_MENU
#BUTTON
def check_button_click(mouse_x, mouse_y, button_rect):
    return button_rect.collidepoint(mouse_x, mouse_y)
start_ticks = None  
countdown_time = 180

# TỌA ĐỘ BAN ĐẦU CỦA VẬT PHẨM
chuoi_x = 20
chuoi_y = 340
chuoi_speed = 0.1
chuoi_visible = True
ao_x = 50
ao_y = 450
ao_speed = 0.1
ao_visible = True
caheo_x = 200
caheo_y = 500
caheo_speed = 0.09
caheo_visible = True
ca1_x = 540
ca1_y = 600
ca1_speed = 0.1
ca1_visible = True
chainhua_x = 390
chainhua_y = 650
chainhua_speed = 0.2
chainhua_visible = True
ca2_x = 0
ca2_y = 730
ca2_speed = 0.02
ca2_visible = True
rua_x = 500
rua_y = 700
rua_speed = 0.07
rua_visible = True
kimtiem_x = 500
kimtiem_y = 270
kimtiem_visible = True
tao_x = 500
tao_y = 400
tao_speed = 0.1 
tao_visible = True
#current_set
current_poster = None
current_item = None
#FUNCTION
def show_score(x, y, show = True): 
    score_surface = font.render(f"Score: {score}", True, WHITE) 
    screen.blit(score_surface, (x, y))

def is_collision(x1, y1, x2, y2, radius):
    distance = math.sqrt((x2 - x1)**2 + (y2 - y1)**2)
    return distance < radius

def update_draw_item(screen, item, item_x, item_y, item_speed):
    item_x += item_speed
    if item_x <= 0 or item_x >= WIDTH - 50:  
        item_speed = -item_speed  
        item = pygame.transform.flip(item, True, False)  
    screen.blit(item, (item_x, item_y))
    return item_x, item_speed, item

def poster_button_plus(poster, screen):
    screen.blit(pygame.image.load("background.png"), (0,0))
    screen.blit(poster, (37.5,50))
    screen.blit(ractaiche, (400, 700))
    screen.blit(rackhac, (250,700))
    screen.blit(rachuuco, (100,700))
def poster_button_minus(poster, screen):
    screen.blit(pygame.image.load("background.png"), (0,0))
    screen.blit(poster,(37.5,50) )
    screen.blit(back, (95, 600))
def show_timer(x, y, time_left):
    timer_surface = font.render(f"Time: {time_left//60:02}:{time_left%60:02}", True, WHITE)
    screen.blit(timer_surface, (x, y))
class Hook:
    def __init__(self):
        self.x = 191
        self.y = 195
        self.angle = 90
        self.length = 100
        self.speed = 0.1 # tốc độ xoay
        self.is_throwing = False
        self.hook_speed = 1 #tốc độ kéo

    def draw(self, screen):
        end_x = self.x + self.length * math.cos(math.radians(self.angle))
        end_y = self.y + self.length * math.sin(math.radians(self.angle))
        pygame.draw.line(screen, BROWN, (self.x, self.y), (end_x, end_y), 5)  # dây màu nâu
        pygame.draw.circle(screen, BROWN, (int(end_x), int(end_y)), 10)  # móc màu nâu
        
    def update(self):
        if self.is_throwing:
            self.length += self.hook_speed
        else:
            self.angle += self.speed
            if self.angle > 180 or self.angle < 0:
                self.speed = -self.speed  # Đổi hướng xoay

    def reset(self):
        self.length = 100
        self.is_throwing = False

hook = Hook()
#GAME CHÍNH
sl_rac = 0
sl_dv = 0
running = True
background = bg_default
sky = background
time_left = countdown_time
while running:
    screen.fill((0, 0, 0))
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.KEYDOWN:
            # Chuyển từ MAIN_MENU sang GAME_RUNNING
            if game_state == MAIN_MENU and event.key == pygame.K_SPACE:
                game_state = GAME_RUNNING
                main_menu_sound.stop()
                start_ticks = pygame.time.get_ticks()
            # Chuyển từ GAME_END sang GAME_RUNNING
            elif game_state == GAME_END and event.key == pygame.K_SPACE:
                score = 0  # Đặt lại điểm số
                sl_rac = 0  # Đặt lại số lượng rác
                sl_dv = 0 # Đặt lại số lượng động vật
                ca1_visible = True
                ca2_visible = True
                caheo_visible = True
                chainhua_visible = True 
                chuoi_visible = True
                kimtiem_visible = True
                tao_visible = True
                rua_visible = True
                ao_visible = True
                game_state = GAME_RUNNING
                water.play()
                start_ticks = pygame.time.get_ticks()
            elif game_state == GAME_END and event.key == pygame.K_m:
                score = 0  # Đặt lại điểm số
                sl_rac = 0  # Đặt lại số lượng rác
                sl_dv = 0 # Đặt lại số lượng động vật
                ca1_visible = True
                ca2_visible = True
                caheo_visible = True
                chainhua_visible = True 
                chuoi_visible = True
                kimtiem_visible = True
                tao_visible = True
                rua_visible = True
                ao_visible = True
                main_menu_sound.play()
                game_state = MAIN_MENU
            elif event.type == pygame.KEYDOWN and game_state == GAME_RUNNING: 
                if event.key == pygame.K_SPACE:
                    hook.is_throwing = True
        elif event.type == pygame.KEYUP and game_state == GAME_RUNNING:  
            if event.key == current_item or event.key == pygame.K_SPACE:
                hook.reset()
        elif event.type == pygame.MOUSEBUTTONDOWN and game_state == POSTER_RAC:
            mouse_x, mouse_y = event.pos
            if check_button_click(mouse_x, mouse_y, rachuuco.get_rect(topleft=(100, 700))):
                if current_item == "chuoi" or current_item == "tao":
                    score += 10
                    pygame.mixer.stop()
                    rainbow.play()
                    sky = win
                elif current_item == "chainhua":
                    score += 0
                    sky = bg_default
                    pygame.mixer.stop()
                    water.play()
                elif current_item == "ao" or current_item == "kimtiem":
                    score += 0
                    sky = bg_default
                    pygame.mixer.stop()
                    water.play()
                elif current_item == "ca1" or current_item == "ca2" or current_item == "rua" or current_item == "caheo":
                    score -= 30
                    pygame.mixer.stop()
                    thunder.play()
                    sky = lose
            elif check_button_click(mouse_x, mouse_y, ractaiche.get_rect(topleft=(400, 700))):
                if current_item == "chainhua":
                    score += 20
                    water.stop()
                    thunder.stop()
                    rainbow.play()
                    sky = win
                elif current_item == "ao" or current_item == "kimtiem":
                    score += 0
                    rainbow.stop()
                    thunder.stop()
                    water.play()
                    sky = bg_default
                elif current_item == "ca1" or current_item == "ca2" or current_item == "rua" or current_item == "caheo":
                    score -= 30
                    rainbow.stop()
                    thunder.play()
                    water.stop()
                    sky = lose
            elif check_button_click(mouse_x, mouse_y, rackhac.get_rect(topleft=(250, 700))):
                if current_item == "ao" or current_item == "kimtiem":
                    score += 15
                    rainbow.play()
                    thunder.stop()
                    water.stop()
                    sky = win
                elif current_item == "chainhua":
                    score += 0
                    rainbow.stop()
                    thunder.stop()
                    water.play()
                    sky = bg_default
                elif current_item == "chuoi" or current_item == "tao":
                    score += 0
                    rainbow.stop()
                    thunder.stop()
                    water.play()
                    sky = bg_default
                elif current_item == "ca1" or current_item == "ca2" or current_item == "rua" or current_item == "caheo":
                    score -= 30
                    rainbow.stop()
                    thunder.play()
                    water.stop()
                    sky = lose
            elif mouse_x == back:
                if current_item == "ao" or current_item == "kimtiem":
                    score += 0
                    rainbow.stop()
                    thunder.stop()
                    water.play()
                    sky = bg_default
                elif current_item == "chainhua":
                    rainbow.stop()
                    thunder.stop()
                    water.play()
                    bsky = bg_default
                elif current_item == "chuoi" or current_item == "tao":
                    score += 0
                    rainbow.stop()
                    thunder.stop()
                    water.play()
                    sky = bg_default
                elif current_item == "ca1" or current_item == "ca2" or current_item == "rua" or current_item == "caheo":
                    score -= 30
                    rainbow.stop()
                    thunder.play()
                    water.stop()
                    sky = lose
            
            background = sky
            game_state = GAME_RUNNING
            current_poster = None
            hook.reset()
        elif event.type == pygame.MOUSEBUTTONDOWN and game_state == POSTER_DONGVAT:
            mouse_x, mouse_y = event.pos
            if mouse_x == back:
                if current_item == "ao" or current_item == "kimtiem":
                    score += 0
                elif current_item == "chainhua":
                    score += 0
                elif current_item == "chuoi" or current_item == "tao":
                    score += 0
                elif current_item == "ca1" or current_item == "ca2" or current_item == "rua" or current_item == "caheo":
                    score -= 30  
            background = lose
            rainbow.stop()
            thunder.play()
            water.stop()
            game_state = GAME_RUNNING
            current_poster = None
            hook.reset()
        elif game_state == GAME_RUNNING and (sl_rac == 5 or sl_dv == 4):
            game_state = GAME_END
    if game_state == MAIN_MENU:
        main_menu_sound.play()
        screen.blit(main_menu, (0, 0))
    elif game_state == GAME_RUNNING:
        water.play()
        screen.blit(background, (0, 0))
        screen.blit(zeen, (74.8, 177.1))
        show_timer(WIDTH - 150, 10, time_left)
        if start_ticks is not None:
            time_left = countdown_time - (pygame.time.get_ticks() - start_ticks) // 1000
        if time_left <= 0:
            time_left = 0
            game_state = GAME_END  # End the game if time is up
        # Update and draw items
        if ao_visible:
            ao_x, ao_speed, ao = update_draw_item(screen, ao, ao_x, ao_y, ao_speed)
        if ca1_visible:
            ca1_x, ca1_speed, ca1 = update_draw_item(screen, ca1, ca1_x, ca1_y, ca1_speed)
        if caheo_visible:
            caheo_x, caheo_speed, caheo = update_draw_item(screen, caheo, caheo_x, caheo_y, caheo_speed)
        if chainhua_visible:
            chainhua_x, chainhua_speed, chainhua = update_draw_item(screen, chainhua, chainhua_x, chainhua_y, chainhua_speed)
        if chuoi_visible:
            chuoi_x, chuoi_speed, chuoi = update_draw_item(screen, chuoi, chuoi_x, chuoi_y, chuoi_speed)
        if ca2_visible:
            ca2_x, ca2_speed, ca2 = update_draw_item(screen, ca2, ca2_x, ca2_y, ca2_speed)
        if tao_visible:
            tao_x, tao_speed, tao = update_draw_item(screen, tao, tao_x, tao_y, tao_speed)
        if rua_visible:
            rua_x, rua_speed, rua = update_draw_item(screen, rua, rua_x, rua_y, rua_speed)
        if kimtiem_visible:
            screen.blit(kimtiem, (kimtiem_x, kimtiem_y))
        hook.update()
        hook.draw(screen)
        show_score(10, 10)
        
        # Check collision for all items
        end_x = hook.x + hook.length * math.cos(math.radians(hook.angle))
        end_y = hook.y + hook.length * math.sin(math.radians(hook.angle))

        if ao_visible and is_collision(end_x, end_y, ao_x + 30, ao_y + 30, 35):
            current_poster = posterquanao
            current_item = "ao"
            pop.play()
            ao_visible = False
            sl_rac += 1
            game_state = POSTER_RAC
        
        if ca1_visible and is_collision(end_x, end_y, ca1_x + 25, ca1_y + 25, 35):
            current_poster = postercabien
            current_item = "ca1"
            pop.play()
            ca1_visible = False
            sl_dv += 1
            score -= 30
            game_state = POSTER_DONGVAT
        if caheo_visible and is_collision(end_x, end_y, caheo_x + 50, caheo_y + 45, 35):
            current_poster = postercaheo
            current_item = "caheo"
            pop.play()
            caheo_visible = False
            sl_dv += 1
            score -= 30
            game_state = POSTER_DONGVAT
        if chainhua_visible and is_collision(end_x, end_y, chainhua_x + 35, chainhua_y + 35, 35):
            current_poster = posterchainhua
            current_item = "chainhua"
            pop.play()
            chainhua_visible = False
            sl_rac += 1
            game_state = POSTER_RAC

        if chuoi_visible and is_collision(end_x, end_y, chuoi_x + 25, chuoi_y + 25, 35):
            current_poster = postertraicay
            current_item = "chuoi"
            pop.play()
            chuoi_visible = False
            sl_rac += 1
            game_state = POSTER_RAC

        if ca2_visible and is_collision(end_x, end_y, ca2_x + 35, ca2_y + 35, 35):
            current_poster = postercabien
            current_item = "ca2"
            pop.play()
            ca2_visible = False
            sl_dv += 1
            score -= 30
            game_state = POSTER_DONGVAT
        if tao_visible and is_collision(end_x, end_y, tao_x + 25, tao_y + 25, 35):
            current_poster = postertraicay
            current_item = "tao"
            pop.play()
            tao_visible = False
            sl_rac += 1
            game_state = POSTER_RAC

        if rua_visible and is_collision(end_x, end_y, rua_x + 35, rua_y + 35, 35):
            current_poster = posterruabien
            current_item = "rua"
            rua_visible = False
            pop.play()
            sl_dv += 1
            score -= 30
            game_state = POSTER_DONGVAT
        if kimtiem_visible and is_collision(end_x, end_y, kimtiem_x + 50, kimtiem_y + 35, 35):
            current_poster = posterkimtiem
            current_item = "kimtiem"
            kimtiem_visible = False
            pop.play()
            sl_rac += 1
            game_state = POSTER_RAC
    elif game_state == POSTER_RAC:
        if current_poster:
            poster_button_plus(current_poster, screen)
            show_timer(WIDTH - 150, 10, time_left)
    elif game_state == POSTER_DONGVAT:
        rainbow.stop()
        thunder.play()
        water.stop()
        if current_poster:
            poster_button_minus(current_poster, screen)
            show_timer(WIDTH - 150, 10, time_left)
    # GAME_END State
    elif game_state == GAME_END:
        rainbow.stop()
        thunder.stop()
        water.stop()
        screen.blit(end_game, (0, 0))
        show_score(WIDTH // 2 - 50, HEIGHT // 2 - 50)
        if sl_rac == 5:
            if score > 0: 
                congrats_surface = font.render("CONGRATULATIONS", True, WHITE)
                winsound.play()
                screen.blit(congrats_surface, (WIDTH // 2 - 120, HEIGHT // 2 ))
            else:
                failed_surface = font.render("FAILED :(", True, WHITE)
                failedsound.play()
                screen.blit(failed_surface, (WIDTH // 2 - 50, HEIGHT // 2))

        elif sl_dv == 4:
            failed_surface = font.render("FAILED :(", True, WHITE)
            failedsound.play()
            screen.blit(failed_surface, (WIDTH // 2 - 50, HEIGHT // 2))
            show_score(WIDTH // 2 - 50, HEIGHT // 2 - 50, show=True)
    pygame.display.update()
pygame.quit()

