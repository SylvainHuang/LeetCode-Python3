class Solution:
    def fourSum(self, nums, target):
        def twoSum(nums, target):
            res = []
            maxNum = target >> 1
            for i in range(len(nums)):
                if nums[i] > maxNum: return res
                if i != 0 and nums[i] == nums[i-1]: continue
                 
                subNum = target - nums[i]
                if subNum in nums:
                    if subNum != nums[i] or nums.count(nums[i]) > 1:
                        res.append([nums[i], subNum])
            return res

        def kSum(nums, target, k):
            if len(nums) < k or nums[0] * k > target or nums[-1] * k < target:
                return []
            if k == 2:
                return twoSum(nums, target)
            res = []
            for i in range(len(nums)):
                if i == 0 or nums[i - 1] != nums[i]:
                    for item in kSum(nums[i+1:], target - nums[i], k-1):
                        res.append([nums[i]] + item)
            return res
        nums.sort()
        return kSum(nums, target, 4)
s = Solution()
print(s.fourSum([1,1,1,1], 4))