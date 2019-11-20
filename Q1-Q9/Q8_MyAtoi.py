class Solution:
    def myAtoi(self, str: str) -> int:
        sign = 1
        result = 0
        bStart = False  # 记录是否开始转换数字
        INT_MAX = 2 ** 31 - 1
        INT_MIN = 2 ** 31 * -1

        str = str.lstrip()

        for ch in str:
            if not bStart:  # 没有开始转换数字,先解释符号
                if ch == '-':
                    sign *= -1
                elif ch == '+':
                    continue
                elif ord(ch) < 48 or ord(ch) > 57:  # 在开始转换数字之前遇到非数字/符号,返回0
                    return 0
                else:   # 数字
                    bStart = True
                    result = result * 10 + ord(ch) - ord('0')
            else:   # 已经开始转换数字
                if ord(ch) < 48 or ord(ch) > 57:
                    return result * sign
                else :
                    if sign == 1:
                        if result  > INT_MAX // 10 or (result == INT_MAX // 10 and ord(ch) - ord('0') > 7):
                            return INT_MAX
                    else:
                        if result  > INT_MAX // 10 or (result == INT_MAX // 10 and ord(ch) - ord('0') > 8):
                            return INT_MIN
                    result = result * 10 + ord(ch) - ord('0')
        return result * sign
