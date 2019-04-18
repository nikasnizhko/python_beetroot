import pygame
import sys
import random
import time

pygame.init()




display_height = 500
display_width = 500

display = pygame.display.set_mode((display_height, display_width))
pygame.display.set_caption("Snake")

#Colors
blue = pygame.Color(0, 153, 153)  # display
white = pygame.Color(255, 255, 255)
red = pygame.Color(255, 102, 102)
green = pygame.Color(153, 255, 204)


fps_controller = pygame.time.Clock()   #(frames per second) controller

score = 0

class Play:
    def __init__(self):
        self.display_height = 500
        self.display_width = 500
        self.speed = 20
        self.score = 0
        self.fps_controller = pygame.time.Clock()


    def loop(self, change_to):
        self.clock = pygame.time.Clock()
        for event in pygame.event.get():
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_RIGHT:
                    change_to = 'RIGHT'
                elif event.key == pygame.K_LEFT:
                    change_to = 'LEFT'
                elif event.key == pygame.K_UP:
                    change_to = 'UP'
                elif event.key == pygame.K_DOWN:
                    change_to = 'DOWN'
                elif event.key == pygame.K_ESCAPE:
                    pygame.quit()
        return change_to


    def game_over(self):
        my_font = pygame.font.SysFont('times new roman', 90)
        game_over_surface = my_font.render('YOU DIED', True, red)
        game_over_rect = game_over_surface.get_rect()
        game_over_rect.midtop = (display_height / 2, display_width / 4)
        display.fill(green)
        display.blit(game_over_surface, game_over_rect)
        #show_score(0, red, 'times', 20)
        pygame.display.flip()
        time.sleep(30)
        pygame.quit()
        sys.exit()

    def show_score(self, choice=1):
        score_font = pygame.font.SysFont("times new roman", 16)
        score_surface = score_font.render('Score : ' + str(score), True, blue)
        score_rect = score_surface.get_rect()
        if choice == 1:
            score_rect.midtop = (display_height / 10, 15)
        else:
            score_rect.midtop = (display_height / 2, display_width / 1.25)
        display.blit(score_surface, score_rect)
        #pygame.display.flip()


    def refresh_screen_and_fps(self):
        pygame.display.flip()
        game.fps_controller.tick(5)


class Snake:
    def __init__(self):
        self.head_pos = [100, 50]
        self.snake_body = [[100, 50], [90, 50], [80, 50]]
        self.direction = "RIGHT"
        self.change_to = self.direction


    def change_direction(self):
        if self.change_to == "RIGHT" and not self.direction == "LEFT":
            self.direction = "RIGHT"
        elif self.change_to == "LEFT" and not self.direction == "RIGHT":
            self.direction = "LEFT"
        elif self.change_to == "UP" and not self.direction == "DOWN":
            self.direction = "UP"
        elif self.change_to == "DOWN" and not self.direction == "UP":
            self.direction = "DOWN"


    def move(self):  #foodPos
        if self.direction == 'UP':
            self.head_pos[1] -= 10
        if self.direction == 'DOWN':
            self.head_pos[1] += 10
        if self.direction == 'LEFT':
            self.head_pos[0] -= 10
        if self.direction == 'RIGHT':
            self.head_pos[0] += 10


        # if self.position == foodPos:
        #     return 1
        # else:
        #     self.body.pop()
        #     return 0


    def collisions(self, game_over):
        if self.head_pos[0] < 0 or self.head_pos[0] > display_height - 10:
            game_over()
        if self.head_pos[1] < 0 or self.head_pos[1] > display_width - 10:
            game_over()
            # Touching the snake body
        for block in self.snake_body[1:]:
            if self.head_pos[0] == block[0] and self.head_pos[1] == block[1]:
                game_over()


    def grow_snake(self, score, apple_position):
        self.snake_body.insert(0, list(self.head_pos))
        if self.head_pos[0] == apple_position[0] and self.head_pos[1] == apple_position[1]:
            apple_position = [random.randrange(1, display_width / 10) * 10,
                              random.randrange(1, display_height / 10) * 10]
            score += 1
        else:
            self.snake_body.pop()

        return score, apple_position

    def draw_snake(self):
        display.fill(blue)
        for pos in self.snake_body:
            pygame.draw.rect(display, green, pygame.Rect(pos[0], pos[1], 10, 10))



class Apple:

    def __init__(self):
        self.apple_position = [random.randrange(1, (display_height//10)) * 10,
                               random.randrange(1, (display_width//10)) * 10]



    def draw_apple(self):
        pygame.draw.rect(display, white, pygame.Rect(self.apple_position[0],
                                                     self.apple_position[1], 10, 10))

    # def draw(display, apple_position, apple):
    #     display.blit(apple, (apple_position[0], apple_position[1]))







game = Play()
snake = Snake()
apple = Apple()

while True:
    snake.change_to = game.loop(snake.change_to)
    snake.change_direction()
    snake.move()
    game.score, apple.apple_position = snake.grow_snake(game.score, apple.apple_position)
    snake.draw_snake()

    apple.draw_apple()

    snake.collisions(game.game_over)

    game.show_score()
    game.refresh_screen_and_fps()