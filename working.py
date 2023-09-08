import re
import sys

def main():
    print(convert(input("Hours: ")))

#Checks to make sure input format is valid
def convert(s):
        standard_format = re.search(r"^(([0-9][0-2]*):*([0-5][0-9])*) ([A-P]M) to (([0-9][0-2]*):*([0-5][0-9])*) ([A-P]M)$", s)
        if standard_format:
             groups = standard_format.groups()
             if int(groups[1]) > 12 or int(groups[5]) > 12:
                  raise ValueError
             first_time = military_format(groups[1], groups[2], groups[3])
             second_time = military_format(groups[5], groups[6], groups[7])
             return first_time + " to " + second_time
        else:
             raise ValueError

#Converts from standard time to military time
def military_format(hour, minute, am_pm):
    if am_pm == 'PM':
        if int(hour) == 12:
            new_hour = 12
        else:
            new_hour = int(hour) + 12
    else:
        if int(hour) == 12:
                new_hour = 0
        else:
            new_hour = int(hour)
    if minute == None:
        new_minute = ':00'
        euro_time = f"{new_hour:02}" + new_minute
    else:
        euro_time = f"{new_hour:02}" + ':' + minute
    return euro_time
if __name__ == "__main__":
    main()