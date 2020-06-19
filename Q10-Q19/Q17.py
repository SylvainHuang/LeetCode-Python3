class Solution:
    def letterCombinations(self, digits: str):
        phone = {
                    "2":["a", "b", "c"],
                    "3":["d", "e", "f"],
                    "4":["g", "h", "i"],
                    "5":["j", "k", "l"],
                    "6":["m", "n", "o"],
                    "7":["p", "q", "r", "s"],
                    "8":["t", "u", "v"],
                    "9":["w", "x", "y", "z"],
                }
        ans = []
        for num in digits:
            if not ans:
                for ch in phone[num]:
                    ans.append(ch)
            else:
                for i in range(len(ans)):
                    s = ans.pop(0)
                    for ch in phone[num]:
                        ans.append(s+ch)
        return ans
                