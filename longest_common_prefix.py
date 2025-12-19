class Solution:
    def longest_common(self, strs : list[str]) -> str:
        res = ""
        for i in range (len(strs[0])):
            for s in strs:
                if i == len(s) or s[i] != strs[0][i]:
                    return res
            res += strs[0][i]
        return res
#if __name__ == "__main__":
   # print(Solution().longest_common(["flower", "flow", "flight"]))  # expected "fl"
    #print(Solution().longest_common([]))                            # expected ""
    #print(Solution().longest_common(["", "abc"]))                   # expected ""
#words1 = ["flower", "flow", "flight"]
#words2 = ["dog", "racecar", "car"]

#print(f"LCP of {words1}: '{longest_common(words1)}'")
#print(f"LCP of {words2}: '{longest_common(words2)}'")
sol = Solution()
print(sol.longest_common(["flower", "flow", "flight"]))  # Output: "fl"
print(sol.longest_common(["dog", "racecar", "car"]))     # Output: ""










