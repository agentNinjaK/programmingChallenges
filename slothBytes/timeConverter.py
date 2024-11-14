
import time

# pep-257 is guidelines on docstring conventions, see I'm learning.
# as always, assuming non-evil input
def convertTime(timeString):
    """convert a 12-hour time to 24-hour time or vice versa."""
    if timeString.find('m') == -1:
        timeForm = time.strptime(timeString,"%H:%M")
        return time.strftime("%-I:%M %P",timeForm)
    else:
        timeForm = time.strptime(timeString,"%I:%M %p")
        return time.strftime("%-H:%M", timeForm)

#print(convertTime("12:00 am"))
#print(convertTime("6:20 pm"))
#print(convertTime("21:00"))
#print(convertTime("5:05"))

assert convertTime("12:00 am")== "0:00"
assert convertTime("6:20 pm") == "18:20"
assert convertTime("21:00") == "9:00 pm"
assert convertTime("5:05") == "5:05 am"

