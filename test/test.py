from src.bowling import *


def test_special_sign():
    assert Bowling.special_sign("X") == (10)
    assert Bowling.special_sign("/") == (10)
    assert Bowling.special_sign("-") == (0)


def test_spare():
    assert Bowling.spare("1/111111111111111111", 1) == 10
    assert Bowling.spare("-/X--X--X--X--X--", 1) == 20
    assert Bowling.spare("25XXX4/2111XX43", 6) == 8
    assert Bowling.spare("XXX-/145136/9/154", 13) == 2


def test_strike():
    assert Bowling.strike("X111111111111111111", 0) == 12
    assert Bowling.strike("--X--X--X--X--X--", 14) == 10
    assert Bowling.strike("25XXX4/2111XX43", 3) == 24
    assert Bowling.strike("25XXX4/2111XX43", 2) == 30
    assert Bowling.strike("25XXX4/2111XX43", 4) == 20


def test_turns():
    assert Bowling.turns("12345123451234512345") == [
        '12', '34', '51', '23', '45', '12', '34', '51', '23', '45']

    assert Bowling.turns(
        "9-9-9-9-9-9-9-9-9-9-") == ['9-', '9-', '9-', '9-', '9-', '9-', '9-', '9-', '9-', '9-']
    assert Bowling.turns(
        "5/5/5/5/5/5/5/5/5/5/5") == ['5/', '5/', '5/', '5/', '5/', '5/', '5/', '5/', '5/', '5/5']
    assert Bowling.turns("XXXXXXXXXXXX") == ['X', 'X', 'X',
                                             'X', 'X', 'X', 'X', 'X', 'X', 'XXX']
    assert Bowling.turns(
        "XXX9-9-9-9-9-9-9-") == ['X', 'X', 'X', '9-', '9-', '9-', '9-', '9-', '9-', '9-']
    assert Bowling.turns(
        "8-7-539/9/X8-513/9-") == ['8-', '7-', '53', '9/', '9/', 'X', '8-', '51', '3/', '9-']
    assert Bowling.turns(
        "8/9-44729-XX8-359/7") == ['8/', '9-', '44', '72', '9-', 'X', 'X', '8-', '35', '9/7']
    assert Bowling.turns(
        "-/-/-/-/-/-/-/-/-/-/-") == ['-/', '-/', '-/', '-/', '-/', '-/', '-/', '-/', '-/', '-/-']
    assert Bowling.turns(
        "X5/X5/XX5/--5/X5/") == ['X', '5/', 'X', '5/', 'X', 'X', '5/', '--', '5/', 'X5/']
    assert Bowling.turns(
        "8/549-XX5/53639/9/X") == ['8/', '54', '9-', 'X', 'X', '5/', '53', '63', '9/', '9/X']


def test_score():
    assert Bowling.score("11111111111111111111") == 20
    assert Bowling.score("12345123451234512345") == 60
    assert Bowling.score("9-9-9-9-9-9-9-9-9-9-") == 90
    assert Bowling.score("5/5/5/5/5/5/5/5/5/5/5") == 150
    assert Bowling.score("XXXXXXXXXXXX") == 300
    assert Bowling.score("XXX9-9-9-9-9-9-9-") == 141
    assert Bowling.score("8-7-539/9/X8-513/9-") == 122
    assert Bowling.score("8/9-44729-XX8-359/7") == 133
    assert Bowling.score("-/-/-/-/-/-/-/-/-/-/-") == 100
    assert Bowling.score("X5/X5/XX5/--5/X5/") == 175
    assert Bowling.score("8/549-XX5/53639/9/X") == 149
