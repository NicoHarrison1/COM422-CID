"""
Imports modules and Classes for testing
Sets up fixtures used in tests
"""
import pytest
from car import Car
from motorcycle import Motorcycle
from lorry import Lorry


@pytest.fixture(name='test_car', scope='function', autouse=True)
def setup_car():
    """
    Creates a test car for tests
    """
    test_car = Car("ABC", 300)
    return test_car


@pytest.fixture(name='test_motorbike', scope='function', autouse=True)
def setup_motorbike():
    """
    Creates a test Motorcycle for tests
    """
    test_motorbike = Motorcycle("xyz", 100)
    return test_motorbike

@pytest.fixture(name='test_lorry', scope='function', autouse=True)
def setup_lorry():
    """
    Creates a test Lorry for tests
    """
    test_lorry = Lorry("abc 123", 500)
    return test_lorry
