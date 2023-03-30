import pytest
from src.classess.demo import Demo


@pytest.fixture(name="single_odd",scope="function")
def single_odd_number():
    """
    Sets up a fixture for an odd number
    """
    new_demo_class = Demo()
    result = new_demo_class.is_odd_number(3)
    yield result

@pytest.fixture(name="single_even",scope="function")
def single_even_number():
    """
    Sets up a fixture for an even number
    """
    new_demo_class = Demo()
    result = new_demo_class.is_odd_number(2)
    yield result

@pytest.fixture(name="multi_example_class", scope="function",
    params=[
        ("2 is Even",2),("3 is Odd",3),("4 is Even",4),("5 is Odd",5)
        ],
    ids=[
        "2-Even","3-Odd","4-Even","5-Odd"
        ]
    )
def multi_example_class(request):
    """
    Sets up a mutli fixture and passes back just values
    """
    expected_value = request.param[0]
    number = request.param[1]
    another_class = Demo()
    message = another_class.is_odd_number(number)
    results = (expected_value, message)
    yield results

@pytest.fixture(name="multi_example_value", scope="function",
    params=[
        ("2 is Even",2),("3 is Odd",3),("4 is Even",4),("5 is Odd",5)
        ],
    ids=[
        "2-Even","3-Odd","4-Even","5-Odd"
        ]
    )
def multi_example_value(request):
    """
    Sets up a mutli fixture and instaniates a new class each time
    """
    return request.param
