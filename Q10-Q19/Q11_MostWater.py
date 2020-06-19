class Solution:
    def maxArea(self, height) -> int:
    	start = 0
    	end = len(height) - 1
    	marea = area = 0
    	while end > start:
    		area = (end - start) * min(height[start], height[end])
    		marea = max(area, marea)
    		if height[start] > height[end]:
    			end-=1
    		else:
    			start+=1
    	return marea
