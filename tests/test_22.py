from problems.problem_22 import DifferentialEquationSolver

def test_euler_method():
    solver = DifferentialEquationSolver()
    f = lambda t, y: t + y
    y0 = 1
    t0 = 0
    h = 0.1
    num_steps = 10
    approx_solution = solver.euler_method(f, y0, t0, h, num_steps)
    assert len(approx_solution) == num_steps + 1
    assert approx_solution[0] == y0
    assert approx_solution[-1] == 5.9848486570859375