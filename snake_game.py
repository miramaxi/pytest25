import pygame
import random

# Инициализация Pygame
pygame.init()

# Настройки окна
WIDTH, HEIGHT = 640, 480
win = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Змейка")

# Цвета
BLACK = (0, 0, 0)
GREEN = (0, 255, 0)
RED = (255, 0, 0)

# Начальные координаты змейки
snake_pos = [100, 50]
snake_body = [[100, 50], [90, 50], [80, 50]]

# Координаты еды
food_pos = [random.randrange(1, (WIDTH//10)) * 10,
            random.randrange(1, (HEIGHT//10)) * 10]
food_spawn = True

# Направление движения
direction = 'RIGHT'
change_to = direction

# Скорость и FPS
snake_speed = 15
fps = pygame.time.Clock()

# Основной цикл игры
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            quit()

        # Определение направления движения
        keys = pygame.key.get_pressed()
        for key in keys:
            if keys[pygame.K_UP]:
                change_to = 'UP'
            if keys[pygame.K_DOWN]:
                change_to = 'DOWN'
            if keys[pygame.K_LEFT]:
                change_to = 'LEFT'
            if keys[pygame.K_RIGHT]:
                change_to = 'RIGHT'

    # Проверка на движение в противоположную сторону
    if change_to == 'UP' and not direction == 'DOWN':
        direction = 'UP'
    if change_to == 'DOWN' and not direction == 'UP':
        direction = 'DOWN'
    if change_to == 'LEFT' and not direction == 'RIGHT':
        direction = 'LEFT'
    if change_to == 'RIGHT' and not direction == 'LEFT':
        direction = 'RIGHT'

    # Изменение координат змейки в зависимости от направления
    if direction == 'UP':
        snake_pos[1] -= 10
    if direction == 'DOWN':
        snake_pos[1] += 10
    if direction == 'LEFT':
        snake_pos[0] -= 10
    if direction == 'RIGHT':
        snake_pos[0] += 10

    # Добавление головы змейки в начало списка и удаление хвоста
    snake_body.insert(0, list(snake_pos))
    if snake_pos[0] == food_pos[0] and snake_pos[1] == food_pos[1]:
        food_spawn = False
    else:
        snake_body.pop()

    if not food_spawn:
        food_pos = [random.randrange(1, (WIDTH//10)) * 10,
                    random.randrange(1, (HEIGHT//10)) * 10]
    food_spawn = True

    # Заливка экрана черным цветом
    win.fill(BLACK)

    # Отрисовка змейки
    for pos in snake_body:
        pygame.draw.rect(win, GREEN,
                         pygame.Rect(pos[0], pos[1], 10, 10))

    # Отрисовка еды
    pygame.draw.rect(win, RED, pygame.Rect(
        food_pos[0], food_pos[1], 10, 10))

    # Обновление экрана
    pygame.display.update()
    fps.tick(snake_speed)
