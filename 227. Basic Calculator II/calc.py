class Solution:
    def calculate(self, s: str) -> int:
        custom_stack =[]
        current_operation ="+"
        i=0
        while i< len(s):
            if s[i]==" ":
                i+=1
                continue
            elif s[i].isdigit() and current_operation =="+":
                number =""
                while i< len(s) and s[i].isdigit():
                    number+= s[i]
                    i+=1
                custom_stack.append(int(number))
            elif s[i].isdigit() and current_operation =="*":
                number =""
                while i< len(s) and s[i].isdigit():
                    number+= s[i]
                    i+=1
                num1 = custom_stack.pop()
                custom_stack.append(int(number) * num1)
                current_operation ="+"
            elif s[i].isdigit() and current_operation =="/":
                number =""
                while i< len(s) and s[i].isdigit():
                    number+= s[i]
                    i+=1
                num1 = custom_stack.pop()
                divide =int(num1) // int(number)
                if divide<0 and divide!=int(num1) / int(number):
                    divide+=1
                custom_stack.append(divide)
                current_operation ="+"
            elif s[i]=="-" and current_operation =="+":
                number = "-"
                i+=1
                if s[i]==" ":
                    i+=1
                while i< len(s) and  s[i].isdigit():
                    number+= s[i]
                    i+=1
                custom_stack.append(int(number))
            elif s[i]=="-" and current_operation =="*":
                number = "-"
                i+=1
                if s[i]==" ":
                    i+=1
                while i< len(s) and s[i].isdigit():
                    number+= s[i]
                    i+=1
                num1 =custom_stack.pop()
                custom_stack.append(int(number) * num1)
                current_operation ="+"
            elif s[i]=="-" and current_operation =="/":
                number = "-"
                i+=1
                if s[i]==" ":
                    i+=1
                while i< len(s) and s[i].isdigit():
                    number+= s[i]
                    i+=1
                num1 =custom_stack.pop()
                divide =int(num1) // int(number)
                if divide<0 and divide!=int(num1) / int(number):
                    divide+=1
                custom_stack.append(divide)
                current_operation ="+"
            elif s[i] =="*":
                current_operation ="*"
                i+=1
            elif s[i] =="+":
                current_operation ="+"
                i+=1
            elif s[i] =="/":
                current_operation="/"
                i+=1
        return sum(custom_stack)
s =Solution()
a =s.calculate(" 14 - 3 / 2 ")
print(a)

                