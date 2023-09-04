from problems.problem_90 import LogAnalyzer

def test_add_log_entry():
    analyzer = LogAnalyzer()

    analyzer.add_log_entry("2023-09-01 10:00:00", "User logged in")
    analyzer.add_log_entry("2023-09-01 15:30:00", "File uploaded")
    analyzer.add_log_entry("2023-09-02 08:45:00", "User logged in")
    analyzer.add_log_entry("2023-09-02 12:15:00", "File downloaded")

    assert analyzer.get_events_by_day("2023-09-01") == ["User logged in", "File uploaded"]
    assert analyzer.get_events_by_day("2023-09-02") == ["User logged in", "File downloaded"]
    assert analyzer.get_total_events() == 4
def test_get_events_by_day():
    analyzer = LogAnalyzer()

    analyzer.add_log_entry("2023-09-01 10:00:00", "User logged in")
    analyzer.add_log_entry("2023-09-01 15:30:00", "File uploaded")
    analyzer.add_log_entry("2023-09-02 08:45:00", "User logged in")
    analyzer.add_log_entry("2023-09-02 12:15:00", "File downloaded")

    assert analyzer.get_events_by_day("2023-09-01") == ["User logged in", "File uploaded"]
    assert analyzer.get_events_by_day("2023-09-02") == ["User logged in", "File downloaded"]
    assert analyzer.get_total_events() == 4

def test_get_total_events():
    analyzer = LogAnalyzer()

    analyzer.add_log_entry("2023-09-01 10:00:00", "User logged in")
    analyzer.add_log_entry("2023-09-01 15:30:00", "File uploaded")
    analyzer.add_log_entry("2023-09-02 08:45:00", "User logged in")
    analyzer.add_log_entry("2023-09-02 12:15:00", "File downloaded")

    assert analyzer.get_events_by_day("2023-09-01") == ["User logged in", "File uploaded"]
    assert analyzer.get_events_by_day("2023-09-02") == ["User logged in", "File downloaded"]
    assert analyzer.get_total_events() == 4