import argparse
from components.plato import Plato
from components.rover import Rover


def enter_rover_path(rover):
    print(f'-> Enter rover path line, e.g. "RLMLRLM"')
    current = rover.current_position
    rover.move(input())
    print(rover.grid_position)
    print(f'-> Rover moved from {current} to position {rover.current_position}')
    return rover


def control(coordinate='5 5', cnt=0):
    plato = Plato(coordinate)
    numbers = list(range(1, cnt+1))
    rovers = {}
    while True:
        print('-' * 40)
        try:
            print(f'-> Choose rover {numbers} (enter number):')
            value = int(input())
            if value in numbers:
                rover = rovers.get(value, None)
                if rover:
                    print(f'-> Current position {rover.current_position}')
                    rovers[value] = enter_rover_path(rover)
                else:
                    print(f'-> Enter rover current position, e.g. "0 0 N"')
                    rover = Rover(plato, input(''))
                    rovers[value] = rover
                    rovers[value] = enter_rover_path(rover)
            else:
                print(f'-> You have chosen a non-existent rover')
        except KeyboardInterrupt:
            print(f'\n -> Rovers say goodbye')
            exit()
        except Exception as exc:
            print(f'-> Data entered incorrectly, detail {exc}')
        print('-' * 40)


if __name__ == '__main__':
    parser = argparse.ArgumentParser(description='Mars rovers controller')
    parser.add_argument('--coord',
                        default='5 5',
                        help='This is the upper-right coordinates of the '
                             'plateau, expected str "X Y"')
    parser.add_argument('--rovers',
                        default=1,
                        help='This is the count of the rovers, e.g. "5"')
    args = parser.parse_args()
    control(coordinate=args.coord, cnt=int(args.rovers))
