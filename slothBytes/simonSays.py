import re

def simon_says(args):
    answer = 0
    for val in args:
        if val.startswith("Simon says"):
            number = int(re.search(r'\d+', val).group())
            if("add") in val:
                answer += number
            elif("subtract") in val:
                answer -= number
            elif("multiply") in val:
                answer *= number
    return answer

#examples (not tests!)
print(simon_says([
  "Simon says add 4",
  "Simon says add 6",
  "Then add 5"
]))
#output = 10

print(simon_says([
  "Susan says add 10",
  "Simon says add 3",
  "Simon says multiply by 8"
]))
#output = 24

print(simon_says([
  "Firstly, add 4",
  "Simeon says subtract 100" # Look at the name closely :)
]))
#output = 0

#TODO actual tests