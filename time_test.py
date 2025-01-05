import time
import random


class Node:
    def __init__(self, key):
        self.key = key
        self.left = None
        self.right = None

class BinarySearchTree:
    def __init__(self):
        self.root = None

    def insert(self, key):
        if self.root is None:
            self.root = Node(key)
        else:
            self._insert(self.root, key)

    def _insert(self, current_node, key):
        if key < current_node.key:
            if current_node.left is None:
                current_node.left = Node(key)
            else:
                self._insert(current_node.left, key)
        elif key > current_node.key:
            if current_node.right is None:
                current_node.right = Node(key)
            else:
                self._insert(current_node.right, key)

    def search(self, key):
        return self._search(self.root, key)

    def _search(self, current_node, key):
        if current_node is None:
            return False
        if key == current_node.key:
            return True
        elif key < current_node.key:
            return self._search(current_node.left, key)
        else:
            return self._search(current_node.right, key)

    def inorder_traversal(self):
        result = []
        self._inorder_traversal(self.root, result)
        return result

    def _inorder_traversal(self, current_node, result):
        if current_node:
            self._inorder_traversal(current_node.left, result)
            result.append(current_node.key)
            self._inorder_traversal(current_node.right, result)


class Timer:
    def __init__(self):
        self.start = None

    def __enter__(self):
        self.start = time.time()
        return self

    def __exit__(self, *args):
        self.end = time.time()
        self.interval = self.end - self.start

bst = BinarySearchTree()

# сбалансированное дерево
random_data = random.sample(range(0, 100), 100)
with Timer() as t_random:
    for value in random_data:
        bst.insert(value)

print(f"Время вставки (случайные данные): {t_random.interval:.4f} сек")


with Timer() as t_search:
    bst.search(random_data[50])
print(f"Время поиска (случайные данные): {t_search.interval:.8f} сек")

# несбалансированное дерево
bst_unbalanced = BinarySearchTree()
ordered_data = list(range(0, 100))
with Timer() as t_ordered:
    for value in ordered_data:
        bst_unbalanced.insert(value)

print(f"Время вставки (упорядоченные данные): {t_ordered.interval:.4f} сек")


with Timer() as t_unbalanced_search:
    bst_unbalanced.search(ordered_data[-1])
print(f"Время поиска (упорядоченные данные): {t_unbalanced_search.interval:.8f} сек")










