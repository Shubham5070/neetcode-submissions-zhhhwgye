class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        left=0
        maxlen=0
        x=set()
        
        for right in range(len(s)):
            while s[right] in x:
                x.remove(s[left])
                left+=1
                
            x.add(s[right])
            maxlen=max(maxlen,right-left+1)
        return maxlen


