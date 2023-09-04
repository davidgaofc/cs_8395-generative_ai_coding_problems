from problems.problem_7 import TaskScheduler

def test_schedule_task():
    scheduler = TaskScheduler()

    def task_function(task_id):
        print(f"Executing task {task_id}")

    task_id1 = scheduler.schedule_task(1, 2, task_function)
    task_id2 = scheduler.schedule_task(2, 3, task_function)

    assert task_id1 is not None
    assert task_id2 is not None

def test_cancel_task():
    scheduler = TaskScheduler()

    executed_tasks = []

    def task_function(task_id):
        executed_tasks.append(task_id)

    task_id1 = scheduler.schedule_task(1, 2, task_function)
    task_id2 = scheduler.schedule_task(2, 3, task_function)

    scheduler.cancel_task(task_id1)

    assert executed_tasks == [2]