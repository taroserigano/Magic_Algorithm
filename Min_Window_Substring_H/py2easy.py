class Solution:
    def minWindow(self, s: str, t: str) -> str:
        """
        :type s: str
        :type t: str
        :rtype: str
        """
        len_s, len_t = len(s), len(t)
        if not s or not t or len_s<len_t:
            return ""
        
        dic, count = {}, 0
        left, right, min_width = 0, 0, len_s + 1
        res = ""
        for c in t:
            dic[c] = dic.get(c,0)+1

        while right < len_s:
            if s[right] in dic:
                if dic[s[right]]>0:
                    count+=1
                dic[s[right]]-=1
            
            while count == len(t):
                if right-left+1 < min_width:
                    min_width = right-left+1
                    res = s[left:right+1]
                
                if s[left] in dic:
                    dic[s[left]]+=1
                    if dic[s[left]] > 0:
                        count-=1
                left+=1
            right+=1
        return res
