from source_code.game import Game
from source_code.main import *

def test_master_mind_check1():
    my_game = Game(['RED', 'BLUE', 'GREEN', 'YELLOW'])
    result = master_mind(my_game, ['RED', 'ORANGE', 'YELLOW', 'ORANGE'])
    assert result.count('White') == 1
    assert result.count('Black') == 1


def test_master_mind_check2():
    my_game = Game(['RED', 'BLUE', 'GREEN', 'YELLOW'])
    assert master_mind(my_game, ['RED', 'BLUE', 'GREEN', 'YELLOW']) == 'WON'


def test_master_mind_check3():
    my_game = Game(['RED', 'BLUE', 'GREEN', 'YELLOW'])
    result = master_mind(my_game, ['PURPLE', 'PURPLE', 'PURPLE', 'PURPLE'])
    assert len(result) == 0


def test_master_mind_no_of_inputs_check():
    my_game = Game(['RED', 'BLUE', 'GREEN', 'YELLOW'])
    assert master_mind(my_game, ['RED', 'BLUE', 'GREEN']) == 'You should specify exactly 4 colors'


def test_master_mind_invalid_inputs_check():
    my_game = Game(['RED', 'BLUE', 'GREEN', 'YELLOW'])
    assert master_mind(my_game, ['RED', 'BLU', 'GREEN', 'PURPLE']) == 'You have given an invalid color(s)!!!'
