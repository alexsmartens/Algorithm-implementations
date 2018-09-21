import math
import Queue
import numpy as np


class AVLNode:

    def __init__(self, key):
        self.key = key
        self.parent = None
        self.left = None
        self.right = None
        self.height = 0
        self.bf = 0

    def bfs(self):
        q = Queue.Queue()
        q.put(self)
        # output_str = ''
        output_arr = np.zeros((self.height + 1, pow(2, self.height)), dtype=int)
        i = 0
        j = 0

        # print output_arr.shape
        # print output_arr[1][1]

        while not q.empty():
            node = q.get()
            if node is not None:
                if node.left is not None:
                    q.put(node.left)
                else:
                    q.put(None)
                if node.right is not None:
                    q.put(node.right)
                else:
                    q.put(None)

                # Write to 2d array
                if node is None:
                    output_arr[i][j] = None
                else:
                    output_arr[i][j] = node.key

            # Increment row or col of array as needed
            if j == pow(2, i) - 1:
                i += 1
                j = 0
            else:
                j += 1

            # output_str += str(node.key) + ' '
        return output_arr


def transplant(root, u, v):
    if u.parent is None:
        root = v
    elif u == u.parent.left:
        u.parent.left = v
    else:
        u.parent.right == v
    if v is not None:
        v.parent = u.parent
    return root


def right_rotate(root, x):
    # print 'right_rotate on ' + str(root.key) + ' & ' + str(x.key)
    xlh = -1
    xrh = -1
    ylh = -1
    yrh = -1

    y = x.left

    root = transplant(root, x, y)

    x.left = y.right

    if x.left is not None:
        x.left.parent = x
    y.right = x
    x.parent = y

    if x.left is not None:
        xlh = x.left.height
    if x.right is not None:
        xrh = x.right.height

    x.height = max(xlh, xrh) + 1

    if y.left is not None:
        ylh = y.left.height
    if y.right is not None:
        yrh = y.right.height

    x.bf = xrh - xlh
    # print 'xrh: ' + str(xrh) + ' xlh: ' + str(xlh)
    # print 'yrh: ' + str(yrh) + ' ylh: ' + str(ylh)
    # print 'x.bf: ' + str(x.bf)
    y.height = max(ylh, yrh) + 1
    y.bf = yrh - ylh
    # print 'y.bf: ' + str(y.bf)
    # print 'root: ' + str(root.key) + ' new left + LR: ' + str(root.left.key) + \
    #     ' ' + str(root.left.left.key) + ' ' + str(root.left.right.key) +  \
    #     ' new right: ' + str(root.right.key)
    # print 'left bf: ' + str(root.left.bf)
    return root


def left_rotate(root, x):
    # print 'left_rotate on ' + str(root.key) + ' & ' + str(x.key)
    y = x.right
    root = transplant(root, x, y)
    x.right = y.left
    xlh = -1
    xrh = -1
    ylh = -1
    yrh = -1
    if x.right is not None:
        x.right.parent = x
    y.left = x
    x.parent = y

    if x.left is not None:
        xlh = x.left.height
    if x.right is not None:
        xrh = x.right.height

    x.height = max(xlh, xrh) + 1
    x.bf = xrh - xlh

    if y.left is not None:
        ylh = y.left.height
    if y.right is not None:
        yrh = y.right.height

    y.height = max(ylh, yrh) + 1
    y.bf = yrh - ylh
    return root


def insert(x, z):
    if x is None:
        x = z
    elif z.key < x.key:
        x.left = insert(x.left, z)
        x.left.parent = x
        z.parent = rebalance(z.parent)
        print 'insert left ' + str(z.key)
    else:
        x.right = insert(x.right, z)
        x.right.parent = x
        z.parent = rebalance(z.parent)
        print 'insert right ' + str(z.key)
    return x


def rebalance(z):
    while z is not None:
        cur_height = z.height
        lh = -1
        rh = -1
        if z.left is not None:
            lh = z.left.height
        if z.right is not None:
            rh = z.right.height
        if z is not None:
            z.height = max(lh, rh) + 1
            print 'z.key: ' + str(z.key)
            print 'z.height: ' + str(z.height)
            z.bf = rh - lh
            print 'z.bf: ' + str(z.bf)
        if z.bf == -2:
            print 'bf == -2, parent: ' + str(z.key) + ' lchild: ' + str(z.left.key) + ' lchild.lchild: ' + str(z.left.left.key)
            if z.left.bf <= 0:
                z.parent = right_rotate(z.parent, z)
            else:
                z.parent = left_rotate(z.parent, z.left)
                z.parent = right_rotate(z.parent, z)
        if z.bf == 2:
            print 'bf == 2, parent: ' + str(z.key) + ' rchild: ' + str(z.reft.key) + ' rchild.rchild: ' + str(
                z.right.right.key)
            if z.right.bf >= 0:
                z.parent = left_rotate(z.parent, z)
            else:
                z.parent = right_rotate(z.parent, z.right)
                z.parent = left_rotate(z.parent, z)
        if cur_height == z.height and z.bf == 0:
            print 'parent: ' + str(z.key) + ' lchild: ' + str(z.left.key) + ' rchild: ' + str(z.right.key)
            break
        z = z.parent
    return z


def print_tree(root):
    if root is None:
        return ''
    else:
        newline = ''
        if root.key == find_max(find_root(root), root.height):
            newline = '\n'
        return str(root.key) + newline + print_tree(root.left) + ' ' + print_tree(root.right)


def print_bfs(z):
    output = []
    for i in range(np.size(z, 0)):
        output.append('')
        for j in range(pow(2, i)):
            if z[i][j] == 0:
                val = ' '
            else:
                val = str(z[i][j])
            output[i] += val.center(pow(2, np.size(z, 0) - i + 1), ' ')
        print output[i]


def find_root(u):
    if u.parent is not None:
        find_root(u.parent)
    else:
        return u


def find_max(u, level=None):
    if level is None:
        level = 999  # need to change to math.inf
    if u.height < level:
        if u.right is not None:
            return find_max(u.right, level)
        else:
            return u.key
    else:
        return u.key


a = AVLNode(5)
b = AVLNode(6)
c = AVLNode(4)

# print a.height
a = insert(a, b)
# print a.height
a = insert(a, c)
# print a.height
a = insert(a, AVLNode(2))

# print c.right


# print 'aaa'

a = insert(a, AVLNode(1))

# print 'bbb'


# print c.left.key
print
print a.key
print a.left.key

print
print 'a.height: ' + str(a.height) + ' a.bf: ' + str(a.bf)
print 'a.left.height: ' + str(a.left.height) + ' a.left.bf: ' + str(a.left.bf)
print 'a.right.height: ' + str(a.right.height) + ' a.right.bf: ' + str(a.right.bf)

# print a.bfs()

# print_bfs(a.bfs())

# print print_tree(a)

# zzz22
