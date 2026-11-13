from typing import List
from collections import deque

class Solution:
    def countNonDecreasingSubarrays(self, nums: List[int], k: int) -> int:
        n = len(nums)

        # Stores [value, count]
        dq = deque()

        left_cost = 0
        right = n - 1
        answer = 0

        # Process from right to left
        for left in range(n - 1, -1, -1):
            value = nums[left]
            count = 1

            # Merge elements smaller than the current value
            while dq and dq[0][0] <= value:
                old_value, old_count = dq.popleft()

                left_cost += (value - old_value) * old_count
                count += old_count

            dq.appendleft((value, count))

            # If cost is greater than k, shrink from the right
            while left_cost > k:
                value_at_right, count_at_right = dq[-1]

                # Remove the cost contributed by nums[right]
                left_cost -= value_at_right - nums[right]

                count_at_right -= 1

                if count_at_right == 0:
                    dq.pop()
                else:
                    dq[-1] = (value_at_right, count_at_right)

                right -= 1

            # All subarrays from left to right, left to right-1, etc. are valid
            answer += right - left + 1

        return answer