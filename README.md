# PythonGame
A simple Python Game 

## Setup/Installation
- This game uses Python3 and Pygame engine in order to run
- Game supports Windows, Mac, Linux
- An IDE is not required 

### Installing Python
#### Step 1. Head over to `https://www.python.org/downloads` to download the latest Python
#### Step 2. Run the Python installer and use default settings
#### Step 3. Verify Python was installed correctly
- On Windows, open the command prompt and run the following command
```bash 
python -V
```
- The Python version should be displayed
```bash
Python 3.x.x
```
- If you do not see a version appear, go back and attempt to reinstall Python with default settings
--- 
### Installing Pygame
#### Step 1. Open the command prompt and enter the following command
```bash
python -m pip install -U pygame --user
```
#### Step 2. To see if works, run the following command
```bash
python -m pygame.examples.aliens
```
- If it works, then you are ready to proceed , otherwise retry Pygame installation

--- 

### Installing PyCharm
#### Step.1 Head over to `https://www.jetbrains.com/pycharm/download/` to download Python Community Edition (Free)
#### Step.2 Run the install and use default settings 
#### Step.3 Open Pycharm and verify installation

--- 

### Download and open the starter project in Pycharm
### Step.1 Head over to `dummy` and click on download 
```bash
dummy dummy 
```

### Step.2 Open Pycharm and open the starter project
```bash
dummy dummy 
```

### Step.3 Verify all starter files exist
- The folder should contain 3 Files that we will be using
- `Main.py` This is the main file that will run our game
- `Game.py` This is where all the Game logic and graphics will be defined, partially filled out
- `Master.py` This holds what the final verison of `Game.py` should look like, use it as reference

## Coding the Game

### Main.py
This is main file that gets executed when we run the program.  
Its purpose is to contain and run our Game that is created in another file.  
Enter the following in `Main.py` 

```Python
from Game import Game

def main():
    game = Game()
    game.run()

if __name__ == "__main__":
    main()
```

### Game.py
This file will define and hold all the game logic and properties. Any changes to the game will need to be done within this file.  
The game is split up into multiple functions that each define a single aspect of the game.  
The functions are the following  
* `__init__` - First function that is called, in here we define all our game settings, screen size , colors and positioning.
* `drop_enemies`- Creates a random number of enemies at various positions and stores them into a list.
* `draw_enemies`- Iterates through the list of enemies and individually draw them on the screen at their given positions.
* `draw_player` - Draws the player on the screen at their given positions.
* `update_enemy_positions` - Iterates through the list of enemies, updates their position on the screen so they fall down.
* `update_score` - Draws a label at the bottom of the screen displaying current score. 
* `update_level` - Increases the speed of falling enemeies corresponding to the current score.
* `collision_check` - Iterates through the list of all enemies, checks if a collision has occured with player. 
* `detect_collision` - Compares an enemy and player position, checks for overlaps, indicating a collision.
* `end_game` - Called when the game is over, updates the screen to show the final score. 
* `run` - Runs the game loop, calls all the seperate functions we created above. Keep tracks of keyboard input from the player.

#### __init__
* This function initializes are game settings such as window size, enemy size, player size, positioning, colors and labels.
* Our screen and width are defined using pixels.  
* Colors are defined with a RGB value, example. (255,255,255). 
* Player and enemy are defined with default size of 50 pixels. 
* Player is positioned at the bottom of the screen in the middle. We use the defined height and widths to calculate the position.
* Enemies are positioned at random locations throughout the screen.
* A clock is defined to keep track of time during the game and to render the drawings. This is similar to (frames per second).
* A default speed value is set, that will dictate how fast the enemeies will initially drop.
* Score will be tracked throughout the game, a point is awarded for every successful dodge of an enemy object.  
Enter the following code  
```python
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
```

#### drop_enemies
* This function generates a random number to be used as a delay. This is so enemies dont spawn all at once. 
* Every enemy has a (x,y) coordinate that dictates its position on the screen. 
* Here these coordinates are calculated using a random number generator. 
* Once an enemy has their coordinates,they are added to our list of enemies.  
Enter the following code  

```python
def drop_enemies(self):
        delay = random.random()
        if len(self.enemy_list) < self.enemy_count and delay < 0.1:
            x_pos = random.randint(0, self.SCREEN_WIDTH-self.ENEMY_SIZE) #create random location
            y_pos = 0
            self.enemy_list.append([x_pos, y_pos]) #add the new enemy to our list
```

#### draw_enemies
* This function simply iterates through the list of enemies and draws each one individually to the screen. 
* In order to draw them, we are using Pygame's built in draw rectangles function. 
* It requires a screen on which to draw on, a color, (x,y) coordinates, and pixel size.

```python 
def draw_enemies(self):
        for enemy in self.enemy_list: #iterate through the list 
           pygame.draw.rect(self.screen, self.ENEMY_COLOR, (enemy[0], enemy[1], self.ENEMY_SIZE, self.ENEMY_SIZE)) #draw enemy
```

#### draw_player
* This function simply draws the player to the screen 
* In order to draw them, we are using Pygame's built in draw rectangles function. 
* It requires a screen on which to draw on, a color, (x,y) coordinates, and pixel size.

```python 
def draw_player(self):
        pygame.draw.rect(self.screen, self.PLAYER_COLOR, (self.player_pos[0], self.player_pos[1], self.PLAYER_SIZE, self.PLAYER_SIZ) #draw player
```

#### update_enemy_positions
* This function iterates through the list of enemies and updates their position.
* We check to see if the enemy position is still within the defined screen dimensions,then move the enemy down.
* If the enemy is no longer on the screen, we remove from the list of enemies and increase the score by one. 

```python 
def update_enemy_positions(self):
        for index, enemy in enumerate(self.enemy_list):
          #set enemy position
            if enemy[1] >= 0 and enemy[1] < self.SCREEN_HEIGHT:
                enemy[1] += self.SPEED
            else:
                 self.enemy_list.pop(index)
                 self.score = self.score + 1 #increase the score
```
#### update_score
* This function draws a score label at the bottom right of the screen. 
* Creates a text label using the gameFont defined earlier, colors it yellow.

```python 
def update_score(self):
        text = "Score:" + str(self.score) #create text containing score
        label = self.gameFont.render(text,1,self.score_color) #create a label with a color
        self.screen.blit(label,(self.SCREEN_WIDTH-200, self.SCREEN_HEIGHT-40)) #draw label
```
#### update_level 
* This function updates the speed of the game corresponding to the player score.
* At certain scores, the speed will be adjusted to go faster and make it more difficult.
* Feel free to modify and change these values to suit your playing style.

```python 
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
```

#### collision_check
* This function iterates through the list of all enemies and compares it against the player's position.
* It uses another helper function called `detect_collision`, that returns true if there is a collision.
* This helper function takes the player position and enemy position as arguments. 
* If the helper function returns true, than a collision has happened.
* If none of the enemies have a collision, than we return false. 

```python
def collision_check(self):
        for enemy in self.enemy_list: #iterate through list
             if self.detect_collision(self.player_pos, enemy): #check for collision
                 return True
        return False
```

#### detect_collision
* This function detects if there is a collision between player and enemy.
* Because the player and enemies are rectangle shapes,it is easier to detect if there is a collision.
* We simply check to see if there is any overlap between the coordinates, if there is then we know a collision has occured, return true
* If no overlap exists, there is no collision and we can return false

```python
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
```
#### end_game
* This function is called when a collision has been detected and the game is over.
* First it sets `game_over` equal to true, which stops the game screen.
* Labels and text are created to show the final score.
* The loop `while not player_exit` is ran continiously until the user exits the program.  
Everything inside this loop gets executed over and over again until an event happens from the user.  
* The part `for event in pygame.event.get():` is a built in function from pygame.  
It it used to detect various events throughout the game. It is continuously running in the background.
* Common type of events are keypresses, keys being held, exiting a window.
* In our case `if event.type == pygame.QUIT` we look for when the player clicks the exit button of the game.
* Lastly it draws a game over screen and displays the final score.

```python
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
```

#### run
* This function is the game loop and is in charge of running all the game logic defined above.
* Runs constantly every second until the player has quit or died. 
* Draws the game screen , enemies and player. 
* Keeps track of player keyboard events, detecting the arrow keys for movement.
* Checks for collisions and increases the score.
* Updates the game screen.

```python
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
```












