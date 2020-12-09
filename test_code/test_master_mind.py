from source_code.game import Game


def test_master_mind_check1():
    master_mind = Game(['RED', 'BLUE', 'GREEN', 'YELLOW'])
    result = master_mind.check(['RED', 'ORANGE', 'YELLOW', 'ORANGE'])
    assert result.count('White') == 1
    assert result.count('Black') == 1


def test_master_mind_check2():
    master_mind = Game(['RED', 'BLUE', 'GREEN', 'YELLOW'])
    result = master_mind.check(['RED', 'BLUE', 'GREEN', 'YELLOW'])
    assert result.count('Black') == 4


def test_master_mind_check3():
    master_mind = Game(['RED', 'BLUE', 'GREEN', 'YELLOW'])
    result = master_mind.check(['GREY', 'GREY', 'GREY', 'GREY'])
    assert len(result) == 0


def test_master_mind_no_of_inputs_check():
    master_mind = Game(['RED', 'BLUE', 'GREEN', 'YELLOW'])
    result = master_mind.check(['RED', 'BLUE', 'GREEN'])
    assert result == 'You should specify exactly 4 colors'
