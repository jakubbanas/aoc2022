with open("day7_input.txt") as f:
    input_data = [item.replace("\n", "") for item in f]


class Node:
    def __init__(self, parent, name) -> None:
        self.parent = parent
        self.name = name
        self.children = []
        self.size = 0


def feed_parent(node: Node, size: int):
    node.size += size
    if node.parent:
        feed_parent(node.parent, size)


def get_sizes(node: Node, result: list):
    for child in node.children:
        get_sizes(child, result)

    result.append(node.size)


root = Node(None, "/")
current_node = root
total_size = 0

for item in input_data:
    if item == "$ ls":
        continue

    if item == "$ cd ..":
        current_node = current_node.parent
        continue

    if "$ cd" in item:
        name = item.split(" ")[2]
        new_node = Node(current_node, name)
        current_node.children.append(new_node)
        current_node = new_node
        continue

    size = item.split(" ")[0]
    if size != "dir":
        feed_parent(current_node, int(size))
        total_size += int(size)

sizes = []
get_sizes(root, sizes)

print(sum(list(filter(lambda size: size <= 100000, sizes))))
to_cleanup = total_size - 40000000

print(min(list(filter(lambda size: size >= to_cleanup, sizes))))
