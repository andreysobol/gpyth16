b0_montgomery = 16772280239760917788496391897731603718812008455956943122563801666366297604776
gminus1 = pow(2, 256 * (q-2), FieldQ.modulo)
b0 = (gminus1 * b0_montgomery) % q
b1 = 568440292453150825972223760836185707764922522371208948902804025364325400423

from field import FieldQ12, FieldQ2, FieldQ

class EllipticCurve:

    def __init__(self, x_coord, y_coord) -> None:
        self.x_coord = x_coord
        self.y_coord = y_coord

class EllipticCurveG1(EllipticCurve):

    @classmethod
    def generator(cls):
        gen = EllipticCurveG1(
            
        )

        return gen