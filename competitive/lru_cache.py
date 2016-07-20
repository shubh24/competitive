import operator
import datetime

class LRUCache:

    # @param capacity, an integer
    def __init__(self, capacity):
        self.heap = {}
        self.capacity = capacity
        self.total = 0
        self.dict = {}

    # @return an integer
    def get(self, key):
        if key in self.heap:
            self.heap[key] = datetime.datetime.now()
            return self.dict[key]
        else:
        	return -1
        	

    # @param key, an integer
    # @param value, an integer
    # @return nothing
    def set(self, key, value):

        while (self.total >= self.capacity):
            # heappop(self.heap)
            elem = sorted(self.heap.items(), key = operator.itemgetter(1))[0]
            del self.heap[elem[0]]
            self.total -= 1

        self.heap[key] = datetime.datetime.now()
        self.dict[key] = value
        self.total += 1


# cache = LRUCache(2)
# cache.set(2, 1)
# cache.set(1, 1)
# cache.set(2, 3)
# cache.set(4, 1)

# print cache.get(1)
# print cache.get(2)

