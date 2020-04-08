"""
Consider the following:
>> A string, s , of length n, where: s = c[0],c[1],c[2]....c[n-1]
>> An integer, k , where k is a factor of n.
We can split "s" into "n/k" subsegments where each subsegment, t[i] , consists of a contiguous block of k characters in
"s". Then, use each t[i] to create string Ui such that:

>> The characters in Ui are a subsequence of the characters in t[i].
>> Any repeat occurrence of a character is removed from the string such that each character in Ui occurs exactly once.
In other words, if the character at some index j in t[i] occurs at a previous index < j in t[i], then do not include the
character in string Ui.
Given s and k, print "n/k" lines where each line i denotes string u[i].

Input Format:
The first line contains a single string denoting s.
The second line contains an integer, k, denoting the length of each subsegment.

Constraints:
>> 1 <= n <= 10^4, where n is the length of s.
>> It is guaranteed that n is a multiple of k.

Output Format:
Print "n/k" lines where each line i contains string Ui.

Sample Input:
AABCAAADA
3

Sample Output:
AB
CA
AD

Explanation:
String s is split into n/k = 9/3 = 3 equal parts of length k=3. We convert each t[i] to Ui by removing any subsequent
occurrences non-distinct characters in t[i]:

1>> t[0] = "AAB" -> u[0] = "AB"
2>> t[1] = "CAA" -> u[1] = "CA"
3>> t[2] = "ADA" -> u[2] = "AD"

We then print each Ui on a new line.
"""

"""
def merge_the_tools(string, k):
    arr = []
    for i in range(0, len(string), k):
        arr.append(string[k])
    return arr
    

if __name__ == '__main__':
    string, k = input(), int(input())
    merge_the_tools(string, k)
    print(merge_the_tools(string, k))
"""


def merge_the_tools(string, k):
    arr = []
    new_arr = []

    for _ in string:
        if len(string) > 0:
            arr.append(string[:k])
            string = string[k:]
        else:
            break

    for i in arr:
        new_string = ''
        for j in i:
            if j not in new_string:
                new_string += j
        new_arr.append(new_string)

    for w in new_arr:
        print(w)


if __name__ == '__main__':
    string, k = input(), int(input())
    merge_the_tools(string, k)