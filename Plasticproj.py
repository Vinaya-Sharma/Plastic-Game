import pygame 
import os
import random
import time 

b = "not excited"
while b!="excited":
    b = input("Hey are you ready to play plastic pollution clean up? \nTry to collect all the plastic water bottles before 15 secounds are up.\nGood luck and type EXCITED to begin!").lower()

pygame.init()

endtime = 0 
startime = 0 

WIDTH, HEIGHT = 500, 500
WHITE = (255,50,0)
FPS = 60
PLAYERW = 50
PLAYERH = 100 
BOTTLEW = 30
BOTTLEH = 50
VEL = 2

WIN = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Plasic Game")
PLAYER = pygame.image.load(os.path.join('Assets', "GUYFINAL.png"))
player  = pygame.transform.scale(PLAYER, (PLAYERW,PLAYERH))
BOTTLE = pygame.image.load(os.path.join('Assets', 'WATERBOTTLE.png'))
bottle = pygame.transform.scale(BOTTLE, (BOTTLEW,BOTTLEH))

    
    
bco = []
def bottle_co():
    for i in range (10):
        x = 300
        y = 300
        while x == 300 or y == 100:
            x = random.randint(0,500)
            y = random.randint(0,500)

        bco.append((x,y))
bottle_co()

def draw_window(character):
    WIN.fill(WHITE)
    WIN.blit(player, (character.x, character.y))
    
    for co in bco:
        WIN.blit(bottle, co)
    pygame.display.update()

def keyc(character, keys_pressed):

    if keys_pressed[pygame.K_LEFT]: character.x -= VEL
    if keys_pressed[pygame.K_RIGHT]: character.x += VEL
    if keys_pressed[pygame.K_UP]: character.y -= VEL
    if keys_pressed[pygame.K_DOWN]: character.y += VEL

def tcheck(bco, character):
    for co in bco:
        cco = (character.x, character.y)
        
        if cco[0] > co[0]-20 and cco[0] < co[0]+20 and cco[1] > co[1]-20 and cco[1] < co[1]+20:
            bco.remove(co)

startime = time.time()            
def main():
    
    
    character = pygame.Rect(0, 100, PLAYERW, PLAYERH)
    clock = pygame.time.Clock()
    run = True
    while run:
        clock.tick(FPS)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
        
        keys_pressed = pygame.key.get_pressed()
        keyc(character, keys_pressed)
        tcheck(bco, character)
        
        draw_window(character)
        if len(bco)==0:
            endtime = time.time()
            e = endtime
            run = False
            for i in range(3):print()
            print("Congratulations! You were able to collect a ton of plastic waste in your local area")
            print("Unfortunately at least 8 million tons of plastic end up in our oceans every year, meaning we must do more than just one ocean clean up.") 
            print("Try eliminating the use of disposable plastics, Stop buying bottled water, Recycle and best of all raise awareness and don’t litter.")
            print("Your small actions can make a huge difference, just remember we must change our habits before it is too late!")
            print()
            print("Yay you beat the timer it only took you " + str(e-startime) + " secounds")
        end = time.time()
        if (end > startime + 15):
            run = False 
            print("\n\nOh no you went over the time limit :(\n")
    pygame.quit()
if __name__ == "__main__":
    main()

