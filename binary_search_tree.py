# This binary_search_tree.py is an implementation of binary search tree based on the idea from CLRS, Chapter 12
# * tree visualization is designed based on my own idea only

# Queue is required for tree visualization
from queue import Queue
import math

class Binary_tree:

    def __init__(self):
        self.root = None

    def node(self, key, p=None, left=None, right=None):
        return {
                "key": key,
                "p": p,
                "left": left,
                "right": right
                }

    def tree_insert(self, key):
        new_node = self.node(key)
        p = None
        node = self.root
        while node is not None:
            p = node
            if new_node["key"] < node["key"]:
                node = node["left"]
            else:
                node = node["right"]
        new_node["p"] = p
        if p is None:
            # Tree is empty
            self.root = new_node
        elif new_node["key"] < p["key"]:
            p["left"] = new_node
        else:
            p["right"] = new_node

    def inorder_tree_walk(self, alternative_root="not provided"):
        if alternative_root == "not provided":
            root = self.root
        else:
            root = alternative_root
        if root is not None:
            self.inorder_tree_walk(root["left"])
            print(str(root["key"]) + ", ", end="")
            self.inorder_tree_walk(root["right"])

    def tree_search(self, k):
        node = self.root
        while node is not None and node["key"] != k:
            if k < node["key"]:

                node = node["left"]
            else:
                node = node["right"]
        return node

    def tree_minimum(self, node=None):
        if node is None:
            node = self.root
        while node["left"] is not None:
            node = node["left"]
        return node

    def tree_maximum(self, node=None):
        if node is None:
            node = self.root

        while node["right"] is not None:
            node = node["right"]
        return node

    def tree_successor(self, node=None):
        if node is None:
            node = self.root

        if node["right"] is not None:
            return self.tree_minimum(node["right"])

        p = node["p"]
        while p is not None and p["right"] is not None and node["key"] == p["right"]["key"]:
            node = p
            p = node["p"]
        return p

    def transplant(self, u, v):
        if u["p"] is None:
            self.root = v
        elif u["p"]["left"] is not None and u["key"] == u["p"]["left"]["key"]:
            u["p"]["left"] = v
        else:
            u["p"]["right"] = v
        if v is not None:
            v["p"] = u["p"]

    def tree_delete(self, k):
        z = self.tree_search(k)
        if z is None:
            return z
        if z["left"] is None:
            self.transplant(z, z["right"])
        elif z["right"] is None:
            self.transplant(z, z["left"])
        else:
            y = self.tree_minimum(z["right"])
            if y["p"]["key"] != z["key"]:
                self.transplant(y, y["right"])
                y["right"] = z["right"]
                if y["right"] is not None:
                    y["right"]["p"] = y
            self.transplant(z, y)
            y["left"] = z["left"]
            y["left"]["p"] = y


    def tree_visualize(self, is_add_extra_lines = False):
        print("\n> tree visualization")

        queue = Queue()

        # Check tree depth
        max_key = - math.inf
        height = 0
        queue.enqueue({"height": height, "node": self.root})
        while not queue.is_empty():
            current_node = queue.dequeue()
            if current_node["node"]["key"] > max_key:
                max_key = current_node["node"]["key"]
            # Check/update current height
            if current_node["height"] != height:
                height = current_node["height"]
            # Enqueue current node children
            if current_node["node"]["left"] is not None:
                queue.enqueue({"height": height + 1, "node": current_node["node"]["left"]})
            if current_node["node"]["right"] is not None:
                queue.enqueue({"height": height + 1, "node": current_node["node"]["right"]})

        # Tree visualization

        # Parameter initialization
        max_height = height
        height = 0
        unit = len(str(max_key)) # number of characters in each node & white space between the nodes
        # Indexing starts from a first node and incremented with 1 by each next node
        # this type of indexing is similar to the standard heap indexing
        index = 1
        # Empty string template for printing each level of nodes / branches
        str_init = [" " * unit for i in range(0, 2 ** (max_height + 1) - 1)]
        str_len = len(str_init)
        # Strings for printing nodes and branches
        nodes = str_init.copy()
        branches = str_init.copy()
        # Skip printing first empty lines
        is_print_required = False

        queue.enqueue({"height": 0, "index": index, "delimiter": " ", "node": self.root})
        while not queue.is_empty():
            current_node = queue.dequeue()
            # Initialization on the first node in a row
            if current_node["height"] != height or current_node["height"] == 0:
                # Printing
                if is_print_required:
                    if is_add_extra_lines:
                        print("")
                    print("".join(branches))
                    if is_add_extra_lines:
                        print("")
                    print("".join(nodes))
                else:
                    is_print_required = True

                # Compute space form the beginning to the first node and between the successive nodes
                if current_node["index"] == 1:
                    space_init = (str_len - 1) // 2
                    space_between = 0
                else:
                    space_between = space_init
                    space_init = (space_init - 1) // 2

                branches = str_init.copy()
                nodes = str_init.copy()
                height = current_node["height"]
                nodes_in_row = 2 ** height

            # Adding current node key to the corresponding place in the string
            key = str(current_node["node"]["key"])
            space_key_correction = unit - len(key)
            key_text = " " * math.ceil(space_key_correction / 2) + key + " " * math.floor(space_key_correction / 2)
            nodes[space_init + (space_between + 1) * (current_node["index"] - nodes_in_row)] = key_text

            space_delim = math.ceil((space_between - 1) / 2 / 2)
            if current_node["delimiter"] == "\\":
                space_delim = - space_delim
                space_delim_correction_before = 0
                space_delim_correction_after = unit - 1
            else:
                space_delim_correction_before = unit - 1
                space_delim_correction_after = 0
            branch_text = " " * space_delim_correction_before + current_node["delimiter"] + " " * space_delim_correction_after
            branches[space_init + (space_between + 1) * (current_node["index"] - nodes_in_row) + space_delim] = branch_text

            # Enqueue current node children
            if current_node["node"]["left"] is not None:
                queue.enqueue({"height": height + 1, "index": 2 * current_node["index"], "delimiter": "/", "node": current_node["node"]["left"]})
            if current_node["node"]["right"] is not None:
                queue.enqueue({"height": height + 1, "index": 2 * current_node["index"] + 1, "delimiter": "\\", "node": current_node["node"]["right"]})

        if is_add_extra_lines:
            print("")
        print("".join(branches))
        if is_add_extra_lines:
            print("")
        print("".join(nodes))


# Running simple examples
my_tree = Binary_tree()
my_tree.tree_insert(18)
my_tree.tree_insert(14)
my_tree.tree_insert(25)
my_tree.tree_insert(1)
my_tree.tree_insert(21)
my_tree.tree_insert(19)
my_tree.tree_insert(12)
my_tree.tree_insert(23)
my_tree.tree_insert(16)
print("my_tree.root " + str(my_tree.root))

my_tree.inorder_tree_walk()
my_tree.tree_visualize()
# my_tree.visualize_tree(True)
print("my_tree.tree_search(18)[key]: " + str(my_tree.tree_search(18)["key"]))
print("my_tree.tree_minimum()[key]: " + str(my_tree.tree_minimum()["key"]))
print("my_tree.tree_maximum()[key]: " + str(my_tree.tree_maximum()["key"]))

print("my_tree.tree_successor()[key]: " + str(my_tree.tree_successor()["key"]))
print("my_tree.tree_successor(my_tree.tree_search(1))[key]: " + str(my_tree.tree_successor(my_tree.tree_search(1))["key"]))
print("my_tree.tree_successor(my_tree.tree_search(16))[key]: " + str(my_tree.tree_successor(my_tree.tree_search(16))["key"]))
print("my_tree.tree_successor(my_tree.tree_search(18))[key]: " + str(my_tree.tree_successor(my_tree.tree_search(18))["key"]))
print("my_tree.tree_successor(my_tree.tree_search(12))[key]: " + str(my_tree.tree_successor(my_tree.tree_search(12))["key"]))
print("my_tree.tree_successor(my_tree.tree_search(21))[key]: " + str(my_tree.tree_successor(my_tree.tree_search(21))["key"]))
print("my_tree.tree_successor(my_tree.tree_search(23))[key]: " + str(my_tree.tree_successor(my_tree.tree_search(23))["key"]))
print("my_tree.tree_successor(my_tree.tree_search(25)): " + str(my_tree.tree_successor(my_tree.tree_search(25))))

my_tree.tree_visualize()
my_tree.tree_delete(25)
my_tree.tree_delete(14)
my_tree.tree_delete(18)
my_tree.tree_delete(1)
my_tree.tree_insert(18)
my_tree.tree_visualize()