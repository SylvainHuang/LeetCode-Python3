class Solution:
    def intToRoman(self, num: int) -> str:
    	if num > 3999: return 'out of range'
    	res = ''

    	tmp = num
    	M = tmp // 1000
    	tmp = tmp % 1000
    	C = tmp // 100
    	tmp = tmp % 100
    	X = tmp // 10
    	I = tmp % 10

    	if M:
    		res += 'M' * M
    	if C:
    		if 9 == C:
    			res += 'CM'
    		elif C // 5:
    			res += 'D'
    			res += 'C' * (C % 5)
    		elif 4 == C:
    			res += 'CD'
    		else:
    			res += 'C' * C
    	if X:
    		if 9 == X:
    			res += 'XC'
    		elif X // 5:
    			res += 'L'
    			res += 'X' * (X % 5)
    		elif 4 == X:
    			res += 'XL'
    		else:
    			res += 'X' * X
    	if I:
    		if 9 == I:
    			res += 'IX'
    		elif I // 5:
    			res += 'V'
    			res += 'I' * (I % 5)
    		elif 4 == I:
    			res += 'IV'
    		else:
    			res += 'I' * I
    	print(res)


if __name__ == '__main__':
	s = Solution()
	s.intToRoman(33)