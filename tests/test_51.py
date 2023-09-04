from problems.problem_51 import EncryptionSystem

def test_decrypt():
    encryption_key = "secret"
    system = EncryptionSystem(encryption_key)

    message = "Hello, world!"
    encrypted_message = system.encrypt(message)
    decrypted_message = system.decrypt(encrypted_message)

    assert decrypted_message == message

def test_encrypt():
    encryption_key = "secret"
    system = EncryptionSystem(encryption_key)

    message = "Hello, world!"
    encrypted_message = system.encrypt(message)
    decrypted_message = system.decrypt(encrypted_message)

    assert decrypted_message == message