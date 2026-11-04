from typing import List
import heapq
from collections import defaultdict


class Solution:
    def minOperations(self, nums: List[int], x: int, k: int) -> int:
        n = len(nums)
        m = n - x + 1
        cost = [0] * m

        # Two heaps
        # left: max heap (store negative values)
        # right: min heap
        left = []
        right = []

        # Delayed deletion
        delayed = defaultdict(int)

        left_sum = 0
        right_sum = 0

        def prune_left():
            while left:
                num = -left[0]
                if delayed[num] > 0:
                    delayed[num] -= 1
                    heapq.heappop(left)
                else:
                    break

        def prune_right():
            while right:
                num = right[0]
                if delayed[num] > 0:
                    delayed[num] -= 1
                    heapq.heappop(right)
                else:
                    break

        # Instead of complicated lazy deletion with duplicates,
        # use a sorted list approach for smaller windows.
        # But for maximum constraints, we need an efficient method.

        # Coordinate compression + Fenwick Trees
        values = sorted(set(nums))
        rank = {v: i + 1 for i, v in enumerate(values)}
        size = len(values)

        bit_count = [0] * (size + 1)
        bit_sum = [0] * (size + 1)

        def update(bit, idx, val):
            while idx <= size:
                bit[idx] += val
                idx += idx & -idx

        def query(bit, idx):
            result = 0
            while idx > 0:
                result += bit[idx]
                idx -= idx & -idx
            return result

        def find_kth(target):
            idx = 0
            step = 1 << (size.bit_length() - 1)

            while step:
                next_idx = idx + step
                if next_idx <= size and bit_count[next_idx] < target:
                    target -= bit_count[next_idx]
                    idx = next_idx
                step >>= 1

            return idx + 1

        # Add/remove elements and calculate window costs
        for i in range(n):
            v = nums[i]
            r = rank[v]

            update(bit_count, r, 1)
            update(bit_sum, r, v)

            if i >= x:
                old = nums[i - x]
                old_r = rank[old]

                update(bit_count, old_r, -1)
                update(bit_sum, old_r, -old)

            if i >= x - 1:
                total_count = x
                total_sum = query(bit_sum, size)

                # Lower median position
                median_rank = find_kth((x + 1) // 2)
                median = values[median_rank - 1]

                left_count = query(bit_count, median_rank)
                left_sum_window = query(bit_sum, median_rank)

                # Cost for elements <= median
                left_cost = median * left_count - left_sum_window

                right_count = total_count - left_count
                right_sum_window = total_sum - left_sum_window

                # Cost for elements > median
                right_cost = right_sum_window - median * right_count

                cost[i - x + 1] = left_cost + right_cost

        # DP for choosing k non-overlapping subarrays
        INF = 10**30

        prev = [0] * (n + 1)

        for groups in range(1, k + 1):
            curr = [INF] * (n + 1)

            for i in range(1, n + 1):
                # Skip current element
                curr[i] = curr[i - 1]

                # Take subarray of length x ending at i
                if i >= x and prev[i - x] != INF:
                    curr[i] = min(
                        curr[i],
                        prev[i - x] + cost[i - x]
                    )

            prev = curr

        return prev[n]