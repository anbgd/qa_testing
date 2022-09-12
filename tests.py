import pytest

def test_reverse_str():
	assert 'Kitten'[::-1] == 'nettiK'

def test_size_tuple():
	assert (1, 2, 3, 4, 5, 6).__sizeof__() == 72

def test_two_str():
	try:
		assert 'aaa'-'a' 
	except TypeError:
		pass

def test_two_tuple():
	try:
		my_tuple = ('Apple','Banana')
		assert my_tuple[2] == 'Banana'
	except IndexError:
		pass

@pytest.mark.parametrize("test_input, expected_result", [('',0), ('2, 4',4), ('We\n are\n the champions', 22)])
def test_three_str(test_input, expected_result):
    assert len(test_input) == expected_result

@pytest.mark.parametrize("test_input,expected", [((1,1), 0), ((1,2,1,1,1,0,2), 2), (('2',), 0)])
def test_three_tuple(test_input, expected):
    assert test_input.count(2) == expected
