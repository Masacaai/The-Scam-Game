import pygame
import sys
import random
import os

qns = []
scammed = []
legit = []
emails = {"q1":1,
          "q2":1,
          "q3":1,
          "q4":1,
          "q5":1,
          "q6": 1,
          "q7": 1,
          "q8": 1,
          "q9": 0,
          "q10": 0,
          "q11": 0,
          "q12": 1,
          "q13": 1,
          "q14": 0,
          "q15": 0,
          "q16": 0,
          "q17": 0,
          "q18": 0,
          "q19": 0,
          "q20": 0,
          "q21": 0,
          "q22": 0,
          "q23": 0,
          "q24": 0,
          "q25": 1,
          "q26": 1,
          "q27": 1,
          "q28": 1,
          "q29": 1,
          "q30": 0,
          "q31": 1,
          "q32": 1,
          "q33": 1,
          "q34": 1,
          "q35": 1,
          "q36": 1,
          "q37": 1,
          "q38": 1,
          "q39": 1,
          "q40": 1,
          "q41": 1,
          "q42": 1,
          "q43": 1,
          "q44": 1,
          "q45": 0,
          "q46": 0,
          "q47": 0,
          "q48": 0,
          "q49": 0,
          "q50": 0
          }
while len(qns)<30:
    a = random.choice(list(emails.keys()))
    if a in qns:
        continue
    else:
        qns.append(a)
def resource_path(relative_path):
    """ Get absolute path to resource, works for dev and for PyInstaller """
    try:
        # PyInstaller creates a temp folder and stores path in _MEIPASS
        base_path = sys._MEIPASS
    except Exception:
        base_path = os.path.abspath(".")

    return os.path.join(base_path, relative_path)

def drawButton(surface, color, position,text,font,size):
    pygame.draw.rect(surface,color,position)
    words(surface,text,font,size,(255,255,255),position[0]+(position[2]//2),position[1]+(position[3]//2))
def words(surface,text,font,size,color,x_location,y_location,yes = True):
    if yes:
        type = pygame.font.SysFont(font,size)
    else:
        type = pygame.font.Font(font,size)
    words = type.render(text,True,color)
    wordsRect = words.get_rect()
    wordsRect.center = (x_location,y_location)
    surface.blit(words, wordsRect)
def score(surface,size,x,y):
    global counter
    score_keeper = "Emails seen: "+str(counter)+"/30"
    words(surface,score_keeper,"open sans",size,(255,255,255),x,y)


def redrawWin(surface):
    global trash,arrow,trash2,arrow2,counter,throw_sound,height,width,move_up,move_left,nwidth,display_width,back,back2,e
    surface.fill((0,0,0))
    score(surface,25,90,20)
    if counter == 30:
        endgame()
    if move_up:
        while height>-20 or nwidth>100:
            surface.fill((0,0,0))
            height-=5
            nwidth-=5
            surface.blit(e[counter-1],(width,height))
            surface.blit(e[counter],(nwidth,60))
            pygame.display.update()
        else:
            move_up= False
            nwidth = display_width
            width = 100
            height = 60
            surface.blit(e[counter],(width,height))
            pygame.display.update()
    elif move_left:
        while width>-90 or nwidth>100:
            surface.fill((0,0,0))
            width-=5
            nwidth-=5
            surface.blit(e[counter-1],(width,height))
            surface.blit(e[counter], (nwidth, 60))
            pygame.display.update()
        else:
            move_left= False
            nwidth = display_width
            width = 100
            height = 60
            surface.blit(e[counter], (width, height))
            pygame.display.update()

    else:
        surface.blit(e[counter], (width, height))
    mouse = pygame.mouse.get_pos()
    if 900<mouse[0]<973 and 1<mouse[1]<87:
        surface.blit(trash2,(900,5))
        for event in pygame.event.get():
            if event.type == pygame.MOUSEBUTTONDOWN:
                if event.button == 1:
                    throw_sound.play()
                    if emails[qns[counter]] == 1:
                        pass
                    else:
                        legit.append(qns[counter])
                    counter+=1
                    move_up = True
    else:
        surface.blit(trash, (900,5))
    if 900<mouse[0]<973 and 500<mouse[1]<586:
        surface.blit(arrow2,(900,500))
        for event in pygame.event.get():
            if event.type == pygame.MOUSEBUTTONDOWN:
                if event.button == 1:
                    click_sound.play()
                    if emails[qns[counter]] == 1:
                        scammed.append(qns[counter])
                    else:
                        pass
                    counter+=1
                    move_left = True
    else:
        surface.blit(arrow, (900,500))
    if 1<mouse[0]<87 and 500<mouse[1]<577:
        surface.blit(back2,(1,500))
        for event in pygame.event.get():
            if event.type == pygame.MOUSEBUTTONDOWN:
                if event.button == 1:
                    click_sound.play()
                    main_menu()
    else:
        surface.blit(back, (1,500))
    pygame.display.update()
def game_intro():
    global win, display_width,display_height,clock,click_sound,throw_sound,tada_sound
    pygame.init()
    display_width = 1000
    display_height = 600
    clock = pygame.time.Clock()
    win = pygame.display.set_mode((display_width, display_height))
    pygame.display.set_caption("The Scam Game")
    gameIcon = pygame.image.load(resource_path("icon.png"))
    pygame.display.set_icon(gameIcon)
    click_sound = pygame.mixer.Sound(resource_path("click.wav"))
    throw_sound = pygame.mixer.Sound(resource_path("throw.wav"))
    tada_sound = pygame.mixer.Sound(resource_path("tada.wav"))
    intro = True
    while intro:
        win.fill((0, 0, 0))
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    pygame.quit()
                    sys.exit()
        words(win,"Welcome!",resource_path("Bungee.ttf"),83,(255,255,255),display_width//2,display_height//2,yes = False)
        pygame.display.update()
        pygame.time.delay(1000)
        intro = False
def main_menu():
    pygame.mixer.music.load(resource_path("music.wav"))
    pygame.mixer.music.play(-1)
    menu = True
    while menu:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    pygame.quit()
                    sys.exit()
        win.fill((0, 0, 0))
        logo = pygame.image.load(resource_path("logo.png"))
        win.blit(logo,(120,100))
        mouse = pygame.mouse.get_pos()
        click = pygame.mouse.get_pressed()
        if 510 < mouse[0] < 710 and 400 < mouse[1] < 450:
            drawButton(win, (65, 193, 123), (510, 400, 200, 50),"Start", "open sans",25)
            if click[0] == 1:
                click_sound.play()
                menu = False
                main()
        else:
            drawButton(win, (45, 173, 103), (510, 400, 200, 50),"Start","open sans",25)
        if 300 < mouse[0] < 500 and 400 < mouse[1] < 450:
            drawButton(win, (65, 193, 123), (300, 400, 200, 50),"Instructions","open sans",25)
            if click[0] == 1:
                click_sound.play()
                menu = False
                instructions()
        else:
            drawButton(win, (45, 173, 103), (300, 400, 200, 50),"Instructions","open sans",25)
        words(win,"An Aaqel-Pratyay production","open sans",25,(255,255,255),display_width//2,580)
        pygame.display.update()


def instructions():
    global win, display_width, display_height
    instro = True
    while instro:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    pygame.quit()
                    sys.exit()
        win.fill((0, 0, 0))
        instructions = pygame.image.load(resource_path("Instructions.png"))
        win.blit(instructions, (60, 60))
        mouse = pygame.mouse.get_pos()
        click = pygame.mouse.get_pressed()
        if 400<mouse[0]<600 and 500<mouse[1]<550:
            drawButton(win, (65, 193, 123), (400, 500, 200, 50),"Continue","open sans",25)
            if click[0] ==1:
                click_sound.play()
                main()
        else:
            drawButton(win, (45, 173, 103), (400, 500, 200, 50),"Continue","open sans",25)
        pygame.display.update()

def main():
    global win,trash,display_height,display_width,arrow,trash2,arrow2,counter,height,width,move_up,move_left,nwidth,back,back2,start_time,e
    start_time = pygame.time.get_ticks()
    counter = 0
    height = 60
    width = 100
    nwidth = display_width
    trash = pygame.image.load(resource_path("trash.png"))
    arrow = pygame.image.load(resource_path("arrow.png"))
    trash2 = pygame.image.load(resource_path("trash2.png"))
    arrow2 = pygame.image.load(resource_path("arrow2.png"))
    back = pygame.image.load(resource_path("back.png"))
    back2 = pygame.image.load(resource_path("back2.png"))
    e1 = pygame.image.load(resource_path(qns[0]+".png"))
    e2 = pygame.image.load(resource_path(qns[1]+".png"))
    e3 = pygame.image.load(resource_path(qns[2]+".png"))
    e4 = pygame.image.load(resource_path(qns[3]+".png"))
    e5 = pygame.image.load(resource_path(qns[4]+".png"))
    e6 = pygame.image.load(resource_path(qns[5]+".png"))
    e7 = pygame.image.load(resource_path(qns[6]+".png"))
    e8 = pygame.image.load(resource_path(qns[7]+".png"))
    e9 = pygame.image.load(resource_path(qns[8]+".png"))
    e10 = pygame.image.load(resource_path(qns[9]+".png"))
    e11= pygame.image.load(resource_path(qns[10]+".png"))
    e12 = pygame.image.load(resource_path(qns[11]+".png"))
    e13 = pygame.image.load(resource_path(qns[12]+".png"))
    e14 = pygame.image.load(resource_path(qns[13]+".png"))
    e15 = pygame.image.load(resource_path(qns[14]+".png"))
    e16 = pygame.image.load(resource_path(qns[15]+".png"))
    e17 = pygame.image.load(resource_path(qns[16]+".png"))
    e18 = pygame.image.load(resource_path(qns[17]+".png"))
    e19 = pygame.image.load(resource_path(qns[18]+".png"))
    e20 = pygame.image.load(resource_path(qns[19]+".png"))
    e21 = pygame.image.load(resource_path(qns[20]+".png"))
    e22 = pygame.image.load(resource_path(qns[21]+".png"))
    e23 = pygame.image.load(resource_path(qns[22]+".png"))
    e24 = pygame.image.load(resource_path(qns[23]+".png"))
    e25 = pygame.image.load(resource_path(qns[24]+".png"))
    e26 = pygame.image.load(resource_path(qns[25]+".png"))
    e27 = pygame.image.load(resource_path(qns[26]+".png"))
    e28 = pygame.image.load(resource_path(qns[27]+".png"))
    e29 = pygame.image.load(resource_path(qns[28]+".png"))
    e30 = pygame.image.load(resource_path(qns[29]+".png"))
    e = [e1,e2,e3,e4,e5,e6,e7,e8,e9,e10,e11,e12,e13,e14,e15,e16,e17,e18,e19,e20,e21,e22,e23,e24,e25,e26,e27,e28,e29,e30]
    move_up = False
    move_left = False
    flag = True
    while flag:
        clock.tick(60)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    pygame.quit()
                    sys.exit()
        redrawWin(win)
def endgame():
    global win,tada_sound,counting_minutes
    pygame.mixer.music.stop()
    tada_sound.play()
    counting_time = pygame.time.get_ticks() - start_time
    counting_minutes = str(counting_time//60000)
    end = True
    s = 25
    xw = 90
    yh = 20
    score(win, s, xw, yh)
    while end:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    pygame.quit()
                    sys.exit()
        win.fill((0, 0, 0))
        while s<83 or xw<(display_width//2) or yh<(display_height//2):
            win.fill((0,0,0))
            if s<83:
                s+=1
            if xw<(display_width//2):
                xw+=1
            if yh<(display_height//2):
                yh+=1
            score(win,s,xw,yh)
            pygame.display.update()
        if s ==83:
            pygame.time.delay(1000)
            game_over()
        pygame.display.update
def game_over():
    global counting_minutes
    over = True
    while over:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    pygame.quit()
                    sys.exit()
        win.fill((0,0,0))
        mouse = pygame.mouse.get_pos()
        click = pygame.mouse.get_pressed()
        if counting_minutes == 1:
            words(win,"You were scammed "+str(len(scammed))+" times and ","open sans",50,(255,255,255),display_width//2,(display_height//2)-20)
            words(win, "you deleted " + str(len(legit)) + " genuine emails in 1 minute!","open sans", 50, (255, 255, 255), display_width // 2, (display_height // 2)+20)

        else:
            words(win, "You were scammed " + str(len(scammed)) + " times and ","open sans", 50, (255, 255, 255), display_width // 2, (display_height // 2)-20)
            words(win, "you deleted " + str(len(legit)) + " genuine emails in "+counting_minutes+" minutes!","open sans", 50, (255, 255, 255), display_width // 2, (display_height // 2)+20)

        if 510 < mouse[0] < 710 and 400 < mouse[1] < 450:
            drawButton(win, (65, 193, 123), (510, 400, 200, 50),"Maybe not.", "open sans",25)
            if click[0] == 1:
                click_sound.play()
                pygame.quit()
                sys.exit()
        else:
            drawButton(win, (45, 173, 103), (510, 400, 200, 50),"Maybe not.","open sans",25)
        if 300 < mouse[0] < 500 and 400 < mouse[1] < 450:
            drawButton(win, (65, 193, 123), (300, 400, 200, 50),"Play again?","open sans",25)
            if click[0] == 1:
                click_sound.play()
                main()
        else:
            drawButton(win, (45, 173, 103), (300, 400, 200, 50),"Play again?","open sans",25)
        pygame.display.update()
game_intro()
main_menu()
