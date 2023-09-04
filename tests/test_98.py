from problems.problem_98 import OrderProcessor

def test_add_order():
    processor = OrderProcessor()

    processor.add_order({"item": "apple", "quantity": 5})
    processor.add_order({"item": "banana", "quantity": 3})
    processor.add_order({"item": "orange", "quantity": 2})

    processed_orders = processor.process_orders()

    assert len(processed_orders) == 3
    assert processed_orders[0]["status"] == "Processed"
    assert processed_orders[1]["status"] == "Processed"
    assert processed_orders[2]["status"] == "Processed"

def test_process_orders():
    processor = OrderProcessor()

    processor.add_order({"item": "apple", "quantity": 5})
    processor.add_order({"item": "banana", "quantity": 3})
    processor.add_order({"item": "orange", "quantity": 2})

    processed_orders = processor.process_orders()

    assert len(processed_orders) == 3
    assert processed_orders[0]["status"] == "Processed"
    assert processed_orders[1]["status"] == "Processed"
    assert processed_orders[2]["status"] == "Processed"