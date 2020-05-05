#!/usr/bin/python3
palindrome = 0
max = 1000
for a in range(max / 10, max):
    for b in range(a, max):
        str = str(a * b)
        rev = str[::-1]
        if a * b > palindrome and str == rev:
            palindrome = a * b
print(palindrome)
