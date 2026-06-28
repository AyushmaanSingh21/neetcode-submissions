class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        res = set()

        for i in range(len(nums)):

            target = -nums[i]

            left = i+1
            right = len(nums)-1

            while left < right:

                current = nums[left] + nums[right]

                if current == target:
                    res.add((nums[i], nums[left], nums[right]))
                    left +=1
                    right -=1


                elif current < target:
                    left += 1

                else:
                    right -= 1

        return [list(t) for t in res]
        