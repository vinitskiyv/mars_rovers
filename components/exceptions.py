

class PlateauRightCoordinatesException(Exception):
    """Exception for plateau upper-right coordinates"""

    def __init__(self, coordinates='0 0', text=''):
        self.coordinates = coordinates
        self.text = text

    def __repr__(self):
        return f'Invalid upper-right coordinates of the ' \
               f'plateau "{self.coordinates}", expected str "X Y". ' \
               f'Details {self.text}'

    def __str__(self):
        return str(self.__repr__())


class InvalidPlateauCoordinateException(Exception):
    """Exception for invalid coordinate"""

    def __init__(self, coordinate=0):
        self.coordinate = coordinate

    def __repr__(self):
        return f'Invalid coordinate "{self.coordinate}", ' \
               f'expected positive value or 0"'

    def __str__(self):
        return str(self.__repr__())


class OutsidePlateauException(Exception):
    """Exception for outside object"""

    def __init__(self, coordinates=(0, 0), stop=(0, 0)):
        self.coordinates = coordinates
        self.stop = stop

    def __repr__(self):
        return f'Rover "{self.coordinates}" is outside the plateau, ' \
               f'rover stop on {self.stop}'

    def __str__(self):
        return str(self.__repr__())


class InitialRoverLocationException(Exception):
    """Exception for initial rover location"""

    def __init__(self, coordinates='0 0 N', text=''):
        self.coordinates = coordinates
        self.text = text

    def __repr__(self):
        return f'Invalid initial rover location "{self.coordinates}", ' \
               f'expected str "X Y L". ' \
               f'Details {self.text}'

    def __str__(self):
        return str(self.__repr__())


class MoveRoverLocationException(Exception):
    """Exception for invalid direction symbol"""

    def __init__(self, symbol):
        self.symbol = symbol

    def __repr__(self):
        return f'Invalid direction symbol "{self.symbol}", ' \
               f'expected str "M" or "R" or "L".'

    def __str__(self):
        return str(self.__repr__())
