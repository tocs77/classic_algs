import typing
import random
import string

from csp import CSP, Constraint

Grid = typing.List[typing.List[str]]


class GridLocation(typing.NamedTuple):
    row: int
    column: int


def generate_grid(rows: int, columns: int) -> Grid:
    return[[random.choice(string.ascii_uppercase) for c in range(columns)] for r in range(rows)]


def display_grid(grid: Grid) -> None:
    for row in grid:
        print(''.join(row))


if __name__ == '__main__':
    g: Grid = generate_grid(20, 20)
    display_grid(g)
