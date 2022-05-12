class Solution:
    def lengthOfLongestSubstring(self, str: str) -> int:
        # "pwwkew"
        # abc abc bb 
        charSet = set()
        l = 0 
        res = 0 

        for r in range(len(str)):
            # if character in charSet, remove it
            # then move the Left
            while str[r] in charSet:
                print(charSet)
                charSet.remove(str[l])
                l += 1
            
            # add the character
            charSet.add(str[r]) 
            print("res ", res, " r ", r, " l ", l )
            res = max(res, r - l + 1) 
        return res     
