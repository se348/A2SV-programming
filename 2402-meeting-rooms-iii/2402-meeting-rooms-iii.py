class Solution:
    def mostBooked(self, n: int, meetings: List[List[int]]) -> int:
        being_used = []
        available = [i for i in range(n)]
        
        heapq.heapify(available)
        
        count = [0] * n
        meetings.sort()
        
        for start, end in meetings:
            
            while being_used and being_used[0][0] <= start:
                time, room = heapq.heappop(being_used)
                heapq.heappush(available, room)
                
            if available:
                room = heapq.heappop(available)
                heapq.heappush(being_used, (end, room))
                count[room] += 1

            else:
                time, room = heapq.heappop(being_used)
                heapq.heappush(being_used, (time + end- start, room))
                count[room] += 1

        return count.index(max(count))