class Solution:
    def validateBinaryTreeNodes(self, n: int, leftChild: List[int], rightChild: List[int]) -> bool:
        length = len(leftChild)
        arr = [False] * (length )
        
        
        def dfs(current):
            if arr[current]:
                return False
            
            
            arr[current] = True
            valid = True
            if leftChild[current] != -1 and  not dfs(leftChild[current]):
                return False
            if rightChild[current] != -1 and not dfs(rightChild[current]):
                return False
            return True
        
        
        settVersion = set()
        for i in leftChild:
            settVersion.add(i)
        for i in rightChild:
            settVersion.add(i)
        
        start = -1
        for i in range(length):
            if i not in settVersion:
                start = i
                break
        else:
            return False
        
        isvalid = dfs(start)
        
        if not isvalid:return False
        
        for i in arr:
            if not i:
                return False
        
        return True 