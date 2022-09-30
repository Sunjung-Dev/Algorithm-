n = 9
arr = []
for _ in range(9):
    arr.append(int(input()))
max = 0 
index = 0 

for a in range(len(arr)):
    if arr[a] > max:
        max = arr[a]
        index = a
print(max)
print(index +1)