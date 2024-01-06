# 1. პროგრამამ უნდა შეგაყვანინოს სასურველი მოწინააღმდეგის რაოდენობა და შესაბამისი კვადრატები შექმნას რანდომულ ლოკაციებზე.

import turtle
import random

def create(size):
    x = random.randint(-300, 300)
    y = random.randint(-300, 300)
    turtle.penup()
    turtle.goto(x, y)
    turtle.pendown()
    for i in range(4):
        turtle.forward(size)
        turtle.left(90)

def main():
    turtle.speed(7)

    num_opponents = int(input("Enter the number of opponents: "))

    for i in range(num_opponents):
        square_size = random.randint(20, 100)
        create(square_size)

    turtle.done()

if __name__ == "__main__":
    main()

# 2. დაგუგლე pygame_ის colliderect ფუნქცია, და როდესაც რომელიმე მოწინააღმდეგე მოთამაშეს დაიჭერს, თამაში დაასრულე. 

import pygame
import sys
import random

pygame.init()

width, height = 800, 600
screen = pygame.display.set_mode((width, height))
pygame.display.set_caption("Bee Game")

original_background_image = pygame.image.load("background.jpg")
background_image = pygame.transform.scale(original_background_image, (width, height)) 
bee_image = pygame.image.load("bee.jpg")
small_bee_image = pygame.transform.scale(bee_image, (30, 30)) 

original_flower_image = pygame.image.load("flower.jpg")
flower_width, flower_height = 30, 30
flower_image = pygame.transform.scale(original_flower_image, (flower_width, flower_height))

bee_x = width - 30
bee_y = height - 170 
bee_speed = 5

flowers = []

def spread_flowers(num_flowers):
    for i in range(num_flowers):
        x = random.randint(0, width - flower_width)
        y = random.randint(0, height - flower_height)
        flowers.append(pygame.Rect(x, y, flower_width, flower_height))

clock = pygame.time.Clock()
running = True

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    keys = pygame.key.get_pressed()
    if keys[pygame.K_LEFT] and bee_x > 0:
        bee_x -= bee_speed
    if keys[pygame.K_RIGHT] and bee_x < width - 30:
        bee_x += bee_speed
    if keys[pygame.K_UP] and bee_y > 0:
        bee_y -= bee_speed
    if keys[pygame.K_DOWN] and bee_y < height - 30:
        bee_y += bee_speed

    if not flowers:
        spread_flowers(14)

    bee_rect = pygame.Rect(bee_x, bee_y, 50, 50)
    for flower_rect in flowers:
        if bee_rect.colliderect(flower_rect):
            print("Game Over!")
            running = False

    screen.blit(background_image, (0, 0))
    screen.blit(small_bee_image, (bee_x, bee_y))
    for flower_rect in flowers:
        screen.blit(flower_image, flower_rect.topleft)

    pygame.display.flip()

    clock.tick(30)

pygame.quit()
sys.exit()