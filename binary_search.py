array = [10, 20, 30, 40, 50, 60, 70, 80, 90]
def binary(array,target):
    left, right = 0, len(array)-1
    while left<=right:
        mid=(left+right)//2
        if array[mid]==target:
            return mid
        elif array[mid]<=target:
            left=mid+1
        else:
            right = mid - 1
    return -1
if __name__ == "__main__":
    target = 80
    idx = binary(array, target)
    print(f"target {target} found at index: {idx}" if idx != -1 else f"target {target} not found")