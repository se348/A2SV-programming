class Solution:
    def dailyTemperatures(self, temperatures: list) -> list:
        size = len(temperatures)
        counters=[0]* size
        stack =[]
        for index in range(size):
            while len(stack)>0 and stack[-1][0]< temperatures[index]:
                small_ind_and_temp = stack.pop()
                index_of_popped =small_ind_and_temp[1]
                counters[index_of_popped] = index -index_of_popped
            stack.append((temperatures[index], index))
        return counters

s= Solution()
d = s.dailyTemperatures([30,40,50,60])
print(d)