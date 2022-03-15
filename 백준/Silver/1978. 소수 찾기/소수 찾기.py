num = int(input())
count = 0 

num_list = list(map(int, input().split()))

for n in num_list:
    if n != 1:
        for i in range(2, n):
            if n % i == 0:
                break
        else:
            count += 1

print(count)