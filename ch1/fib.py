import typing

memo: typing.Dict[int, int] = {0: 0, 1: 1}


def fib(n: int) -> int:
    if n in memo:
        return memo[n]
    res = fib(n-1)+fib(n-2)
    memo[n] = res
    return res


print(fib(50))
