class Solution:
    def garbageCollection(self, garbage: List[str], travel: List[int]) -> int:
        g_count, m_count, p_count = 0, 0, 0
        curr_garbage = []
        
        for i in range(len(garbage)):
            curr_count = [0,0,0]
            for j in range(len(garbage[i])):
                if garbage[i][j] == "G":
                    curr_count[0] += 1
                elif garbage[i][j] == "M":
                    curr_count[1] += 1
                else:
                    curr_count[2] += 1
                    
            g_count += curr_count[0]
            m_count += curr_count[1]
            p_count += curr_count[2]
            curr_garbage.append(curr_count)
        
        res = 0
        
        for i in range(len(garbage)):
            temp = 0
            
            if g_count != 0:
                temp += curr_garbage[i][0]
                g_count -= curr_garbage[i][0]
                
                if i != 0:
                    temp += travel[i - 1]
                    
            if m_count != 0:
                temp += curr_garbage[i][1]
                m_count -=  curr_garbage[i][1]
                
                if i != 0:
                    temp += travel[i - 1]
            
            if p_count != 0:
                temp += curr_garbage[i][2]
                p_count -= curr_garbage[i][2]
                
                if i!= 0:
                    temp += travel[i - 1]
            
            res += temp
        
        return res
                