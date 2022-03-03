num = int(input())
num_list = list()

for n in range(1, num+1):
    a, b =map(int, input().split())
    num_list.append(a+b)

for n in range(0, len(num_list)):
    print("Case #{}:".format(n+1), num_list[n])
