import unittest


class TestNothing(unittest.TestCase):
    def test_nothing_1(self):
        pass

    def test_nothing_2(self):
        raise RuntimeError("This should be committed on 'push' branch.")

    def test_nothing_3(self):
        pass
