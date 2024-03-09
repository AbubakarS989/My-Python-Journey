import pygame
import random
import os

# Initialization
pygame.init()

# Colors
WHITE = (255, 255, 255)
RED = (255, 0, 0)
BLACK = (0, 0, 0)
SNAKE_GREEN = (35, 45, 40)

# Game Backgrounds
BG2 = pygame.image.load("Screen/bg2.jpg")
INTRO = pygame.image.load("Screen/intro1.png")
OUTRO = pygame.image.load("Screen/outro.png")

# Creating The window
SCREEN_WIDTH = 900
SCREEN_HEIGHT = 600
GAME_WINDOW = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))

# Game Title
pygame.display.set_caption("Snake By CodeWithHarry")
pygame.display.update()

# Variables For The Game
CLOCK = pygame.time.Clock()
FONT = pygame.font.SysFont('Harrington', 35)

def text_screen(text, color, x, y):
    screen_text = FONT.render(text, True, color)
    GAME_WINDOW.blit(screen_text, [x,y])

def plot_snake(game_window, color, snk_list, snake_size):
    for x, y in snk_list:
        pygame.draw.rect(game_window, color, [x, y, snake_size, snake_size])

def welcome():
    exit_game = False
    while not exit_game:
        GAME_WINDOW.blit(INTRO, (0,0))
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                exit_game = True
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_RETURN:
                    gameloop()
        pygame.display.update()
        CLOCK.tick(60)

def gameloop():
    # Game specific variables
    exit_game = False
    game_over = False
    snake_x = 45
    snake_y = 55
    velocity_x = 0
    velocity_y = 0
    snk_list = []
    snk_length = 1

    # Highscore Build
    if not os.path.exists("highscore.txt"):
        with open("highscore.txt", "w") as f:
            f.write("0")
    with open("highscore.txt", "r") as f:
        highscore = int(f.read())

    # Food
    food_x = random.randint(20, SCREEN_WIDTH / 2)
    food_y = random.randint(20, SCREEN_HEIGHT / 2)

    # Game Variables
    score = 0
    init_velocity = 5
    snake_size = 30
    fps = 60

    while not exit_game:
        if game_over:
            with open("highscore.txt", "w") as f:
                f.write(str(highscore))
            
            # Game Over Screen
            GAME_WINDOW.blit(OUTRO, (0, 0))
            text_screen("Score: " + str(score), SNAKE_GREEN, 385, 350)
            pygame.display.update()

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    exit_game = True
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_RETURN:
                        welcome()
        else:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    exit_game = True
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_RIGHT:
                        velocity_x = init_velocity
                        velocity_y = 0
                    if event.key == pygame.K_LEFT:
                        velocity_x = -init_velocity
                        velocity_y = 0
                    if event.key == pygame.K_UP:
                        velocity_y = -init_velocity
                        velocity_x = 0
                    if event.key == pygame.K_DOWN:
                        velocity_y = init_velocity
                        velocity_x = 0
                    if event.key == pygame.K_q:
                        score += 10

            snake_x += velocity_x
            snake_y += velocity_y

            if abs(snake_x - food_x) < 12 and abs(snake_y - food_y) < 12:
                score += 10
                food_x = random.randint(20, SCREEN_WIDTH / 2)
                food_y = random.randint(20, SCREEN_HEIGHT / 2)
                snk_length += 5
                if score > highscore:
                    highscore = score

            GAME_WINDOW.blit(BG2, (0, 0))
            text_screen("Score: " + str(score) + "  Highscore: " + str(highscore), SNAKE_GREEN, 5, 5)
            pygame.draw.rect(GAME_WINDOW, RED, [food_x, food_y, snake_size, snake_size])
            head = []
            head.append(snake_x)
            head.append(snake_y)
            snk_list.append(head)

            if len(snk_list) > snk_length:
                del snk_list[0]

            if head in snk_list[:-1]:
                game_over = True

            if snake_x < 0 or snake_x > SCREEN_WIDTH or snake_y < 0 or snake_y > SCREEN_HEIGHT:
                game_over = True

            plot_snake(GAME_WINDOW, BLACK, snk_list, snake_size)

        pygame.display.update()
        CLOCK.tick(fps)

    pygame.quit()
    quit()

welcome()
