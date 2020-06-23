class Solution:
    def isValid(self, s: str) -> bool:
        length = len(s)
        if length == 0: return True
        if length % 2: return False
    
        bracket = {
            ")": "(",
            "]": "[",
            "}": "{"
        }
        l = []

        for item in s:
            print(l,"   ", item)
            if not l:
                l.append(item)
            elif item in bracket:
                print("====", item)
                if l[-1] == bracket[item]:
                    l.pop()
                else:
                    return False
            else:
                l.append(item)

        return False if l else True
    
s = Solution()
print(s.isValid("{[]}"))