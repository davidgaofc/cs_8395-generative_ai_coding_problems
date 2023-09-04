from problems.problem_86 import EmailValidator

def test_validate_email():
    whitelist = ["example.com", "test.org"]
    validator = EmailValidator(whitelist)
    assert validator.validate_email("user@example.com")
    assert not validator.validate_email("user@test.org")
    assert not validator.validate_email("user@example.org")
    assert not validator.validate_email("user@test.com")