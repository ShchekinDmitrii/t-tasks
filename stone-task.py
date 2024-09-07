n,m = input().split(' ')
n = int(n)
m = int(m)

Photo = [[0 for x in range(n)] for y in range(m)]
Result = [['.' for x in range(n)] for y in range(m)]
for i in range(n):
    line = input()
    for k in range(m):
        if (line[k]=='M'):
            Photo[k][i] = 1
        elif (line[k]=='#'):
            Photo[k][i] = 2
            Result[k][i] = '#'

# Search for the minimal shift with no collision
shift = n
for row in range(m):
    slice = Photo[row]
    current_shift = shift
    stone_start = 0
    stone_end = 0
    depth_iter = 0
    item = 0
    while (depth_iter<n and item!=2):
        item = slice[depth_iter]
        depth_iter += 1
        if (stone_start==0 and item==1):
            stone_start = 1
        if (stone_start==1 and item!=1):
            stone_end = 1
            stone_start = 0
            current_shift = 0
        if (stone_end==1 and item==0):
            current_shift += 1
    if current_shift<shift:
        shift = current_shift

for i in range(n):
    for k in range(m):
        if (Photo[k][i] == 1):
            Result[k][i+shift] = 'M'

for i in range(n):
    for k in range(m):
        print(Result[k][i], end='')
    print('')