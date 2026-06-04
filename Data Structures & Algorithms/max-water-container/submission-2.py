class Solution:
    def maxArea(self, heights: List[int]) -> int:
        l=0
        r=len(heights)-1
        maxlen=0
        while l<=r:
            lens=min(heights[l],heights[r])*(r-l)
            maxlen=max(maxlen,lens)
            if heights[l]<=heights[r]:
                l+=1
            else:
                r-=1
            print(maxlen,l,r)
        return maxlen


        