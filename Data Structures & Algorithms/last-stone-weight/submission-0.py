class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        #make a maxheap and while the length is greater than 1, we will compare the top element and the index 1 element. if equal, remove both eleemnts. If one is larger, return the diff. IF one element left we return the top element left
        for i in range(len(stones)):
            stones[i] = -stones[i]
        heapq.heapify(stones)
        while len(stones) > 1:
            x = -heapq.heappop(stones)
            y = -heapq.heappop(stones)
            if x != y:
                heapq.heappush(stones, -abs(x-y))
        return -stones[0] if stones else 0
