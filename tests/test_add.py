import unittest

from core.add import add


class Test(unittest.TestCase):
    def test_add(self):
        res = add(1, 2)
        self.assertEqual(res, 3)
