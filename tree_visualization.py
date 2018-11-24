# Tree visualization is designed based on my own idea only

from queue import Queue
import math


def tree_visualize(root, is_add_extra_lines=False):
    print("\n> tree visualization")

    queue = Queue()

    # Check tree depth
    max_key = - math.inf
    height = 0
    queue.enqueue({"height": height, "node": root})
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

    # Visualization itself
    queue.enqueue({"height": 0, "index": index, "delimiter": " ", "node": root})
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