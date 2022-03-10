num = int(input())
num_list = list()
tmp = 0

for i in range(num):
    num_list.append(int(input()))

for i in range(len(num_list)):
    for j in range(len(num_list)):
        if num_list[i] < num_list[j]:
            num_list[i], num_list[j] = num_list[j], num_list[i]

for num in num_list:
    print(num)
