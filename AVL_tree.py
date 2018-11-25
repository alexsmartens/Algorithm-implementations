# This AVL_tree.py is an implementation of binary search tree based on the idea from AVL lectures of
# Dr. Rob Edwards from San Diego State University (https://www.youtube.com/watch?v=-9sHvAnLN_w)

from tree_visualization import tree_visualize


class AVL_tree:


    def __init__(self):
        self.root = None


    def node(self, key, p=None, left=None, right=None, h_left=0, h_right=0):
        return {
                "key": key,
                "p": p,
                "left": left,
                "right": right,
                "h_left": h_left,
                "h_right": h_right
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
        self.AVL_update_balance(new_node)


    def AVL_update_balance(self, node):
        # Update left and right node balance factors

        if node["h_left"] > node["h_right"]:
            height = node["h_left"]
        else:
            height = node["h_right"]

        # Initial check whether rebalancing required
        p = node["p"]
        if abs(node["h_left"] - node["h_right"]) == 2:
            if p is not None:
                if p["left"]["key"] == node["key"]:
                    branch = "left"
                else:
                    branch = "right"

            node = self.AVL_rebalance(node)
            height = max(node["h_left"], node["h_right"])

            if p is None:
                self.root = node
            else:
                p[branch] = node

        # Follow node's parents until the root is reached
        while p is not None:

            if p["left"] is not None and node["key"] == p["left"]["key"]:
                height += 1
                p["h_left"] = height
                if p["h_right"] > height:
                    height = p["h_right"]
            else:
                height += 1
                p["h_right"] = height
                if p["h_left"] > height:
                    height = p["h_left"]

            node = p
            p = p["p"]

            # Check whether rebalancing required
            if abs(node["h_left"] - node["h_right"]) == 2:
                if p is not None:
                    if p["left"]["key"] == node["key"]:
                        branch = "left"
                    else:
                        branch = "right"

                node = self.AVL_rebalance(node)
                height = max(node["h_left"], node["h_right"])

                if p is None:
                    self.root = node
                else:
                    p[branch] = node


    def AVL_rebalance(self, node):

        if node["h_left"] - node["h_right"] == 2:
            if node["left"]["h_left"] - node["left"]["h_right"] >= node["left"]["h_right"] - node["left"]["h_left"]:
                node = self.AVL_right_rotation(node)

            else:
                print("**----+ Left Right rotation")
                node["left"] = self.AVL_left_rotation(node["left"])
                node = self.AVL_right_rotation(node)

        if node["h_right"] - node["h_left"] == 2:
            if node["right"]["h_right"] - node["right"]["h_left"] >= node["right"]["h_left"] - node["right"]["h_right"]:
                node = self.AVL_left_rotation(node)

            else:
                print("**----+ Right Left rotation")
                node["right"] = self.AVL_right_rotation(node["right"])
                node = self.AVL_left_rotation(node)
        return node


    def AVL_right_rotation(self, node):
        print("**----- Right rotation")
        # Relink pointer pairs
        new_node = node["left"]
        new_node["p"] = node["p"]

        node["left"] = new_node["right"]
        if node["left"] is not None:
            node["left"]["p"] = node

        new_node["right"] = node
        node["p"] = new_node

        # Updating balance factors
        if node["left"] is not None:
            node["h_left"] = max(node["left"]["h_left"], node["left"]["h_right"]) + 1
        else:
            node["h_left"] = 0
        new_node["h_right"] = max(new_node["right"]["h_left"], new_node["right"]["h_right"]) + 1
        return new_node


    def AVL_left_rotation(self, node):
        print("**----- Left rotation")
        # Relink pointer pairs
        new_node = node["right"]
        new_node["p"] = node["p"]

        node["right"] = new_node["left"]
        if node["right"] is not None:
            node["right"]["p"] = node

        new_node["left"] = node
        node["p"] = new_node

        # Updating balance factors
        if node["right"] is not None:
            node["h_right"] = max(node["right"]["h_left"], node["right"]["h_right"]) + 1
        else:
            node["h_right"] = 0
        new_node["h_left"] = max(new_node["left"]["h_left"], new_node["left"]["h_right"]) + 1
        return new_node


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

        # Parameter initialization
        extra_balance_point = None

        if z["left"] is None:

            if z["right"] is not None:
                balance_point = z["right"]
            else:
                balance_point = z["p"]

            self.transplant(z, z["right"])
        elif z["right"] is None:

            balance_point = z["left"]

            self.transplant(z, z["left"])
        else:
            y = self.tree_minimum(z["right"])
            if y["p"]["key"] != z["key"]:

                extra_balance_point = y
                balance_point = y["p"]

                self.transplant(y, y["right"])
                y["right"] = z["right"]
                if y["right"] is not None:
                    y["right"]["p"] = y
            else:

                balance_point = y

            self.transplant(z, y)
            y["left"] = z["left"]
            y["left"]["p"] = y

        # Update balance factors (height) at directly affected node/s by deletion
        for node in [balance_point, extra_balance_point]:
            if node is not None:
                # Left child check
                if node["left"] is not None:
                    node["h_left"] = max(node["left"]["h_left"], node["left"]["h_right"]) + 1
                else:
                    node["h_left"] = 0
                # Right child check
                if node["right"] is not None:
                    node["h_right"] = max(node["right"]["h_left"], node["right"]["h_right"]) + 1
                else:
                    node["h_right"] = 0
        # Update balance factors (height) on the branch affected by deletion and rebalance if required
        self.AVL_update_balance(balance_point)


# Running simple example
print("Right rotation example: ")
my_tree = AVL_tree()
my_tree.tree_insert(10)
my_tree.tree_insert(11)
my_tree.tree_insert(6)
my_tree.tree_insert(7)
my_tree.tree_insert(4)
tree_visualize(my_tree.root)
print("-> insert 2")
my_tree.tree_insert(2)
tree_visualize(my_tree.root)

print("Left rotation example: ")
my_tree = AVL_tree()
my_tree.tree_insert(4)
my_tree.tree_insert(6)
my_tree.tree_insert(2)
my_tree.tree_insert(10)
my_tree.tree_insert(5)
tree_visualize(my_tree.root)
print("-> insert 11")
my_tree.tree_insert(11)
tree_visualize(my_tree.root)


print("Right Left rotation example: ")
my_tree = AVL_tree()
my_tree.tree_insert(4)
my_tree.tree_insert(2)
my_tree.tree_insert(9)
my_tree.tree_insert(6)
my_tree.tree_insert(10)
tree_visualize(my_tree.root)
print("-> insert 7")
my_tree.tree_insert(7)
tree_visualize(my_tree.root)

print("Left Right rotation example: ")
my_tree = AVL_tree()
my_tree.tree_insert(9)
my_tree.tree_insert(10)
my_tree.tree_insert(4)
my_tree.tree_insert(11)
my_tree.tree_insert(6)
my_tree.tree_insert(3)
my_tree.tree_insert(2)
my_tree.tree_insert(5)
my_tree.tree_insert(7)
tree_visualize(my_tree.root)
print("-> insert 8")
my_tree.tree_insert(8)
tree_visualize(my_tree.root)


print("\n\n\n Dr. Rob Edwards' rotation example: ")
my_tree = AVL_tree()
my_tree.tree_insert(43)
my_tree.tree_insert(18)
my_tree.tree_insert(23)
my_tree.tree_insert(9)
my_tree.tree_insert(21)
my_tree.tree_insert(6)
my_tree.tree_insert(8)
my_tree.tree_insert(20)
my_tree.tree_insert(63)
my_tree.tree_insert(50)
my_tree.tree_insert(62)
my_tree.tree_insert(51)
print("my_tree.root: ")
print(my_tree.root)
print("my_tree.root[left]")
print(my_tree.root["left"])
print("my_tree.root[right]")
print(my_tree.root["right"])
tree_visualize(my_tree.root)

# # Delete example 1
# my_tree.tree_delete(43)
# my_tree.tree_delete(62)
# my_tree.tree_delete(63)
# my_tree.tree_delete(8)
# my_tree.tree_delete(9)

# my_tree.tree_delete(6)
# my_tree.tree_delete(50)

# Delete example 2
my_tree.tree_delete(50)


print("my_tree.root: ")
print(my_tree.root)
print("my_tree.root[left]")
print(my_tree.root["left"])
print("my_tree.root[right]")
print(my_tree.root["right"])
tree_visualize(my_tree.root)
