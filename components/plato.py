from components.exceptions import (
    OutsidePlateauException,
    PlateauRightCoordinatesException,
    InvalidPlateauCoordinateException,
)


class Plato:
    """Plateau on Mars

    :param right_coordinates (str): upper-right coordinates of the plateau
    """

    def __init__(self, right_coordinates: str):
        self._right_coordinates = right_coordinates

    @property
    def bounds(self):
        """Indicates the boundaries of the plateau"""

        coord = self._right_coordinates.split(' ')
        if len(coord) != 2:
            raise PlateauRightCoordinatesException(self._right_coordinates)
        try:
            return 0, 0, *list(map(self.validate, coord))
        except Exception as exc:
            raise PlateauRightCoordinatesException(
                self._right_coordinates,
                str(exc)
            )

    @staticmethod
    def validate(coordinate: str):
        """Validate initial coordinate of the plateau"""

        if int(coordinate) >= 0:
            return int(coordinate)
        else:
            raise InvalidPlateauCoordinateException(coordinate)

    def check(self, coordinates, stop=(0, 0)):
        """Checks if an object belongs to a plane of a plateau

        :param coordinates: list [X, Y]
        """
        x1, y1, x2, y2 = self.bounds
        if x1 <= coordinates[0] <= x2 and y1 <= coordinates[1] <= y2:
            return list(coordinates)
        else:
            raise OutsidePlateauException(coordinates=coordinates, stop=stop)
