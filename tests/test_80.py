from problems.problem_80 import VendingMachine

def test_add_item():
    machine = VendingMachine()
    machine.add_item("Soda", 10, 1.5)
    machine.add_item("Chips", 20, 1.0)

    assert "Soda" in machine.stock
    assert "Chips" in machine.stock
    assert "Soda" in machine.prices
    assert "Chips" in machine.prices

def test_purchase():
    machine = VendingMachine()
    machine.add_item("Soda", 10, 1.5)

    assert machine.purchase("Soda", 2.0) == "Item dispensed. Change: $0.50"
    assert machine.purchase("Soda", 1.0) == "Insufficient funds. Please insert more money."
    assert machine.purchase("Chips", 2.0) == "Item not available."