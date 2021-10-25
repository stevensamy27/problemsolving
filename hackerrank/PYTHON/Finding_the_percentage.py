if __name__ == '__main__':
    n = int(input())
    student_marks = {}
    for _ in range(n):
        name, *numbers = input().split()
        scores = list(map(float, numbers))
        student_marks[name] = scores
    name = input()
    
    # if name in student_marks:
    print(student_marks)