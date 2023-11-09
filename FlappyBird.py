import pygame
import time
import random

pygame.init()

#
black = (0, 0, 0)
blue = (153, 204, 255)
green = (0, 255, 0)

#
winW = 800
winH = 600
dis = pygame.display.set_mode((winW, winH))
pygame.display.set_caption("SDSS Flappy Bird")

#
clock = pygame.time.Clock()
gameSpeed = 40
gameOver = False
ballX = 150
ballY = winH / 2
ballR = 20
heights = []
font_style = pygame.font.SysFont(None, 50)

#
for count in range(0, 1000):
    heights.append(random.randint(25, 400))

#
upperRectangles = []
lowerRectangles = []

#
xCoords = []
for count in range(1, 1001):
    xCoords.append(400 * count)

#
score = int(0)


#
def message(msg, color):
    mesg = font_style.render(msg, True, color)
    dis.blit(mesg, [20, 20])


#
while not gameOver:

    for event in pygame.event.get():
        #
        if event.type == pygame.QUIT:
            #
            gameOver = True

        if event.type == pygame.KEYDOWN:
            #
            if event.key == pygame.K_SPACE:
                ballY -= 50

    #
    if(winH- 15 < ballY + ballR):
        ballY = winH - 25
    elif ballY < 20:
        ballY += 25
    else:
        ballY += 3

    #
    dis.fill(blue)
    #
    ball = pygame.draw.rect(dis, black, [ballX, ballY, 25, 25])

    #
    for count in range(0, 1000):
        height = random.randint(10, 150)
        upperRectangles.append(pygame.draw.rect(dis, green, [xCoords[count], 0, 75, heights[count]]))
        lowerRectangles.append(pygame.draw.rect(dis, green, [xCoords[count], heights[count] + 150, 75,
                                                             winH - (heights[count] + 150)]))
        #
        if xCoords[count] + 65 < ballX < xCoords[count]+75 and heights[count] <= ballY <= (heights[count] + 150):
            if score == count:
                score += 1
        elif ball.colliderect(upperRectangles[count]) or ball.colliderect(
                lowerRectangles[count]):
            gameOver = True

    #moves pipers across screen
    for count in range(0, len(xCoords) - 1):
        xCoords[count] -= 3

    message("Score: " + str(score), black)

    upperRectangles.clear()
    lowerRectangles.clear()

    #
    pygame.display.update()
    clock.tick(gameSpeed)


def gameOverMsg(msg, color):
    dis.fill(blue)
    mesg = font_style.render(msg, True, color)
    dis.blit(mesg, [200, winH / 2])


gameOverMsg("Game Lost. Final Score:   " + str(score), black)
pygame.display.update()

time.sleep(2)
pygame.quit()
