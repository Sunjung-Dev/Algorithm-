def get_MIN():
    num = int(input())
    A = list(map(int, input().split()))
    B = list(map(int, input().split()))

    A.sort()
    B.sort(reverse=True)

    sum = 0 
    for i in range(0, len(B)):
        sum = sum + (A[i]*B[i])

    return sum

print(get_MIN())
    
    