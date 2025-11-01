import pytest
from calculator import Calculator

class TestCalculator:
    def test_symbols(self):
        with pytest.raises(ValueError):
            Calculator("z","!")

    def test_no_symbol(self):
        with pytest.raises(TypeError):
            Calculator(3, None)

    def test_add(self):
        calc = Calculator(3,4)
        assert calc.add() == 7
        calc2 = Calculator(3, -4)
        assert calc2.add() == -1
        calc3 = Calculator(-3, -4)
        assert calc3.add() == -7
        calc4 = Calculator(0.3, 0.4)
        assert calc4.add() == 0.7
    def test_sub(self):
        calc = Calculator(3,4)
        assert calc.sub() == -1
        calc2 = Calculator(3, -4)
        assert calc2.sub() == 7
        calc3 = Calculator(-3, -4)
        assert calc3.sub() == 1
        calc4 = Calculator(0.3, 0.4)
        assert calc4.sub() == pytest.approx(-0.1)
    def test_mul(self):
        calc = Calculator(3,4)
        assert calc.mul() == 12
        calc2 = Calculator(3, -4)
        assert calc2.mul() == -12
        calc3 = Calculator(-3, -4)
        assert calc3.mul() == 12
        calc4 = Calculator(0.3, 0.4)
        assert calc4.mul() == pytest.approx(0.12)
    def test_div(self):
        calc = Calculator(3,4)
        assert calc.div()== 0.75
        calc2 = Calculator(3, -4)
        assert calc2.div() == -0.75
        calc3 = Calculator(-3, -4)
        assert calc3.div() == pytest.approx(0.75)
        calc4 = Calculator(0.3, 0.4)
        assert calc4.div() == pytest.approx(0.75)
    def test_div_by_zero(self):
        calc = Calculator(3, 0)
        with pytest.raises(ValueError, match = "Nie możemy dzielić przez 0"):
            calc.div()








