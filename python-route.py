k,x,n = input().split(' ')

scale = int(k)
step  = int(x)
turns = int(n)

N_row = 0
N_col = 0

if turns == 1:
    N_row = 1
    N_col = step + 1
    for i in range(N_col):
        print('#', end='')
    print('')
elif turns == 2:
    N_row = 1 + step * scale
    N_col = step + 1
    for i in range(N_row-1):
        for i in range(N_col-1):
            print('.', end='')
        print('#')
    for i in range(N_col):
        print('#', end='')
    print('')
elif turns == 3:
    N_row = 1 + step * scale
    N_col = 1 + step * scale * scale
    for i in range(N_col):
        print('#', end='')
    print('')
    for i in range(N_row-2):
        for i in range(N_col-1):
            print('.', end='')
        print('#')
    for i in range(N_col-step-1):
        print('.', end='')
    for i in range(step+1):
        print('#', end='')
    print('')
elif turns == 4:
    N_row = 1 + step * scale * scale * scale
    N_col = 1 + step * scale * scale
    for i in range(N_col):
        print('#', end='')
    print('')
    for i in range(step * scale - 1):
        print('#', end='')
        for i in range(N_col-2):
            print('.', end='')
        print('#')
    print('#', end='')
    for i in range(N_col-step-2):
        print('.', end='')
    for i in range(step):
        print('#', end='')
    print('#')
    for i in range(N_row - step*scale - 1):
        print('#', end='')
        for i in range(N_col-1):
            print('.', end='')
        print('')
else:
    N_row = 1 + step * scale * scale * scale
    N_col = 1 + step * scale * scale * scale * scale
    for i in range(1 + step * scale * scale):
        print('#', end='')
    for i in range(N_col - 1 - step * scale * scale):
        print('.', end='')
    print('')
    for i in range(step * scale - 1):
        print('#', end='')
        for i in range(step * scale * scale - 1):
            print('.', end='')
        print('#', end='')
        for i in range(N_col - 1 - step * scale * scale):
            print('.', end='')
        print('')
    print('#', end='')
    for i in range(step * scale * scale - step - 1):
        print('.', end='')
    for i in range(step + 1):
        print('#', end='')
    for i in range(N_col - 1 - step * scale * scale):
        print('.', end='')
    print('')
    for i in range(N_row - step*scale - 2):
        print('#', end='')
        for i in range(N_col-2):
            print('.', end='')
        print('.')
    for i in range(N_col-1):
        print('#',end='')
    print('#')