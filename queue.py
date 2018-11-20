# This queue.py is a dynamic queue implementation based on ideas from CLRS,
# Chapter 10.1: "Stack and queues" and Chapter 17.4: "Dynamic tables"


class Queue:

    def __init__(self):
        self.items = []
        self.head = -1
        self.tail = -1
        self.size = 0

    def enqueue(self, x):
        self.tail += 1
        if self.head == -1:
            self.head += 1
        self.items.append(x)
        self.size += 1

    def dequeue(self):
        if self.head >= 0 and self.head <= self.tail:
            item = self.items[self.head]
            self.items[self.head] = None
            self.head += 1
            # Dynamic contraction
            load_factor = (self.tail - self.head) / self.size
            if load_factor < 1/4:
                self.items = self.items[self.head:self.tail + 1]
                self.tail = self.tail - self.head
                self.head = 0
                self.size = self.tail + 1
            return item
        else:
            print("Attention: queue underflow")
            return None


# Running simple examples
my_queue = Queue()
my_queue.enqueue(1)
my_queue.enqueue(2)
my_queue.enqueue(10)
my_queue.enqueue(3)
print("my_queue.dequeue(): ")
print(my_queue.dequeue())
print("my_queue.dequeue(): ")
print(my_queue.dequeue())
print("my_queue.dequeue(): ")
print(my_queue.dequeue())
my_queue.enqueue(100)
print("my_queue.dequeue(): ")
print(my_queue.dequeue())
print("my_queue.dequeue(): ")
print(my_queue.dequeue())
print("my_queue.dequeue(): ")
print(my_queue.dequeue())
my_queue.enqueue(101)
my_queue.enqueue(2)
my_queue.enqueue(3)
my_queue.enqueue(17)
print("my_queue.dequeue(): ")
print(my_queue.dequeue())

print("my_queue.items: ")
print(my_queue.items)
print("my_queue.head index: ")
print(my_queue.head)
print("my_queue.tail index: ")
print(my_queue.tail)
print("my_queue.size: ")
print(my_queue.size)





