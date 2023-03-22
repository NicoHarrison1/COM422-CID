import pytest


def test_car() -> None:
    """
    Test for car object
    """

    # arrange
    expected = True

    # act
    result = True

    # assert
    assert result == expected


@pytest.mark.skip(reason="Test in development new")
def test_new() -> None:
    '''

    '''

    # arrange
    expected = True

    # act
    result = False

    # assert
    assert result == expected
