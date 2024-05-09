def sum_of_multiples(n: int, x: int) -> int:
    sum = 0
    for i in range(x, n+1, x):
        sum += i
    return sum

def min_window_substring(s: str, t: str) -> str:
    pass
