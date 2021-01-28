class F:
    pass


class A(F):
    pass


class B(F):
    pass


class Y(A, B):
    pass


class X(A, B):
    pass


print(Y.__mro__)
print(X.__mro__)
