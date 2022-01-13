### FIRST SOLUTION ###
def split_and_join(line):
    x = line.split()
    x = "-".join(x)
    return x
if __name__ == '__main__':
    line = input()
    result = split_and_join(line)
    print(result)



### ANOTHER SOLUTION ###
        
'''
def split_and_join(line):
    x = line.replace(" ", "_")
    return x
if __name__ == '__main__':
    line = input()
    result = split_and_join(line)
    print(result)
'''
