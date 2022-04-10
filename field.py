import sys
sys.setrecursionlimit(5000)

class Field:

    def __init__(self, value) -> None:
        self.value = value

    def get_value(self) -> int:
        return self.value

madgic_u = 4965661367192848881

def get_q(u):
    q = 36*(u**4) + 36*(u**3) + 24*(u**2) + 6*u + 1
    return q

class FieldQ(Field):
    #modulus = 21888242871839275222246405745257275088696311157297823662689037894645226208583
    modulus = get_q(madgic_u)
    generator = 2

    @classmethod
    def add(cls, a, b):
        return cls((a.value + b.value) % cls.modulus)

    @classmethod
    def mul(cls, a, b):
        return cls((a.value * b.value) % cls.modulus)

def get_r(u):
    r = 36*(u**4) + 36*(u**3) + 18*(u**2) + 6*u + 1
    return r

class FieldR(Field):
    #modulus = 21888242871839275222246405745257275088548364400416034343698204186575808495617
    modules = get_r(madgic_u)
    generator = 7

def get_q(u):
    q = 36*(u**4) + 36*(u**3) + 24*(u**2) + 6*u + 1
    return q

class FieldQ2(Field):

    @classmethod
    def add(cls, a, b):
        return cls([FieldQ.add(FieldQ(els[0]), FieldQ(els[1])) for els in zip(a.value, b.value)])

    @classmethod
    def mul(cls, a, b):
        r0 = a.value[0] * b.value[0] - a.value[1] * b.value[1]
        r1 = a.value[0] * b.value[1] + a.value[1] * b.value[0]
        return cls((r0, r1))

class FieldQ12(Field):

    modules = [1, 0, 0, 0, 0, 0, FieldQ2([9, 1])]

    @classmethod
    def add(cls, a, b):
        return cls([FieldQ2.add(els[0], els[1]) for els in zip(a.value, b.value)])

    @classmethod
    def mul(cls, a, b):
        res = [FieldQ2([0, 0]) for i in range(11)]
        for i in range(6):
            for j in range(6):
                res[i+j] = FieldQ2.add(
                    res[i+j],
                    FieldQ2.mul(
                        a.value[i],
                        b.value[i],
                    )
                )

        for i in range(5):
            res[i] = FieldQ2.add(
                res[i],
                FieldQ2.mul(
                    FieldQ2([9, 1]),
                    res[i+6]
                )
            )

        return FieldQ12(res[0:6])

    def pow(self, power):
        curent = self
        res = FieldQ12([FieldQ2([e, 0]) for e in [1, 0, 0, 0, 0, 0]])

        while power > 0 :
            if power % 2 == 1 :
                res = FieldQ12.mul(res, curent)
                power -= 1
            else:
                curent = FieldQ12.mul(curent, curent)
                power //= 2

        return res