import re

def find_calibration_values_sum(file_name):
    f = open(file_name, "r")
    
    sum = 0
    for line in f:
        sum += calibration_value(line)

    f.close()

    return sum


def find_calibration_value(string):
    first_digit_pattern = "(\d)"
    last_digit_pattern = "\d(?!.*\d)"

    first_digit = re.search(first_digit_pattern, string).group()
    last_digit = re.search(last_digit_pattern, string).group()

    return int(first_digit + last_digit)

# Better solution that includes digits in word form
def calibration_value(string):
    digit_pattern = "(?=(\d|one|two|three|four|five|six|seven|eight|nine))" 
    
    digit_list = re.findall(digit_pattern, string)

    first_digit = digit_list[0]
    last_digit = digit_list[-1]

    string_nums = {
        "one": "1",
        "two": "2",
        "three": "3",
        "four": "4",
        "five": "5",
        "six": "6",
        "seven": "7",
        "eight": "8",
        "nine": "9"
    }

    if string_nums.get(first_digit):
        first_digit = string_nums[first_digit]

    if string_nums.get(last_digit):
        last_digit = string_nums[last_digit]

    return int(first_digit + last_digit)

print(find_calibration_values_sum("input.txt"))
