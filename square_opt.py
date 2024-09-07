def merge(arr, l, m, r):
    n1 = m - l + 1
    n2 = r - m

    L = [0] * (n1)
    R = [0] * (n2)

    for i in range(0, n1):
        L[i] = arr[l + i]
    
    for j in range(0, n2):
        R[j] = arr[m + 1 + j]
    
    i = 0
    j = 0
    k = l

    while i < n1 and j < n2:
        if L[i] > R[j]:
            arr[k] = L[i]
            i += 1
        else:
            arr[k] = R[j]
            j += 1
        k += 1
    while i < n1:
        arr[k] = L[i]
        i += 1
        k += 1
    while j < n2:
        arr[k] = R[j]
        j += 1
        k += 1

def mergeSort(arr, l ,r):
    if l < r:
        m = l + (r-l)//2
        mergeSort(arr, l, m)
        mergeSort(arr, m+1, r)
        merge(arr, l, m, r)

tasks,people = input().split(' ')
tasks = int(tasks)
people = int(people)
req_line = input().split(' ')
req = [int(x) for x in req_line]

mergeSort(req, 0 , people-1)

stop_global = 0
while (tasks>0 and not stop_global):
    max_item = req[0]
    item_ptr = 0
    stop = max_item==0
    stop_global = stop
    while (not stop):
        req[item_ptr] -= 1
        tasks -= 1
        stop = (item_ptr==people-1 or tasks==0)
        if (not stop):
            stop = (req[item_ptr] != req[item_ptr+1] or tasks==0)
        item_ptr += 1

iter_ptr = 0
res = 0
add = 1
while (add > 0 and iter_ptr < people):
    add = req[iter_ptr]**2
    res += add
    iter_ptr += 1

print(res)