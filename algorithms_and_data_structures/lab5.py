import matplotlib.pyplot as plt

class Node:
    def __init__(self, value):
        self.value = value
        self.parent = None
        self.left = None
        self.right = None

class BinTree:
    def __init__(self):
        self.root = None
        self.nodes_to_delete = []

    def add_element(self, value):
        if self.root is None:
            self.root = Node(value)
        else:
            current = self.root
            while True:
                if value < current.value:
                    if current.left is None:
                        current.left = Node(value)
                        current.left.parent = current
                        break
                    else:
                        current = current.left
                else:
                    if current.right is None:
                        current.right = Node(value)
                        current.right.parent = current
                        break
                    else:
                        current = current.right

    def find(self, value):
        current = self.root
        while current is not None:
            if value == current.value:
                return current
            elif value < current.value:
                current = current.left
            else:
                current = current.right
        return None

    def __plot_tree(self, ax, node, x, y, dx):
        if node:
            ax.plot([x], [y], 'o', color='black')
            bbox_props = dict(boxstyle="round,pad=0.3", fc="lightgrey", ec="black", lw=1)
            ax.text(x, y + 0.5, str(node.value), bbox=bbox_props, verticalalignment='center',
                    horizontalalignment='center', fontsize=12)

            if node.left:
                ax.plot([x, x - dx / 2], [y, y - 15], '-k')
                self.__plot_tree(ax, node.left, x - dx / 2, y - 15, dx / 2)

            if node.right:
                ax.plot([x, x + dx / 2], [y, y - 15], '-k')
                self.__plot_tree(ax, node.right, x + dx / 2, y - 15, dx / 2)

    def visualize(self, title='Tree'):
        if self.root is None:
            print("Tree is empty.")
            return

        fig, ax = plt.subplots()
        self.__plot_tree(ax, self.root, 0, 0, 100)
        ax.set_aspect('equal')
        ax.axis('off')
        plt.title(title, y=1.2)
        plt.show()

    def delete_node_by_letter(self, letter):
        self.find_with_letter(self.root, letter)
        self.nodes_to_delete.reverse()
        for node in self.nodes_to_delete:
            self.delete_node(node)
        self.nodes_to_delete = []

    def find_with_letter(self, node, letter):
        if node:
            if node.value[0] == letter:
                self.nodes_to_delete.append(node)
            self.find_with_letter(node.left, letter)
            self.find_with_letter(node.right, letter)

    def delete_node(self, node):
        parent_node = node.parent

        if node.left is None and node.right is None:
            # no children
            if parent_node is None:
                self.root = None
            elif parent_node.left is node:
                parent_node.left = None
            else:
                parent_node.right = None
        elif node.left is not None and node.right is not None:
            # two children
            successor = node.right
            successor_parent = node

            while successor.left is not None:
                successor_parent = successor
                successor = successor.left

            node.value = successor.value
            if successor_parent.left is successor:
                successor_parent.left = successor.right
            else:
                successor_parent.right = successor.right
        else:
            # one child
            if node.left is not None:
                child = node.left
            else:
                child = node.right

            if parent_node is None:
                self.root = child
            elif parent_node.left is node:
                parent_node.left = child
            else:
                parent_node.right = child

tree = BinTree()
with open("data/text.csv", "r") as text:
    words = text.read()
    print(words)
    for word in words.split():
        tree.add_element(word)
    tree.visualize()

letter_to_delete = input('Enter letter to delete words with: ')
tree.delete_node_by_letter(letter_to_delete)
tree.visualize()
