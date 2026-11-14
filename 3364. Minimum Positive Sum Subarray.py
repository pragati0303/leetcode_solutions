class Solution:
    def minimumSumSubarray(self, nums, l, r):
        answer = float('inf')

        for i in range(len(nums)):
            current_sum = 0

            for j in range(i, min(len(nums), i + r)):
                current_sum += nums[j]
                length = j - i + 1

                if l <= length <= r and current_sum > 0:
                    answer = min(answer, current_sum)

        return answer if answer != float('inf') else -1