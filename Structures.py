import math
class Heap:
    def __init__(self, arr):
        self.arr = arr
        self.size = len(arr)

    def siftUp(self, i):
        while self.arr[i] < self.arr[int((i - 1) / 2)]:
            self.arr[i], self.arr[int((i - 1) / 2)] = self.arr[int((i - 1) / 2)], self.arr[i]
            i = int((i - 1) / 2)


    def siftDown(self, i):
        while 2 * i + 1 < self.size:
            left = 2 * i + 1
            right = 2 * i + 2
            j = left
            if right < self.size and self.arr[right] > self.arr[left]:
                j = right
            if self.arr[i] >= self.arr[j]:
                break
            self.arr[i], self.arr[j] = self.arr[j], self.arr[i]
            i = j


    def build(self):
        for i in range(int(self.size / 2), -1, -1):
            self.siftDown(i)
        return self.arr



