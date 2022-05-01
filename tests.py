import unittest

from field import FieldQ12, FieldQ2, FieldQ, FieldR
from curve import EllipticCurveG1, EllipticCurveG2


class UnitTest(unittest.TestCase):

    def test_field_q2(self):
        f = FieldQ2([FieldQ(3), FieldQ(4)])
        r = f.pow(FieldQ.modulus**12 - 1)
        self.assertEqual(r.value[1].value, 0)
        self.assertEqual(r.value[0].value, 1)

    def test_field_q12_mul(self):
        f1 = FieldQ12([
            FieldQ2([FieldQ(1), FieldQ(0)]),
            FieldQ2([FieldQ(0), FieldQ(0)]),
            FieldQ2([FieldQ(0), FieldQ(0)]),
            FieldQ2([FieldQ(0), FieldQ(0)]),
            FieldQ2([FieldQ(0), FieldQ(0)]),
            FieldQ2([FieldQ(0), FieldQ(0)]),
        ])
        f2 = FieldQ12([
            FieldQ2([FieldQ(1), FieldQ(0)]),
            FieldQ2([FieldQ(0), FieldQ(0)]),
            FieldQ2([FieldQ(0), FieldQ(0)]),
            FieldQ2([FieldQ(0), FieldQ(0)]),
            FieldQ2([FieldQ(0), FieldQ(0)]),
            FieldQ2([FieldQ(0), FieldQ(0)]),
        ])
        r = FieldQ12.mul(f1, f2)

        self.assertEqual(r.value[0].value[1].value, 0)
        self.assertEqual(r.value[0].value[0].value, 1)
        for i in range(1,6):
            self.assertEqual(r.value[i].value[1].value, 0)
            self.assertEqual(r.value[i].value[0].value, 0)

    def test_field_q12_pow(self):
        f = FieldQ12([
            FieldQ2([FieldQ(1), FieldQ(2)]),
            FieldQ2([FieldQ(3), FieldQ(4)]),
            FieldQ2([FieldQ(5), FieldQ(6)]),
            FieldQ2([FieldQ(7), FieldQ(8)]),
            FieldQ2([FieldQ(9), FieldQ(10)]),
            FieldQ2([FieldQ(11), FieldQ(12)]),
        ])
        r = f.pow(FieldQ.modulus**12 - 1)

        self.assertEqual(r.value[0].value[1].value, 0)
        self.assertEqual(r.value[0].value[0].value, 1)
        for i in range(1,6):
            self.assertEqual(r.value[i].value[1].value, 0)
            self.assertEqual(r.value[i].value[0].value, 0)


class CurveTest(unittest.TestCase):

    def test_curve_g2(self):
        generator = EllipticCurveG2.generator()
        scalar = FieldR(FieldR.modules - 1)
        result = generator.mul_by_scalarr(scalar)
        self.assertEqual(result.x_coord.value[0].value, generator.x_coord.value[0].value)
        self.assertEqual(result.x_coord.value[1].value, generator.x_coord.value[1].value)

    def test_curve_g1(self):
        generator = EllipticCurveG1.generator()
        scalar = FieldR(FieldR.modules - 1)
        result = generator.mul_by_scalar(scalar)
        self.assertEqual(result.x_coord.value, 1)
        self.assertEqual(result.y_coord.value, FieldQ.modulus - 2)


if __name__ == '__main__':
    unittest.main()