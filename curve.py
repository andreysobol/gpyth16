import copy

from field import FieldQ12, FieldQ2, FieldQ

b0_montgomery = 16772280239760917788496391897731603718812008455956943122563801666366297604776
q = FieldQ.modulus
gminus1 = pow(2, 256 * (q-2), q)
b0 = (gminus1 * b0_montgomery) % q
b1 = 568440292453150825972223760836185707764922522371208948902804025364325400423

x0 = 10857046999023057135944570762232829481370756359578518086990519993285655852781
x1 = 11559732032986387107991004021392285783925812861821192530917403151452391805634
y0 = 8495653923123431417604973247489272438418190587263600148770280649306958101930
y1 = 4082367875863433681332203403145435568316851327593401208105741076214120093531


class EllipticCurve:

    def __init__(*args):
        if len(args) == 1:
            self = args[0]
            self.is_inf = True
            return
        else:
            self = args[0]
            self.x_coord = args[1]
            self.y_coord = args[2]
            self.is_inf = False
            return

class EllipticCurveG1(EllipticCurve):

    @classmethod
    def generator(cls):
        gen = EllipticCurveG1(
            FieldQ(1),
            FieldQ(2)
        )
        return gen

    @classmethod
    def b_coeff(cls):
        return FieldQ(3)

    def mul_by_scalar(self, scalar):
        scalar_value = scalar.value

        current = self
        res = EllipticCurveG1()

        while scalar_value > 0:
            if scalar_value % 2 == 1:
                res = res.add(current)
                scalar_value -= 1
            else:
                current = current.add(current)
                scalar_value //= 2

        return res

    def add(self, other):

        if self.is_inf and other.is_inf:
            return EllipticCurveG1()

        if self.is_inf and (not other.is_inf):
            return copy.copy(other)

        if (not self.is_inf) and other.is_inf:
            return copy.copy(self)

        if (
            (self.x_coord.value == other.x_coord.value) and
            (self.y_coord.value == -other.y_coord.value)
        ):
            return EllipticCurveG1()

        if (
            (self.x_coord.value == other.x_coord.value) and
            (self.y_coord.value == other.y_coord.value)
        ):
            s = FieldQ.div(
                FieldQ.mul(
                    FieldQ.mul(
                        FieldQ(3),
                        self.x_coord
                    ),

                    self.x_coord
                ),
                FieldQ.mul(self.y_coord, FieldQ(2))
            )
        else:
            s = FieldQ.div(
                FieldQ.sub(self.y_coord, other.y_coord),
                FieldQ.sub(self.x_coord, other.x_coord)
            )

        s_2 = FieldQ.mul(s, s)

        result_x_coord = FieldQ.sub(
            s_2,
            FieldQ.add(self.x_coord, other.x_coord)
        )

        result_y_coord = FieldQ.sub(
            FieldQ.mul(
                FieldQ.sub(self.x_coord, result_x_coord),
                s
            ),
            self.y_coord,
        )

        return EllipticCurveG1(result_x_coord, result_y_coord)


class EllipticCurveG2(EllipticCurve):

    @classmethod
    def generator(cls):
        gen = EllipticCurveG2(
            FieldQ2([
                FieldQ(x0),
                FieldQ(x1)
            ]),
            FieldQ2([
                FieldQ(y0),
                FieldQ(y1)
            ])
        )
        return gen

    @classmethod
    def b_coeff(cls):
        return FieldQ2([
                    FieldQ(b0),
                    FieldQ(b1)
                ])

    def mul_by_scalarr(self, scalar):
        scalar_value = scalar.value

        current = self
        res = EllipticCurveG2()

        while scalar_value > 0:
            if scalar_value % 2 == 1:
                res = res.add(current)
                scalar_value -= 1
            else:
                current = current.add(current)
                scalar_value //= 2

        return res

    def add(self, other):

        if self.is_inf and other.is_inf:
            return EllipticCurveG2()

        if self.is_inf and (not other.is_inf):
            return copy.copy(other)

        if (not self.is_inf) and other.is_inf:
            return copy.copy(self)

        if (
            (self.x_coord.value[0].value == other.x_coord.value[0].value) and
            (self.x_coord.value[1].value == other.x_coord.value[1].value) and
            (self.y_coord.value[0].value == -other.y_coord.value[0].value) and
            (self.y_coord.value[1].value == -other.y_coord.value[1].value)
        ):
            return EllipticCurveG2()

        if (
            (self.x_coord.value[0].value == other.x_coord.value[0].value) and
            (self.x_coord.value[1].value == other.x_coord.value[1].value) and
            (self.y_coord.value[0].value == other.y_coord.value[0].value) and
            (self.y_coord.value[1].value == other.y_coord.value[1].value)
        ):
            s = FieldQ2.div(
                FieldQ2.mul(
                    FieldQ2.mul(
                        FieldQ2([FieldQ(3), FieldQ(0)]),
                        self.x_coord
                    ),

                    self.x_coord
                ),
                FieldQ2.mul(self.y_coord, FieldQ2([FieldQ(2), FieldQ(0)]))
            )
        else:
            s = FieldQ2.div(
                FieldQ2.sub(self.y_coord, other.y_coord),
                FieldQ2.sub(self.x_coord, other.x_coord)
            )

        s_2 = FieldQ2.mul(s, s)

        result_x_coord = FieldQ2.sub(
            s_2,
            FieldQ2.add(self.x_coord, other.x_coord)
        )

        result_y_coord = FieldQ2.sub(
            FieldQ2.mul(
                FieldQ2.sub(self.x_coord, result_x_coord),
                s
            ),
            self.y_coord,
        )

        return EllipticCurveG2(result_x_coord, result_y_coord)

