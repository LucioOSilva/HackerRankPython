"""
Task:
Given the names and grades for each student in a Physics class of N students, store them in a nested list and print the
name(s) of any student(s) having the second lowest grade.

Note: if there are multiple students with the same grade, order their names alphabetically and print each name on a new
line.

Input Format:
The first line contains an integer, N , the number of students.
The 2N subsequent lines describe each student over 2 lines; the first line contains a student's name, and the second line
contains their grade.

Constraints:
2 <= N <= 5
There will always be one or more students having the second lowest grade.

Output Format:
Print the name(s) of any student(s) having the second lowest grade in Physics; if there are multiple students, order
their names alphabetically and print each one on a new line.

Sample Input 0:
5
Harry
37.21
Berry
37.21
Tina
37.2
Akriti
41
Harsh
39

Sample Output 0:
Berry
Harry

Explanation 0:

There are 5 students in this class whose names and grades are assembled to build the following list:

python students = [['Harry', 37.21], ['Berry', 37.21], ['Tina', 37.2], ['Akriti', 41], ['Harsh', 39]]

The lowest grade of 37.2 belongs to Tina. The second lowest grade of 37.21 belongs to both Harry and Berry, so we order
their names alphabetically and print each name on a new line.
"""

if __name__ == '__main__':
    try:
        n = int(input())
    except (ValueError, TypeError) as error:
        print('An error occurred: ', {error})
    else:
        if 2 <= n <= 5:
            list_students = []
            try:
                for _ in range(n):
                    name = str(input())
                    score = float(input())
                    list_students.append([name, score])
            except (ValueError, TypeError) as error:
                print('An error occurred: ', {error})
            else:
                setnum = (set([obj for name, obj in list_students]))
                sec_hig = sorted(list(setnum))[1]  # transforming set to list, second lower valor, [0] means the lowest
                print('\n'.join([a for a, b in sorted(list_students) if b == sec_hig]))
