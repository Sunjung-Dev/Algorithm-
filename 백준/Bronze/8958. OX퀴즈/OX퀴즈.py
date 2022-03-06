num = int(input())
score_list = list()

for i in range(0, num):
    case = list((input()))

    score = 0
    sum = 0
    for c in case:
        if c == 'O':
            score += 1
            sum += score
            
        else:
            score = 0
    score_list.append(sum)

for score in score_list:
    print(score)