class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        # Optimal
        hashmap = {}
        for i in range(0,len(nums)):
            req = target - nums[i]

            if req in hashmap:
                return [i, hashmap[req]]
            hashmap[nums[i]] = i
                
       
