'''The input will be a sequence of //, /* and */. Every /* must have a */ that immediately follows it. 
To add, there can be no single-line comments in between multi-line comments in between the /* and */
return true if the formatting is correct, false otherwise'''

def comments_correct(input):
    noDoubles = input.replace("/**/","")
    return noDoubles.count('*') == 0 and noDoubles.count("/")%2 == 0


print(comments_correct("//////") )
# True, 3 single-line comments: ["//", "//", "//"]

print(comments_correct("/**//**////**/"))
# True, 3 multi-line comments + 1 single-line comment:
# ["/*", "*/", "/*", "*/", "//", "/*", "*/"]

print(comments_correct("///*/**/"))
# False, The first /* is missing a */

print(comments_correct("/////"))
# False, The 5th / is single, not a double //