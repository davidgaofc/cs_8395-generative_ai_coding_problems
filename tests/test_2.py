from problems.problem_2 import Stack


def test_push():
    stack = Stack()

    stack.push(5)
    assert stack.peek() == 5
    assert stack.pop() == 5

    stack.push(10)
    assert stack.peek() == 10
    assert stack.pop() == 10

    stack.push(15)
    stack.push(20)
    assert stack.peek() == 20
    assert stack.pop() == 20
    assert stack.pop() == 15

def test_pop():
    stack = Stack()

    assert stack.pop() is None

    stack.push(5)
    stack.push(10)
    stack.push(15)

    assert stack.pop() == 15
    assert stack.pop() == 10
    assert stack.pop() == 5
    assert stack.pop() is None

def test_peek():
    stack = Stack()

    assert stack.peek() is None

    stack.push(5)
    stack.push(10)
    stack.push(15)

    assert stack.peek() == 15
    assert stack.peek() == 15
    assert stack.pop() == 15
    assert stack.pop() == 10
    assert stack.peek() == 5
    assert stack.peek() == 5
    assert stack.pop() == 5
    assert stack.pop() is None
    assert stack.peek() is None