from problems.problem_96 import EmailManager

def test_send_email():
    manager = EmailManager()

    manager.send_email("sender@example.com", "recipient@example.com", "Hello", "This is a test email.")
    manager.send_email("sender@example.com", "recipient@example.com", "Greetings", "Another test email.")

    inbox = manager.get_inbox("recipient@example.com")
    assert len(inbox) == 2

    sent = manager.get_sent("sender@example.com")
    assert len(sent) == 2
def test_get_inbox():
    manager = EmailManager()

    manager.send_email("sender@example.com", "recipient@example.com", "Hello", "This is a test email.")
    manager.send_email("sender@example.com", "recipient@example.com", "Greetings", "Another test email.")

    inbox = manager.get_inbox("recipient@example.com")
    assert len(inbox) == 2

    sent = manager.get_sent("sender@example.com")
    assert len(sent) == 2
def test_get_sent():
    manager = EmailManager()

    manager.send_email("sender@example.com", "recipient@example.com", "Hello", "This is a test email.")
    manager.send_email("sender@example.com", "recipient@example.com", "Greetings", "Another test email.")

    inbox = manager.get_inbox("recipient@example.com")
    assert len(inbox) == 2

    sent = manager.get_sent("sender@example.com")
    assert len(sent) == 2