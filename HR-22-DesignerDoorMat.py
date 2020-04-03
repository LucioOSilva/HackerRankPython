"""
Mr. Vincent works in a door mat manufacturing company. One day, he designed a new door mat with the following
specifications:

Task:
Mat size must be N x M. (N is an odd natural number, and M is 3 times N.)
The design should have 'WELCOME' written in the center.
The design pattern should only use |, . and - characters.
Sample Designs

    Size: 7 x 21
    ---------.|.---------
    ------.|..|..|.------
    ---.|..|..|..|..|.---
    -------WELCOME-------
    ---.|..|..|..|..|.---
    ------.|..|..|.------
    ---------.|.---------

    Size: 11 x 33
    ---------------.|.---------------
    ------------.|..|..|.------------
    ---------.|..|..|..|..|.---------
    ------.|..|..|..|..|..|..|.------
    ---.|..|..|..|..|..|..|..|..|.---
    -------------WELCOME-------------
    ---.|..|..|..|..|..|..|..|..|.---
    ------.|..|..|..|..|..|..|.------
    ---------.|..|..|..|..|.---------
    ------------.|..|..|.------------
    ---------------.|.---------------

Input Format:
A single line containing the space separated values of N and M.

Constraints:
5 < N < 101
15 < M < 303

Output Format
Output the design pattern.

Sample Input:
9 27

Sample Output:

------------.|.------------
---------.|..|..|.---------
------.|..|..|..|..|.------
---.|..|..|..|..|..|..|.---
----------WELCOME----------
---.|..|..|..|..|..|..|.---
------.|..|..|..|..|.------
---------.|..|..|.---------
------------.|.------------
"""

# input params
try:
    y, x = map(int, input().split())
except (ValueError, TypeError) as error:
    print('An error occurred', error)
else:
    dif = int(x/y)
    # type of strings
    c = '-'
    d = '.'
    s = '|'
    string = 'WELCOME'.center(x, '-')

    # start of code
    dif_base = 0
    # top of pattern
    for i in range(y//2):
        print(((x // 2 - dif_base - 1)*c) + (i*'.|.') + '.|.' + (i*'.|.') + ((x // 2 - dif_base - 1)*c))
        dif_base += dif
    # mid of pattern
    print(string)
    # bot of pattern
    for i in range(y//2-1, -1, -1):
        dif_base -= dif
        print(((x // 2 - dif_base - 1)*c) + (i*'.|.') + '.|.' + (i*'.|.') + ((x // 2 - dif_base - 1)*c))
