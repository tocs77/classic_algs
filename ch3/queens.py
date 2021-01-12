import typing
from csp import Constraint, CSP


class QueensConstraint(Constraint[int, int]):
    def __init__(self, columns: typing.List[int]) -> None:
        super().__init__(columns)
        self.columns: typing.List[int] = columns

    def satisfied(self, assignment: typing.Dict[int, int]) -> bool:
        # q1c queen on first column, q1r queen on first row
        for q1c, q1r in assignment.items():
            # q2c queen on 2nd column
            for q2c in range(q1c+1, len(self.columns)+1):
                if q2c in assignment:
                    q2r: int = assignment[q2c]  # q2r queen on 2nd row
                    if q1r == q2r:  # the same row
                        return False
                    if(abs(q1r-q2r) == abs(q1c-q2r)):  # the same diagonal
                        return False
        return True


if __name__ == "__main__":
    columns: typing.List[int] = [1, 2, 3, 4, 5, 6, 7, 8]
    rows: typing.Dict[int, typing.List[int]] = {}
    for column in columns:
        rows[column] = [1, 2, 3, 4, 5, 6, 7, 8]
    csp: CSP[int, int] = CSP(columns, rows)
    csp.add_constraint(QueensConstraint(columns))
    solution: typing.Optional[typing.Dict[int, int]
                              ] = csp.backtracking_search()
    if solution is None:
        print("No solution found")
    else:
        print(solution)
