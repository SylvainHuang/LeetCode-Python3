class Solution:
    def longestPalindrome(self, s: str) -> str:
        if len(s) <= 1:
            return s
        # 在查找回文串之前,先对原串预处理,避免对偶数回文串特殊处理
        ss = '#' + '#'.join([x for x in s]) + '$'
        print(ss)

        idx = 0                 # 记录当前回文串右边界最大的中心下标
        mx  = 0                 # 记录当前回文串最大右边界的下标
        p   = [0] * len(ss)     # 记录下标为i的回文串的半径,不包含i本身 
        maxStr = ""

        for i in range(1, len(ss)-1):   # 开始和结尾的特殊符号可以不处理
            if i < mx:
                j = idx * 2 - i # 关于中心点对称下标
                p[i] = min(mx-i, p[j])

            # 重新拓展比较
            while ss[i - p[i] - 1] == ss[i + p[i] + 1]: # 不必担心溢出,首尾都是特殊符号
                p[i] += 1

            # 更新中心下标
            if i + p[i] > mx:
                mx = i + p[i]
                idx = i

            # 更新最长串
            if 1 + 2 * p[i] >= len(maxStr) * 2 + 1:
                tmpStr = ss[i-p[i] : i+p[i]+1].replace('#', '')
                if len(tmpStr) > len(maxStr):
                    maxStr = tmpStr
        return maxStr
