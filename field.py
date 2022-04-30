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
    def sub(cls, a, b):
        return cls((a.value - b.value) % cls.modulus)

    def pow(self, power):
        current = self
        res = FieldQ(1)

        while power > 0 :
            if power % 2 == 1 :
                res = FieldQ.mul(res, current)
                power -= 1
            else:
                current = FieldQ.mul(current, current)
                power //= 2

        return res

    @classmethod
    def mul(cls, a, b):
        return cls((a.value * b.value) % cls.modulus)

    def inverce(self):
        return self.pow(FieldQ.modulus - 2)

    @classmethod
    def div(cls, a, b):
        b_inv = b.inverce()
        return FieldQ.mul(a, b_inv)

    def __repr__(self):
        return "FieldQ(" + str(self.value) + ")"

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
        return cls([FieldQ.add(els[0], els[1]) for els in zip(a.value, b.value)])

    @classmethod
    def sub(cls, a, b):
        return cls([FieldQ.sub(FieldQ(els[0]), FieldQ(els[1])) for els in zip(a.value, b.value)])

    @classmethod
    def mul(cls, a, b):
        r0 = FieldQ.sub(FieldQ.mul(a.value[0], b.value[0]), FieldQ.mul(a.value[1], b.value[1]))
        r1 = FieldQ.add(FieldQ.mul(a.value[0], b.value[1]), FieldQ.mul(a.value[1], b.value[0]))
        return cls([r0, r1])

    def pow(self, power):
        current = self
        res = FieldQ2([
            FieldQ(1),
            FieldQ(0)
        ])

        while power > 0 :
            if power % 2 == 1 :
                res = FieldQ2.mul(res, current)
                power -= 1
            else:
                current = FieldQ2.mul(current, current)
                power //= 2

        return res

    def inverce(self):
        return self.pow(FieldQ.modulus - 2)

    def __repr__(self):
        return "FieldQ2(" + str(self.value) + ")"

class FieldQ12(Field):

    modules = [FieldQ2([1, 0]),
               FieldQ2([0, 0]),
               FieldQ2([0, 0]),
               FieldQ2([0, 0]),
               FieldQ2([0, 0]),
               FieldQ2([0, 0]),
               FieldQ2([9, 1])]

    @classmethod
    def add(cls, a, b):
        return cls([FieldQ2.add(els[0], els[1]) for els in zip(a.value, b.value)])

    @classmethod
    def sub(cls, a, b):
        return cls([FieldQ2.sub(els[0], els[1]) for els in zip(a.value, b.value)])

    @classmethod
    def mul(cls, a, b):
        res = [FieldQ2([FieldQ(0), FieldQ(0)]) for i in range(11)]
        for i in range(6):
            for j in range(6):
                res[i+j] = FieldQ2.add(
                    res[i+j],
                    FieldQ2.mul(
                        a.value[i],
                        b.value[j],
                    )
                )

        for i in range(5):
            res[i] = FieldQ2.add(
                res[i],
                FieldQ2.mul(
                    FieldQ2([FieldQ(9), FieldQ(1)]),
                    res[i+6]
                )
            )

        return FieldQ12(res[0:6])

    def pow(self, power):
        current = self
        res = FieldQ12([FieldQ2([
            FieldQ(e),
            FieldQ(0)
        ]) for e in [1, 0, 0, 0, 0, 0]])

        while power > 0 :
            if power % 2 == 1 :
                res = FieldQ12.mul(res, current)
                power -= 1
            else:
                current = FieldQ12.mul(current, current)
                power //= 2

        return res

    def __repr__(self):
        return "FieldQ12(" + str(self.value) + ")"