def test_should_have_regisistration(test_motorbike):
    """

    Should have registration number
    """
    # arrange

    expected = "xyz"

    # act

    # assert
    assert test_motorbike.registration == expected


def test_shoud_have_weight(test_motorbike) -> None:
    '''

    Car should have weight
    '''

    # arrange

    expected = 100
    
    # act
    
    # assert

    assert test_motorbike.weight == expected
    