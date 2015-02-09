from nose.tools import *
from square import square


def test_dir():
    s=square(4,4)
    assert_equal(dir(s),['__init__', 'addentry', 'tabletotext'])

def test_datastructure():
    s=square(4,4)
    assert_equal(s.box,[[0, 0, 0, 0], [0, 0, 0, 0], [0, 0, 0, 0], [0, 0, 0, 0]])
    

    