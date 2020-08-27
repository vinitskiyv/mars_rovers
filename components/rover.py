import copy
from components.exceptions import (
    MoveRoverLocationException,
    InitialRoverLocationException,
)


class Rover:
    """Rover receives raw position and terrain data (plateau)

    :param plato: obj Plato
           coordinates: (str) - A rover's position is represented by a
                                combination of an x and y co-ordinates and a
                                letter representing one of the four cardinal
                                compass points, e.g. '0, 0, N'
    """

    DIRECTIONS = ['N', 'E', 'S', 'W', ]

    def __init__(self, plato, coordinates: str):
        self.plato = plato
        self.coordinates, self.direction = self.__location(coordinates)

    def __location(self, coordinates: str):
        """Sets initial location of the rover

        :param coordinates: str '0, 0, N'"""
        try:
            coordinates = coordinates.split(' ')
            return (self.plato.check(list(map(int, coordinates[:2]))),
                    coordinates[2].upper())
        except Exception as exc:
            raise InitialRoverLocationException(
                coordinates=coordinates,
                text=str(exc)
            )

    def __forward(self):
        """Attempting to move the rover one position in the specified
        direction
        """
        coord = copy.deepcopy(self.coordinates)
        if self.direction == 'N':
            coord[1] += 1
        if self.direction == 'E':
            coord[0] += 1
        if self.direction == 'S':
            coord[1] -= 1
        if self.direction == 'W':
            coord[0] -= 1
        self.plato.check(coord, self.coordinates)
        self.coordinates = coord

    def __rotate(self, direction: str):
        """Makes the rover spin 90 degrees left or right respectively,
        without moving from its current spot

        :param direction: (str) - A string of the direction, e.g. 'L'  or 'R'
        """
        position = self.DIRECTIONS.index(self.direction.upper())
        if direction == 'L':
            if position == 0:
                self.direction = self.DIRECTIONS[-1]
            else:
                self.direction = self.DIRECTIONS[position-1]
        else:
            if position == 3:
                self.direction = self.DIRECTIONS[0]
            else:
                self.direction = self.DIRECTIONS[position+1]

    @property
    def current_position(self):
        """Show current rover position"""
        return f'{self.coordinates[0]} {self.coordinates[1]} {self.direction}'

    @property
    def grid_position(self):
        """Rover position on grid"""
        x1, y1, x2, y2 = self.plato.bounds
        width = x2 - x1
        height = y2 - y1
        grid = []
        vertical = '|  ' * width + '|'
        line = ('*--' * width + '*')
        for i in range(height+1):
            if self.coordinates[1] == i:
                grid.insert(
                    0, line[:3*self.coordinates[0]] +
                       ('@--' if self.coordinates[0] != width else '@') +
                       line[3*self.coordinates[0]+3:]
                )
            else:
                grid.insert(0, line)
            if i != height:
                grid.insert(0, vertical)
        return '\n'.join(grid)

    def move(self, path: str):
        """Move a rover to a new location

        :param path: str - Rover path line, e.g. "RLMLRLM"
        """
        for symbol in path:
            if symbol.upper() == 'M':
                self.__forward()
            elif symbol.upper() == 'L' or symbol.upper() == 'R':
                self.__rotate(symbol.upper())
            else:
                raise MoveRoverLocationException(symbol=symbol)
