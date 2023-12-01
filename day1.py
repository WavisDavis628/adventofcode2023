# import re
# Take in Time to check later
import time
start_time = time.time()

# Grab all lines
inputFile = open('inputs/input_day_1.txt', 'r')
inputFileLines = inputFile.readlines()

# TEST
# Define counter
lineCount = 0

# Total Count
total = 0

# Strips the file for each line
for line in inputFileLines:
    lineCount += 1
    charCount = 0

    # Speedy
    # Time taken: 0.0009992122650146484s
    firstDigit = 0
    lastDigit = 0
    for char in line:
        charCount += 1
        if char.isdigit():
            firstDigit = int(char)
            # print(f'Line{lineCount}: {line.strip()} = First digit {char}')
            break

    charCount = len(line)
    for char in line[::-1]:
        charCount -= 1
        if char.isdigit():
            lastDigit = int(char)
            # print(f'Line{lineCount}: {line.strip()} = Last digit {char}')
            break

    firstDigit *= 10
    total += firstDigit + lastDigit

    # # Slow
    # # Time taken: 0.0019979476928710938s
    # # Regex for the first digit
    # firstDigitPattern = re.compile(r'\d')
    # firstDigitMatch = firstDigitPattern.search(line)
    # firstDigit = int(firstDigitMatch.group())
    #
    # # Regex for the last digit
    # lastDigitPattern = re.compile(r'\d(?=\D*$)')
    # lastDigitMatch = lastDigitPattern.search(line)
    # lastDigit = int(lastDigitMatch.group())
    #
    # # Print Digits
    # # print(f'Line{lineCount}: {line.strip()} = First digit {firstDigit}')
    # # print(f'Line{lineCount}: {line.strip()} = Last digit {lastDigit}')
    # total += firstDigit * 10 + lastDigit

# Total
print(f'{total}')

# How fast was this?
end_time = time.time()
timeDiff = end_time - start_time
print(f"Time taken: {timeDiff}s")
