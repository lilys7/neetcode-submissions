class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        #use a queue and a max heap (that stores the counts of the characters) keep a time variable as well
        #counts.values
        counts = Counter(tasks)
        #create a maxheap with the counts
        maxHeap = [-count for count in counts.values()]
        heapq.heapify(maxHeap)
        time = 0
        q = collections.deque()
        #we wanna start with the most frequent elements
        #queue is gonna store [count, idletime]
        while maxHeap or q:
            time += 1
            if maxHeap:
                val = 1 + heapq.heappop(maxHeap)
                if val:
                    q.append([val, time + n])
            if q and q[0][1] == time:
                heapq.heappush(maxHeap, q.popleft()[0])
        return time

        

