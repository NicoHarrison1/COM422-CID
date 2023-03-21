import pytest
from vehicle import Vehicle
from car import Car

def test_create_car():
    car1 = Car("ABCD", 300)
    assert car1.registration == "ABCD"






