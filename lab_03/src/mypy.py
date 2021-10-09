from multipledispatch import dispatch


@dispatch((int, float))
def frange(end):
    count = 0
    while count < end:
        yield count
        count += 1


@dispatch((int, float), (int, float))
def frange(start, end):
    count = start
    while count < end:
        yield count
        count += 1


@dispatch((int, float), (int, float), (int, float))
def frange(start, end, step):
    count = start
    while count < end:
        yield count
        count += step
