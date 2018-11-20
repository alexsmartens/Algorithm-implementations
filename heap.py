# This heap.py is an implementation of max heap based on the idea from CLRS, Chapter 6

import math


class Heap:
    # MAX heap
    def __init__(self, arr=None):
        # heap indexing starts at 1
        if arr:
            self.items = arr
            self.size = len(arr)
            self.length = self.size
        else:
            self.items = []
            self.length = 0

    def idx(self, i):
        # returns index of an array element corresponding to the i-th heap node
        if i == 0:
            return 0
        elif i < 0:
            print("Error: Incorrect Index assigning attempt")
            return None
        else:
            return i - 1

    def parent(self, i):
        return math.floor(i / 2)

    def left(self, i):
        return 2 * i

    def right(self, i):
        return 2 * i + 1

    def max_heapify(self, i):
        l = self.left(i)
        r = self.right(i)

        if l <= self.length and self.items[self.idx(l)] and self.items[self.idx(l)] > self.items[self.idx(i)]:
            largest = l
        else:
            largest = i
        if r <= self.length and self.items[self.idx(r)] and self.items[self.idx(r)] > self.items[self.idx(largest)]:
            largest = r
        if largest != i:
            # exchanging A[largest] and A[i]
            new_largest_element = self.items[self.idx(largest)]
            self.items[self.idx(largest)] = self.items[self.idx(i)]
            self.items[self.idx(i)] = new_largest_element
            self.max_heapify(largest)

    def build_max_heap(self):
        for i in range(math.floor(self.length), 0, -1):
            self.max_heapify(i)

    def heapsort(self):
        self.build_max_heap()
        # copy original heap because heapsort is performed on itself (performance reason)
        heap_copy = self.items.copy()
        heap_copy_length = self.length
        for i in range(self.length, 1, - 1):
            # exchanging A[1] and A[i]
            temp = self.items[self.idx(1)]
            self.items[self.idx(1)] = self.items[self.idx(i)]
            self.items[self.idx(i)] = temp
            self.length -= 1
            self.max_heapify(1)
        # take back the original heap values
        sorted_arr = self.items
        self.items = heap_copy
        self.length = heap_copy_length
        return sorted_arr

    # MAX priority queue methods
    def heap_max(self):
        return self.items[self.idx(1)]

    def heap_extract_max(self):
        if self.length < 1:
            print("Attention: heap underflow")
            return None
        max = self.items[self.idx(1)]
        self.items[self.idx(1)] = self.items[self.idx(self.length)]
        self.items[self.length - 1] = None
        self.length -= 1
        self.max_heapify(1)
        return max

    def heap_increase_key(self, i, key):
        if key < self.items[self.idx(i)]:
            print("Attention: new key is smaller than current key")
        else:
            self.items[self.idx(i)] = key
            while i > 1 and self.items[self.idx(self.parent(i))] < self.items[self.idx(i)]:
                # exchanging A[i] and A[parent(i)]
                temp = self.items[self.idx(i)]
                self.items[self.idx(i)] = self.items[self.idx(self.parent(i))]
                self.items[self.idx(self.parent(i))] = temp
                i = self.parent(i)

    def max_heap_insert(self, key):
        self.length += 1
        if self.length < self.size:
            self.items[self.idx(self.length)] = -math.inf
        else:
            self.items.append(-math.inf)
        self.heap_increase_key(self.length, key)


# Running simple examples
print("::::: my_heap :::::")
my_heap = Heap([16, 14, 10, 8, 7, 9, 3, 2, 4, 1])

print("left child of #{} is #{}".format(4, my_heap.left(4)))
print("right child of #{} is #{}".format(3, my_heap.right(3)))
print("parent of #{} is #{}".format(2, my_heap.parent(2)))

print("left child of #{} is #{}".format(8, my_heap.left(8)))
print("right child of #{} is #{}".format(10, my_heap.right(10)))
print("parent of #{} is #{}".format(1, my_heap.parent(1)))

print("\n::::: my_heap2 :::::")
my_heap2 = Heap([16, 4, 10, 14, 7, 9, 3, 2, 8, 1])
my_heap2.max_heapify(2)
print("Updated heap is \n{}".format(my_heap2.items))

print("\n::::: my_heap3 :::::")
my_heap3 = Heap([5, 3, 17, 10, 84, 19, 6, 22, 9])
my_heap3.build_max_heap()
print("New heap is \n{}".format(my_heap3.items))
print("Sorted heap is \n{}".format(my_heap3.heapsort()))

print("\n::::: my_heap4 :::::")
my_heap4 = Heap([16, 14, 10, 8, 7, 9, 3, 2, 4, 1])
print("New heap is \n{}".format(my_heap4.items))
print("this heap length is \n{}".format(my_heap4.length))
print("Sorted heap is \n{}".format(my_heap4.heapsort()))
print("MAX is \n{}".format(my_heap4.heap_max()))
print("Extracted MAX is \n{}".format(my_heap4.heap_extract_max()))
print("New heap is \n{}".format(my_heap4.items))
print("this heap length is \n{}".format(my_heap4.length))

# Extract all heap nodes
my_heap4.heap_extract_max()
my_heap4.heap_extract_max()
my_heap4.heap_extract_max()
my_heap4.heap_extract_max()
my_heap4.heap_extract_max()
my_heap4.heap_extract_max()
my_heap4.heap_extract_max()
my_heap4.heap_extract_max()
print("Extracted MAX is \n{}".format(my_heap4.heap_extract_max()))
print("New heap is \n{}".format(my_heap4.items))
print("this heap length is \n{}".format(my_heap4.length))
my_heap4.heap_extract_max()


print("\n::::: my_queue :::::")
my_queue = Heap([17, 14, 10, 8, 7, 9, 3, 2, 4, 1])
my_queue.heap_increase_key(9, 15)
print("New heap is \n{}".format(my_queue.items))
my_queue.max_heap_insert(16)
print("New heap is \n{}".format(my_queue.items))
my_queue.max_heap_insert(90)
my_queue.max_heap_insert(40)
print("New heap is \n{}".format(my_queue.items))