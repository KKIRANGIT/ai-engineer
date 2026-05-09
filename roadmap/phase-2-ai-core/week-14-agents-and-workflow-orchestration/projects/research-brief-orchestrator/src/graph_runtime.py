"""A tiny educational graph runtime for state-machine style workflows."""

from __future__ import annotations

from collections.abc import Callable

from .models import WorkflowState


NodeFunc = Callable[[WorkflowState], WorkflowState]
EdgeFunc = Callable[[WorkflowState], str]


class StateGraph:
    def __init__(self) -> None:
        self.nodes: dict[str, NodeFunc] = {}
        self.edges: dict[str, EdgeFunc] = {}
        self.start_node = ""

    def add_node(self, name: str, func: NodeFunc) -> None:
        self.nodes[name] = func

    def add_router(self, node_name: str, router: EdgeFunc) -> None:
        self.edges[node_name] = router

    def set_start(self, node_name: str) -> None:
        self.start_node = node_name

    def run(self, state: WorkflowState) -> WorkflowState:
        current = self.start_node

        while current != "END":
            state = self.nodes[current](state)
            router = self.edges.get(current)
            if router is None:
                raise ValueError(f"No router configured for node {current}")
            current = router(state)

        return state
