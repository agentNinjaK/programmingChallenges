lines = []
with open("day2.txt", "r") as file:
    for line in file:
        lines+=[list(map(int, line.strip().split()))]

def checkSafe(line):
    decrease = line[1]-line[0] < 0
    safe = True
    for i in range(1,len(line)):
        diff = line[i]-line[i-1]
        if(decrease and (diff > -1 or diff < -3)):
            safe = False
        if(not decrease and (diff > 3 or diff < 1)):
            safe = False
    return safe


count = 0
for line in lines:
    if(checkSafe(line)):
        count+=1
print(count)



count = 0
for line in lines:
    decrease = line[1]-line[0] < 0
    safe = True
    removed = False
    if(checkSafe(line)):
        count+=1
    else:
        #print(line)
        #print("yeah")
        for i in range(0,len(line)):
            newLine = line[0:i]+line[i+1:]
            if(checkSafe(newLine)):
                count+=1
                break
print(count)
