"""
Calculator do dodawania dwóch liczb, odejmowania, mnożenia, dzielenia
"""
class Calculator:
    """
    Klasa która przechowuje dwie liczby i wykonuje podstawowe operacje rachunkowe
    """
    def __init__(self, op1: float, op2: float):
        """
        :param op1:
        :param op2:
        """
        try:
            self._op1 = float(op1)
            self._op2 = float(op2)
        except ValueError as exc:
            raise ValueError("Argumenty op1 i op2 muszą być liczbami rzeczywistymi") from exc
        except TypeError as exc:
            raise TypeError("Trzeba podać dwie liczby") from exc
    def add(self):
        """
        Zwraca sumę _op1 i _op2

        """
        return self._op1 + self._op2
    def sub(self):
        """
        Zwraca różnicę _op1 i _op2

        """
        return self._op1 - self._op2
    def mul(self):
        """
        Zwraca mnożenie _op1 i _op2

        """
        return self._op1 * self._op2
    def div(self):
        """
        Zwraca dzielenie _op1 i _op2

        """
        if self._op2 == 0:
            raise ValueError("Nie możemy dzielić przez 0")
        return self._op1 / self._op2
