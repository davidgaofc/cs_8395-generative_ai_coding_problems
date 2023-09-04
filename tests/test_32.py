from problems.problem_32 import PhysicsCalculator

def test_velocity():
    calculator = PhysicsCalculator()
    assert calculator.velocity(10, 2, 5) == 20

def test_distance():
    calculator = PhysicsCalculator()
    assert calculator.distance(10, 5, 2) == 60
    assert calculator.distance(15, 2) == 30