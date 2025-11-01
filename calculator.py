class Calculator:
        def __init__(self, op1: float, op2: float):
            try:
                self._op1 = float(op1)
                self._op2 = float(op2)
            except ValueError:
                raise ValueError("Argumenty op1 i op2 muszą być liczbami rzeczywistymi")
            except TypeError:
                raise TypeError("Trzeba podać dwie liczby")
        def add(self):
            return self._op1 + self._op2
        def sub(self):
            return self._op1 - self._op2
        def mul(self):
            return self._op1 * self._op2
        def div(self):
            if self._op2 == 0:
                raise ValueError("Nie możemy dzielić przez 0")
            return self._op1 / self._op2