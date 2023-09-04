from problems.problem_81 import PhoneNumberValidator

def test_validate():
    def rule1(phone_number):
        return phone_number.startswith("1") and len(phone_number) == 11

    def rule2(phone_number):
        return phone_number.startswith("9") and len(phone_number) == 10

    rules = [rule1, rule2]
    validator = PhoneNumberValidator(rules)

    assert validator.validate("12345678901") == True
    assert validator.validate("9876543210") == True
    assert validator.validate("5555555555") == False