class NumArray:

    def __init__(self, nums: List[int]):
        self.tree_size = pow(2, ceil(log(len(nums), 2))) * 2
        self.tree = [0] * self.tree_size
        self.length = len(nums)
        
        def construct_tree(tree_ptr, l, r):
            if l == r:
                self.tree[tree_ptr] = nums[l]
                return nums[l]
            
            mid = (l + r)//2
            
            a = construct_tree(2* tree_ptr+ 1, l, mid)
            b = construct_tree(2* tree_ptr+ 2,mid + 1, r)
            self.tree[tree_ptr] = a + b
            return self.tree[tree_ptr]
        
        construct_tree(0, 0, len(nums)- 1)
        

    def update(self, index: int, val: int) -> None:
        
        def update_val(tree_ptr, l, r):
            
            if l == r == index:
                diff = val - self.tree[tree_ptr]
                self.tree[tree_ptr] = val
                return diff
            
            mid = (l + r) // 2
            
            if index <= mid:
                change = update_val(2 * tree_ptr + 1, l, mid)
                self.tree[tree_ptr] += change
                return change
            else:
                change = update_val(2 * tree_ptr + 2, mid+1, r)
                self.tree[tree_ptr] += change
                return change
            
        update_val(0,0, self.length - 1)

    def sumRange(self, left: int, right: int) -> int:
        def get_range(tree_ptr, l, r):
            if l >= left and r <= right:
                return self.tree[tree_ptr]
            if l > right or r < left:
                return 0
            mid = (l + r)//2
            
            a = get_range(2* tree_ptr+ 1, l, mid)
            b = get_range(2* tree_ptr+ 2,mid + 1, r)
            return a + b
        
        return get_range(0, 0, self.length- 1)

        


# Your NumArray object will be instantiated and called as such:
# obj = NumArray(nums)
# obj.update(index,val)
# param_2 = obj.sumRange(left,right)