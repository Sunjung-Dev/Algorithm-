N = int(input())
L = list(map(int, input().split()))
times = 0
time_list = []

def sum_time(a, b):
    return a + b 

def get_time_list(L):
    L.sort()
    for i in range(0, len(L)):
        if i == 0:
            time_list.append(L[i])
        else:
            times = time_list[i-1] + L[i]
            time_list.append(times)
    return time_list
    
def get_sumTimes(time_list):
    sum = 0
    for time in time_list:
        sum = sum + time
    return sum

timed = get_time_list(L)
print(get_sumTimes(timed))

