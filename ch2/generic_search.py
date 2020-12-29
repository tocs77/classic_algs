from __future__ import annotations
import typing

T = typing.TypeVar('T')


def linear_contains(iterable: typing.Iterable[T], key: T) -> bool:
    for item in iterable:
        if item == key:
            return True
    return False


C = typing.TypeVar("C", bound="Comparable")


class Comparable(typing.Protocol):
    def __eq__(self, other: typing.Any) -> bool:
        ...

    def __lt__(self: C, other: C) -> bool:
        ...

    def __gt__(self: C, other: C) -> bool:
        return(not self < other) and self != other

    def __le__(self: C, other: C) -> bool:
        return self < other or self != other

    def __ge__(self: C, other: C) -> bool:
        return not self < other


def binary_contains(sequence: typing.Sequence[C], key: C) -> bool:
    low: int = 0
    high: int = len(sequence)-1
    while low <= high:
        mid: int = (low+high) // 2
        if sequence[mid] < key:
            low = mid+1
        elif sequence[mid] > key:
            high = mid-1
        else:
            return True
    return False


class Stack(typing.Generic[T]):
    def __init__(self) -> None:
        self._container: typing.List[T] = []

    @property
    def empty(self) -> bool:
        return not self._container

    def push(self, item: T) -> None:
        self._container.append(item)

    def pop(self) -> T:
        return self._container.pop()

    def __repr__(self) -> str:
        return repr(self._container)


class Node(typing.Generic[T]):
    def __init__(self, state: T, parent: typing.Optional[Node],
                 cost: float = 0.0, heuristic: float = 0.0) -> None:
        self.state: T = state
        self.parent: typing.Optional[Node] = parent
        self.cost: float = cost
        self.heuristic: float = heuristic

    def __lt__(self, other: Node):
        return(self.cost+self.heuristic) < (other.cost+other.heuristic)


def node_to_path(node: Node[T]) -> typing.List[T]:
    path: typing.List[T] = [node.state]
    while node.parent is not None:
        node = node.parent
        path.append(node.state)
    path.reverse()
    return path


class Queue(typing.Generic[T]):
    def __init__(self) -> None:
        self._container: typing.Deque[T] = typing.Deque()

    @property
    def empty(self) -> bool:
        return not self._container

    def push(self, item: T) -> None:
        self._container.append(item)

    def pop(self) -> T:
        return self._container.popleft()

    def __repr__(self) -> str:
        return repr(self._container)


def dfs(initial: T, goal_test: typing.Callable[[T], bool],
        successors: typing.Callable[[T], typing.List[T]]) -> typing.Optional[Node[T]]:
    frontier: Stack[Node[T]] = Stack()
    frontier.push(Node(initial, None))
    explored: typing.Set[T] = {initial}
    while not frontier.empty:
        current_node: Node[T] = frontier.pop()
        current_state: T = current_node.state
        if goal_test(current_state):
            return current_node
        for child in successors(current_state):
            if child in explored:
                continue
            explored.add(child)
            frontier.push(Node(child, current_node))
    return None


def bfs(initial: T, goal_test: typing.Callable[[T], bool],
        successors: typing.Callable[[T], typing.List[T]]) -> typing.Optional[Node[T]]:
    frontier: Queue[Node[T]] = Queue()
    frontier.push(Node(initial, None))
    explored: typing.Set[T] = {initial}
    while not frontier.empty:
        current_node: Node[T] = frontier.pop()
        current_state: T = current_node.state
        if goal_test(current_state):
            return current_node
        for child in successors(current_state):
            if child in explored:
                continue
            explored.add(child)
            frontier.push(Node(child, current_node))
    return None


if __name__ == "__main__":
    print(linear_contains([1, 5, 15, 15, 15, 15, 20], 5))  # True
    print(binary_contains(["a", "d", "е", "f", "z"], "f"))  # True
    print(binary_contains(["john", "mark", "ronald", "sarah"], "sheila"))
