import sys
num = int(input())
num_list = list()

for n in range(0, num):
    n = int(sys.stdin.readline())
    num_list.append(n)

num_list.sort()

for num in num_list:
    print(num)
