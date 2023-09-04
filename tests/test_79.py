from problems.problem_79 import CalendarEvent

def test_duration():
    event = CalendarEvent("Meeting", "09:00", "10:30")
    assert event.duration() == 90

def test_overlaps():
    event1 = CalendarEvent("Event 1", "08:00", "09:30")
    event2 = CalendarEvent("Event 2", "09:00", "10:00")
    event3 = CalendarEvent("Event 3", "10:30", "11:30")

    assert event1.overlaps(event2)
    assert not event1.overlaps(event3)
    assert event2.overlaps(event3)