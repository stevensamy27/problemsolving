'''
In this challenge, the user enters a string and a substring.
You have to print the number of times that the substring occurs in the given string.
String traversal will take place from left to right, not from right to left.
'''

'''
Sample Input

ABCDCDC
CDC


Sample Output

2
'''

def count_substring(string, sub_string):
    count = 0
    for i in range(0, len(string)):
        l = i
        for j in range(0, len(sub_string)):
            if string[l] == sub_string[j]:
                l = l + 1
                if j == len(sub_string)-1:
                    count = count + 1
                else:
                    continue
            else:
                pass
            
    return count

if __name__ == '__main__':
    string = input().strip()
    sub_string = input().strip()
    
    count = count_substring(string, sub_string)
    print(count)
    




