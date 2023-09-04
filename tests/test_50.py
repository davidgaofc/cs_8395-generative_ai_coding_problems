from problems.problem_50 import PasswordValidator


def test_validate_password():
    validator = PasswordValidator()

    assert validator.validate_password("Abcdefgh1") == True
    assert validator.validate_password("password123") == False
    assert validator.validate_password("P@ssw0rd") == False

    validator = PasswordValidator(min_length=10, require_special_char=False)
    assert validator.validate_password("Abcdefghijkl") == True
    assert validator.validate_password("1234567890") == False

    validator = PasswordValidator(require_digit=False)
    assert validator.validate_password("Password@") == True
    assert validator.validate_password("Abcdefgh") == False
