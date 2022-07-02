class Solution:
    def carFleet(self, target: int, position: list, speed: list) -> int:
        n= len(position)
        position_targest= []
        for i in range(n):
            tempo=(position[i], speed[i])
            position_targest.append(tempo)
        sorted_by_first =sorted(position_targest ,key=lambda tup: tup[0])
        current_position = sorted_by_first[-1][0]
        current_time =(target -current_position)/sorted_by_first[-1][1]
        count= 1
        for k in range(n-1,-1,-1):
            temp_position=sorted_by_first[k][0]
            temp_time =(target - temp_position)/sorted_by_first[k][1]
            if temp_time > current_time:
                count+=1
                current_position =temp_position
                current_time =temp_time
        return count


s= Solution()
a= s.carFleet(100, [0,2,4],[4,2,1])
print(a)