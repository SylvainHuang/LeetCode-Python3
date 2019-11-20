class Solution:
    def lengthOfLongestSubstring(self, s):
        """
        :type s: str
        :rtype: int
        """
        smax = scur = startidx = 0
        slen = len(s)
        for i in range(0,slen):
        	fidx = s[startidx:i].find(s[i])
        	if -1 != fidx:
        		smax = smax if smax > scur else scur
        		startidx += fidx + 1
        		scur -= fidx
        	else: scur += 1
        smax = smax if smax > scur else scur
        return smax
