from abc import ABC, abstractmethod


class AbstractCloth(ABC):
    @abstractmethod
    def show_name(self):
        pass


class Coat(AbstractCloth):
    V: int

    def __init__(self, V):
        self.V = V

    def show_name(self):
        print(f"Кол-во ткани равно:{self.V / 6.5 + 0.5}")


class Suit(AbstractCloth):
    H: int

    def __init__(self, H):
        self.H = H

    def show_name(self):
        print(f"Кол-во ткани равно:{2 * self.H + 0.3}")


a = Coat(5)
b = Suit(2)
a.show_name()
b.show_name()
