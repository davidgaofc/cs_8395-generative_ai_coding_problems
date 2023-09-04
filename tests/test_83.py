from problems.problem_83 import VotingSystem

def test_vote():
    system = VotingSystem()
    system.add_candidate("Alice")
    system.add_candidate("Bob")

    system.vote("Alice")
    system.vote("Bob")
    system.vote("Alice")
    system.vote("Bob")
    system.vote("Bob")

    assert system.get_winner() == "Bob"
def test_add_candidate():
    system = VotingSystem()
    system.add_candidate("Alice")
    system.add_candidate("Bob")

    system.vote("Alice")
    system.vote("Bob")
    system.vote("Alice")
    system.vote("Bob")
    system.vote("Bob")

    assert system.get_winner() == "Bob"

def test_get_winner():
    system = VotingSystem()
    system.add_candidate("Alice")
    system.add_candidate("Bob")

    system.vote("Alice")
    system.vote("Bob")
    system.vote("Alice")
    system.vote("Bob")
    system.vote("Bob")

    assert system.get_winner() == "Bob"