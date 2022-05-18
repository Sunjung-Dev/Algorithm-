N, K = map(int, input().split())
student = list(map(int, input().split()))
cost = list()

if N == K:
    print("0")

else:
    for i in range(1, N):
        t_cost = student[i] - student[i-1]
        cost.append(t_cost)

    cost.sort()
    total_cost = 0

    for i in range(0, N-K):
        total_cost += cost[i]

    print(total_cost)