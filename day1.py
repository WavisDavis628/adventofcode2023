import time
import re

start_time = time.time()


def find_first_and_last_digit_or_string(text):
    # Regex Expression for the first or last number(int or string), overlapping in case of 'nineight'
    matches = re.findall(r'(?=(\d|one|two|three|four|five|six|seven|eight|nine))', text)
    single_digits = {'one': 1, 'two': 2, 'three': 3, 'four': 4, 'five': 5, 'six': 6, 'seven': 7, 'eight': 8, 'nine': 9}
    if matches:
        if matches[0].isnumeric():
            first_match = matches[0]
        else:
            # if our match isn't an int, grab the value for it
            first_match = single_digits[matches[0]]
        if matches[-1].isnumeric():
            last_match = matches[-1]
        else:
            # if our match isn't an int, grab the value for it
            last_match = single_digits[matches[-1]]

        return int(first_match), int(last_match)
    else:
        return 'Failed'


input_file = open('inputs/input_day_1.txt', 'r')
input_file_lines = input_file.readlines()

line_count = 0

total = 0

# Strips the file for each line
for line in input_file_lines:

    both_digits = find_first_and_last_digit_or_string(line)

    first_digit = both_digits[0]
    last_digit = both_digits[-1]

    # All of this is just for display
    line_count += 1
    print(f'Line {line_count}: {line.strip()} ')
    print(f'First = {first_digit}, Last = {last_digit} ', end='\n \n')

    total += (first_digit * 10) + last_digit

print(f'{total}')

# How fast was this?
end_time = time.time()
time_diff = end_time - start_time
print(f"Time taken: {time_diff}s")
