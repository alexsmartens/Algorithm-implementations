# This stack.py implementation follows idea from CLRS, Chapter 10.2


class Stack:

    def __init__(self):
        self.items = []
        self.top = 0
        self.debug = True

    def is_empty(self):
        return self.top == 0

    def size(self):
        return self.top

    def peek(self):
        if self.top > 0:
            return self.items[self.top - 1]
        else:
            return None

    def push(self, new_item):
        self.items.append(new_item)
        self.top += 1

        if self.debug:
            self.print()

    def pop(self):
        if self.is_empty():
            print("Attention: stack underflow")
            return None
        else:
            new_item = self.items[self.top - 1]
            self.items = self.items[:self.top - 1] # the last list item is not included
            self.top -= 1

            if self.debug:
                self.print()

            return new_item

    def print(self):
        print(self.items)


# Running simple examples
myStack = Stack()
print("is_empty: " + str(myStack.is_empty()))
print("top: " + str(myStack.top))

myStack.push(15)
myStack.push(6)
myStack.push(2)
myStack.push(9)
print("is_empty: " + str(myStack.is_empty()))
print("top: " + str(myStack.top))

myStack.push(17)
myStack.push(3)
print("size " + str(myStack.size()))
print("peek " + str(myStack.peek()))

myStack.pop()
print("top: " + str(myStack.top))
myStack.pop()
myStack.pop()
myStack.pop()
myStack.pop()
print("top: " + str(myStack.top))
myStack.pop()
print("top: " + str(myStack.top))
myStack.pop()
myStack.pop()
