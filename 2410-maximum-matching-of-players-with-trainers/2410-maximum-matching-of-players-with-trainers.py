class Solution:
    def matchPlayersAndTrainers(self, players: List[int], trainers: List[int]) -> int:
        
        ply_ptr, trn_ptr = 0, 0
        
        count = 0
        
        players.sort()
        trainers.sort()
        
        while ply_ptr < len(players) and trn_ptr < len(trainers):
            
            if players[ply_ptr] <= trainers[trn_ptr]:
                count +=1
                ply_ptr +=1
                trn_ptr += 1
            
            else:
                trn_ptr += 1
                
        return count