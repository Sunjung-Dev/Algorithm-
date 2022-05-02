num_string = str(input())

def calculate_num(num_string):
    final_calcuation = list()
    if num_string.__contains__("-"):
        num_string = num_string.split("-")
        for num in range(0, len(num_string)):
            if num_string[num].find("+"):
                num_string[num] = num_string[num].split("+")
                sum = 0
                for nums in num_string[num]:
                    sum += int(nums)
                final_calcuation.append(sum)
        result = final_calcuation[0]
        for cal in range(1, len(final_calcuation)):
            result = result - final_calcuation[cal]
            
    else:
        num_string = num_string.split("+")
        sum = 0
        for num in num_string:
            sum += int(num) 
        result = sum
    return result

print(calculate_num(num_string))