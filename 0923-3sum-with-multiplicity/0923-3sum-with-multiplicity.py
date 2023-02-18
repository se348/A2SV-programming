class Solution:
    def threeSumMulti(self, arr: List[int], target: int) -> int:
        
        ans = 0
        arr.sort()
        
        for left in range(len(arr)):
            mid = left + 1
            right = len(arr)-1
            
            while mid < right:
                curr = arr[left] + arr[mid] + arr[right]
                
                if curr < target:
                    mid += 1
                
                elif curr > target:
                    right -= 1
                
                else:
                    if arr[right] == arr[mid]:
                        diff = right - mid
                        ans += (diff + 1) * diff /2
                        break
                    else:
                        
                        count_mid, count_right = 1, 1
                        
                        while mid + 1 < right and arr[mid] == arr[mid + 1]:
                            mid += 1
                            count_mid += 1
                        
                        while right - 1 > mid and arr[right] == arr[right - 1]:
                            right -= 1
                            count_right += 1
                        
                        ans += count_mid * count_right
                        mid += 1
                        right -= 1
                
        return int(ans % (10 **9 + 7))