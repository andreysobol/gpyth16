b0_montgomery = 16772280239760917788496391897731603718812008455956943122563801666366297604776
gminus1 = pow(2, 256 * (q-2), FieldQ.modulo)
b0 = (gminus1 * b0_montgomery) % q
b1 = 568440292453150825972223760836185707764922522371208948902804025364325400423

x0 = 10857046999023057135944570762232829481370756359578518086990519993285655852781
x1 = 11559732032986387107991004021392285783925812861821192530917403151452391805634
y0 = 8495653923123431417604973247489272438418190587263600148770280649306958101930
y1 = 4082367875863433681332203403145435568316851327593401208105741076214120093531

from field import FieldQ12, FieldQ2, FieldQ

class EllipticCurve:

    def __init__(self, x_coord, y_coord) -> None:
        self.x_coord = x_coord
        self.y_coord = y_coord

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

class EllipticCurveG1(EllipticCurve):

    @classmethod
    def generator(cls):
        gen = EllipticCurveG1(
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
