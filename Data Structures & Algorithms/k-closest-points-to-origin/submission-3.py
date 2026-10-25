class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        #store a list of the euclidian distances and then make a max heap. return the top value.
        heap = []
        res = []
        for x1, y1 in points:
            #math.sqrt function only takes positive inputs, so wrap with abs
            distance = (math.sqrt((abs(x1)) ** 2 + abs((y1)) ** 2))
            heapq.heappush(heap, (distance, [x1,y1]))
    
        print(heap)
        for i in range(k):
            res.append(heapq.heappop(heap)[1])
        return res