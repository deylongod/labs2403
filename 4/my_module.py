def sm(n, m):
    return n + m


def sb(n, m):
    return n - m


def dv(n, m):
    try:
        return n / m
    except ZeroDivisionError:
        return "Делить на ноль нельзя"


def mp(n, m):
    return n * m