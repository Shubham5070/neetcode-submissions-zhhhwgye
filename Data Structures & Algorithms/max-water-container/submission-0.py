class Solution:
    def maxArea(self, heights: List[int]) -> int:
        left=0
        s=heights
        right=len(s)-1
        area=0
        maxarea=0
        
        while left<right:
            area=min(s[left],s[right])*(right-left)
            maxarea=max(maxarea,area)
            if s[left]<s[right]:
                left+=1
            else:
                right-=1
        return maxarea
            