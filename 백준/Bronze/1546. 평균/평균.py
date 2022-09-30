subject_num = int(input())
subject = list(map(int, input().split()))

average = 0

max_score = max(subject)
sum = 0 

for sub in subject:
    sub = sub/max_score*100
    sum += sub

sum = sum/subject_num
print(sum)