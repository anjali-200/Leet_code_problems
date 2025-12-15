def quick_sort(arr):
    if len(arr) <=1:
        return arr
    pivot = arr[len(arr)//2]
    left = [i for i in arr if i < pivot]
    middle= [j for j in arr if j == pivot]
    right = [k for k in arr if k > pivot]
    return quick_sort(left)+middle+quick_sort(right)

input_arr = [6,3,8,4,1236,23,1,9]
print(quick_sort(input_arr))