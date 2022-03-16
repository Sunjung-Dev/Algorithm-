num_1, num_2 = input().split()
num1 = int(num_1[::-1])
num2 = int(num_2[::-1])


if num1 > num2 :
    print(num1)
else:
    print(num2)