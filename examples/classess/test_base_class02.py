from .base_test import BaseTest

class TestClass2(BaseTest):
    """
        Run this with the -s switch on pytest
        eg: pytest -s
    """

    def test_method_1(self):
        print("RUNNING METHOD 2-1")

    def test_method_2(self):
        print("RUNNING METHOD 2-2")
