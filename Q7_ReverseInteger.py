class Solution:
    def reverse(self, x: int) -> int:
        result = 0
        isPositive = True
        INT_MAX = 2**31 - 1

        if x < 0:   # 如果是负数,设置标识,并转正数
            x = x * -1
            isPositive = False
        
        while x != 0:
            pop = x % 10
            x //= 10
            if result > INT_MAX//10 or (result == INT_MAX//10 and pop > 7):
                return 0
            result = result * 10 + pop
        
        if not isPositive:  # 如果是负数,则转为正数
            result *= -1
            
        return result
