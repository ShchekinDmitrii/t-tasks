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
    current_shift = 0
    depth_iter = n-1
    item = 0
    while (depth_iter>=0 and item!=1):
        item = slice[depth_iter]
        depth_iter -= 1
        if (item==0):
            current_shift += 1
            if depth_iter==0:
                current_shift = n
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