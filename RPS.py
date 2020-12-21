# RPS.py
import pygame as pg
from pygame.locals import *
import random
import time, os, sys




pg.font.init()
randomlist=list(range(9999))
random.shuffle(randomlist)
size = [1500, 1000]
fps = 60
rock=pg.image.load(r'Images/Small_Rock.jpg') 
paper = pg.image.load(r'Images/Small_paper.jpg') 
scissor = pg.image.load(r'Images/Small_Scissor.jpg')
font = pg.font.SysFont(None, 48)
RED = [255, 0, 0]
WHITE = [255, 255, 255]
BLACK = [0, 0, 0]
WEIRD_YELLOW = [255, 255, 153]
text_loc = (500, 500)
centre_x = size[0]/2
centre_y = size[1]/2



def Rock_Paper_Scissors():
    os.environ['SDL_VIDEO_CENTERED'] = 'True'
    i=-1
    score_player = 0
    score_computer = 0
    screen = pg.display.set_mode(size)
    main_game(i, score_player, score_computer,screen)

def main_game(i, score_player, score_computer, screen):
    pg.init()
    clock = pg.time.Clock()
    pg.display.set_caption('Rock Paper Scissors') #pylint: disable=undefined-variable
    text = font.render("Player's Move", 1, BLACK)
    textpos = text.get_rect()
    textpos.centerx = screen.get_rect().centerx
    textpos.centery = (screen.get_rect().centery)/4

    player_score = font.render("Player's Score : "+str(score_player), 1, BLACK)
    player_score_pos = player_score.get_rect()
    player_score_pos.centerx = screen.get_rect().centerx - (screen.get_rect().centerx/2)
    player_score_pos.centery = screen.get_rect().centery + (screen.get_rect().centery/1.2)

    comp_score = font.render("Computer's Score : " +str(score_computer), 1, BLACK)
    comp_score_pos = comp_score.get_rect()
    comp_score_pos.centerx = screen.get_rect().centerx + (screen.get_rect().centerx/2)
    comp_score_pos.centery = screen.get_rect().centery + (screen.get_rect().centery/1.2)

    Exit_text = font.render('Exit',True,RED)
    Exit_rect = Exit_text.get_rect()
    Exit_rect.centerx = screen.get_rect().centerx
    Exit_rect.centery = screen.get_rect().centery + (screen.get_rect().centery/1.2)
    Exit_rect[2] = Exit_rect[2] + 10
    Exit_rect[3] = Exit_rect[3] + 10
    exit_button = pg.Rect(Exit_rect)

    while True:
        screen.fill(WHITE)
        screen.convert()

        screen.blit(text, textpos)
        screen.blit(player_score, player_score_pos)
        screen.blit(comp_score, comp_score_pos)
        pg.draw.rect(screen, WEIRD_YELLOW, exit_button)
        pg.draw.rect(screen, BLACK, exit_button, 3)
        screen.blit(Exit_text, (exit_button[0]+5, exit_button[1]+5))

        (rock_hitbox, b_rck) =  Button_Maker('Rock', RED,  size[0]/6, size[1]/1.4, screen)
        (paper_hitbox, b_ppr) = Button_Maker('Paper', RED, centre_x, size[1]/1.4, screen)
        (scissor_hitbox, b_scr) = Button_Maker('Scissor', RED,  size[0] - size[0]/6, size[1]/1.4, screen)
        Exit_hitbox = pg.Rect(exit_button[0], exit_button[1], 350, 250)
        pg.display.update()
        clock.tick(fps)

        for event in pg.event.get():
            if event.type == pg.QUIT:
                pg.quit()
                sys.exit()
                return False

            if event.type == pg.MOUSEBUTTONDOWN:
                mouse_pos = event.pos

                if b_rck.collidepoint(mouse_pos) or rock_hitbox.collidepoint(mouse_pos):
                    i = i+1
                    Comp_Move('Rock', i+1, score_player, score_computer, screen)
                elif b_ppr.collidepoint(mouse_pos) or paper_hitbox.collidepoint(mouse_pos):
                    i = i+1
                    Comp_Move('Paper', i+1, score_player, score_computer, screen)
                elif b_scr.collidepoint(mouse_pos) or scissor_hitbox.collidepoint(mouse_pos):
                    i = i+1
                    Comp_Move('Scissor', i+1, score_player, score_computer, screen)
                elif Exit_hitbox.collidepoint(mouse_pos):
                    Exit(screen,score_player,score_computer)
                

    pg.quit()
    sys.exit()

def Comp_Move(text, i, player, computer, screen):
    while True:
        for event in pg.event.get():

            if event.type == pg.QUIT:
                pg.quit()
                sys.exit()
                return False

            screen.fill(WHITE)

            OK = font.render("OK", 1, RED)
            OK_pos = OK.get_rect()
            OK_pos.centerx = screen.get_rect().centerx
            OK_pos.centery = screen.get_rect().centery + (screen.get_rect().centery/2)

            button_OK = pg.Rect(OK_pos[0], OK_pos[1], 100, 60)
            pg.draw.rect(screen, WEIRD_YELLOW, button_OK)
            pg.draw.rect(screen, BLACK, button_OK, 3)
            screen.blit(OK, (button_OK[0]+25, button_OK[1]+15))

            played = font.render("You Played "+ text, 1, BLACK)
            played_pos = played.get_rect()
            played_pos.centerx = screen.get_rect().centerx - (screen.get_rect().centerx/2)
            played_pos.centery = screen.get_rect().centery - (screen.get_rect().centery/1.2)
            screen.blit(played, played_pos)

            comp = Roll(i + 1)
            k = Score(text, comp, player, computer)

            comp_played = font.render("The Computer Played " + comp, 1, BLACK)
            comp_played_pos = comp_played.get_rect()
            comp_played_pos.centerx = screen.get_rect().centerx + (screen.get_rect().centerx/2)
            comp_played_pos.centery = screen.get_rect().centery - (screen.get_rect().centery/1.2)
            screen.blit(comp_played, comp_played_pos)
                
            Winner = font.render(k, 1, BLACK)
            Winner_pos = Winner.get_rect()
            Winner_pos.centerx = screen.get_rect().centerx
            Winner_pos.centery = screen.get_rect().centery/2
            screen.blit(Winner, Winner_pos)

            Draw(played_pos, comp_played_pos, text, comp, screen)

            if event.type == pg.MOUSEBUTTONDOWN:
                mouse_pos = event.pos
                if button_OK.collidepoint(mouse_pos):
                    Think(i, player, computer, k, screen)
            pg.display.flip()

def Draw(played_pos, comp_played_pos, player, comp, screen):
    
    image_player = Select_Image(player)
    image_comp = Select_Image(comp)
    image_rect = played_pos
    image_rect2 = comp_played_pos
    screen.blit(image_player, (image_rect[0], image_rect[1]+300))
    screen.blit(image_comp, (image_rect2[0], image_rect2[1]+300))

def Roll(c):
    if(randomlist[c] % 3 == 0):
        return 'Rock'
    elif(randomlist[c] % 3 == 1):
        return('Paper')
    elif(randomlist[c] % 3 == 2):
        return('Scissor') 

def Score(choice, comp, p, c):
    if choice == 'Rock' and comp == 'Rock':
        return 'It\'s a Draw'
    elif choice == 'Rock' and comp == 'Paper':
        return 'The Computer Wins'
    elif choice == 'Rock' and comp == 'Scissor':
        return 'The Player Wins'
    elif choice == 'Paper' and comp == 'Rock':
        return ' The Player Wins'
    elif choice == 'Paper' and comp == 'Paper':
        return 'It\'s a Draw'
    elif choice == 'Paper' and comp == 'Scissor':
        return 'The Computer Wins'
    elif choice == 'Scissor' and comp == 'Rock':
        return 'The Computer Wins'
    elif choice == 'Scissor' and comp == 'Paper':
        return 'The Player Wins'
    elif choice == 'Scissor' and comp == 'Scissor':
        return 'It\'s a Draw'

def Think(i, p, c, k, screen):
    if k == 'The Player Wins':
        p = p + 1
    elif k == 'The Computer Wins':
        c = c + 1
    main_game(i, p, c, screen)

def Button_Maker(text, color, x, y, screen):
    text_rend = font.render(text, True, color)
    text_rect = text_rend.get_rect()
    text_rect[2] = text_rect[2] + 10
    text_rect[3] = text_rect[3] + 10
    text_rect.centerx = x
    text_rect.centery = y
    button = pg.Rect(text_rect)
    image = Select_Image(text)

    pg.draw.rect(screen, WEIRD_YELLOW, button)
    pg.draw.rect(screen, BLACK, button, 3)
    img = pg.Surface((350, 249))                                     #pylint: disable=too-many-function-args
    image_rect = img.get_rect()
    image_rect.centerx = x
    screen.blit(text_rend, (button[0]+5, button[1]+5))
    screen.blit(image, (image_rect[0], button[1]-300))
    hitbox = pg.Rect(button[0], button[1]-300, 350, 250)

    return(hitbox,button)

def Exit(screen,p,c):
    os.environ['SDL_VIDEO_CENTERED'] = 'True'
    screen = pg.display.set_mode([300,300])
    print('heres')
    if c > p: 
        text = font.render('The Computer Wins!', True,BLACK)
    elif p > c:
        text = font.render('The Player Wins!', True,BLACK)
    else:
        text = font.render('It\'s a Draw!', True,BLACK)
    while True:
        for event in pg.event.get():
            screen.fill(WHITE)
            text_rect = text.get_rect()
            text_rect.centerx= screen.get_rect().centerx
            text_rect.centery= screen.get_rect().centerx
            screen.blit(text, text_rect)
            pg.display.update()
            if event.type == pg.QUIT:
                pg.quit()
                sys.exit()
                return False


def Select_Image(text):
    if text == 'Rock':
        return rock
    elif text == 'Paper':
        return paper
    elif text == 'Scissor':
        return scissor

Rock_Paper_Scissors()