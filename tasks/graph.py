from typing import Any

__all__ = (
    'Node',
    'Graph'
)


class Node:
    def __init__(self, value: Any):
        self.value = value

        self.outbound = []
        self.inbound = []

    def point_to(self, other: 'Node'):
        self.outbound.append(other)
        other.inbound.append(self)

    def __str__(self):
        return f'Node({repr(self.value)})'

    __repr__ = __str__


class Graph:
    def __init__(self, root: Node):
        self._root = root
        self._visited = set()
        self._result = []


    def dfs(self) -> list[Node]:
        def dfs_helper(node):
            self._visited.add(node)
            self._result.append(node)
            for neighbor in node.outbound:
                if neighbor not in self._visited:
                    dfs_helper(neighbor)
        dfs_helper(self._root)
        return self._result



    def bfs(self) -> list[Node]:
        queue = [self._root]
        while queue:
            node = queue.pop(0)
            if node not in self._visited:
                self._visited.add(node)
                self._result.append(node)
                queue.extend(node.outbound)
        return self._result
