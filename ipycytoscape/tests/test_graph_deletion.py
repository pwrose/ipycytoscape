#!/usr/bin/env python
# coding: utf-8

# Copyright (c) 2020, QuantStack and ipycytoscape Contributors
#
# Distributed under the terms of the Modified BSD License.
#
# The full license is in the file LICENSE, distributed with this software.

import pytest

from ipycytoscape.cytoscape import Graph, Node, Edge
import networkx as nx


class TestNetworkx:
    def test_lonely_nodes(self):
        """
        Test to ensure that nodes with no associated edges end up in the graph
        """
        G1 = nx.complete_graph(5)
        G2 = nx.Graph()
        G2.add_node("unconnected_node")
        G2 = nx.complete_graph(1)
        graph = Graph()
        graph.add_graph_from_networkx(G1)
        graph.add_graph_from_networkx(G2)

        expected_nodes = [
            Node(data={"id": "0"}, position={}),
            Node(data={"id": "1"}, position={}),
            Node(data={"id": "2"}, position={}),
            Node(data={"id": "3"}, position={}),
            Node(data={"id": "4"}, position={}),
            Node(data={"id": "unconnected_node"}, position={}),
        ]

        # remove individual node using node as input
        graph.remove_node(graph.nodes[0])

        expected_nodes = [
            Node(data={"id": "1"}, position={}),
            Node(data={"id": "2"}, position={}),
            Node(data={"id": "3"}, position={}),
            Node(data={"id": "4"}, position={}),
            Node(data={"id": "unconnected_node"}, position={}),
        ]

        # remove individual node using index node as input
        graph.remove_node_by_id("3")

        expected_nodes = [
            Node(data={"id": "1"}, position={}),
            Node(data={"id": "2"}, position={}),
            Node(data={"id": "4"}, position={}),
            Node(data={"id": "unconnected_node"}, position={}),
        ]

        # remove all nodes of the graph
        graph.clear()
        expected_nodes = []
