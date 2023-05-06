n= int(input())


x, y, z =0,0,0

for i in range(n):
    curr_x, curr_y, curr_z = map(int, input().split())    
    x += curr_x
    y += curr_y
    z += curr_z
    
if not x and not y and not z:
    print("YES")
else:
    print("NO")
