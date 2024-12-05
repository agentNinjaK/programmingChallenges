#Advent of Code start.
list1 = []
list2 = []
with open("day1.txt", "r") as file:
    for line in file:
        a, b = line.strip().split()
        list1+=[int(a)]
        list2+=[int(b)]
list1.sort()
list2.sort()
answer = 0
for i in range(len(list1)):
    answer+=abs(list1[i]-list2[i])
print(answer)

answer_two = 0
for i in list1:
    answer_two+=i*list2.count(i)
print(answer_two)