"""
Imports modules and Classes for testing
Sets up fixtures used in tests
"""
import pytest
from car import Car
from motorcycle import Motorcycle


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
    Creates a test car for tests
    """
    test_motorbike = Car("xyz", 100)
    return test_motorbike
