def numToEng(num):
    answer = ""
    singles = ["zero","one","two","three","four","five","six","seven","eight","nine"]
    endsInTy = ["","","twen","thir","for","fif","six","seven","eigh","nine"]
    others = ["ten","eleven","twelve"]
    if num > 100:
        answer += singles[num//100]+" hundred"
        if(num %100 != 0):
            answer+= " "
    if num > 10:
        if(num % 100 >= 19):
            answer += endsInTy[(num%100) // 10]+ "ty"
            if(num % 10 != 0):
                answer += " "+singles[num % 10]
        elif(num % 100 >= 13):
            answer += endsInTy[num % 10]+"teen"
        elif(num % 100 > 9):# num > 10 but  < 13
            answer += others[num % 10]
    if(num <= 10):
        answer = singles[num]

    return answer

print(numToEng(0))
#output = "zero"

print(numToEng(18))
#output = "eighteen"

print(numToEng(126))
#output = "one hundred twenty six"

print(numToEng(909))
#output = "nine hundred nine"

print(numToEng(412))
# 'four hundred twelve'

# possible tests to improve this - negative integers, leading zeroes, non-numbers