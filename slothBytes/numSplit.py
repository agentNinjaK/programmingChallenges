def num_split(number):
    answer = []
    place = 1
    switchFlag = number < 0
    if(switchFlag):
        number = number * -1
    while(place <= number):
        digit = number//place%10*place
        answer = [digit]+answer 
        place*=10
    if(switchFlag):
        answer = [-1*key for key in answer]
    print(answer)
    return number

num_split(39)
#output =[30, 9]

num_split(-434)
#output = [-400, -30, -4]

num_split(100)
#output =[100, 0, 0]