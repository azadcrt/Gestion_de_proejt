# Simple pygame program


# Import and initialize the pygame library

import pygame

pygame.init()


# Set up the drawing window

ws = 600
screen = pygame.display.set_mode([ws, ws])



# Run until the user asks to quit

running = True



def lect(nbcol, indexx,indexy):
	gap=ws/nbcol
	locx=(gap*indexx)+(gap/2)
	locy=(gap*indexy)+(gap/2)
	loctab = [None] * 3
	loctab[0] = locx
	loctab[1] = locy
	loctab[2] = gap
	return loctab




def grill(x):
	i=0
	while i<x:
		pygame.draw.line(screen, (0,0,0), ((ws/x)*(i+1),0), ((ws/x)*(i+1),600), 2)
		pygame.draw.line(screen, (0,0,0), (0,(ws/x)*(i+1)), (600,(ws/x)*(i+1)), 2)
		i=i+1

def cross(posx,posy,x):
	pygame.draw.line(screen, (255,0,0),(posy - (x/4) ,posx + (x/4)), (posy + (x/4) ,posx - (x/4)), int((x/4)))
	pygame.draw.line(screen, (255,0,0),(posy + (x/4) ,posx - (x/4)), (posy - (x/4) ,posx + (x/4)), int((x/4)))
	pygame.draw.line(screen, (255,0,0),(posy - (x/4) ,posx - (x/4)), (posy + (x/4) ,posx + (x/4)), int((x/4)))
	pygame.draw.line(screen, (255,0,0),(posy - (x/4) ,posx - (x/4)), (posy + (x/4) ,posx + (x/4)), int((x/4)))
		
def circle(posx,posy,x):
	pygame.draw.circle(screen, (0, 0, 255), (posx , posy ), (x/4))
	
	

while running:


    # Did the user click the window close button?

    for event in pygame.event.get():

        if event.type == pygame.QUIT:

            running = False


    # Fill the background with white

    screen.fill((255, 255, 255))


    # Draw a solid blue circle in the center
    loctab = lect(5,0,0)

    grill(int(ws/loctab[2]))
    cross(loctab[0],loctab[1],loctab[2])
    circle(loctab[0],loctab[1],loctab[2])
    

    # Flip the display

    pygame.display.flip()


# Done! Time to quit.

pygame.quit()
