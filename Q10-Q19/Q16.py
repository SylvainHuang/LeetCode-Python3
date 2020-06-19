class Solution:
    def threeSumClosest(self, nums, target: int) -> int:
        diff = 0xFFFF

        # judge nums length
        length = len(nums)
        if length < 3: return diff
        if length == 3: return nums[0] + nums[1] + nums[2]
        
        nums.sort()

        for i in range(length - 2):
            k = length - 1
            for j in range(i+1, length - 1):
                if j >= k: break
                while k > j:
                    tmp = nums[i] + nums[j] + nums[k] - target
                    diff = diff if abs(tmp) > abs(diff) else tmp
                    if 0 == diff: return target
                    if tmp > 0: k -= 1
                    else: break
        return target+diff
