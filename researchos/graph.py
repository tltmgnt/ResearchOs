"""ResearchOS knowledge and evidence graph."""

from dataclasses import dataclass, field
from typing import Dict, List, Set


@dataclass
class GraphNode:
    identifier: str
    node_type: str
    metadata: dict = field(default_factory=dict)


class KnowledgeGraph:
    """Manage claim and evidence relationships."""

    def __init__(self):
        self.nodes: Dict[str, GraphNode] = {}
        self.edges: Dict[str, Set[str]] = {}

    def add_node(self, node: GraphNode):
        if node.identifier in self.nodes:
            raise ValueError("duplicate node")

        self.nodes[node.identifier] = node
        self.edges[node.identifier] = set()

    def add_edge(self, source: str, target: str):
        if source not in self.nodes:
            raise ValueError("unknown source")

        if target not in self.nodes:
            raise ValueError("unknown target")

        self.edges[source].add(target)

    def dependencies(self, identifier: str) -> List[str]:
        if identifier not in self.nodes:
            raise ValueError("unknown node")

        return sorted(self.edges[identifier])

    def has_cycle(self) -> bool:
        visited = set()
        active = set()

        def visit(node):
            if node in active:
                return True

            if node in visited:
                return False

            active.add(node)

            for neighbor in self.edges[node]:
                if visit(neighbor):
                    return True

            active.remove(node)
            visited.add(node)

            return False

        return any(
            visit(node)
            for node in self.nodes
            if node not in visited
        )
