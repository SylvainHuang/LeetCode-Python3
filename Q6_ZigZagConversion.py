class Solution:
    def convert(self, s: str, numRows: int) -> str:
        if numRows == 0 or numRows == 1:
            return s
        if len(s) < numRows:
            return s
        
        result = ""
        lines = [""] * numRows
        direction = 0
        row = 0
        
        for ch in s:
            lines[row] += ch

            # 设置行走向
            if row == 0:
                direction = 1
            elif row == numRows - 1:
                direction = 0

            if direction:
                row += 1
            else :
                row -= 1
        
        # 将每一行的字符串合并为结果
        for line in lines:
            result += line 
        return result
