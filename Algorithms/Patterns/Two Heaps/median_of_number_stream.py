from heapq import *

class MedianStream:

    minHeap = []
    maxHeap = []

    def insertNum(self, num):
        if not self.maxHeap or -self.maxHeap[0] >= num:
            heappush(self.maxHeap, -num)
        else:
            heappush(self.minHeap, num)

        if len(self.maxHeap) > len(self.minHeap) + 1:
            heappush(self.minHeap, -heappop(self.maxHeap))
        elif len(self.maxHeap) < len(self.minHeap):
            heappush(self.maxHeap, -heappop(self.minHeap))


    def find_median(self):
        if len(self.maxHeap) == len(self.minHeap):
            return (-self.maxHeap[0] / 2.0) + (self.minHeap[0])
        
        return -self.maxHeap[0]

if __name__ == "__main__":
    test = MedianStream()
    test.insertNum(5)
    test.insertNum(10)
    test.insertNum(12)
    print(test.maxHeap, test.minHeap)
    print(test.find_median())