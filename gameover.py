import pygame
from pygame.locals import *
import sys
import time
import pyganim
import pygame.mixer
import splashscreen

pygame.font.init()
pygame.mixer.init(22050,-16,1,4096)
#sound
sound=pygame.mixer.Sound('fireman.wav')
#time
minutes = 0
seconds = 0
milliseconds = 0
#colors
RED      = ( 255,   0,   0)
BLACK    = (   0,   0,   0)
WHITE    = ( 255, 255, 255)
GREEN    = (  0, 255,   0 )
DARKGREEN= (  0, 155,   0 )
DARKGRAY = ( 40,  40,  40 )
skyblue  = ( 126, 192, 238)
black    = (  0 ,  0 ,  0 )
white    = ( 255, 255, 255)
red      = ( 255,   0,  0 )
blue     = (   0,   0, 255)
BGCOLOR  = (   0,   0,   0)
#screen
window=pygame.display.set_mode((800,600))
font = pygame.font.SysFont(None, 48)
BASICFONT = font
DISPLAYSURF=window
screen = pygame.display.set_mode((800,600))
font = pygame.font.SysFont(None, 48)
BASICFONT = font



FPSCLOCK=pygame.time.Clock()
# Screen dimensions
SCREEN_WIDTH  = 800
SCREEN_HEIGHT = 600
WINDOWWIDTH=800
WINDOWHEIGHT=500

#terminate
def terminate():
        pygame.quit()
        sys.exit()
#game over
def showGameOverScreen(minutes,seconds):
    gameOverFont = pygame.font.Font('freesansbold.ttf', 100)
    gameSurf = gameOverFont.render('Game', True, red)
    overSurf = gameOverFont.render('Over', True, red)
    gameRect = gameSurf.get_rect()
    overRect = overSurf.get_rect()
    gameRect.midtop = (WINDOWWIDTH / 2, 10)
    overRect.midtop = (WINDOWWIDTH / 2, gameRect.height + 35)
    
    DISPLAYSURF.blit(gameSurf, gameRect)
    DISPLAYSURF.blit(overSurf, overRect)
    #message_to_screen("Time: "+str(minutes)+ ":"+str(seconds),black)
    message_to_screen4("Better luck next time.",black)

    drawPressKeyMsg()
    pygame.display.update()
    pygame.time.wait(500)
    checkForKeyPress() 
    
    while True:
        if checkForKeyPress():
            main()
            return
#check for key press
def checkForKeyPress():
    if len(pygame.event.get(QUIT)) > 0:
        terminate()
    keyUpEvents = pygame.event.get(KEYUP)
    if len(keyUpEvents) == 0:
        return None
    if keyUpEvents[0].key == K_ESCAPE:
        terminate()
    return keyUpEvents[0].key
#drawscore on screen
def drawScore(minutes,seconds):
    scoreSurf = BASICFONT.render(str(minutes)+ ":"+str(seconds), True, black)
    scoreRect = scoreSurf.get_rect()
    scoreRect.topleft = (800 - 80, 10)
    DISPLAYSURF.blit(scoreSurf, scoreRect)
#you won screen
def showwin(minutes,seconds):
    gameOverFont = pygame.font.Font('freesansbold.ttf', 100)
    gameSurf = gameOverFont.render('YOU', True, red)
    overSurf = gameOverFont.render('WON', True, red)
    gameRect = gameSurf.get_rect()
    overRect = overSurf.get_rect()
    gameRect.midtop = (WINDOWWIDTH / 2, 10)
    overRect.midtop = (WINDOWWIDTH / 2, gameRect.height + 10 + 25)

    DISPLAYSURF.blit(gameSurf, gameRect)
    DISPLAYSURF.blit(overSurf, overRect)
    high_minutes=get_high_minutes(minutes,seconds)
    high_seconds=get_high_seconds(minutes,seconds)
    if minutes<high_minutes:
            
        # We do! Save to disk
         message_to_screen1("New Best Time is "+str(high_minutes)+":"+str(high_seconds),black)
         save_high_minutes(minutes)
         save_high_seconds(seconds)
    elif minutes==high_minutes:
          if seconds<high_seconds:
                 message_to_screen1("New Best Time is "+str(minutes)+":"+str(seconds),black)
                 save_high_minutes(minutes)
                 save_high_seconds(seconds)
    else:
         message_to_screen("Better luck next time.",black)

                    
    
    message_to_screen("Time: "+str(minutes)+ ":"+str(seconds),black)
    drawPressKeyMsg()
    pygame.display.update()
    pygame.time.wait(500)
    checkForKeyPress() 
    
    while True:
        if checkForKeyPress():
            main()
            return
#draw press any key msg
def get_high_minutes(minutes,seconds):
        # Default high score
        high_minutes = 59

        # Try to read the high score from a file
        try:
            high_minutes_file = open("high_minutes.txt", "r")
            high_minutes = int(high_minutes_file.read())
            high_minutes_file.close()
            high_seconds_file = open("high_seconds.txt", "r")
            high_seconds = int(high_seconds_file.read())
            high_seconds_file.close()
            
            message_to_screen3("Last Best Time is: "+str(high_minutes)+ ":"+str(high_seconds),black)
        except IOError:
        # Error reading file, no high score
            message_to_screen1("There is no Best Time yet.",black)
        except ValueError:
        # There's a file there, but we don't understand the number.
            print("I'm confused. Starting with no high score.")

        return high_minutes

def get_high_seconds(minutes,seconds):
        # Default high score
        high_seconds = 59

        # Try to read the high score from a file
        try:
            high_minutes_file = open("high_minutes.txt", "r")
            high_minutes = int(high_minutes_file.read())
            high_minutes_file.close()
            high_seconds_file = open("high_seconds.txt", "r")
            high_seconds = int(high_seconds_file.read())
            high_seconds_file.close()
            message_to_screen3("Last Best Time is: "+str(high_minutes)+ ":"+str(high_seconds),black)
        except IOError:
        # Error reading file, no high score
            message_to_screen1("There is no Best Time yet.",black)
        except ValueError:
        # There's a file there, but we don't understand the number.
            print("I'm confused. Starting with No Best Time.")

        return high_seconds
def save_high_minutes(new_high_minutes):
        try:
                # Write the file to disk
            high_minutes_file = open("high_minutes.txt", "w")
            high_minutes_file.write(str(new_high_minutes))
            high_minutes_file.close()
        except IOError:
                # Hm, can't write it.
            print("Unable to save the high minutes.")
def save_high_seconds(new_high_seconds):
        try:
                # Write the file to disk
            high_seconds_file = open("high_seconds.txt", "w")
            high_seconds_file.write(str(new_high_seconds))
            high_seconds_file.close()
        except IOError:
                # Hm, can't write it.
            print("Unable to save the high seconds.")
            

    
def drawPressKeyMsg():
    pressKeySurf = BASICFONT.render('Press any key to play.', True, blue)
    pressKeyRect = pressKeySurf.get_rect()
    pressKeyRect.topleft = (WINDOWWIDTH - 500, WINDOWHEIGHT - 20)
    DISPLAYSURF.blit(pressKeySurf, pressKeyRect)
#start screen
def showStartScreen():
    titleFont = pygame.font.Font(None, 100)
    titleSurf1 = titleFont.render('Jumpy', True, WHITE, skyblue)
    titleSurf2 = titleFont.render('Jumpy', True, blue)

    degrees1 = 0
    degrees2 = 0
    while True:
        DISPLAYSURF.fill(white)
        rotatedSurf1 = pygame.transform.rotate(titleSurf1, degrees1)
        rotatedRect1 = rotatedSurf1.get_rect()
        rotatedRect1.center = (WINDOWWIDTH / 2, WINDOWHEIGHT / 2)
        DISPLAYSURF.blit(rotatedSurf1, rotatedRect1)

        rotatedSurf2 = pygame.transform.rotate(titleSurf2, degrees2)
        rotatedRect2 = rotatedSurf2.get_rect()
        rotatedRect2.center = (WINDOWWIDTH / 2, WINDOWHEIGHT / 2)
        DISPLAYSURF.blit(rotatedSurf2, rotatedRect2)

        drawPressKeyMsg()

        if checkForKeyPress():
            pygame.event.get() 
            return
        pygame.display.update()
        FPSCLOCK.tick(10)
        degrees1 += 3 # rotate by 3 degrees each frame
        degrees2 += 7 # rotate by 7 degrees each frame
#key pressed        
def keyPressed(inputKey):
    keysPressed = pygame.key.get_pressed()
    if keysPressed[inputKey]:
        return True
    else:
        return False
#msg to screen
def message_to_screen(msg,color):
      font=pygame.font.SysFont(None, 60)
      screen_text=font.render(msg,True,skyblue)
      window.blit(screen_text,[300,300])
      
def message_to_screen1(msg,color):
      font=pygame.font.SysFont(None, 45)
      screen_text=font.render(msg,True,skyblue)
      window.blit(screen_text,[250,350])
      
def message_to_screen2(msg,color):
      font=pygame.font.SysFont(None, 45)
      screen_text=font.render(msg,True,skyblue)
      window.blit(screen_text,[300,430])

def message_to_screen3(msg,color):
      font=pygame.font.SysFont(None, 45)
      screen_text=font.render(msg,True,skyblue)
      window.blit(screen_text,[250,400])

def message_to_screen4(msg,color):
      font=pygame.font.SysFont(None, 45)
      screen_text=font.render(msg,True,skyblue)
      window.blit(screen_text,[250,300])


class Player(pygame.sprite.Sprite):
    """ This class represents the  player
        controls. """
    change_x=0
    change_y=0
    level=None
    
    # -- Methods
    def __init__(self):
        """ Constructor function """
        
        # Call the parent's constructor
        pygame.sprite.Sprite.__init__(self)
 
        width = 40
        height = 60
        
        #image of player        
        self.image = pygame.image.load("CRONO_BACK.gif").convert()
         
        # Set a referance to the image rect.
        self.rect = self.image.get_rect()
 
        # Set speed vector of player
        self.change_x = 0
        self.change_y = 0
 
        # List of sprites we can bump against
        self.level = None
 
 
    def update(self):
        """ Move the player. """
        # Gravity
        self.calc_grav()
 
        # Move left/right
        self.rect.x += self.change_x
 
        # See if we hit anything
        block_hit_list = pygame.sprite.spritecollide(self, self.level.platform_list, False)
        for block in block_hit_list:
            if self.change_x > 0:
                self.rect.right = block.rect.left
            elif self.change_x < 0:
                # Otherwise if we are moving left, do the opposite.
                self.rect.left = block.rect.right
 
        # Move up/down
        self.rect.y += self.change_y
 
        block_hit_list = pygame.sprite.spritecollide(self, self.level.platform_list, False)
        for block in block_hit_list:
 
            # Reset our position based on the top/bottom of the object.
            if self.change_y > 0:
                self.rect.bottom = block.rect.top
            elif self.change_y < 0:
                self.rect.top = block.rect.bottom
 
            # Stop our vertical movement
            self.change_y = 0
 
    def calc_grav(self):
        """ Calculate effect of gravity. """
        if self.change_y == 0:
            self.change_y = 1
                
        else:
            self.change_y += .35
        # See if we are on the ground.
        if self.rect.y >= SCREEN_HEIGHT - self.rect.height and self.change_y >= 0:
            self.change_y = 0
            self.rect.y = SCREEN_HEIGHT - self.rect.height
        if self.rect.y>550 :
                showGameOverScreen(minutes,seconds)
                
    def jump(self):
        """ Called when user hits 'jump' button. """
 
        self.rect.y += 2
        platform_hit_list = pygame.sprite.spritecollide(self, self.level.platform_list, False)
        self.rect.y -= 2
        
        if len(platform_hit_list) > 0 or self.rect.bottom >= SCREEN_HEIGHT:
            self.change_y = -10
 
    def go_left(self):
        """ Called when the user hits the left arrow. """
        self.change_x = -6
        
    def go_right(self):
        """ Called when the user hits the right arrow. """
        self.change_x = 6
        
    def stop(self):
        self.change_x = 0
        
    def checkover(self,minutes,seconds):
           if self.rect.y>520 :
                        showGameOverScreen(minutes,seconds)      
    def checkwin(self,minutes,seconds):
        if self.rect.y<90 and self.rect.x<10 :
                showwin(minutes,seconds)

class Platform(pygame.sprite.Sprite):
 
    def __init__(self, width, height):
        pygame.sprite.Sprite.__init__(self) 
        self.image = pygame.Surface([width, height])
        self.image.fill(GREEN)
        self.rect = self.image.get_rect()


class MovingPlatform(Platform):
    """ This is a fancier platform that can actually move. """
    change_x = 0
    change_y = 0

    boundary_top = 0
    boundary_bottom = 0
    boundary_left = 0
    boundary_right = 0

    player = None

    level = None

    def update(self):
        """ Move the platform.
            If the player is in the way, it will shove the player
            out of the way. This does NOT handle what happens if a
            platform shoves a player into another object. Make sure
            moving platforms have clearance to push the player around
            or add code to handle what happens if they don't. """

        # Move left/right
        self.rect.x += self.change_x

        # See if we hit the player
        hit = pygame.sprite.collide_rect(self, self.player)
        if hit:
            
            if self.change_x < 0:
                self.player.rect.right = self.rect.left
            else:
                # Otherwise if we are moving left, do the opposite.
                self.player.rect.left = self.rect.right

        # Move up/down
        self.rect.y += self.change_y

        # Check and see if we the player
        hit = pygame.sprite.collide_rect(self, self.player)
        if hit:
            
            if self.change_y < 0:
                self.player.rect.bottom = self.rect.top
            else:
                self.player.rect.top = self.rect.bottom

        # Check the boundaries and see if we need to reverse
        # direction.
        if self.rect.bottom > self.boundary_bottom or self.rect.top < self.boundary_top:
            self.change_y *= -1

        cur_pos = self.rect.x - self.level.world_shift
        if cur_pos < self.boundary_left or cur_pos > self.boundary_right:
            self.change_x *= -1

        
class Level(object):
    platform_list = None
    enemy_list = None
 
    # Background image
    background = None
    world_shift = 0
    level_limit = -1000
    def __init__(self, player):
        self.platform_list = pygame.sprite.Group()
        self.enemy_list = pygame.sprite.Group()
        self.player = player
 
    # Update everythign on this level
    def update(self):
        """ Update everything in this level."""
        self.platform_list.update()
        self.enemy_list.update()
 
    def draw(self, screen):
        """ Draw everything on this level. """
 
        # Draw the background
        screen.fill(WHITE)
         
        # Draw all the sprite lists that we have
        self.platform_list.draw(screen)
        self.enemy_list.draw(screen)
        
    def shift_world(self, shift_x):
        """ When the user moves left/right and we need to scroll everything:
        """

        # Keep track of the shift amount
        self.world_shift += shift_x

        # Go through all the sprite lists and shift
        for platform in self.platform_list:
            platform.rect.x += shift_x

        for enemy in self.enemy_list:
            enemy.rect.x += shift_x

 
# Create platforms for the level
class Level_01(Level):
    """ Definition for level 1. """
 
    def __init__(self, player):
        """ Create level 1. """
 
        # Call the parent constructor
        Level.__init__(self, player)
        self.level_limit = -1500

        # Array with width, height, x, and y of platform
        level = [[90, 20, 0, 65],[40, 20, 600, 70],
                 [40, 20, 400, 100],
                 [40, 20, 700, 200],
                 [40, 20, 600, 350],
                 
                 [40, 20, 650, 500]
                 ]
 
        # Go through the array above and add platforms
        for platform in level:
            block = Platform(platform[0], platform[1])
            block.rect.x = platform[2]
            block.rect.y = platform[3]
            block.player = self.player
            self.platform_list.add(block)
        # Add a custom moving platform
        block = MovingPlatform(40, 20)
        block.rect.x = 200
        block.rect.y = 300
        block.boundary_top = 225
        block.boundary_bottom = 500
        block.change_y = -1
        block.player = self.player
        block.level = self
        self.platform_list.add(block)


def runGame():
    minutes = 0
    seconds = 0
    milliseconds = 0
    # Create the player
    player = Player()
 
    # Create all the levels
    level_list = []
    level_list.append( Level_01(player) )
 
    # Set the current level
    current_level_no = 0
    current_level = level_list[current_level_no]
 
    active_sprite_list = pygame.sprite.Group()
    player.level = current_level
    
    player.rect.x = 650
    player.rect.y = 450
    active_sprite_list.add(player)
    
    door = pygame.image.load("door2.png").convert()

    #Loop until the user clicks the close button.
    done = False
        
    fireAnim = pyganim.PygAnimation([('testimages/flame_a_0001.png', 0.1),
                                 ('testimages/flame_a_0002.png', 0.1),
                                 ('testimages/flame_a_0003.png', 0.1),
                                 ('testimages/flame_a_0004.png', 0.1),
                                 ('testimages/flame_a_0005.png', 0.1),
                                 ('testimages/flame_a_0006.png', 0.1)])

    fireAnim2=fireAnim.getCopy()
        
    fireAnim2.smoothscale((200, 200))
    
    fireAnim.rate = 1.2 
    # start playing the fire animations
    fireAnim.play()
    fireAnim2.play()
    
    # Used to manage how fast the screen updates
    clock = pygame.time.Clock()
    
    # -------- Main Program Loop -----------
    while not done:
        sound.play()
        player.checkwin(minutes,seconds)
        player.checkover(minutes,seconds)
        for event in pygame.event.get():
            
            if event.type == pygame.QUIT: 
                terminate()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LEFT:
                    player.go_left()                   
                if event.key == pygame.K_RIGHT:
                    player.go_right()
                if event.key == pygame.K_UP:
                    player.jump()
                if event.key == K_ESCAPE:
                    showGameOverScreen(minutes,seconds)
            if event.type == pygame.KEYUP:
                if event.key == pygame.K_LEFT and player.change_x < 0:
                    player.stop()
                if event.key == pygame.K_RIGHT and player.change_x > 0:
                    player.stop()
                if event.key == K_ESCAPE:
                    showGameOverScreen(minutes,seconds)
 
        # Update the player.
        active_sprite_list.update()
 
        # Update items in the level
        current_level.update()
 
        # If the player gets near the right side, shift the world left (-x)
        if player.rect.right > SCREEN_WIDTH:
            player.rect.right = SCREEN_WIDTH
 
        # If the player gets near the left side, shift the world right (+x)
        if player.rect.left < 0:
            player.rect.left = 0
        screen.blit(door,(10,10))
              
        current_level.draw(screen)
        screen.blit(door,(10,10))
        active_sprite_list.draw(screen)
        
        fireAnim2.blit(screen, (-75,480))              
        fireAnim2.blit(screen, (0, 480))
        fireAnim2.blit(screen, (75,480))
        fireAnim2.blit(screen, (150,480))
        
        fireAnim2.blit(screen, (225,480))        
        fireAnim2.blit(screen, (300,480))
        fireAnim2.blit(screen, (375,480))
        fireAnim2.blit(screen, (450,480))
         
        fireAnim2.blit(screen, (525,480))
        fireAnim2.blit(screen, (600,480))
        fireAnim2.blit(screen, (675,480))
        drawScore(minutes,seconds) 
        pygame.display.update()
                
        if milliseconds > 1000:
                seconds += 1
                milliseconds -= 1000
        if seconds > 60:
                minutes += 1
                seconds -= 60
       
        drawScore(minutes,seconds)
        milliseconds += FPSCLOCK.tick_busy_loop(60)

        clock.tick(60)
 
        pygame.display.flip()
 
def main():
    """ Main Program """
    pygame.init()
    pygame.font.init()
    # Set the height and width of the screen
    size = [SCREEN_WIDTH, SCREEN_HEIGHT]
    screen = pygame.display.set_mode(size)
    font = pygame.font.SysFont(None, 48)
    BASICFONT = font
    pygame.display.set_caption('jumpy')
    splashscreen.splash_screen()
    showStartScreen()
    while True:
        runGame()
        showGameOverScreen(minutes,seconds)
         
if __name__ == "__main__":
    main()
