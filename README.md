# Langton_Ant
Python script of the Langton's Ant game. 

Game description: A "virtual ant" is moving in a board/map/plane in function of the color of the tile she is. The tiles on the board are colored variously either black or white. We arbitrarily identify one tile as the "ant" (colored in red). The ant can travel in any of the four cardinal directions at each step it takes. The "ant" moves according to the rules below:
    - At a white square, turn 90° right, flip the color of the square, move forward one unit
    - At a black square, turn 90° left, flip the color of the square, move forward one unit

In this code you can choose from 4 different boards/maps:
  (0) Random board              --> You specify how many black tiles  has the board at the beginning. the tiles are placed randomly
  (1) White board               --> The board is composed by only white tiles
  (2) Chess board               --> The board is composed by black and white tiles as in a chess board
  (3) Black pyramid on the side --> The board is composed by white tiles and a black pyramid on the left side
  (4) White pyramid on the top  --> The board is composed by black tiles and a white inverted pyramid on the top


In function of the board selected, the Langton's ant will move differently.

The configLangAnt.py contain the values of different parameters that the user can update to fit his/her needs.

WARNINIG: It uses the PyGame package


For more information about the Langton's Ant game, check its Wikipedia page (https://en.wikipedia.org/wiki/Langton%27s_ant)
