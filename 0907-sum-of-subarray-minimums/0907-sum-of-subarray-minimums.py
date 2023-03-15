class Solution:
    def sumSubarrayMins(self, arr: List[int]) -> int:
        monotonic_stack = []
        
        res = 0
        
        arr_new= [1] * len(arr)
        
        for i in range(len(arr)):
            
            if not monotonic_stack :
                monotonic_stack.append((arr[i], i))
                arr_new[i] *= (i + 1)
                continue
            elif arr[i] >= monotonic_stack[-1][0]:
                monotonic_stack.append((arr[i], i))
                arr_new[i] *= (i - monotonic_stack[-1][-1] + 1)
                continue
            while monotonic_stack and arr[i] < monotonic_stack[-1][0]:
                val, ind = monotonic_stack.pop()
                arr_new[ind] *= (i - ind)

            if monotonic_stack:
                arr_new[i] *= (i - monotonic_stack[-1][1])
            else:
                arr_new[i] *= (i + 1)
            monotonic_stack.append((arr[i], i))
        for val, ind in monotonic_stack:
            arr_new[ind] *= (len(arr) -ind)
        
        res = 0
        for i in range(len(arr)):
            res += arr[i] * arr_new[i]
            
        return (res % (10 ** 9+ 7))