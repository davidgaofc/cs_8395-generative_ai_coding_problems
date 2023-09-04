from problems.problem_17 import Server, LoadBalancer

def test_add_server():
    load_balancer = LoadBalancer()
    server = Server(1, 10)
    load_balancer.add_server(server)
    assert len(load_balancer.servers) == 1
    assert load_balancer.servers[0] == server

def test_balance_load():
    load_balancer = LoadBalancer()
    server1 = Server(1, 10)
    server2 = Server(2, 15)
    server3 = Server(3, 20)
    load_balancer.add_server(server1)
    load_balancer.add_server(server2)
    load_balancer.add_server(server3)

    load_balancer.balance_load()

    assert server1.load == 15
    assert server2.load == 15
    assert server3.load == 15

def test_get_server_with_lowest_load():
    load_balancer = LoadBalancer()
    server1 = Server(1, 10)
    server2 = Server(2, 5)
    server3 = Server(3, 8)
    load_balancer.add_server(server1)
    load_balancer.add_server(server2)
    load_balancer.add_server(server3)

    lowest_load_server = load_balancer.get_server_with_lowest_load()
    assert lowest_load_server == server2