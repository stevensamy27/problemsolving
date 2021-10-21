'''
A and B are preparing themselves for programming contests.

B loves to debug his code. But before he runs the solution and starts debugging,
 he has to first compile the code.

Initially, the compiler displayed n compilation errors, each of them is represented as a positive integer.
 After some effort, B managed to fix some mistake and then another one mistake.

However, despite the fact that B is sure that he corrected the two errors,
 he can not understand exactly what compilation errors disappeared — the compiler of the language which B uses shows errors in the new order every time! B is sure that unlike many other programming languages, 
 compilation errors for his programming language do not depend on each other, that is, if you correct one error,
  the set of other error does not change.

Can you help B find out exactly what two errors he corrected?

Input
The first line of the input contains integer n (3 ≤ n ≤ 105) — the initial number of compilation errors.

The second line contains n space-separated integers a1, a2, ..., an (1 ≤ ai ≤ 109) — the errors the compiler displayed for the first time.

The third line contains n - 1 space-separated integers b1, b2, ..., bn - 1 — the errors displayed at the second compilation.
 It is guaranteed that the sequence in the third line contains all numbers of the second string except for exactly one.

The fourth line contains n - 2 space-separated integers с1, с2, ..., сn - 2 — the errors displayed at the third compilation.
 It is guaranteed that the sequence in the fourth line contains all numbers of the third line except for exactly one.

Output
Print two numbers on a single line: the numbers of the compilation errors that disappeared after B made the first and the second correction,
 respectively.

Examples
input
5
1 5 8 123 7
123 7 5 1
5 1 7
output
8
123

input
6
1 4 3 3 5 7
3 7 5 4 3
4 3 7 5
output
1
3
'''

n = int (input())
errors   = list(map(int,input().strip().split()))
errors_1 = list(map(int,input().strip().split()))
errors_2 = list(map(int,input().strip().split()))

SUM_errors   = sum(errors)
SUM_errors_1 = sum(errors_1)
SUM_errors_2 = sum(errors_2)
x = SUM_errors - SUM_errors_1
y = SUM_errors_1 - SUM_errors_2
print(x)
print(y)



# n = int (input())
# errors   = input().split()
# errors_1 = input().split()
# errors_2 = input().split()
# x = ()
# y = ()
# for i in errors:
#   if i not in errors_1:
#     x = i
# for i in errors_1:
#   if i not in errors_2:
#     y = i

# print(x)
# print(y)

