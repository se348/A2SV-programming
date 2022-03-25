class Solution(object):
    def fizzBuzz(self, n):
        rtype= []
        
        for i in range(1, n+1):
            if i%15 == 0:
                rtype.append("FizzBuzz")
                continue
            elif i%3 ==0:
                rtype.append("Fizz")
            elif i%5 ==0:
                rtype.append("Buzz")
            else:
                rtype.append(str(i))
        return rtype 