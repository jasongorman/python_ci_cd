import unittest

from src.dummy import Dummy


class DummyTest(unittest.TestCase):
    def test_something(self):
        dummy = Dummy()
        self.assertEqual(True, True)


if __name__ == '__main__':
    unittest.main()
