class Solutuion:
    def longest_consecutive(self, nums:list[int])  ->int:
        numSet= set(nums)
        longest = 0
        for n in nums:
            if(n-1) not in numSet:
                length=0
                while(n+length) in numSet:
                    length+=1
                    longest=max(length, longest)
        return longest
print(Solutuion().longest_consecutive([88, 1, 55, 4, 5, 11, 20, 2, 3,]))

