def censor(input):
    split_input = input.split()
    for i in range(len(split_input)):
        word_dist = len(split_input[i])
        if word_dist > 4:
            split_input[i] = "*"*word_dist

    #replace long ones with stars
    return " ".join(split_input)

assert censor("The code is fourty")== "The code is ******"

assert censor("Two plus three is five") == "Two plus ***** is five"

assert censor("aaaa aaaaa 1234 12345") == "aaaa ***** 1234 *****"