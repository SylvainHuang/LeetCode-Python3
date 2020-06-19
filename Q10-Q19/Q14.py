class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        if len(strs) == 0:
            return ''
        if len(strs) == 1:
            return strs[0]
        
        prefix = ''
        ch = ""
        
        smallLen = 9999
        for str in strs:
            smallLen = min(len(str), smallLen)
            
        for i in range(smallLen):
            ch = strs[0][i]
            for j in range(1, len(strs)):
                if strs[j][i] != ch:
                    return prefix
            prefix += ch
        return prefix