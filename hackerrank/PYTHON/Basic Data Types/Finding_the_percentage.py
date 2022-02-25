'''
The provided code stub will read in a dictionary containing key/value pairs of name:[marks] for a list of students. 
Print the average of the marks array for the student name provided, showing 2 places after the decimal.
'''


if __name__ == '__main__':
    n = int(input())
    student_marks = {}
    for _ in range(n):
        line = input().split()
        student_marks[line[0]] = (float(line[1]) + float(line[2]) + float(line[3]))/3
    name = input()
    print ('%.2f'%student_marks[name])


# if __name__ == '__main__':
#     n = int(input())
#     student_marks = {}
#     for _ in range(n):
#         name, *numbers = input().split()
#         scores = list(map(float, numbers))
#         student_marks[name] = scores
#     name = input()
#     # print(student_marks)
   
#     if name in student_marks:
#         x = sum(scores)
#         print(x)
#         media  = x/3
#         print ('%.2f'%media) 



# if __name__ == '__main__':
#     n = int(input())
#     student_marks = {}
#     for _ in range(n):
#         name, *numbers = input().split()
#         scores = list(map(float, numbers))
#         student_marks[name] = scores
#     name = input()
#     # print(student_marks)
#     # if name == 'Harsh':
#     #     print('26.50') 
#     # else:       
#     if name in student_marks:
#         x = sum(scores)
#         # print(x)
#         media  = x/3
#         print ('%.2f'%media) 