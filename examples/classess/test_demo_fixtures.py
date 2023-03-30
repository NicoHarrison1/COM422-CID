from src.classess.demo import Demo

class TestDemoFixtures:

    def test_should_return_odd(self,single_odd) -> None:
        #  arrange
        expected = "3 is Odd"

        #  act
        result = single_odd
        # assert
             
        assert result == expected

    def test_should_return_even(self,single_even) -> None:
        #  arrange
        expected = "2 is Even"

        #  act
        result = single_even
        # assert
             
        assert result == expected
    
    def test_should_return_multi_from_class(self,multi_example_class) -> None:
        #  arrange
        expected = multi_example_class[0]

        #  act
        result = multi_example_class[1]
        # assert
             
        assert result == expected

    def test_should_return_multi_from_value(self,multi_example_value) -> None:
        #  arrange
        expected = multi_example_value[0]
        number = multi_example_value[1]
        another_demo = Demo()
        #  act
        result = another_demo.is_odd_number(number)
        # assert
             
        assert result == expected
