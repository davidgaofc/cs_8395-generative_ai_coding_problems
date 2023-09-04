from problems.problem_71 import PasswordValidator

def test_set_password():
    validator = PasswordValidator()
    validator.set_password("Abcd123")
    assert validator.is_valid_length() == True

    validator.set_password("short")
    assert validator.is_valid_length() == False

def test_is_valid_length():
    validator = PasswordValidator()
    validator.set_password("Abcd123")
    assert validator.is_valid_length() == True

    validator.set_password("short")
    assert validator.is_valid_length() == False

def test_has_uppercase_letter():
    validator = PasswordValidator()
    validator.set_password("Password1")
    assert validator.has_uppercase_letter() == True

    validator.set_password("lowercase")
    assert validator.has_uppercase_letter() == False

def test_has_lowercase_letter():
    validator = PasswordValidator()
    validator.set_password("P@ssW0RD")
    assert validator.has_lowercase_letter() == True

    validator.set_password("UPPERCASE")
    assert validator.has_lowercase_letter() == False

def test_has_digit():
    validator = PasswordValidator()
    validator.set_password("Secure2022")
    assert validator.has_digit() == True

    validator.set_password("NoDigits")
    assert validator.has_digit() == False

    validator.set_password("Digits123")
    assert validator.has_digit() == True
