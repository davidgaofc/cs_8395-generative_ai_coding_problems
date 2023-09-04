from problems.problem_18 import Process, Scheduler

def test_add_process():
    scheduler = Scheduler()
    process = Process(1, 10)
    scheduler.add_process(process)
    assert len(scheduler.processes) == 1
    assert scheduler.processes[0] == process

def test_simulate_scheduling():
    scheduler = Scheduler()
    process1 = Process(1, 10)
    process2 = Process(2, 5)
    process3 = Process(3, 8)
    scheduler.add_process(process1)
    scheduler.add_process(process2)
    scheduler.add_process(process3)

    scheduled_order = scheduler.simulate_scheduling()
    assert scheduled_order == [2, 3, 1]