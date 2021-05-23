import calculator

"""
Unit test for Calculator Library

"""

# python -m pytest -v --cov .

# .yaml file uses the serialization language called YAML designed to be pretty human readable

# Docker is like minimal container which contians all the resources which can be required to run the code
class TestCalculator:

    def test_addition(self):
        assert 4 == calculator.add(2, 2)

    def test_subtraction(self):
        assert 2 == calculator.subtract(4, 2)
