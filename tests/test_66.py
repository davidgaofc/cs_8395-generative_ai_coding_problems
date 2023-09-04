from problems.problem_66 import MathExpression

def test_set_expression():
    math_expr = MathExpression()
    math_expr.set_expression("3 + 5 * 2")
    assert math_expr.expression == "3 + 5 * 2"



def test_evaluate():
    math_expr = MathExpression()
    math_expr.set_expression("3 + 5 * 2")
    assert math_expr.evaluate() == 13.0

    math_expr.set_expression("(2 + 3) * 4")
    assert math_expr.evaluate() == 20.0

