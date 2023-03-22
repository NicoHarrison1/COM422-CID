
def test_should_have_regisistration(test_car):
    """
    Should have registration number
    """
    # arrange
    expected = "ABC"

    # act

    # assert
    assert test_car.registration == expected

def test_shoud_have_weight(test_car) -> None:
    '''
    Car should have weight
    '''

    # arrange
    expected = 300
    
    # act
    
    # assert
    assert test_car.weight == expected
    