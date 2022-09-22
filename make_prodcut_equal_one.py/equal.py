n=input()
y= input()
arr= y.split()
for i in range(len(arr)):
    arr[i]=int(arr[i])
negative_count = 0
zero_count = 0
result = 0
for i in arr:
    if i < 0:
        negative_count += 1
        result-= 1 + i
    elif i== 0:
        zero_count+=1
    else:
        result += i - 1
if negative_count % 2 == 0:
	result = result + zero_count
else:
	if zero_count > 0:
		result = result + zero_count
	else:
		result = result + 2
print(result)


