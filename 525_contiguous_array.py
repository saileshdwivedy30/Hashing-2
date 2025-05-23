# Replace 0 with -1 and find the longest subarray with sum = 0.
# Use a hashmap to store the first occurrence of each prefix sum.
# If the same sum is seen again, the subarray between has sum = 0.

# Time Complexity: O(n)
# Space Complexity: O(n)

class Solution:
    def findMaxLength(self, nums: List[int]) -> int:
        prefix_sum = 0
        max_len = 0
        index_map = {0: -1}  # sum 0 occurs before the array starts

        for i, num in enumerate(nums):
            prefix_sum += -1 if num == 0 else 1

            if prefix_sum in index_map:
                max_len = max(max_len, i - index_map[prefix_sum])
            else:
                index_map[prefix_sum] = i

        return max_len
