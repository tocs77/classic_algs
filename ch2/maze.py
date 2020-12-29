import enum
import typing
import random
import math
from generic_search import Node, dfs, bfs, node_to_path, astar


class Cell(str, enum.Enum):
    EMPTY = " "
    BLOCKED = "X"
    START = "S"
    GOAL = "G"
    PATH = "*"


class MazeLocation(typing.NamedTuple):
    row: int
    column: int


class Maze:
    def __init__(self, rows: int = 10, columns: int = 10, sparseness: float = 0.2,
                 start: MazeLocation = MazeLocation(0, 0),
                 goal: MazeLocation = MazeLocation(9, 9)) -> None:
        self._rows: int = rows
        self._columns: int = columns
        self.start: MazeLocation = start
        self.goal: MazeLocation = goal
        self._grid: typing.List[typing.List[Cell]] = [
            [Cell.EMPTY for c in range(columns)] for r in range(rows)]
        self._randomly_fill(rows, columns, sparseness)
        self._grid[start.row][start.column] = Cell.START
        self._grid[goal.row][goal.column] = Cell.GOAL

    def _randomly_fill(self, rows: int, columns: int, sparseness: float) -> None:
        for row in range(rows):
            for column in range(columns):
                if random.uniform(0, 1.0) < sparseness:
                    self._grid[row][column] = Cell.BLOCKED

    def __str__(self):
        output: str = ""
        for row in self._grid:
            output += "".join([c.value for c in row]) + "\n"
        return output

    def goal_test(self, ml: MazeLocation) -> bool:
        return ml == self.goal

    def successors(self, ml: MazeLocation) -> typing.List[MazeLocation]:
        locations: typing.List[MazeLocation] = []
        if ml.row+1 < self._rows and self._grid[ml.row+1][ml.column] != Cell.BLOCKED:
            locations.append(MazeLocation(ml.row+1, ml.column))
        if ml.row-1 >= 0 and self._grid[ml.row-1][ml.column] != Cell.BLOCKED:
            locations.append(MazeLocation(ml.row-1, ml.column))
        if ml.column+1 < self._columns and self._grid[ml.row][ml.column+1] != Cell.BLOCKED:
            locations.append(MazeLocation(ml.row, ml.column+1))
        if ml.column-1 >= 0 and self._grid[ml.row][ml.column-1] != Cell.BLOCKED:
            locations.append(MazeLocation(ml.row, ml.column-1))
        return locations

    def mark(self, path: typing.List[MazeLocation]):
        for maze_location in path:
            self._grid[maze_location.row][maze_location.column] = Cell.PATH
        self._grid[self.start.row][self.start.column] = Cell.START
        self._grid[self.goal.row][self.goal.column] = Cell.GOAL

    def clear(self, path: typing.List[MazeLocation]):
        for maze_location in path:
            self._grid[maze_location.row][maze_location.column] = Cell.EMPTY
        self._grid[self.start.row][self.start.column] = Cell.START
        self._grid[self.goal.row][self.goal.column] = Cell.GOAL


def euclidian_distance(goal: MazeLocation) -> typing.Callable[[MazeLocation], float]:
    def distance(ml: MazeLocation) -> float:
        xdist: int = ml.column-goal.column
        ydist: int = ml.row-goal.row
        return math.sqrt((xdist*xdist)+(ydist*ydist))
    return distance


def manhattan_distance(goal: MazeLocation) -> typing.Callable[[MazeLocation], float]:
    def distance(ml: MazeLocation) -> float:
        xdist: int = abs(ml.column-goal.column)
        ydist: int = abs(ml.row-goal.row)
        return xdist+ydist
    return distance


if __name__ == "__main__":
    maze: Maze = Maze()
    print(maze)
    solution1: typing.Optional[Node[MazeLocation]] = dfs(
        maze.start, maze.goal_test, maze.successors)
    if solution1 is None:
        print("No solution found")
    else:
        path1: typing.List[MazeLocation] = node_to_path(solution1)
        maze.mark(path1)
        print(maze)
        maze.clear(path1)

    print('\n\n')
    solution2: typing.Optional[Node[MazeLocation]] = bfs(
        maze.start, maze.goal_test, maze.successors)
    if solution2 is None:
        print("No solution found")
    else:
        path2: typing.List[MazeLocation] = node_to_path(solution2)
        maze.mark(path2)
        print(maze)
        maze.clear(path2)

    print('\n\n')
    solution3: typing.Optional[Node[MazeLocation]] = astar(
        maze.start, maze.goal_test, maze.successors, euclidian_distance(maze.goal))
    if solution3 is None:
        print("No solution found")
    else:
        path3: typing.List[MazeLocation] = node_to_path(solution3)
        maze.mark(path3)
        print(maze)
        maze.clear(path3)
