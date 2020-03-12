import pygame
import random
from pygame.locals import *

pygame.init()

screen_info = pygame.display.Info()
screen_size = (screen_info.current_w, screen_info.current_h)

#set size
size = (width, height) = (850, 480)
screen = pygame.display.set_mode(size)
clock = pygame.time.Clock()
color = (254, 255, 255)

# ball
ball_image = pygame.image.load("ball-6x6.png")
ball_image - pygame.transform.smoothscale(ball_image, (30,30))
ball_rect = ball_image.get_rect()
ball_rect.center = (width//2, height//2)
speed = pygamemath.vector2(0, 5)
speed.rotate_ip(random.randint(0, 360))

def move_ball():
    ball.rect.move_ip(speed)

def main():
    while True:
        clock.tick(60)
        for event in pygame.event.get():
            if event.type == QUIT:
                sys.exit
        screen.fill(color)
        screen.blit(ball_image, ball_rect)
        pygame.display.flip()


if __name__ == '__main__':
    main()