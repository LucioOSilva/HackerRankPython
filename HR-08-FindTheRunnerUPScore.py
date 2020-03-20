if __name__ == '__main__':
    try:
        n = int(input())
        arr = list(map(int, input().split()))
    except (ValueError, TypeError) as error:
         print('An error occurred: ', error)
    else:
        if n == len(arr):
            if 2 <= n <= 10:
                if -100 <= max(arr) <= 100:
                    maxqt = arr.count(max(arr))
                    arr.sort(reverse=True)
                    print(arr[maxqt])
