class Solution:
    def minWindow(self, s: str, t: str) -> str:
        if t == "": return ""
        
        countT, window = {}, {}
        for c in t:
            # if saved, add 1 + .get(c) * 1 = 2
            # if not saved, 1 + 0*default value = 1 
            countT[c] = 1 + countT.get(c, 0)
        
        have, need = 0, len(countT)
        res, resLen = [-1, -1], float("infinity")
        l = 0
        for r in range(len(s)):
            # current character
            c = s[r]
            # add to substring window
            window[c] = 1 + window.get(c, 0)
            # if substring window  matches with countT required character
            if c in countT and window[c] == countT[c]:
                have += 1
            # if all characters now match
            while have == need:
                # this should always be less than infinite number
                if (r - l + 1) < resLen:
                    # now update the variables
                    res = [l, r]
                    resLen = (r - l + 1)
                # pop from the left of our window
                window[s[l]] -= 1
                # if window is now less than countT, meaning the matching character was extracted
                # get it out of the loop and return result 
                if s[l] in countT and window[s[l]] < countT[s[l]]:
                    have -= 1
                # otherwise, keep moving left
                l += 1
        l, r = res
        return s[l:r+1] if resLen != float("infinity") else ""
