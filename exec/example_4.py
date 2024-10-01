# Python program invoking a
# method using super()

from abc import ABC


class R(ABC):

    def rk(self):
        print("Abstract Base Class")


class K(R):

    def rk(self):
        super().rk()
        print("subclass")


# Driver code
r = K()
r.rk()
