class Solution:
    def validateStackSequences(self, pushed: list, popped: list) -> bool:
        step=[pushed[0]]
        upto_index =len(pushed)
        pushed_index=1
        popped_index=0
        while True:
            if pushed_index == upto_index:
                if step==[]:
                    return True
                if step[-1] != popped[popped_index]:
                    break
            if step==[] or step[-1] != popped[popped_index]:
                step.append(pushed[pushed_index])
                pushed_index+=1
            else:
                step.pop()
                popped_index+=1
        return False

s= Solution()
a =s.validateStackSequences([1,2,3,4,5],[4,5,3,2,1])
print(a)