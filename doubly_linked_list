// This doubly linked list implementation follows the following guide: https://hackernoon.com/the-little-guide-of-linked-list-in-javascript-9daf89b63b54

// Creating a separate scope for declaring variables 
{
    // Initializing linked list
    function LinkedList() {
      this.head = null;
      this.tail = null;
    }
    
    function Node(value, next, prev) {
      this.value = value;
      this.next = next;
      this.prev = prev;
    }

    // Adding required functional
    LinkedList.prototype.addToHead = function(value) {
      const newNode = new Node(value, this.head, null);
      if (this.head) this.head.prev = newNode;
      else this.tail = newNode; 
      this.head = newNode;
    };

    LinkedList.prototype.addToTail = function(value) {
      const newNode = new Node(value, null, this.tail);
      if (this.tail) this.tail.next = newNode;
      else this.head = newNode;
      this.tail = newNode;
    }

    LinkedList.prototype.removeHead = function() {
    if (this.head) {
        if (this.head.next) {
            this.head = this.head.next
            this.head.prev = null
        } else {
            this.head = null
            this.tail = null
        }
     }
    }

    LinkedList.prototype.removeTail = function () {
        if (this.tail) {
            if (this.tail.prev) {
                this.tail = this.tail.prev
                this.tail.next = null
            } else {
                this.head = null
                this.tail = null
            }
        }
    }

    // search from head
    LinkedList.prototype.search = function (searchValue) {
        let currentNode = this.head
        while (currentNode) {
            if (currentNode.value == searchValue) return currentNode;
            else currentNode = currentNode.next 
        }
    }

    LinkedList.prototype.searchBackwards = function (searchValue) {
        let currentNode = this.tail
        while (currentNode) {
            if (currentNode.value == searchValue) return currentNode
            else currentNode = currentNode.prev
        }
    }


    // Simple test of the implementation
    const list = new LinkedList();
    list.addToHead(300);
    list.addToHead(200);
    list.addToHead(100);

    list.addToTail(400);
    list.addToTail(500);
    list.addToTail(600);

//     list.removeHead()
//     list.removeTail()
//     console.log(list);
//     console.log(list.head.next.value);
//     searchResult = list.search(300)

    searchResult = list.searchBackwards (300)
    console.log("Search results: ")
    console.log(searchResult)
}
