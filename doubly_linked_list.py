# This doubly_linked_list.py is an implementation of doubly linked list based on the idea from CLRS, Chapter 10.2

class Linked_list:
    def __init__(self):
        self.head = None
        self.tail = None

    def node(self, key, prev=None, next=None):
        return {"key": key,
                "prev": prev,
                "next": next}

    def list_insert(self, key, start_from_head=True):
        if self.head:
            if start_from_head:
                new_node = self.node(key, None, self.head)
                self.head["prev"] = new_node
                self.head = new_node
            else:
                new_node = self.node(key, self.tail, None)
                self.tail["next"] = new_node
                self.tail = new_node

        else:
            new_node = self.node(key)
            self.head = new_node
            self.tail = self.head

    def list_search(self, k, start_from_head=True):
        if start_from_head:
            method = "next"
            node = self.head
        else:
            method = "prev"
            node = self.tail
        while node is not None and node["key"] != k:
            node = node[method]
        return node

    def list_delete(self, k):
        node = self.list_search(k)
        node_clone = node.copy()
        if node:
            if node["prev"] is not None:
                node["prev"]["next"] = node["next"]
            else:
                self.head = node["next"]
            if node["next"] is not None:
                node["next"]["prev"] = node["prev"]
        return node_clone

    def list_traverse(self, start_from_head=True):
        if start_from_head:
            print("> List traverse starting from head:")
            method = "next"
            node = self.head
        else:
            print("> List traverse starting from tail:")
            method = "prev"
            node = self.tail
        while node is not None:
            print(node)
            node = node[method]


# Running simple examples
print("\n::::: myList :::::")
myList = Linked_list()
myList.list_insert(1)
myList.list_insert(2)
myList.list_insert(3)
myList.list_insert(4)
myList.list_insert(5)
print("myList.head[key] = " + str(myList.head["key"]))
print("myList.list_search(3): ")
print(myList.list_search(3))
myList.list_search(3)["prev"] = None
print("myList.list_search(3): ")
print(myList.list_search(3))
print('myList.list_search(22)')
print(myList.list_search(22))

print("\n::::: mylist1 :::::")
myList1 = Linked_list()
myList1.list_insert(1)
myList1.list_insert(2)
myList1.list_insert(3)
myList1.list_insert(4)
myList1.list_insert(5)
myList1.list_traverse()
myList1.list_traverse(False)
print("myList1.list_search(3): ")
print(myList1.list_search(3))
myList1.list_delete(3)
myList1.list_traverse()
myList1.list_traverse(False)

print("myList1.list_search(3): ")
print(myList1.list_search(3))
print("myList1.list_search(2): ")
print(myList1.list_search(2))
print("myList1.list_search(2) starting from tail: ")
print(myList1.list_search(2, False))

print("\n::::: mylist2 :::::")
myList2 = Linked_list()
myList2.list_insert(1)
myList2.list_insert(2)
myList2.list_insert(3)
myList2.list_insert(4)
myList2.list_insert(5)
myList2.list_traverse()

print("\n::::: mylist3 :::::")
myList3 = Linked_list()
myList3.list_insert(1, False)
myList3.list_insert(2, False)
myList3.list_insert(3, False)
myList3.list_insert(4, False)
myList3.list_insert(5, False)
myList3.list_insert(7)
myList3.list_insert(7, False)
myList3.list_traverse()