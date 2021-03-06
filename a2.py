# Do not import any modules. If you do, the tester may reject your submission.

# Constants for the contents of the maze.

# The visual representation of a wall.
WALL = '#'

# The visual representation of a hallway.
HALL = '.'

# The visual representation of a brussels sprout.
SPROUT = '@'

# Constants for the directions. Use these to make Rats move.

# The left direction.
LEFT = -1

# The right direction.
RIGHT = 1

# No change in direction.
NO_CHANGE = 0

# The up direction.
UP = -1

# The down direction.
DOWN = 1

# The letters for rat_1 and rat_2 in the maze.
RAT_1_CHAR = 'J'
RAT_2_CHAR = 'P'


class Rat:
    """ A rat caught in a maze. """

    def __init__(self, symbol, row, col):
        """ (Rat, str, int, int) -> NoneType

        The Rat with name and location information
        """

        self.symbol = symbol;
        self.row = row;
        self.col = col;
        self.num_sprouts_eaten = 0;
        
    def set_location(self, rw, cl):
        """ (Rat, int, int) -> NoneType

        Set the rat's row and col instance variables to the given row and column.
        """

        self.row = rw
        self.col = cl

    def eat_sprout(self):
        """ (Rat) -> NoneType

        Add one to the rat's count of sprouts.
        """

        self.num_sprouts_eaten += 1
        
    def __str__(self):
        """ (Rat) -> str

        Return a string representation of the rat.

        >>> rat = Rat('J', 4, 3)
        >>> rat.__str__()
        'J at (4, 3) ate 0 sprouts.'
        """

        return '{0} at ({1}, {2}) ate {3} sprouts.'.format(
            self.symbol, self.row, self.col, self.num_sprouts_eaten)


class Maze:
    """ A 2D maze. """

    def __init__(self, maze, rat_1, rat_2):
        """ (Maze, list of list of str, Rat, Rat) -> NoneType

        Initialize the maze with rats.
        """

        self.maze = maze
        self.rat_1 = rat_1
        self.rat_2 = rat_2
        self.num_sprouts_left = sum([x.count(SPROUT) for x in maze])
        self.maze[self.rat_1.row][self.rat_1.col] = self.rat_1.symbol
        self.maze[self.rat_2.row][self.rat_2.col] = self.rat_2.symbol

    def is_wall(self, row, col):
        """ (Maze, int, int) -> bool

        Return true if and only if there is a wall at the given row and column of the maze.
        """

        return self.maze[row][col] == WALL
    
    def get_character(self, row, col):
        """ (Maze, int, int) - > str

        Return the charatcer in the maze at the given row and column
        """

        return self.maze[row][col] if self.maze[row][col] != Rat else HALL

    def move(self, rat, ver_direct, hor_direct):
        """ (Maze, Rat, int, int) -> bool

        Return true if and only if there isn't a wall in the way.
        """

        rw = rat.row + ver_direct
        cl = rat.col + hor_direct
        if not self.is_wall(rw, cl) and (ver_direct != 0 or hor_direct != 0):
            if self.maze[rw][cl] == SPROUT:
                if self.num_sprouts_left > 0:
                    self.num_sprouts_left -= 1
                    rat.eat_sprout()
                    self.maze[rw][cl] = HALL
            self.maze[rw - ver_direct][cl - hor_direct] = HALL
            self.maze[rw][cl] = rat.symbol
            rat.set_location(rw, cl)
        return not self.is_wall(rw, cl)
            
    def __str__(self):
        """ (Maze) -> str

        Return a string representation of the Maze class object.
        """

        return "".join(["".join(x)+'\n' for x in self.maze]) + \
               self.rat_1.__str__() + '\n' + self.rat_2.__str__()

