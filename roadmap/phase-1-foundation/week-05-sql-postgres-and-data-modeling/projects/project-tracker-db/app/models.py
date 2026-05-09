"""
Simple data models for the Week 05 project tracker.
"""

from dataclasses import dataclass


@dataclass
class ProjectSummary:
    """Represent a project plus simple task counts."""

    project_id: int
    project_name: str
    owner_name: str
    total_tasks: int
    open_tasks: int


@dataclass
class TaskRecord:
    """Represent one task row in a readable Python shape."""

    task_id: int
    project_name: str
    title: str
    status: str
    priority: int
