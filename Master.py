import pygame
import random
import sys

class Master:

    def __init__(self):

        #Game settings
        pygame.init()
        self.SCREEN_WIDTH = 800
        self.SCREEN_HEIGHT = 600
        self.BACKGROUND_COLOR = (0,0,0) #black color
        self.PLAYER_COLOR = (0,0,255) #blue color
        self.PLAYER_SIZE = 50
        self.screen = pygame.display.set_mode((self.SCREEN_WIDTH, self.SCREEN_HEIGHT))
        self.player_pos = [self.SCREEN_WIDTH/2, self.SCREEN_HEIGHT-2*self.PLAYER_SIZE]
        self.game_over = False

        #create enemy 
        self.ENEMY_SIZE = 50 
        self.ENEMY_COLOR = (191, 255, 0) #green color
        self.enemy_pos = [random.randint(0,self.SCREEN_WIDTH-self.ENEMY_SIZE), 0]
        self.enemy_list = [self.enemy_pos] #create a list of enemites
        self.enemy_count = 10

        #set game speed
        self.clock = pygame.time.Clock()
        self.SPEED = 10
        
        #score settings
        self.score = 0
        self.gameFont = pygame.font.SysFont("monospace",35)
        self.score_color = (255,255,0) #yellow

    def drop_enemies(self):
        delay = random.random()
        if len(self.enemy_list) < self.enemy_count and delay < 0.1:
            x_pos = random.randint(0, self.SCREEN_WIDTH-self.ENEMY_SIZE) #create random location
            y_pos = 0
            self.enemy_list.append([x_pos, y_pos]) #add the new enemy to our list

    def draw_enemies(self):
        for enemy in self.enemy_list: #iterate through the list 
           pygame.draw.rect(self.screen, self.ENEMY_COLOR, (enemy[0], enemy[1], self.ENEMY_SIZE, self.ENEMY_SIZE)) #draw enemy

    def draw_player(self):
        pygame.draw.rect(self.screen, self.PLAYER_COLOR, (self.player_pos[0], self.player_pos[1], self.PLAYER_SIZE, self.PLAYER_SIZE)) #draw player

    def update_enemy_positions(self):
        for index, enemy in enumerate(self.enemy_list):
          #set enemy position
            if enemy[1] >= 0 and enemy[1] < self.SCREEN_HEIGHT:
                enemy[1] += self.SPEED
            else:
                 self.enemy_list.pop(index)
                 self.score = self.score + 1 #increase the score

    def update_score(self):
        text = "Score:" + str(self.score) #create text containing score
        label = self.gameFont.render(text,1,self.score_color) #create a label with a color
        self.screen.blit(label,(self.SCREEN_WIDTH-200, self.SCREEN_HEIGHT-40)) #draw label

    def update_level(self):
        if self.score < 20:
            self.SPEED = 5
        elif self.score < 40:
            self.SPEED = 10
        elif self.score < 60:
            self.SPEED = 15
        elif self.score < 100:
            self.SPEED = 25
        else:
            self.SPEED = 35

    def collision_check(self):
        for enemy in self.enemy_list: #iterate through list
             if self.detect_collision(self.player_pos, enemy): #check for collision
                 return True
        return False

    def detect_collision(self, player_pos, enemy_pos):

        #player coordinate
        player_x = player_pos[0]
        player_y = player_pos[1]

        #enemy coodrinate
        enemy_x = enemy_pos[0]
        enemy_y = enemy_pos[1]

        #if player and enemy overlap at anypoint, return true 
        if(enemy_x >= player_x and enemy_x < (player_x + self.PLAYER_SIZE)) or (player_x >= enemy_x and player_x < (enemy_x + self.ENEMY_SIZE)):
             if(enemy_y >= player_y and enemy_y < (player_y + self.PLAYER_SIZE)) or (player_y >= enemy_y and player_y < (enemy_y + self.ENEMY_SIZE)):
                 return True

        return False

    def end_game(self):

        #set the game over 
         self.game_over = True
         player_exit = False

        #create labels for game over screen
         exitFont = pygame.font.SysFont("monospace",80)
         RED = (255,0,0)

         game_over = "Game Over"
         game_over_label = exitFont.render(game_over,1,RED)

         score = "Score:" + str(self.score)
         score_label = exitFont.render(score,1,(RED))
       
        #show game over screen until player quits
         while not player_exit:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    sys.exit() 
            self.screen.fill(self.BACKGROUND_COLOR) 
            self.screen.blit(game_over_label,(250, 50)) 
            self.screen.blit(score_label,(250, 300)) 
            pygame.display.update()


    def run(self):
        while not self.game_over:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    sys.exit()
                
                if event.type == pygame.KEYDOWN:
                    x_coordinate = self.player_pos[0]
                    y_coordinate = self.player_pos[1]

                    if event.key == pygame.K_LEFT:
                        x_coordinate -= self.PLAYER_SIZE #get new coordinate
                        if(x_coordinate < 0): #check if smaller than the width
                            x_coordinate = 0  #set it within bound

                    elif event.key == pygame.K_RIGHT:
                        x_coordinate += self.PLAYER_SIZE #get new coordinate
                        if(x_coordinate > self.SCREEN_WIDTH-self.PLAYER_SIZE): #check if bigger than width
                            x_coordinate = self.SCREEN_WIDTH-self.PLAYER_SIZE #set it within bound

                    self.player_pos = [x_coordinate,y_coordinate] #update the coordinate for player

            self.screen.fill(self.BACKGROUND_COLOR)
            self.drop_enemies()
            self.update_enemy_positions()
            self.update_score()
            self.update_level()

            if self.collision_check():
                self.end_game()

            self.draw_enemies()
            self.draw_player()

            self.clock.tick(30)
            pygame.display.update()




