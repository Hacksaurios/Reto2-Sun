#!/usr/bin/python3

def solutions():
    e = 1
    for s in range(9, -1, -1):
        for o in range(9, -1, -1):
            for l in range(9, -1, -1):
                for a in range(9, -1, -1):
                    for r in range(9, -1, -1):
                        for p in range(9, -1, -1):
                            for w in range(9, -1, -1):
                                for x in range(9, -1, -1):
                                    for c in range(9, -1, -1):
                                        if len(set([s, o, l, a, r, p, w, e, x, c])) == 10:
                                            solar = 10000 * s + 1000 * o + 100 * l + 10 * a + r
                                            power = 10000 * p + 1000 * o + 100 * w + 10 * e + r
                                            excels = 100000 * e + 10000 * x + 1000 * c + 100 * e + 10 * l + s

                                            if solar + power == excels:
                                                print(solar, "+", power, "=", excels)
