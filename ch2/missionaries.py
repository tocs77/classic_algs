
from __future__ import annotations
import typing
from generic_search import bfs, Node, node_to_path

MAX_NUM: int = 3


class MCState:
    def __init__(self, missionaries: int, cannibals: int, boat: bool) -> None:
        self.wm: int = missionaries  # west bank missionaries
        self.wc: int = cannibals  # west bank cannibals
        self.em: int = MAX_NUM-self.wm  # east bank missionaries
        self.ec: int = MAX_NUM-self.wc  # east coat cannibals
        self.boat: bool = boat

    def __str__(self) -> str:
        return f"""On the west bank there are {self.wm} missionaries and {self.wc} cannibals.
On the east bank there are {self.em} missionaries and {self.ec} cannibals.
The boat is оп the {'west' if self.boat else 'east'} bank. \n"""

    @property
    def is_legal(self) -> bool:
        if self.wm < self.wc and self.wm > 0:
            return False
        if self.em < self.ec and self.em > 0:
            return False
        return True

    def goal_test(self) -> bool:
        return self.is_legal and self.em == MAX_NUM and self.ec == MAX_NUM

    def successors(self) -> typing.List[MCState]:
        sucs: typing.List[MCState] = []
        if self.boat:  # boat is on west bank
            if self.wm > 1:
                sucs.append(MCState(self.wm-2, self.wc, not self.boat))
            if self.wm > 0:
                sucs.append(MCState(self.wm-1, self.wc, not self.boat))
            if self.wc > 1:
                sucs.append(MCState(self.wm, self.wc-2, not self.boat))
            if self.wc > 0:
                sucs.append(MCState(self.wm, self.wc-1, not self.boat))
            if self.wc > 0 and self.wm > 0:
                sucs.append(MCState(self.wm-1, self.wc-1, not self.boat))
        else:  # boat is on east bank
            if self.em > 1:
                sucs.append(MCState(self.wm+2, self.wc, not self.boat))
            if self.em > 0:
                sucs.append(MCState(self.wm+1, self.wc, not self.boat))
            if self.ec > 1:
                sucs.append(MCState(self.wm, self.wc+2, not self.boat))
            if self.ec > 0:
                sucs.append(MCState(self.wm, self.wc+1, not self.boat))
            if self.ec > 0 and self.em > 0:
                sucs.append(MCState(self.wm+1, self.wc+1, not self.boat))
        return [x for x in sucs if x.is_legal]


def display_solution(path: typing.List[MCState]) -> None:
    if len(path) == 0:
        return
    old_state: MCState = path[0]
    print(old_state)
    for current_state in path[1:]:
        if current_state.boat:
            print(f"{old_state.em-current_state.em} missionaries and {old_state.ec-current_state.ec} cannibals moved from the east to the west bank.\n")
        else:
            print(f"{old_state.wm-current_state.wm} missionaries and {old_state.wc-current_state.wc} cannibals moved from the west to the east bank.\n")
        print(current_state)
        old_state = current_state


if __name__ == "__main__":
    start: MCState = MCState(MAX_NUM, MAX_NUM, True)
    solution: typing.Optional[Node[MCState]] = bfs(
        start, MCState.goal_test, MCState.successors)
    if solution is None:
        print("No solution found")
    else:
        path: typing.List[MCState] = node_to_path(solution)
        display_solution(path)
