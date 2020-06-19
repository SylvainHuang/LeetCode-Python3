class Solution:
    def threeSum(self, nums):
        length = len(nums)
        if length < 3: return []
        
        ans = []
        nums.sort()

        for i in range(length - 2):
            k = length-1
            if i > 0 and nums[i] == nums[i-1]: continue
            if nums[i] > 0:
                return ans
            for j in range(i+1, k):
                if j > i+1 and nums[j] == nums[j-1]: continue
                if nums[i] + nums[j] > 0: break
                while k > j:
                    if nums[i] + nums[j] + nums[k] > 0:
                        k -= 1
                    elif nums[i] + nums[j] + nums[k] == 0:
                        ans.append([nums[i], nums[j], nums[k]])
                        break
                    else:
                        break
        return ans

s = Solution()
print(s.threeSum([-4,-2,-2,-2,0,1,2,2,2,3,3,4,4,6,6]))