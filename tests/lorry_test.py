
def test_should_have_regisistration(test_lorry):
    """
    Should have registration number
    """
    # arrange
    expected = "abc 123"

    # act

    # assert
    assert test_lorry.registration == expected

def test_shoud_have_weight(test_lorry) -> None:
    '''
    Car should have weight
    '''

    # arrange
    expected = 500
    
    # act
    
    # assert
    assert test_lorry.weight == expected
    