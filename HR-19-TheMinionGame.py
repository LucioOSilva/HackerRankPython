"""TheMinionGame
Kevin and Stuart want to play the 'The Minion Game'.

Game Rules:
Both players are given the same string, "S".
Both players have to make substrings using the letters of the string "S".
Stuart has to make words starting with consonants.
Kevin has to make words starting with vowels.
The game ends when both players have made all possible substrings.

Scoring:
A player gets +1 point for each occurrence of the substring in the string "S".

For Example:
String "S" = BANANA
Kevin's vowel beginning word = ANA
Here, ANA occurs twice in BANANA. Hence, Kevin will get 2 Points.

Your task is to determine the winner of the game and their score.

Input Format:
A single line of input containing the string "S".
Note: The string "S" will contain only uppercase letters: [A -Z].

Constraints:
0 <= len(S) <= 10**6

Output Format:
Print one line: the name of the winner and their score separated by a space.
If the game is a draw, print Draw.

Sample Input:
BANANA

Sample Output:
Stuart 12

Note:
Vowels are only defined as AEIOU. In this problem, "Y" is not considered a vowel.
"""

"""
------------------------------------------------------------------------------------------------------------------------
The test was solved by two ways, one of they shows up the strings formed with the initial string (list).
------------------------------------------------------------------------------------------------------------------------
"""
string_input = 'banana'

string = string_input.upper()
cons = vow = 0
for k, v in enumerate(string):
    if v in 'AEIOU':
        vow += len(string)-k
    else:
        cons += len(string)-k
if cons == vow:
    print('Draw')
elif cons > vow:
    print('Stuart', cons)
else:
    print('Kevin', vow)

print('-='*20)  # ######################################################

sname = string_input.upper()
list_vowel = []
list_consonant = []

for w, x in enumerate(sname):
    if x in 'AEIOU':
        namecut = sname[w:]
        for k, v in enumerate(namecut):
            name = namecut[0:k + 1]
            list_vowel.append(name)
    else:
        namecut = sname[w:]
        for k, v in enumerate(namecut):
            name = namecut[0:k + 1]
            list_consonant.append(name)

if len(list_consonant) == len(list_vowel):
    print('Draw')
elif len(list_consonant) > len(list_vowel):
    print('Stuart', len(list_consonant))
else:
    print('Kevin', len(list_vowel))
