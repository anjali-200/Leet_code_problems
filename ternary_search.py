def ternary_search(array, target):
    return ts(array, 0, len(array)-1, target)
def ts(array, l, r, target):
    if l>r:
        return -1
    mid1 = l+(r-l)//3
    mid2 = r-(r-l)//3
    if target == array[mid1]:
        return mid1
    if target == array[mid2]:
        return mid2 
    if target < array[mid1]:
        return ts(array, l, mid1-1, target)
    elif target > array[mid2]:
        return ts(array, mid2+1, r, target)
    else:
        return ts(array, mid1+1, mid2-1, target)

if __name__ == "__main__":
    array = [7,12,19,24,31,48,51,65,67,63,74,81,92]
    target = 48
    result = ternary_search(array, target)
    print("result:", result)

