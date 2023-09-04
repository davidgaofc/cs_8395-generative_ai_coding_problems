from problems.problem_21 import NumericalIntegrator

def test_trapezoidal_rule():
    integrator = NumericalIntegrator()
    f = lambda x: x**2
    a = 0
    b = 1
    n = 4
    result = integrator.trapezoidal_rule(f, a, b, n)
    assert round(result, 6) == 0.333333