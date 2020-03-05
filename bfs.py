from queue import Queue
from typing import Set


class Node:
    def __init__(self, idx: int, prev=None):
        self.idx = idx
        self.adj = set()
        self.prev_node = prev

    def __hash__(self):
        return self.idx

    def __eq__(self, other):
        return self.idx == other.idx

    def __str__(self):
        return str(self.idx)


def get_info(file):
    with open(file) as file:
        n = int(file.readline())
        nodes = [Node(i) for i in range(n)]
        for i in range(n):
            for adj_node in map(int, file.readline().split()):
                if adj_node == 0:
                    break
                nodes[i].adj.add(nodes[adj_node-1])
    return nodes


def bfs(nodes):
    nodes_to_visit = Queue()
    visited_nodes: Set[Node] = set()
    nodes_to_visit.put(nodes[0])
    visited_nodes.add(nodes[0])
    while not nodes_to_visit.empty():
        current_node = nodes_to_visit.get()
        for adj_node in current_node.adj:
            adj_node.prev = current_node
            if adj_node in visited_nodes and adj_node != current_node.prev:
                return adj_node
            visited_nodes.add(adj_node)
            nodes_to_visit.put(adj_node)


if __name__ == '__main__':
    cur_node = bfs(get_info('input.txt'))
    nodes_in_cycle = list()
    while str(cur_node) not in nodes_in_cycle:
        nodes_in_cycle.append(str(cur_node))
        cur_node = cur_node.prev
    nodes_in_cycle.sort()
    with open('outpu.txt', 'w') as file:
        file.write(' '.join(nodes_in_cycle))
