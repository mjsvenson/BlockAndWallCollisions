# Matthew Svenson 2023
# We are gonna use PyGames for this simulation

import pygame as pg
from sys import exit

CalcSpeed = 0

#Used for eleastic collision calculation
def CollisionCalc(m1, v1, m2, v2):
    finalvel1 = ((box1mass-box2mass)* box1vel + 2*box2mass*box2vel) / (box1mass+box2mass)
    finalvel2 = ((box2mass-box1mass)* box2vel + 2*box1mass*box1vel) / (box1mass+box2mass)
    return (finalvel1, finalvel2)

print("Welcome to the Block Wall Collision Simulation! In this simulation, each pixel is a meter.\n")
print("If you run the simulation with Box 1 as 0 m/s, Box 2 as 1 m/s, Box 1 mass as 1kg, and Box 2 mass as any power of 100, you will notice a strange coincidence with pi!\n")
CalcSpeed = input('How fast do you want the simulation to be? (1 is normal speed)\n')
inbox1vel = input('What is the speed of box 1? (meters per second)\n')
inbox2vel = input('What is the speed of box 2? (meters per second)\n')
inbox1mass = input('What is the mass of box 1? (KG)\n')
inbox2mass = input('What is the mass of box 2? (KG)\n')

#string -> int
CalcSpeed = int(CalcSpeed)
box1vel = int(inbox1vel)
box2vel = int(inbox2vel)
box1mass = int(inbox1mass)
box2mass = int(inbox2mass)
#Correcting for velocity (moving left is negative)
box2vel *= -1

#Pygame window started
pg.init()
print('Simulation beginning')
screen = pg.display.set_mode((1200, 800))
pg.display.set_caption("Block Collision Simulation")
clock = pg.time.Clock()

#images, surfaces, and text
font = pg.font.Font(None, 32)

#Creating images
groundimage = pg.image.load('ground.png').convert()
boximage = pg.image.load('box.png').convert()
wallimage = pg.image.load('wall.png').convert()

text_surface = font.render('Collisions: ', True, 'White')

collisions = 0

#Creating Surfaces
collisions_surface = font.render(str(collisions), True, 'White')
ground_surface = pg.transform.scale(groundimage, (1200,800))
boximage1_surface = pg.transform.scale(boximage, (40+(0.1*box1mass),40+(0.1*box1mass)))
boximage2_surface = pg.transform.scale(boximage, (40+(0.1*box2mass),40+(0.1*box2mass)))
wall_surface =  pg.transform.scale(wallimage, (500,700))

#Creating collision rectangles
wallrect = wall_surface.get_rect(midbottom = (40, 590))
box1rect = boximage1_surface.get_rect(midbottom = (500,585))
box2rect = boximage2_surface.get_rect(midbottom = (1200,585))


while True:
    for event in pg.event.get():
        if event.type == pg.QUIT:
            print('Simulation ended')
            pg.quit()
            exit()
    #This for loop allows the user to increase the speed of calculation if the simulation runs for longer than wanted
    for x in range(CalcSpeed):
        #Placing the surfaces on the screen
        screen.blit(ground_surface, (0,0))
        screen.blit(wall_surface, wallrect)

        screen.blit(boximage1_surface, box1rect)
        box1rect.x += box1vel
        screen.blit(boximage2_surface, box2rect)
        box2rect.x += box2vel
        screen.blit(text_surface, (800, 50))

        #If the boxes collide, find their new velocitys
        if box1rect.colliderect(box2rect):
            box1vel, box2vel = CollisionCalc(box1mass, box1vel, box2mass, box2vel)
            collisions += 1
        #If the left most box collides with the wall, reverse the velocity
        if box1rect.colliderect(wallrect):
            box1vel *= -1
            collisions += 1

        #If the left most box goes inside of the right most box, restart positions of both boxes
        if box1rect.centerx > box2rect.left:
            box2rect.left = 1000  
            box1rect.right = 400

    # draw all our elements
    # update everything
    collisions_surface = font.render(str(collisions), True, 'White')
    screen.blit(collisions_surface, (930, 50))

    pg.display.update()
    clock.tick(60)