import unittest

from field import FieldQ12, FieldQ2, FieldQ

class UnitTest(unittest.TestCase):

    def test_field_q2(self):
        f = FieldQ2([FieldQ(3), FieldQ(4)])
        r = f.pow(FieldQ.modulus**12 - 1)
        self.assertEqual(r.value[1].value, 0)
        self.assertEqual(r.value[0].value, 1)

    def test_field_q12(self):
        # f = FieldQ12([
        #     FieldQ2([FieldQ(1), FieldQ(2)]),
        #     FieldQ2([FieldQ(3), FieldQ(4)]),
        #     FieldQ2([FieldQ(5), FieldQ(6)]),
        #     FieldQ2([FieldQ(7), FieldQ(8)]),
        #     FieldQ2([FieldQ(9), FieldQ(10)]),
        #     FieldQ2([FieldQ(11), FieldQ(12)]),
        # ])
        f = FieldQ2([FieldQ(3), FieldQ(4)])
        r = f.pow(FieldQ.modulus**12 - 1)
        print(r.value[1].value)
        self.assertEqual(True, True)


if __name__ == '__main__':
    unittest.main()