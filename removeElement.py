class Solution:
    def removeElement(self, nums: list[int], val: int) -> int:
        k = 0  # Pointer for the position of the next non-val element
        for i in range(len(nums)):
            if nums[i] != val:
                nums[k] = nums[i]
                k += 1
        return k
    
list = [3,2,2,3,96,4,3,5,3]
val = 3
sol = Solution()
new_length = sol.removeElement(list, val)
print(f"New length: {new_length}, Modified list: {list[:new_length]}")
