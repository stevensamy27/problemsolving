if __name__ == '__main__':
    n = int(input())
    integer_list = map(int, input().split())
    x = tuple(integer_list)
    print(hash(x))

## STEPS

# 1- Create a Tuple of integer_list
# 2- using hash function 
#          print a hash of tuple

'''

Input Format

The first line contains an integer, n , denoting the number of elements in the tuple.
The second line contains n space-separated integers describing the elements in tuple t.

------------------

Output Format

Print the result of hash(t) .

'''

'''
Sample Input 0

2
1 2

------------------------------------

Sample Output 0

3713081631934410656

'''