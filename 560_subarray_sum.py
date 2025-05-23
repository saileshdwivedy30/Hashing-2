# Use prefix sum and hashmap to count subarrays that sum to k.
# For each prefix sum check if (prefix - k) has occurred before.
# Add the count of that to the result.

# Time Complexity: O(n)
# Space Complexity: O(n)

class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        count = 0
        prefix_sum = 0
        prefix_counts = defaultdict(int)
        prefix_counts[0] = 1

        for num in nums:
            prefix_sum += num
            count += prefix_counts[prefix_sum - k]
            prefix_counts[prefix_sum] += 1

        return count




