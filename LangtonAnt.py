'''
Squares on a plane are colored variously either black or white. We arbitrarily identify one square as the "ant". The ant can travel in any of the four cardinal directions at each step it takes. The "ant" moves according to the rules below:

    At a white square, turn 90° right, flip the color of the square, move forward one unit
    At a black square, turn 90° left, flip the color of the square, move forward one unit

Developed by Diego Alonso San Alberto under GNU/GPL License
'''
import pygame as pg
import numpy  as np
import time
import sys
import configLangAnt as cfg


# Fct to create a chessboard map. 
# It returns the map and a control list with that keep track of the tile color (0=white, 1=black)
def draw_chessboard(bckgndSurface): 
    boardMap=[]                                         # Map with the color values in each tile
    # Add the caption to the window
    pg.display.set_caption('surface board')

    # Draw a fresh background (a chess board)
    for row in range(cfg.N):                             # Draw each row of the board.
        c_indx = row % 2                                 # Change starting color on each row
        mapRow=[]
        for col in range(cfg.N):                         # Run through cols drawing squares
            #Create a square surface
            surface= pg.Surface((cfg.tile_sz, cfg.tile_sz))
            surface.fill(cfg.colors[c_indx])
            bckgndSurface.blit(surface, (col*cfg.tile_sz, row*cfg.tile_sz) )
            # Add the tile color to the control row 
            mapRow.append(c_indx)

            # now flip the color index for the next square
            c_indx = (c_indx + 1) % 2
        # Add the control row to the control Map
        boardMap.append(mapRow)
    return bckgndSurface, boardMap


def draw_whitePyramidTop_board(bckgndSurface):
    boardMap=[]                                         # Map with the color values in each tile
    # Add the caption to the window
    pg.display.set_caption('surface board')

    # Draw a fresh background (a chess board)
    for row in range(cfg.N):                             # Draw each row of the board.
        
        mapRow=[]
        for col in range(cfg.N):                         # Run through cols drawing squares
            #Create a square surface
            surface= pg.Surface((cfg.tile_sz, cfg.tile_sz))
            if col >= row and col<= cfg.N-row:
                c_indx=0
                surface.fill(cfg.colors[c_indx])
            else:
                c_indx=1
                surface.fill(cfg.colors[c_indx])
            bckgndSurface.blit(surface, (col*cfg.tile_sz, row*cfg.tile_sz) )
            # Add the tile color to the control row 
            mapRow.append(c_indx)

        # Add the control row to the control Map
        boardMap.append(mapRow)
    return bckgndSurface, boardMap


def draw_blackPyramidSide_board(bckgndSurface):
    boardMap=[]                                         # Map with the color values in each tile
    # Add the caption to the window
    pg.display.set_caption('surface board')

    # Draw a fresh background (a chess board)
    for row in range(cfg.N):                             # Draw each row of the board.
        
        mapRow=[]
        for col in range(cfg.N):                         # Run through cols drawing squares
            #Create a square surface
            surface= pg.Surface((cfg.tile_sz, cfg.tile_sz))
            if row >= col or row>= cfg.N-col:
                c_indx=0
                surface.fill(cfg.colors[c_indx])
            else:
                c_indx=1
                surface.fill(cfg.colors[c_indx])
            bckgndSurface.blit(surface, (col*cfg.tile_sz, row*cfg.tile_sz) )
            # Add the tile color to the control row 
            mapRow.append(c_indx)

        # Add the control row to the control Map
        boardMap.append(mapRow)
    return bckgndSurface, boardMap

# Fct to create a whiteboard map
# It returns the map and a control list with that keep track of the tile color (0=white, 1=black)
def draw_whiteboard(bckgndSurface):
    boardMap=[]              #Map with the color values in each row for the board 1st group == row 1  subets num X == row X)

    pg.display.set_caption('Surface white board')

    #Create a square surface
    surface= pg.Surface((cfg.tile_sz, cfg.tile_sz))
    surface.fill(cfg.colors[0])

    # Draw a fresh background (a blank chess board)
    for row in range(cfg.N):           # Draw each row of the board.
        mapRow=[]
        for col in range(cfg.N):       # Run through cols drawing squares
            bckgndSurface.blit(surface, (col*cfg.tile_sz, row*cfg.tile_sz) )
            mapRow.append(0)
        boardMap.append(mapRow)    
    
    #Update the screen
    #pg.display.flip()
    return bckgndSurface, boardMap


def draw_random_board(bckgndSurface):
    #Map with the color values in each row for the board 1st group == row 1  subets num X == row X)   
    boardMap= [[0]*cfg.N for i in range(cfg.N)]
    rowAndColumn=[]     #=[[x values][y values]] == position (3,2) [[...,3][..,2]]
    amountToFill= input('total of black tiles: ')
    
    pg.display.set_caption('Surface random board')
            
    for i in range(amountToFill):
        validSpot= False
        while not validSpot:
            #Fill the board with black squares at random positions
            x= np.random.randint(0, cfg.N-1)    #*cfg.tile_sz             
            y= np.random.randint(0, cfg.N-1)    #*cfg.tile_sz    
            if boardMap[x][y] == 0:
                 #Create a square surface
                surface= pg.Surface((cfg.tile_sz, cfg.tile_sz))
                surface.fill(cfg.colors[1])
                boardMap[x][y]= 1
                validSpot= True
            else:
                validSpot= False

    return bckgndSurface, boardMap


# Fct to create the ant
def create_ant(board):
    #Set the ant position in the middle of the map
    x= (cfg.N/2)*cfg.tile_sz             
    y= (cfg.N/2)*cfg.tile_sz             
    #Create the Ant graphic object
    ant= pg.Surface((cfg.tile_sz,cfg.tile_sz))
    ant.fill([255,0,0])
    pg.display.update()
    
    return ant, ([x,y,cfg.looking[1]]) #The ant starts looking UP


#Fct to update the ant and the board 
def update_game(pos, ant, bckgndBoard, cMap):
    lookingAt= cfg.looking.index(pos[2])    #find the position in looking of the direction we are looking at (0 for LEFT, 1 for UP...)
    temp_X= pos[0]/cfg.tile_sz
    temp_Y= pos[1]/cfg.tile_sz 
    #print('temp x and temp y: (%s,%s) --len(cMap): %s -- len(cMap[0]): %s'%(temp_X, temp_Y, len(cMap), len(cMap[0])))
    if cMap[temp_X][temp_Y] == 0:
        #the ant is in a white cell
        #turn right, flip color cell and move 1 cell forward

        #flip the color index for the next square
        cMap[temp_X][temp_Y]= (cMap[temp_X][temp_Y] + 1) % 2

        if lookingAt == len(cfg.looking)-1:
            pos[2]= cfg.looking[0]
            pos= move_ant(pos)
        else:
            pos[2]= cfg.looking[lookingAt+1]
            pos= move_ant(pos)

    else: 
        #the ant is in a black cell
        #turn left, flip color cell and move 1 cell forward

        #flip the color index for the next square
        cMap[temp_X][temp_Y]= ( cMap[temp_X][temp_Y] + 1) % 2
            

        if lookingAt == 0:
            pos[2]= cfg.looking[len(cfg.looking)-1]
            pos= move_ant(pos)
        else:
            pos[2]= cfg.looking[lookingAt-1]
            pos= move_ant(pos)
    
    #Update the color in the tile the ant is (before it moves to the new tile)
    tile= pg.Surface((cfg.tile_sz, cfg.tile_sz))
    tile.fill(cfg.colors[cMap[temp_X][temp_Y]])
    bckgndBoard.blit(tile, (temp_X*cfg.tile_sz, temp_Y*cfg.tile_sz))
    
    #Move ant to the new position
    bckgndBoard.blit(ant, (pos[0], pos[1]))

    #update board
    pg.display.flip()

    return pos, bckgndBoard, cMap


# Fct to set the new position of the ant in the map
def move_ant_2(pos):  
    if pos[2]== cfg.looking[0]:
        pos[0]-= cfg.tile_sz
        if pos[0] <= 0:
            pos[0]+= cfg.surface_sz
    elif pos[2]== cfg.looking[1]:
        pos[1]-= cfg.tile_sz
        if pos[1] <= 0:
            pos[1]+= cfg.surface_sz
    elif pos[2]== cfg.looking[2]:
        pos[0]+= cfg.tile_sz
        if pos[0] >= cfg.surface_sz:
            pos[0]-= cfg.surface_sz
    elif pos[2]== cfg.looking[3]:
        pos[1]+= cfg.tile_sz
        if pos[1] >= cfg.surface_sz:
            pos[0]-= cfg.surface_sz
    #Check if the ant has reached a border of the map
    #pos= reach_border(pos)
    return pos

# Fct to set the new position of the ant in the map
def move_ant(pos):  
    if pos[2]== cfg.looking[0]:
        pos[0]-= cfg.tile_sz
    elif pos[2]== cfg.looking[1]:
        pos[1]-= cfg.tile_sz
    elif pos[2]== cfg.looking[2]:
        pos[0]+= cfg.tile_sz
    elif pos[2]== cfg.looking[3]:
        pos[1]+= cfg.tile_sz
    
    #Check if the ant has reached a border of the map
    pos= reach_border(pos)
    return pos

#Fct to cross from one side of the board/map to the one in the other side
def reach_border(pos):
    sz= cfg.surface_sz-cfg.tile_sz
    #check if the ant has reached the top or bottom border
    if pos[0] <= 0:
        pos[0]= sz#- pos[0]
    elif pos[0] >= sz:
        pos[0]= 0 #pos[0]- sz
    #check if the ant has reached the left or right border
    if pos[1] <= 0:
        pos[1]= sz#- pos[0]
    elif pos[1] >= sz:
        pos[1]= 0#sz- pos[1]
    return pos


# ---- MAIN SCRIPT -----


# Create map in function of the option selected
print ("MAP OPTIONS")
print (' (0) Random board')
print (' (1) White board')
print (' (2) Chess board ')
print (' (3) draw_blackPyramidSide_board ')
print (' (4)  draw_whitePyramidTop_board ')
option= input('Choose map option:')

pg.init()
colorMap=[]

# Create the window (width, height)
board = pg.display.set_mode((cfg.surface_sz, cfg.surface_sz))

if option == 0:
    board, colorMap= draw_random_board(board)   #to create a random board map
elif option == 1:
    board, colorMap= draw_whiteboard(board)    #to create a whiteboard map
elif option == 2:
    board, colorMap= draw_chessboard(board)     #To create a chessboard map
elif option == 3:
    board, colorMap= draw_blackPyramidSide_board(board)     #To create a chessboard map
elif option == 4:
    board, colorMap=  draw_whitePyramidTop_board(board)     #To create a chessboard map
else:
    print('option not valid!!')
    

#create ant
antDraw, antPos= create_ant(board)
pg.display.update()

totalIter=0
guiCmd= 1
while (True):
    if guiCmd != 0: 
        for i in range(cfg.ITERATIONS):
            #Look for an event from keyboard, mouse, etc.
            ev = pg.event.poll()
            if ev.type == pg.QUIT:
                break
            else:
                antPos, board, colorMap= update_game(antPos, antDraw, board, colorMap)
                time.sleep(0.02)
        totalIter+=i    
        print('Total iterations: %s '%totalIter)
        guiCmd= input('Press: (0) for quit or (1) for Continue ')
    else:
        sys.exit()