from problems.problem_46 import AutocompleteSystem

def test_insert():
    system = AutocompleteSystem([], [])
    system.insert("i love you", 5)
    system.insert("island", 3)
    system.insert("ironman", 2)
    system.insert("i love leetcode", 2)

    assert system.root.children['i'].children['l'].children['o'].children['v'].children['e'].children[' '].children['y'].children['o'].children['u'].count == 5
    assert system.root.children['i'].children['s'].children['l'].children['a'].children['n'].children['d'].count == 3
    assert system.root.children['i'].children['r'].children['o'].children['n'].children['m'].children['a'].children['n'].count == 2
    assert system.root.children['i'].children['l'].children['o'].children['v'].children['e'].children[' '].children['l'].children['e'].children['e'].children['t'].children['c'].children['o'].children['d'].children['e'].count == 2

def test_search():
    system = AutocompleteSystem([], [])
    system.insert("i love you", 5)
    system.insert("island", 3)
    system.insert("ironman", 2)
    system.insert("i love leetcode", 2)

    assert system.search("i love") == ["i love you", "i love leetcode"]
    assert system.search("i lo") == ["i love you", "i love leetcode"]
    assert system.search("iron") == ["ironman"]
    assert system.search("is") == ["island"]