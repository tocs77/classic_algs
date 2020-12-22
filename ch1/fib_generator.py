import typing


def fib_gen(n: int) -> typing.Generator[int, None, None]:
    yield 0
    if n > 0:
        yield 1
    last: int = 0
    next: int = 1
    for _ in range(1, n):
        last, next = next, last+next
        yield next


for i, val in enumerate(fib_gen(50)):
    print(f'{i}->{val}')
