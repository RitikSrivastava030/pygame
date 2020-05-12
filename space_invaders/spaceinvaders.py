# -*- coding: utf-8 -*-
"""
Created on Sun May 10 11:22:35 2020

@author: GROUP 1
"""

import pygame
import random
import math

pygame.init()

score_value = 0
font = pygame.font.Font('freesansbold.ttf', 32)

textX = 10
textY = 10
name=input("ENTER YOUR NAME : ")
screen = pygame.display.set_mode((800,600))
pygame.display.set_caption("Space Invaders")
icon = pygame.image.load("transport.png")
pygame.display.set_icon(icon)
fire_sound=pygame.mixer.Sound('shoot.wav')
die_sound=pygame.mixer.Sound('killed.wav')
player_die_sound=pygame.mixer.Sound('explosion.wav')
music=pygame.mixer.music.load('b_music.mp3')
pygame.mixer.music.play(-1)
pImg = pygame.image.load("gaming.png")
playerX = 370
playerY = 480
player_chng = 0

eImg = []
eImg.clear()
enemyX = []
enemyY = []
enemy_chngX = []
enemy_chngY = []
num_of_enemies = 6

eImg.append(pygame.image.load("enemy.png"))
eImg.append(pygame.image.load("enemy2.png"))
eImg.append(pygame.image.load("enemy3.png"))
eImg.append(pygame.image.load("enemy.png"))
eImg.append(pygame.image.load("enemy2.png"))
eImg.append(pygame.image.load("enemy3.png"))

for k in range(num_of_enemies):
    #eImg.append(pygame.image.load("enemy.png"))
    enemyX.append(random.randint(0,736))
    enemyY.append(0)
    enemy_chngX.append(0)
    enemy_chngY.append(2)

bulletImg = pygame.image.load("bullet.png")
bulletX = 0
bulletY = 480
bullet_chngX = 0
bullet_chngY = 10
bullet_state = "ready"

bImg = pygame.image.load("background.png")
bX = 0
bY = 0

gameover = pygame.font.Font('freesansbold.ttf',64)
def show_name(name,x,y):
    name_show = font.render("PLAYER NAME : "+ str(name),True, (255,100,20))
    screen.blit(name_show,(x, y))

def show_score(x, y):
    score = font.render("SCORE : " + str(score_value), True, (255,100,20))
    screen.blit(score, (x, y))

def player(x,y):
    screen.blit(pImg,(x,y))
    
def enemy(x,y,i):
    screen.blit(eImg[i],(x,y))
    
def background():
    screen.blit(bImg,(bX,bY))
    
def fire_bullet(x,y):
    global bullet_state
    bullet_state = "fire"
    screen.blit(bulletImg,(x + 16, y + 10))
    
def isColliding(x, y, X, Y):
    dist = math.sqrt((math.pow(X - x,2)) + (math.pow(Y - y,2)))
    if dist < 27:
        return True
    else:
        return False    

def game_over_display():
    text = gameover.render("GAME OVER", True, (255,100,20))
    screen.blit(text, (190, 150))
    show_name(name,200,250)
    show_score(300,300)
    #pygame.quit()

running = 1
try:
    while running:
        screen.fill((0,0,0))
        background()
        
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = 0
                pygame.quit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LEFT:
                    player_chng = -4
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_RIGHT:
                    player_chng = 4
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE:
                    fire_sound.play()
                    if bullet_state == "ready":
                        bulletX = playerX
                        fire_bullet(bulletX,bulletY)
            if event.type == pygame.KEYUP:
                if event.key == pygame.K_LEFT or event.key == pygame.K_RIGHT:
                    player_chng = 0
        
        playerX += player_chng
        
        if playerX <= 0:
            playerX = 0
        if playerX >= 736:
            playerX = 736
        
        for i in range(num_of_enemies):
            
            if enemyY[i] >= 536:
                enemyX[i] = random.randint(0,736)
                enemyY[i] = 0
                #game_over_display()
                #break
            
            enemyY[i] += enemy_chngY[i]
        
            if enemyY[i] >= 600:
                enemyX[i] = random.randint(0,736)
                enemyY[i] = 0
                #enemy_chngX[i] = 0
                #enemyY[i] += enemy_chngY[i]
            #elif enemyX[i] >=736:
                #enemy_chngX[i] = 0
                #enemyY[i] += enemy_chngY[i]
            collision1 = isColliding(bulletX, bulletY, enemyX[i], enemyY[i])
            if collision1:
                die_sound.play()
                score_value += 1
                bulletY = 480
                bullet_state = "ready"
                enemyX[i] = random.randint(0,736)
                enemyY[i] = 0
                
            collision2 = isColliding(playerX, playerY, enemyX[i], enemyY[i])
            if collision2:
                for j in range(num_of_enemies):
                    enemyX[j] = 2000
                player_die_sound.play()
                #blast(playerX, playerY)
                game_over_display()
                pygame.display.update()
                i=0
                while i < 1000000:
                    pygame.time.delay(10)
                    i=i+1
                    for event in pygame.event.get():
                        if event.type == pygame.QUIT:
                            i=1000001
                            pygame.quit()
            
            enemy(enemyX[i],enemyY[i],i)
            
        if bullet_state == "fire":
            fire_bullet(bulletX,bulletY)
            bulletY -= bullet_chngY
        if bulletY <= 0:
            bullet_state = "ready"
            bulletY = 480
            
        player(playerX,playerY)
        show_name(name,400,10)
        show_score(textX, textY)
        pygame.display.update()
except:
    print("GAME OVER")
    print("PLayer Name :",name)
    print("Score :",score_value)