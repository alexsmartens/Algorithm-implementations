# This binary_search_tree.py is an implementation of binary search tree based on the idea from CLRS, Chapter 12

from tree_visualization import tree_visualize


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
tree_visualize(my_tree.root)
# tree_visualize(my_tree.root, True)
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

tree_visualize(my_tree.root)
my_tree.tree_delete(25)
my_tree.tree_delete(14)
my_tree.tree_delete(18)
my_tree.tree_delete(1)
my_tree.tree_insert(18)
tree_visualize(my_tree.root)