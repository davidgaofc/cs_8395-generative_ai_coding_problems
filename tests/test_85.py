from problems.problem_85 import PasswordManager

def test_register_user():
    password_manager = PasswordManager()
    password_manager.register_user("alice", "pass123")
    password_manager.register_user("bob", "secure456")

    assert "alice" in password_manager.users
    assert "bob" in password_manager.users

def test_verify_password():
    password_manager = PasswordManager()
    password_manager.register_user("alice", "pass123")
    password_manager.register_user("bob", "secure456")

    assert password_manager.verify_password("alice", "pass123")
    assert not password_manager.verify_password("bob", "wrongpass")

def test_change_password():
    password_manager = PasswordManager()
    password_manager.register_user("alice", "pass123")

    assert password_manager.verify_password("alice", "pass123")
    password_manager.change_password("alice", "pass123", "newpass456")
    assert not password_manager.verify_password("alice", "pass123")
    assert password_manager.verify_password("alice", "newpass456")