if __name__ == '__main__':
    n = int(input())
    arr = map(int, input().split())
    max_value = set(arr)
    max_value.remove(max(max_value))

    print(max(max_value))
