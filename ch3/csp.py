# constraint-satisfaction proЬlems CSP
import typing
import abc

V = typing.TypeVar('V')  # variable
D = typing.TypeVar('D')     # domain


class Constraint(typing.Generic[V, D], abc.ABC):
    def __init__(self, variables: typing.List[V]) -> None:
        self.variables = variables

    @abc.abstractmethod
    def satisfied(self, assignment: typing.Dict[V, D]) -> bool:
        ...


class CSP(typing.Generic[V, D]):
    def __init__(self, variables: typing.List[V],
                 domains: typing.Dict[V, typing.List[D]]) -> None:
        self.variables: typing.List[V] = variables
        self.domains: typing.Dict[V, typing.List[D]] = domains
        self.constraints: typing.Dict[V, typing.List[Constraint[V, D]]] = {}
        for variable in self.variables:
            self.constraints[variable] = []
            if variable not in self.domains:
                raise LookupError(
                    "Every variable should have a domain assigned to it")

    def add_constraint(self, constraint: Constraint[V, D]) -> None:
        for variable in constraint.variables:
            if variable not in self.variables:
                raise LookupError("Variable in constraint not in CSP")
            else:
                self.constraints[variable].append(constraint)

    def consistent(self, variable: V, assignment: typing.Dict[V, D]) -> bool:
        for constraint in self.constraints[variable]:
            if not constraint.satisfied(assignment):
                return False
        return True

    def backtracking_search(self, assignment: typing.Dict[V, D] = {}) -> typing.Optional[typing.Dict[V, D]]:
        if len(assignment) == len(self.variables):
            return assignment

        unassigned: typing.List[V] = [
            v for v in self.variables if v not in assignment]

        first: V = unassigned[0]

        for value in self.domains[first]:
            local_assignment = assignment.copy()
            local_assignment[first] = value
            if self.consistent(first, local_assignment):
                result: typing.Optional[typing.Dict[V, D]] = self.backtracking_search(
                    local_assignment)
                if result is not None:
                    return result
        return None
