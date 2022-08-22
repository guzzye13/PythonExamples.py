def removeDuplicates(arr, n):
    if n == 0 or n == 1:
        return n
    temp = list(range(n))
    j = 0
    for i in range(0, n-1):
        if arr[i] != arr[i+1]:
            temp[j] = arr[i]
            j += 1
    temp[j] = arr[n-1]
    j += 1
    for i in range(0, j):
        arr[i] = temp[i]
    return j


arr = [1, 1, 1, 4, 5, 6, 8, 8, 9]
n = len(arr)
n = removeDuplicates(arr, n)
for i in range(n):
    print(arr[i], end=", ")