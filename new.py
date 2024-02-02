import pygame
import random
import math

pygame.init()
window = pygame.display.set_mode((640, 480))

robot = pygame.image.load("robot.png")

x = random.randint(0, 640)
y = random.randint(0, 480)
velocity_x = 1
velocity_y = 1
count = 0
clock = pygame.time.Clock()

enemies = [pygame.image.load("alien.png") for _ in range(random.randint(5, 10))]
enemies_info = [{'x': random.randint(0, 640), 'y': random.randint(0, 480)} for _ in range(len(enemies))]

def is_collision(x, y, enemy_x, enemy_y, threshold=50):
    dist = math.sqrt(pow((x - enemy_x), 2) + pow((y - enemy_y), 2))
    return dist < threshold

while True:
    for event in pygame.event.get():
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                if x > 0:
                    x -= 10
            if event.key == pygame.K_RIGHT:
                if x < 640:
                    x += 10

        if event.type == pygame.QUIT:
            print(f"Score : {count}")
            exit()

    window.fill((0, 0, 0))
    window.blit(robot, (x, y))

    for i, (enemy_info, enemy_image) in enumerate(zip(enemies_info, enemies)):
        enemy_x, enemy_y = enemy_info['x'], enemy_info['y']
        window.blit(enemy_image, (enemy_x, enemy_y))

        if is_collision(x, y, enemy_x, enemy_y):
            count+=10
            # Handle collision action for this specific enemy, for example, remove it from the screen.
            enemies_info.pop(i)
            enemies.pop(i)
            enemies_info.append({'x': random.randint(0, 640), 'y': random.randint(0, 480)})
            enemies.append(pygame.image.load("alien.png"))

    pygame.display.flip()

    x += velocity_x
    y += velocity_y

    if velocity_x > 0 and x + robot.get_width() >= 640:
        velocity_x = -velocity_x
    if velocity_x < 0 and x <= 0:
        velocity_x = -velocity_x
    if velocity_y > 0 and y + robot.get_height() >= 480:
        velocity_y = -velocity_y
    if velocity_y < 0 and y <= 0:
        velocity_y = -velocity_y

    clock.tick(60)
print(count)