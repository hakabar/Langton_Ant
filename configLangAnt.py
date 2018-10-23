'''
Configuration file containing all the parameters required in the LangtonAnt.py script

Code developed by Diego Alonso San Alberto. 
'''

looking= ['LEFT','UP', "RIGHT", 'DOWN']         # Directions where the ant is able to go
N = 100                                        # This is an NxN chess board.
surface_sz = 800                                # Size (in pixels) of the popup window containig the graphics
tile_sz= surface_sz/N                           # Size of a tile/cell in the board
colors = [(255,255,255), (0,0,0)]               # Set up colors [white, black] fro the board

ITERATIONS= 20000