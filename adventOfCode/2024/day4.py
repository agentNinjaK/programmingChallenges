wordSearch = []
with open("day4.txt", "r") as file:
    for line in file:
        wordSearch+=[line.strip()]

keyword = "XMAS"
wordsFound = 0
#print(wordSearch)
height = len(wordSearch)
width = len(wordSearch[0])
#Do it like sword angles, inefficient but gets them all
#combine loops later!
#also these range boundaries are nonsense.
#1
for col in range(width-1,2,-1):
    for row in range(0,height-3):
        test = wordSearch[row][col]+wordSearch[row+1][col-1]+wordSearch[row+2][col-2]+wordSearch[row+3][col-3]
        if(test==keyword):
            wordsFound+=1
#2
for col in range(width-1,2,-1):
    for row in range(0,height):
        test = wordSearch[row][col]+wordSearch[row][col-1]+wordSearch[row][col-2]+wordSearch[row][col-3]
        if(test==keyword):
            wordsFound+=1
#3
for col in range(width-1,2,-1):
    for row in range(height-1,2,-1):
        test = wordSearch[row][col]+wordSearch[row-1][col-1]+wordSearch[row-2][col-2]+wordSearch[row-3][col-3]
        if(test==keyword):
            wordsFound+=1
#4
for col in range(0,width):
    for row in range(height-1,2,-1):
        test = wordSearch[row][col]+wordSearch[row-1][col]+wordSearch[row-2][col]+wordSearch[row-3][col]
        if(test==keyword):
            wordsFound+=1
#5
for col in range(0,width-3):
    for row in range(height-1,2,-1):
        test = wordSearch[row][col]+wordSearch[row-1][col+1]+wordSearch[row-2][col+2]+wordSearch[row-3][col+3]
        if(test==keyword):
            wordsFound+=1
#6
for col in range(0,width-3):
    for row in range(0,height):
        test = wordSearch[row][col]+wordSearch[row][col+1]+wordSearch[row][col+2]+wordSearch[row][col+3]
        if(test==keyword):
            wordsFound+=1
#7
for col in range(0,width-3):
    for row in range(0,height-3):
        test = wordSearch[row][col]+wordSearch[row+1][col+1]+wordSearch[row+2][col+2]+wordSearch[row+3][col+3]
        if(test==keyword):
            wordsFound+=1
#8
for col in range(0,width):
    for row in range(0,height-3):
        test = wordSearch[row][col]+wordSearch[row+1][col]+wordSearch[row+2][col]+wordSearch[row+3][col]
        if(test==keyword):
            wordsFound+=1
print(wordsFound)

crossesFound = 0
for col in range(1,width-1):
    for row in range(1,height-1):
        if(wordSearch[row][col]=="A"):
            diag1 = wordSearch[row-1][col-1]+wordSearch[row][col]+wordSearch[row+1][col+1]
            diag2 = wordSearch[row-1][col+1]+wordSearch[row][col]+wordSearch[row+1][col-1]
            if(diag1 in ("SAM","MAS") and diag2 in ("SAM","MAS")):
                crossesFound+=1
#1744 is too high (was allowing MAM/SAS), #1697 is too low (what is wrong???)
print(crossesFound)