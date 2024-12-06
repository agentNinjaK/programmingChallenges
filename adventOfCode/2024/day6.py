myMap = []
with open("day6.txt", "r") as file:
    for line in file:
        myMap+=[line.strip()]

startRow = 0
startCol = 0
for i in range(len(myMap)):
    for j in range(len(myMap[i])):
        if myMap[i][j]=="^":
            startRow = i
            startCol = j
            break


row = startRow
col = startCol
isDone = False
#should be enum, but 0/1/2/3 is like n/e/s/w
dir = 0
visited = set()
while not isDone:
    if(dir==0):
        if(row == 0):
            isDone = True
        else:
            if(myMap[row-1][col]=='#'):
                dir = 1
            else:
                if(myMap[row][col]!="x"):
                    myMap[row] = myMap[row][:col] + "x" + myMap[row][col + 1:]
                    visited.add((row,col))
                row-=1
    if(dir==1):
        if(col == len(myMap[0])-1):
            isDone = True
        else:
            if(myMap[row][col+1]=='#'):
                dir = 2
            else:
                if(myMap[row][col]!="x"):
                    myMap[row] = myMap[row][:col] + "x" + myMap[row][col + 1:]
                    visited.add((row,col))
                col+=1
    if(dir==2):
        if(row == len(myMap)-1):
            isDone = True
        else:
            if(myMap[row+1][col]=='#'):
                dir = 3
            else:
                if(myMap[row][col]!="x"):
                    myMap[row] = myMap[row][:col] + "x" + myMap[row][col + 1:]
                    visited.add((row,col))
                row+=1

    if(dir==3):
        if(col == 0):
            isDone = True
        else:
            if(myMap[row][col-1]=='#'):
                dir = 0
            else:
                if(myMap[row][col]!="x"):
                    myMap[row] = myMap[row][:col] + "x" + myMap[row][col + 1:]
                    visited.add((row,col))
                col-=1
#include current spot
visited.add((row,col))
print(len(visited))
'''So the 'dumb' way would be... take all the spots you visited in step 1,
and if putting a box there puts you in a loop - that is, if you encounter the
same obstacle when going in the same direction - then it's valid.
This isn't fast AT ALL but it gets the job done'''
loopCount = 0
visited.remove((startRow,startCol))#don't try to put a box where they start!
obstacles = set()
for x,y in visited:
    myMap[x]=myMap[x][:y]+"#"+myMap[x][y+1:]
    #check if loops
    dir = 0
    row = startRow
    col = startCol
    obstacles.clear()
    isLoop = False
    isDone = False
    while not isDone and not isLoop:
        if(dir==0):
            if(row == 0):
                isDone = True
            else:
                if(myMap[row-1][col]=='#'):
                    if(row-1,col,dir) in obstacles:
                        isLoop = True
                    else:
                        obstacles.add((row-1,col,dir))
                        dir = 1
                else:
                    row-=1
        if(dir==1):
            if(col == len(myMap[0])-1):
                isDone = True
            else:
                if(myMap[row][col+1]=='#'):
                    if(row,col+1,dir) in obstacles:
                        isLoop = True
                    else:
                        obstacles.add((row,col+1,dir))
                        dir = 2
                else:
                    col+=1
        if(dir==2):
            if(row == len(myMap)-1):
                isDone = True
            else:
                if(myMap[row+1][col]=='#'):
                    if(row+1,col,dir) in obstacles:
                        isLoop = True
                    else:
                        obstacles.add((row+1,col,dir))
                        dir = 3
                else:
                    row+=1

        if(dir==3):
            if(col == 0):
                isDone = True
            else:
                if(myMap[row][col-1]=='#'):
                    if(row,col-1,dir) in obstacles:
                        isLoop = True
                    else:
                        obstacles.add((row,col-1,dir))
                        dir = 0
                else:
                    col-=1
    if isLoop:
        loopCount+=1
    myMap[x]=myMap[x][:y]+"."+myMap[x][y+1:]

print(loopCount)


