num = int(input())

max_x = num // 3
max_y = num // 5
xy_list = list()

x, y = 0, 0 
for i in range(max_y, -1, -1):
    if (num - 5 * i) % 3 == 0:
        x = int((num - 5 * i) / 3)
        y = i
        xy_list.append((x,y))
xy_list.sort()

if xy_list == []:
    print(-1)
else:
    print(xy_list[0][0] + xy_list[0][1])
        
    
