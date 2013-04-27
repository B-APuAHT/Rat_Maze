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

    def __str__(self):
        """ (Rat) -> str

        Return a string representation of the rat.

        >>> rat = Rat('J', 4, 3)
        >>> rat.__str__()
        'J at (4, 3) ate 0 sprouts.'
        """

        return '{0} at ({1}, {2}) ate {3} sprouts.'.format(
            self.symbol, self.row, self.col, self.num_sprouts_eaten)

    # Write your Rat methods here.

class Maze:
    """ A 2D maze. """

    # Write your Maze methods here.
if __name__ == '__main__':
    import doctest
    doctest.testmod()
