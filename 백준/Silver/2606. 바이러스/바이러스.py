def find_parent(parent, x):
    if parent[x] != x:
        return find_parent(parent, parent[x])
    return x


def union_parent(parent, a, b):
    a = find_parent(parent, a)
    b = find_parent(parent, b)
    if a < b:
        parent[b] = a
    else:
        parent[a] = b

def main():
    #노드의 갯수, 간선의 갯수 
    v = int(input())
    e = int(input())

    parent = [0] * ( v + 1 )
    result = 0

    for i in range(1, v+1):
        parent[i]= i

    for i in range(e):
        a, b = map(int, input().split())
        union_parent(parent, a, b)

    for i in range(1, v + 1):
        if find_parent(parent, i) == 1:
            result += 1

    return (result -1)

print(main())