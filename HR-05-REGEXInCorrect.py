"""
You are given a string S.
Your task is to find out whether S is a valid regex or not.

Input Format

The first line contains integer T, the number of test cases.
The next T lines contains the string S.

Constraints


Output Format

Print "True" or "False" for each test case without quotes.

Sample Input

2
.*\+
.*+
Sample Output

True
False
Explanation

.*\+ : Valid regex.
.*+: Has the error multiple repeat. Hence, it is invalid.
"""

import re

if __name__ == '__main__':
    t = int(input())
    if 0 < t < 100:
        for _ in range(t):
            strkey = str(input())
            try:
                re.compile(strkey)
                valid = True
            except re.error:
                valid = False
            print(valid)
