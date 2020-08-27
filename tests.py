import unittest
from components.plato import Plato
from components.rover import Rover


class TestRoversPlato5To5(unittest.TestCase):

    def setUp(self):
        self.plato = Plato('5 5')

    def test_rover1(self):
        rover = Rover(self.plato, '1 2 N')
        rover.move('LMLMLMLMM')
        self.assertEqual(rover.current_position, '1 3 N')

    def test_rover2(self):
        rover = Rover(self.plato, '3 3 E')
        rover.move('MMRMMRMRRM')
        self.assertEqual(rover.current_position, '5 1 E')


class TestRoversPlato20To20(unittest.TestCase):

    def setUp(self):
        self.plato = Plato('20 20')

    def test_rover1(self):
        rover = Rover(self.plato, '0 0 N')
        rover.move('MRML' * 20)
        self.assertEqual(rover.current_position, '20 20 N')


class TestRoversPlato400000To400000(unittest.TestCase):

    def setUp(self):
        self.plato = Plato('400000 400000')

    def test_rover1(self):
        rover = Rover(self.plato, '0 0 N')
        rover.move('MRML' * 400000)
        self.assertEqual(rover.current_position, '400000 400000 N')


if __name__ == '__main__':
    unittest.main()
