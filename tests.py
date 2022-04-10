import unittest

from field import FieldQ12, FieldQ2, FieldQ

class UnitTest(unittest.TestCase):

    def test_field_q12(self):
        f = FieldQ12([
            FieldQ2([1, 2]),
            FieldQ2([3, 4]),
            FieldQ2([5, 6]),
            FieldQ2([7, 8]),
            FieldQ2([9, 10]),
            FieldQ2([11, 12]),
        ])
        r = f.pow(FieldQ.modulus**12 - 1)
        print(r)
        self.assertEqual(True, True)


if __name__ == '__main__':
    unittest.main()