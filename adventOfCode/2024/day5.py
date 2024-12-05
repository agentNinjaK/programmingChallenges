rules = []
orders = []
isRules = True
with open("day5.txt", "r") as file:
    for line in file:
        if(line.find("|") > 0):
            rules+=[line.strip()]
        elif(line.find(",") > 0):
             orders+=[line.strip()]

rulesViolations = []
for rule in rules:
    a,b = rule.split("|")
    rulesViolations+=[[b,a]]

answerPart1 = 0
answerPart2 = 0
badOrders = []
for order in orders:
    valid = True
    for violation in rulesViolations:
        if order.find(violation[0])>=0 and order.find(violation[1])>=0 and order.find(violation[0])<order.find(violation[1]):
            valid = False
            badOrders+=[order.split(",")]
            break
    if(valid):
        nums = order.split(",")
        mid = nums[(len(nums) - 1)//2]#we'll see if evens are an issue
        answerPart1+=int(mid)

print(answerPart1)

#print(badOrders)
for order in badOrders:
    i = 0
    while(i < len(rulesViolations)):
        first = order.index(rulesViolations[i][0]) if rulesViolations[i][0] in order else -1
        next = order.index(rulesViolations[i][1]) if rulesViolations[i][1] in order else -1
        if first >=0 and next >=0 and first < next:
            #be dumb and just swap the numbers
            order[next],order[first] = order[first],order[next]
            i = 0
        else:
            i+=1
    mid = order[(len(order) - 1)//2]#we'll see if evens are an issue
    answerPart2+=int(mid)

print(answerPart2)