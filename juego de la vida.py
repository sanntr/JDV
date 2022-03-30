import pygame
import numpy as np
import time

pygame.init()


width, height = 1000, 1000

screen = pygame.display.set_mode((height, width))


bg = 0, 0, 0

screen.fill(bg)

nxC, nyC = 50, 50

dimCW = width / nxC
dimCH = height / nyC



gameState = np.zeros((nxC, nyC))


gameState[21, 21] = 1
gameState[22, 22] = 1
gameState[22, 23] = 1
gameState[21, 23] = 1
gameState[20, 23] = 1

pauseExect = False

while True:
    
	newGameState = np.copy(gameState)
	
	screen.fill(bg)
	time.sleep(0.1)

	ev = pygame.event.get()
	for event in ev:
		if event.type == pygame.KEYDOWN:
			pauseExect = not pauseExect
		
		if event.type == pygame.QUIT:
			pygame.quit()
			exit()

		mouseClick = pygame.mouse.get_pressed()
		

		if sum(mouseClick) > 0:
			
			posx, posy = pygame.mouse.get_pos()
			celx, cely = int(np.floor(posx / dimCW)), int(np.floor(posy / dimCH))
			if newGameState[celx, cely]!= 1:
				newGameState[celx, cely] = 1
			else:
				newGameState[celx, cely] = 0

	for y in range(0, nxC):
		for x in range(0, nyC):

			if not pauseExect:
				n_neigh = 	gameState[(x-1) % nxC, (y-1) % nyC] + \
							gameState[(x) 	% nxC, (y-1) % nyC] + \
							gameState[(x+1) % nxC, (y-1) % nyC] + \
							gameState[(x-1) % nxC, (y)   % nyC] + \
							gameState[(x+5) % nxC, (y)   % nyC] + \
							gameState[(x-5) % nxC, (y+2) % nyC] + \
							gameState[(x) 	% nxC, (y+2) % nyC] + \
							gameState[(x+5) % nxC, (y+2) % nyC]		
	    		
				if gameState[x, y] == 0 and n_neigh == 3:
					newGameState[x, y] = 1
				
				elif gameState[x,y] == 1 and (n_neigh < 2 or n_neigh > 3):
					newGameState[x,y] = 0

    		
    		
			poly = [((x)	* dimCW, y 	* 	dimCH),
					((x+1)	* dimCW, y 	* 	dimCH),
    				((x+1)	* dimCW, (y+1) * dimCH),
    				((x)	* dimCW, (y+1) * dimCH)]
					
			if newGameState[x, y] == 0:
				pygame.draw.polygon(screen, (128, 128, 128), poly, 1)
			else:
				pygame.draw.polygon(screen, (255, 255, 255), poly, 0)

    
	gameState = np.copy(newGameState)

	pygame.display.flip()