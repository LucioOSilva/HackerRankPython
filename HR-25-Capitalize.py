"""
You are asked to ensure that the first and last names of people begin with a capital letter in their passports.
For example, alison heck should be capitalised correctly as Alison Heck.
alisonheck => AlisonHeck

Given a full name, your task is to capitalize the name appropriately.

Input Format:
A single line of input containing the full name, S.

Constraints:
0 < len(S) < 1000
>>The string consists of alphanumeric characters and spaces.

Note: in a word only the first character is capitalized. Example 12abc when capitalized remains 12abc.

Output Format:
Print the capitalized string, S.

Sample Input:
chris alan

Sample Output:
Chris Alan
"""

# case1 - with mutable array
def solve(s):
    arr = s.split(' ')
    arr2 = []
    for i in arr:
        a = i.capitalize()
        arr2.append(a)
    return ' '.join(arr2)



if __name__ == '__main__':
    s = input()
    # s = '      bamama   a q w e r t y u i o p a s d f ghj  k l z x c v b n m Q W E R T Y U I O P A S D F G H J  K L
    # Z X C V B N M --- Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod temporA a           '
    print(solve(s))
