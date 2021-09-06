# Ping Pong
# Date: 17 / jan / 2021
# Author: Edgar A. M.

import pygame
import sys
import random

pygame.mixer.pre_init(44100, -16, 2, 512)
pygame.init()
clock = pygame.time.Clock()

""" Screen """
WIDTH = 1280    # screen width
HEIGHT = 960    # screen height
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption('Pong')

""" Shapes """
ballW = 30
ballH = 30
ball = pygame.Rect(WIDTH/2 - ballW/2, HEIGHT/2 - ballH/2, ballW, ballH)

playerW = 10
playerH = 140
player1 = pygame.Rect(10, HEIGHT/2 - playerH/2, playerW, playerH)
player2 = pygame.Rect(WIDTH - 20, HEIGHT/2 - playerH/2, playerW, playerH)

""" Colors """
bgColor = pygame.Color('grey12')
objColor = (200, 200, 200)

""" Ball speed """
ballUx = 6
ballUy = 6

""" Players' speed """
p1Uy = 0
p2Uy = 0

""" Sound """
hit = pygame.mixer.Sound("soundfile.wav")

while True:

    # Event handler
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_DOWN:
                p1Uy += 9
            if event.key == pygame.K_UP:
                p1Uy -= 9
            if event.key == pygame.K_ESCAPE:
                pygame.quit()
                sys.exit()
        if event.type == pygame.KEYUP:
            if event.key == pygame.K_DOWN:
                p1Uy = 0
            if event.key == pygame.K_UP:
                p1Uy = 0
                
    # Ball Dynamics
    ball.x += ballUx
    ball.y += ballUy

    # ...bounce against top or bottom wall
    if (ball.top <= 0 or ball.bottom >= HEIGHT):
        ballUy *= -1
    # ...reset if it hits left or right wall
    if (ball.left <= 0 or ball.right >= WIDTH):
        ball.center = (WIDTH / 2, HEIGHT / 2)
        ballUx *= random.choice((1, -1))
        ballUy *= random.choice((1, -1))
        
    if ball.colliderect(player1) or ball.colliderect(player2):

        # ...condition 1: ball above player 1
        # ...condition 2: ball below player 1
        # ...condition 3: ball next to player 1
        p1_ballT = abs(ball.bottom - player1.top) < 5
        p1_ballB = abs(ball.top - player1.bottom) < 5
        p1_ballR = abs(ball.left - player1.right) < 5

        # ...condition 4: ball above player 2
        # ...condition 5: ball below player 2
        # ...condition 6: ball next to player 2
        p2_ballT = abs(ball.bottom - player2.top) < 5
        p2_ballB = abs(ball.top - player2.bottom) < 5
        p2_ballL = abs(ball.right - player2.left) < 5

        if p1_ballT and p1_ballR:
            ball.center = (WIDTH / 2, HEIGHT / 2)
            ballUx *= random.choice((1, -1))
            ballUy *= random.choice((1, -1))

        if p1_ballB and p1_ballR:
            ball.center = (WIDTH / 2, HEIGHT / 2)
            ballUx *= random.choice((1, -1))
            ballUy *= random.choice((1, -1))

        if p2_ballT and p2_ballL:
            ball.center = (WIDTH / 2, HEIGHT / 2)
            ballUx *= random.choice((1, -1))
            ballUy *= random.choice((1, -1))

        if p2_ballB and p2_ballL:
            ball.center = (WIDTH / 2, HEIGHT / 2)
            ballUx *= random.choice((1, -1))
            ballUy *= random.choice((1, -1))

        ballUx *= -1
        hit.play()

    # Opponent Dynamics
    player2.centery = ball.centery

    if player2.top <= 0:
        player2.top = 0
    if player2.bottom >= HEIGHT:
        player2.bottom = HEIGHT

    # Player Dynamics
    player1.y += p1Uy
    
    if player1.top <= 0:
        player1.top = 0
    if player1.bottom >= HEIGHT:
        player1.bottom = HEIGHT

    # Visuals
    screen.fill(bgColor)
    pygame.draw.rect(screen, objColor, player1)
    pygame.draw.rect(screen, objColor, player2)
    pygame.draw.ellipse(screen, objColor, ball)
    pygame.draw.aaline(screen, objColor, (WIDTH/2, 0), (WIDTH/2, HEIGHT))

    # Updating the screen
    pygame.display.flip()
    clock.tick(60)
