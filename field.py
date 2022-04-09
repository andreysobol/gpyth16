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

class FieldQ12(Field):
    pass

    @classmethod
    def add(cls, a, b):
        return cls([FieldQ.add(els[0], els[1]) for els in zip(a.value, b.value)])