import math;
from graphs import plot_graph;


def euler_totient(n: int):
    coprime = []
    for i in range(1, n + 1):
        gcd = euclidean_algo(n, i)
        if gcd["gcd"] == 1:
            coprime.append(i)
    return coprime


def euclidean_algo(a: int, b: int):
    _a, _b = a, b
    gcd: int
    if a == b:
        return {"gcd": a}
    while (_a != 0) and (_b != 0):
        greater = max(_a, _b)
        lesser = min(_a, _b)
        g_mod_l: int = greater % lesser
        if greater is _a:
            _a = g_mod_l
        elif greater is _b:
            _b = g_mod_l
    if _a != 0:
        gcd = _a
    elif _b != 0:
        gcd = _b

    return {"gcd": gcd}


try:
    input_range = input("Enter a range of positive whole numbers greater than 1 eg (9-27)")
    higher_boundary = math.floor(float(input_range.split('-')[1]))
    lower_boundary = math.floor(float(input_range.split('-')[0]))
    phi_n: list[int] = []
    n: list = [i for i in range(lower_boundary, higher_boundary + 1)]
except:
    print('Please Enter a valid range')
else:
    iterator: int = lower_boundary
    while iterator <= higher_boundary:
        coprime = euler_totient(iterator)
        phi_n.append(len(coprime))
        iterator += 1
    # print(n,phi_n)
    plot_graph(n, phi_n)
