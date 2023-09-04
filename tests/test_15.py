from problems.problem_15 import Task, TaskList

def test_complete():
    task = Task("Write report", "Complete the monthly sales report.", 2)
    task.complete()
    assert task.completed

def test_add_task():
    task_list = TaskList("Personal Tasks")
    task = Task("Buy groceries", "Purchase items for the week.", 1)
    task_list.add_task(task)
    assert len(task_list.tasks) == 1
    assert task_list.tasks[0] == task

def test_get_high_priority_tasks():
    task_list = TaskList("Work Tasks")

    task1 = Task("Meet with client", "Discuss project requirements.", 3)
    task2 = Task("Code review", "Review code changes.", 2)
    task3 = Task("Update documentation", "Update user manual.", 1)

    task_list.add_task(task1)
    task_list.add_task(task2)
    task_list.add_task(task3)

    high_priority_tasks = task_list.get_high_priority_tasks()
    assert len(high_priority_tasks) == 2
    assert task2 in high_priority_tasks
    assert task3 in high_priority_tasks