from itertools import chain
from typing import Callable, Iterable, T


def camel2snake(x: str) -> str:
    prefix, *rest = map("".join, split(str.isupper, x))
    suffix = map(lambda y: y[0].lower() + y[1:], rest)
    return "_".join(chain([prefix], suffix))


def split(p: Callable[[T], bool], xs: Iterable[T]) -> Iterable[list[T]]:
    ys = []
    for x in iter(xs):
        if p(x):
            yield ys
            ys = [x]
        else:
            ys.append(x)
    yield ys
