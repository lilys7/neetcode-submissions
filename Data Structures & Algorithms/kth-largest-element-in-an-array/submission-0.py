class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        #keep the heap of size k and make it a min heap
        heapq.heapify(nums)
        while len(nums) > k:
            heapq.heappop(nums)
        return nums[0] if nums else None