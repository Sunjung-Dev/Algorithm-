h, m = [int(x) for x in input().split()]
t = ((h*60+m-45)+(24*60))%(24*60)
m=t%60
h=t//60
print(h, m)