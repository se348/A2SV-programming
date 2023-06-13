class Solution:
    def rearrangeBarcodes(self, barcodes: List[int]) -> List[int]:
        count_res = Counter(barcodes)
        max_heap = []
        
        for num, count in count_res.items():
            heapq.heappush(max_heap, (-count, num))
        
        result = []
     
        while max_heap:
            current_count, current_num = heapq.heappop(max_heap)
            
            if result and result[-1] == current_num:
                next_count, next_num = heapq.heappop(max_heap)
                result.append(next_num)
                next_count += 1
                if next_count != 0:
                    heapq.heappush(max_heap, (next_count, next_num))
            
            result.append(current_num)
            current_count += 1
            if current_count != 0:
                heapq.heappush(max_heap, (current_count, current_num))
                
        return result
