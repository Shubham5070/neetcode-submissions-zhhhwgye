class Solution:
    def threeSum(self, nums):
        s = sorted(nums)
        res = []
        
        for i in range(len(s)):
            if i > 0 and s[i] == s[i-1]:
                continue
            
            tar = -s[i]
            left = i + 1
            right = len(s) - 1
            
            while left < right:
                total = s[left] + s[right]
                
                if total == tar:
                    res.append([s[i], s[left], s[right]])
                    
                    # ✅ skip duplicates AFTER match
                    while left < right and s[left] == s[left+1]:
                        left += 1
                    while left < right and s[right] == s[right-1]:
                        right -= 1
                    
                    left += 1
                    right -= 1
                
                elif total < tar:
                    left += 1
                
                else:
                    right -= 1
        
        return res