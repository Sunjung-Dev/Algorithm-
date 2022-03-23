import sys
sys.setrecursionlimit(10*6)

def repeat_star(LEN):
    if LEN == 1:
        return ["*"]

    Stars = repeat_star(LEN//3)
    L = []

    for s in Stars:
        L.append(s*3)
    for s in Stars:
        L.append(s+" "*(LEN//3)+s)
    for s in Stars:
        L.append(s*3)
    return L

n = int(sys.stdin.readline().strip())
print("\n".join(repeat_star(n)))