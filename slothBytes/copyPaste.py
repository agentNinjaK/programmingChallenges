# "Ctrl + C" will copy all text behind it.
#"Ctrl + V" will do nothing if there is no "Ctrl + C" before it.
#A "Ctrl + C" which follows another "Ctrl + C" will overwrite what it copies.
#Keyboard shortcut commands will appear like normal words in a sentence but shouldn't be copied themselves (see example #2).
#Pasting should add a space between words.

def keyboardShortcut(entryString):
    copyPaste = "Ctrl + C Ctrl + V"
    pasteOnly = "Ctrl + V"
    copyOnly = "Ctrl + C"
    copyPasteIndex = entryString.find(copyPaste)
    copyIndex = entryString.find(copyOnly)
    pasteIndex = entryString.find(pasteOnly)
    #there's surely a way to make this logic simpler.
    while(copyPasteIndex>= 0 or pasteIndex>=0 or copyIndex>= 0):
        if(copyPasteIndex < 0):
            entryString = entryString.replace(copyOnly+" ","")
            entryString = entryString.replace(pasteOnly+" ","")
            entryString = entryString.replace(copyOnly,"")
            entryString = entryString.replace(pasteOnly,"")
        else:
            if(copyIndex == copyPasteIndex and pasteIndex > copyPasteIndex):
                thingToCopy = entryString[0:copyPasteIndex-1]
                entryString = entryString.replace(copyPaste,thingToCopy,1)
            else:
                if(pasteIndex < copyPasteIndex):
                    entryString = entryString.replace(pasteOnly+" ","",1)
                else:
                    entryString = entryString.replace(copyOnly+" ","",1)
        #print(entryString)
        copyPasteIndex = entryString.find(copyPaste)
        copyIndex = entryString.find(copyOnly)
        pasteIndex = entryString.find(pasteOnly)
    return entryString

#Example 1
assert keyboardShortcut("the egg and Ctrl + C Ctrl + V the spoon") == "the egg and the egg and the spoon"

#Example 2
assert keyboardShortcut("WARNING Ctrl + V Ctrl + C Ctrl + V") == "WARNING WARNING"

#Example 3
assert keyboardShortcut("The Ctrl + C Ctrl + V Town Ctrl + C Ctrl + V") == "The The Town The The Town"

#Example 4 - no shortcuts
assert keyboardShortcut("No copy paste here") == "No copy paste here"

#Example 5 - weird in between stuff, where I'm uncertain as to desired behavior and am making it up!
assert keyboardShortcut("In Ctrl + C between Ctrl + V words") == "In between words"