class Solution:
    def subarraySum(self, nums: list[int], k:int) -> int:
        sumdict = {0:1}
        n= len(nums)
        count = 0
        s = 0
        for num in nums:
            s+= num 
            if s - k in sumdict:
                count += sumdict[s-k]
                #sumdict[s]= sumdict.get(s, 0)+1
            if s in sumdict:
                sumdict[s]+=1
            else:
                sumdict [s]=1
        return count
            

#input = subarraySum([3,7,14,16,13,14,18,20,1])
print(Solution().subarraySum([3,7,14,16,13,14,18,20,1], 7))






