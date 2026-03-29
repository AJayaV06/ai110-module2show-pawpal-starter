import pytest
from datetime import date, time

from pawpal_system import Owner, Pet, Task, TaskCategory, Scheduler


def test_task_completion_changes_status():
    task = Task(
        title="Walk Dog",
        description="30 minute walk",
        duration_minutes=30,
        priority=4,
        category=TaskCategory.WALK,
        pet_name="Rex",
    )

    assert task.completed is False
    task.set_completed(True)
    assert task.completed is True


def test_add_task_to_pet_increases_task_count():
    pet = Pet(name="Rex", age=5, species="dog", breed="labrador")
    base_count = len(pet.tasks)

    task = Task(
        title="Feed Dog",
        description="Food in bowl",
        duration_minutes=10,
        priority=5,
        category=TaskCategory.FEED,
        pet_name="Rex",
    )

    pet.add_task(task)
    assert len(pet.tasks) == base_count + 1
    assert pet.tasks[-1].title == "Feed Dog"
