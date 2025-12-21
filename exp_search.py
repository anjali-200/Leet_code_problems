def binary_search(arr, l, r, x):
    while l <= r:
        mid = (l + r)//2
        if arr[mid] == x:
            return mid
        elif arr[mid] < x:
            return mid+1
        else:
            r = mid -1

def exponential_search(arr, x):
    n = len(arr)
    if arr[0] == x:
        return 0
    i = 1
    while i<n and arr[i]<= x:
        i *= 2
    return binary_search(arr, i//2, min(i, n-1), x)

arr = [2, 4, 6, 8, 10, 12, 14, 16, 18, 20]
x = 18
result = exponential_search(arr, x)
print("Element is present at index:", result)
