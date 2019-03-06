from heapq import heappush, heappop, heapify
class PriorityQueue:
    def __init__(self):
        self.pq = []

    def push(self, item):
        heappush(self.pq, item)

    def pop(self):
        return heappop(self.pq)

    def top(self):
        return self.pq[0]

    def remove(self, item):
        value = self.pq.remove(item)
        heapify(self.pq)
        return value is not None

    def __len__(self):
        return len(self.pq)
