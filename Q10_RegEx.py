class Solution:
    def isMatch(self, s: str, p: str) -> bool:
        mem = {}
        
        def f(i,j): # 递归函数
            if (i, j) not in mem:
                if j == len(p):
                    ans = i == len(s)
                else:
                    first_match = i < len(s) and p[j] in [s[i], '.']
                    if j + 1 < len(p) and p[j+1] == '*':
                        ans = f(i, j+2) or (first_match and f(i+1, j))
                    else:
                        ans = first_match and f(i+1, j+1)
                mem[i, j] = ans
            return  mem[i, j]
        return f(0,0)
