"""
Clone of 2048 game.
"""

import poc_2048_gui
import random

# Directions, DO NOT MODIFY
UP = 1
DOWN = 2
LEFT = 3
RIGHT = 4

DIRECTIONS = {1:UP,2:DOWN,3:LEFT,4:RIGHT}

# Offsets for computing tile indices in each direction.
# DO NOT MODIFY this dictionary.
OFFSETS = {UP: (1, 0),
           DOWN: (-1, 0),
           LEFT: (0, 1),
           RIGHT: (0, -1)}

def merge(line):
    """
    Function that merges a single row or column in 2048.
    """
    # create new list 
    new = []
    
    switch = 1
    for n1_ in range(0,len(line)):
        
        
        if line[n1_] != 0 and switch == 1:
            new.append(line[n1_])
            switch = 2
        elif line[n1_] != 0 and switch == 2:
            if new[len(new)-1] == line[n1_]:  
                new[len(new)-1] = new[len(new) - 1] + line[n1_]
                switch = 1 
            elif new[len(new)-1] != line[n1_]:
                new.append(line[n1_])
                
              
    # add zeros to equal length of line
    
    while len(line) > len(new):
        new.append(0)
    return new




class TwentyFortyEight:
    """
    Class to run the game logic.
    """

    def __init__(self, grid_height, grid_width):
        self._g_height1_ = grid_height
        self._g_width1_ = grid_width
        #initialize grid of zeros
        self._grid1_ = [ [0 for col in range(self._g_width1_)] for row in range(self._g_height1_)]
        
        #initialize direction indicies
        
        # UP
        self._up1_ = []
        for col in range(self._g_width1_):
            self._up1_.append((0,col))
        # DOWN_
        self._down1_ = []
        for col in range(self._g_width1_):
            self._down1_.append((self._g_height1_ - 1 ,col))
        # LEFT
        self._left1_ = []
        for row in range(self._g_height1_):
            self._left1_.append((row,0))
        # RIGHT
        self._right1_ = []
        for row in range(self._g_height1_):
            self._right1_.append((row,self._g_width1_-1))
        
        self._dict1_ = {UP:self._up1_,DOWN:self._down1_,LEFT:self._left1_,RIGHT:self._right1_}
        
    
    def reset(self):
        """
        Reset the game so the grid is empty except for two
        initial tiles.
        """
        self._grid1_ = [ [0 for col in range(self._g_width1_)] for row in range(self._g_height1_)]
        self.new_tile()
        self.new_tile()

    def __str__(self):
        """
        Return a string representation of the grid for debugging.
        """
        string = ""
        for row in range(self._g_height1_):
            string = "\n".join([string , str(self._grid1_[row])])
        
        return string

    def get_grid_height(self):
        """
        Get the height of the board.
        """
        return self._g_height1_

    def get_grid_width(self):
        """
        Get the width of the board.
        """
        return self._g_width1_

    def move(self, direction):
        """
        Move all tiles in the given direction and add
        a new tile if any tiles moved.
        """
        direction = DIRECTIONS[direction]
        
        length = self._g_width1_
        if direction == 1 or direction == 2:
            length = self._g_height1_
        
            
        points = self._dict1_[direction]
        
        
        new_grid = [ [0 for col in range(self._g_width1_)] for row in range(self._g_height1_)]
        # iterate over idicies
        for point in points:
                
                #build new line to merge
                new_line = []
                for n1_ in range(0,length):
                    # add points to line down OFFSET
                    row = point[0]+OFFSETS[direction][0]*n1_
                    col = point[1]+OFFSETS[direction][1]*n1_
                    
                    new_line.append(self._grid1_[row][col])
                
                new_line = merge(new_line)
                
                # take merged line and place back into original grid
                for n1_ in range(0,length):
                    row = point[0]+OFFSETS[direction][0]*n1_
                    col = point[1]+OFFSETS[direction][1]*n1_
                    new_grid[row][col] = new_line[n1_]
        
        
        # test to see if grid has changed
        changed_dummy = False
        for row in range(self._g_height1_):
            for col in range(self._g_width1_):
                if new_grid[row][col] != self._grid1_[row][col]:
                    changed_dummy = True
                    
        self._grid1_ = new_grid
        
        if changed_dummy == True:          
            self.new_tile()
            
            
    def new_tile(self):
        """
        Create a new tile in a randomly selected empty
        square.  The tile should be 2 90% of the time and
        4 10% of the time.
        """
        new_value = 2
        tile_found = False
        # 2 or 4?
        value = random.randint(1,10)
        if value == 1:
            new_value = 4
            
        # input random location for new_tile, if taken, try again
        timeout = self._g_width1_ * self._g_height1_
        trials = 0
        while tile_found == False:
            # random column
            col = random.randrange(0,self._g_width1_)
            # random row
            row = random.randrange(0,self._g_height1_)
            #check if is taken
            if self._grid1_[row][col] == 0:
                self._grid1_[row][col] = new_value
                tile_found = True
            trials += 1
            
            if trials > timeout:
                tile_found = True
                print "GAME OVER!"
                

    def set_tile(self, row, col, value):
        """
        Set the tile at position row, col to have the given value.
        """
        # replace with your code
        self._grid1_[row][col] = value

    def get_tile(self, row, col):
        """
        Return the value of the tile at position row, col.
        """
        # replace with your code
        return self._grid1_[row][col]
    __repr__ = __str__

    
    


poc_2048_gui.run_gui(TwentyFortyEight(10, 10))
