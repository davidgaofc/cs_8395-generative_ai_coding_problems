from problems.problem_3 import Queue

def test_enqueue():
    queue = Queue()

    queue.enqueue(5)
    assert queue.peek() == 5

    queue.enqueue(10)
    assert queue.peek() == 5

    queue.enqueue(15)
    assert queue.peek() == 5

def test_dequeue():
    queue = Queue()

    assert queue.dequeue() is None

    queue.enqueue(5)
    queue.enqueue(10)
    queue.enqueue(15)

    assert queue.dequeue() == 5
    assert queue.dequeue() == 10
    assert queue.dequeue() == 15
    assert queue.dequeue() is None

def test_peek():
    queue = Queue()

    assert queue.peek() is None

    queue.enqueue(5)
    queue.enqueue(10)
    queue.enqueue(15)

    assert queue.peek() == 5
    assert queue.peek() == 5
    assert queue.dequeue() == 5
    assert queue.dequeue() == 10
    assert queue.peek() == 15
    assert queue.peek() == 15
    assert queue.dequeue() == 15
    assert queue.dequeue() is None
    assert queue.peek() is None