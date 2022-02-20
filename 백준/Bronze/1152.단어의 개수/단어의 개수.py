sentence = input()
sentence = sentence.split(" ")

num = 0

for s in sentence:
    if s == "":
        pass
    else:
        num += 1

print(num)