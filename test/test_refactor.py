from src.refactor_bowling import Game_Score

# Los casos test en comentario estaban destinados a la construcción individualizada de las funciones y son inviables en su conjunto.


# def test_strike_score():
#     assert 19 == Game_Score('X36').strike_score()
#     assert 16 == Game_Score('5X422').strike_score()


# def test_spare():
#     assert 15 == Game_Score('2/5').spare_score()
#     assert 15 == Game_Score('2/56').spare_score()
#     assert 20 == Game_Score('2/X').spare_score()


def test_final_score():
    assert Game_Score("11111111111111111111").final_score() == 20
    assert Game_Score("12345123451234512345").final_score() == 60
    assert Game_Score("9-9-9-9-9-9-9-9-9-9-").final_score() == 90
    assert Game_Score("5/5/5/5/5/5/5/5/5/5/5").final_score() == 150
    assert Game_Score("XXXXXXXXXXXX").final_score() == 300
    assert Game_Score("XXX9-9-9-9-9-9-9-").final_score() == 141
    assert Game_Score("8-7-539/9/X8-513/9-").final_score() == 122
    assert Game_Score("8/9-44729-XX8-359/7").final_score() == 133
    assert Game_Score("-/-/-/-/-/-/-/-/-/-/-").final_score() == 100
    assert Game_Score("X5/X5/XX5/--5/X5/").final_score() == 175
    assert Game_Score("8/549-XX5/53639/9/X").final_score() == 149
