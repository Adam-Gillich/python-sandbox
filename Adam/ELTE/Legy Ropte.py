s = 40000
vl = 100 / 9
v1 = 15 / 2
v2 = 65 / 18
sl = 0


def f(s, sl, vl, v1, v2):
    sl += s / (v1 / vl + 1)
    t1 = (s / (v1 / vl + 1)) / vl
    s -= t1 * (v1 + v2)

    sl += s / (v2 / vl + 1)
    t2 = (s / (v2 / vl + 1)) / vl
    s -= t2 * (v1 + v2)

    return s, sl


def g(s, sl, vl, v1, v2):
    t2 = s / (vl + v2)
    s2 = vl * s / (vl + v2)
    s -= s2
    sl += s2

    t1 = s / (vl + v1)
    s1 = vl * t1
    s -= s1
    sl += s1

    return s, sl


def h(s, sl, vl, v1, v2):
    if s < 1:
        return s, sl

    t2 = s / (vl + v2)
    s2 = vl * s / (vl + v2)
    s -= s2
    sl += s2

    t1 = s / (vl + v1)
    s1 = vl * t1
    s -= s1
    sl += s1

    return h(s, sl, vl, v1, v2)


s, sl = h(s, sl, vl, v1, v2)

# for i in range(10):
#    s, sl = f(s, sl, vl, v1, v2)
#    s, sl = g(s, sl, vl, v1, v2)

print(f"A légy {sl} métert tett meg! \nA két kerékpáros közt maradt út:\n   {s}")
print("\n\n\n\n\n")
