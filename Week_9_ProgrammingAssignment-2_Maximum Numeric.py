# Given an alphanumeric string S, extract maximum numeric value from that string. All the alphabets are in lower case. Take the maximum consecutive digits as a single number.

# Input Format:
# The first line contains the string S.

# Output Format:
# Print the maximum value

# Example:

# Input:
# 23dsa43dsa98

# Output:
# 98

# Program:

import re
ip = input()
l = ((re.findall('\d+', ip)))
l = list(map(int, l))
print(max(l), end='')
