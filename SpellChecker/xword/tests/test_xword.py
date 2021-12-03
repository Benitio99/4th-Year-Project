import xword


def test_empty():
    matches = xword.find_possible_matches("")
    assert len(matches) == 0


def test_python():
    matches = xword.find_possible_matches("_y__o_")
    assert len(matches) == 6
    assert sorted(matches) == [
        "byblos",
        "lyndon",
        "python",
        "symbol",
        "syphon",
        "tycoon",
    ]


def test_all_three():
    matches = xword.find_possible_matches("___")
    assert len(matches) == 744
    assert sorted(matches)[-1] == "zoo"


def test_actual():
    matches = xword.find_possible_matches("actual")
    assert len(matches) == 1
    assert matches.pop() == "actual"


def test_check_lower():
    matches = xword.find_possible_matches("_____ING")
    assert len(matches) == 1351
    assert matches.pop().endswith("ing") == True
