"""Automated tests for the ResearchOS knowledge graph."""

import unittest

from researchos.graph import GraphNode, KnowledgeGraph


class KnowledgeGraphTests(unittest.TestCase):

    def setUp(self):
        self.graph = KnowledgeGraph()

        self.graph.add_node(
            GraphNode("c1", "claim")
        )

        self.graph.add_node(
            GraphNode("c2", "claim")
        )

        self.graph.add_node(
            GraphNode("e1", "evidence")
        )

    def test_node_registration(self):
        self.assertIn("c1", self.graph.nodes)
        self.assertIn("c2", self.graph.nodes)
        self.assertIn("e1", self.graph.nodes)

    def test_node_metadata(self):
        node = GraphNode(
            "c3",
            "claim",
            {"source": "research"}
        )

        self.graph.add_node(node)

        self.assertEqual(
            self.graph.nodes["c3"].metadata["source"],
            "research"
        )

    def test_duplicate_node_rejected(self):
        with self.assertRaisesRegex(
            ValueError, "duplicate node"
        ):
            self.graph.add_node(
                GraphNode("c1", "claim")
            )

    def test_edge_creation(self):
        self.graph.add_edge("c1", "c2")

        self.assertIn(
            "c2",
            self.graph.dependencies("c1")
        )

    def test_dependency_order(self):
        self.graph.add_edge("c1", "e1")
        self.graph.add_edge("c1", "c2")

        self.assertEqual(
            self.graph.dependencies("c1"),
            ["c2", "e1"]
        )

    def test_unknown_source_rejected(self):
        with self.assertRaisesRegex(
            ValueError, "unknown source"
        ):
            self.graph.add_edge("missing", "c1")

    def test_unknown_target_rejected(self):
        with self.assertRaisesRegex(
            ValueError, "unknown target"
        ):
            self.graph.add_edge("c1", "missing")

    def test_unknown_node_dependencies(self):
        with self.assertRaisesRegex(
            ValueError, "unknown node"
        ):
            self.graph.dependencies("missing")

    def test_acyclic_graph(self):
        self.graph.add_edge("c1", "c2")
        self.graph.add_edge("c2", "e1")

        self.assertFalse(
            self.graph.has_cycle()
        )

    def test_circular_dependency(self):
        self.graph.add_edge("c1", "c2")
        self.graph.add_edge("c2", "c1")

        self.assertTrue(
            self.graph.has_cycle()
        )

    def test_self_dependency(self):
        self.graph.add_edge("c1", "c1")

        self.assertTrue(
            self.graph.has_cycle()
        )

    def test_disconnected_graph(self):
        self.assertFalse(
            self.graph.has_cycle()
        )


if __name__ == "__main__":
    unittest.main()
