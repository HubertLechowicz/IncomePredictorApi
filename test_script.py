from script import ValuePredictor
    
list_for_testing_ValuePredictor_overload = ['50', 6, 10, 1, 12, 1, 4, 1, '14084', '0', '50', 38,11]
list_for_testing_ValuePredictor_too_short = ['50', 6, 10, 1, 12, 1, 4, 1, '14084', '0', '50']
list_for_testing_ValuePredictor_0 = ['50', 2, 14, 0, 4, 0, 2, 1, '2174', '0', '40', 38]
list_for_testing_ValuePredictor_1 = ['50', 6, 10, 1, 12, 1, 4, 1, '14084', '0', '50', 38]

def test_ValuePredictor_empty_input():
    assert ValuePredictor([]) == -1
    
def test_ValuePredictor_overload():
    assert ValuePredictor(list_for_testing_ValuePredictor_overload) == -1

def test_ValuePredictor_too_shor_list():
    assert ValuePredictor(list_for_testing_ValuePredictor_too_short) == -1

def test_ValuePredictor_expect_0():
    assert ValuePredictor(list_for_testing_ValuePredictor_0) == 0
    
def test_ValuePredictor_expect_1():
    assert ValuePredictor(list_for_testing_ValuePredictor_1) == 1
    