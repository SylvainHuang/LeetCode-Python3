class Solution:
    def romanToInt(self, s: str) -> int:
        symbol = {
            "I":1, 
            "V":5,
            "X":10,
            "L":50,
            "C":100,
            "D":500,
            "M":1000
        }
        
        res = 0;
        pre = 0;
        
        for ch in s:
            cur = symbol[ch]
            if cur > pre:
                res += cur - (pre << 1)
            else:
                res += cur
            pre = cur
        print(res)

if __name__ == '__main__':
    s = Solution()
    s.romanToInt('XXI')