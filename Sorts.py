from Structures import Heap

def insert_sort(arr):
    for i in range(1, len(arr)):
        key = arr[i]
        j = i - 1
        while j >= 0 and arr[j] > key:
            arr[j + 1] = arr[j]
            j -= 1
        arr[j + 1] = key
    return arr


def rev_insert_sort(arr):
    for i in range(1, len(arr)):
        key = arr[i]
        j = i - 1
        while j >= 0 and arr[j] < key:
            arr[j + 1] = arr[j]
            j -= 1
        arr[j + 1] = key
    return arr


def merge_sort(arr, l, r):
    if l >= r:
        return
    mid = int((l + r) / 2)
    merge_sort(arr, l, mid)
    merge_sort(arr, mid + 1, r)
    merge(arr, l, mid, r)
    return arr


def merge(arr, l, mid, r):
    mid += 1
    res = []
    itl = 0
    itr = 0

    while l + itl < mid and mid + itr <= r:
        if arr[l + itl] < arr[mid + itr]:
            res.insert(itl + itr, arr[l + itl])
            itl += 1
        else:
            res.insert(itl + itr, arr[mid + itr])
            itr += 1

    while l + itl < mid:
        res.insert(itr + itl, arr[l + itl])
        itl += 1

    while mid + itr <= r:
        res.insert(itr + itl, arr[mid + itr])
        itr += 1

    for i in range(itl + itr):
        arr[l + i] = res[i]


def qsort(arr, l, r):
    if l < r:
        mid = div(arr, l, r)
        qsort(arr, l, mid)
        qsort(arr, mid + 1, r)
    return arr


def div(arr, l, r):
    v = arr[int((l + r) / 2)]
    i = l
    j = r
    while i <= j:
        while arr[i] < v:
            i += 1
        while arr[j] > v:
            j -= 1
        if i >= j:
            break
        arr[i], arr[j] = arr[j], arr[i]
        i += 1
        j -= 1
    return j


def rev_merge(arr, l, mid, r):
    mid += 1
    res = []
    itl = 0
    itr = 0

    while l + itl < mid and mid + itr <= r:
        if arr[l + itl] > arr[mid + itr]:
            res.insert(itl + itr, arr[l + itl])
            itl += 1
        else:
            res.insert(itl + itr, arr[mid + itr])
            itr += 1

    while l + itl < mid:
        res.insert(itr + itl, arr[l + itl])
        itl += 1

    while mid + itr <= r:
        res.insert(itr + itl, arr[mid + itr])
        itr += 1

    for i in range(itl + itr):
        arr[l + i] = res[i]


def rev_div(arr, l, r):
    v = arr[int((l + r) / 2)]
    i = l
    j = r
    while i <= j:
        while arr[i] > v:
            i += 1
        while arr[j] < v:
            j -= 1
        if i >= j:
            break
        arr[i], arr[j] = arr[j], arr[i]
        i += 1
        j -= 1
    return j


def rev_qsort(arr, l, r):
    if l < r:
        mid = rev_div(arr, l, r)
        rev_qsort(arr, l, mid)
        rev_qsort(arr, mid + 1, r)
    return arr


def rev_merge_sort(arr, l, r):
    if l >= r:
        return
    mid = int((l + r) / 2)
    rev_merge_sort(arr, l, mid)
    rev_merge_sort(arr, mid + 1, r)
    rev_merge(arr, l, mid, r)
    return arr

def heap_sort(arr):
    heap = Heap(arr)
    heap.build()
    for i in range(len(arr) - 1):
        heap.arr[0], arr[len(heap.arr) - 1 - i] = heap.arr[len(arr) - 1 - i], heap.arr[0]
        heap.size -= 1
        heap.siftDown(0)
    return heap.arr







