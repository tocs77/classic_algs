import typing
from csp import Constraint, CSP


class MapColoringConstraint(Constraint[str, str]):
    def __init__(self, place1: str, place2: str) -> None:
        super().__init__([place1, place2])
        self.place1: str = place1
        self.place2: str = place2

    def satisfied(self, assignment: typing.Dict[str, str]) -> bool:
        if self.place1 not in assignment or self.place2 not in assignment:
            return True
        return assignment[self.place1] != assignment[self.place2]


if __name__ == "__main__":
    variaЬles: typing.List[str] = ["Western Australia", "Northern Territory", "South Australia",
                                   "Queensland", "New South Wales", "Victoria", "Tasmania"]
    domains: typing.Dict[str, typing.List[str]] = {}
    for variaЬle in variaЬles:
        domains[variaЬle] = ["red", "green", "blue"]
    csp: CSP[str, str] = CSP(variaЬles, domains)
    csp.add_constraint(MapColoringConstraint("Western Australia",
                                             "Northern Territory"))
    csp.add_constraint(MapColoringConstraint("Western Australia",
                                             "South Australia"))
    csp.add_constraint(MapColoringConstraint("South Australia",
                                             "Northern Territory"))
    csp.add_constraint(MapColoringConstraint("Queensland",
                                             "Northern Territory"))
    csp.add_constraint(MapColoringConstraint("Queensland", "South Australia"))
    csp.add_constraint(MapColoringConstraint("Queensland", "New South Wales"))
    csp.add_constraint(MapColoringConstraint("New South Wales",
                                             "South Australia"))
    csp.add_constraint(MapColoringConstraint("Victoria", "South Australia"))
    csp.add_constraint(MapColoringConstraint("Victoria", "New South Wales"))
    csp.add_constraint(MapColoringConstraint("Victoria", "Tasmania"))

    solution: typing.Optional[typing.Dict[str, str]
                              ] = csp.backtracking_search()
    if solution is None:
        print("No solution found")
    else:
        print(solution)
