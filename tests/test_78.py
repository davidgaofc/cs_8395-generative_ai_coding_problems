from problems.problem_78 import PasswordGenerator

def test_generate_password():
    generator = PasswordGenerator()
    password = generator.generate_password()
    assert len(password) == 8
    assert any(c.isalpha() for c in password)
    assert any(c.isdigit() for c in password)

def test_set_special_characters():
    generator = PasswordGenerator()
    generator.set_special_characters("!@#$")
    assert generator.generate_password(10) == "!" * 2 + "@" + "#" * 2 + "$" * 5

def test_generate_strong_password():
    generator = PasswordGenerator()
    password = generator.generate_strong_password()
    assert len(password) == 12
    assert any(c.isalpha() for c in password)
    assert any(c.isdigit() for c in password)
    assert any(c.isupper() for c in password)
    assert any(c in "!@#$%^&*()_+-=" for c in password)