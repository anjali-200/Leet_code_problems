class solution:
    def strStr(self, haystack: str, needle: str) -> int:
        if len(needle) == 0:
            return 0
        if len(haystack)< len(needle):
            return -1
        for i in range (len(haystack)):
            if haystack [i: i + len(needle)] == needle:
                return i
        return -1
    
if __name__ == "__main__":
    haystack = "summerumbrella"
    needle = "ummer"
    sol = solution()
    print("string found:", sol.strStr(haystack, needle))