from .base_test import BaseTest


class TestClass1(BaseTest):
    """
        Run this with the -s switch on pytest
        eg: pytest -s
    """

    def test_method_1(self):
        print("RUNNING METHOD 1-1")

    def test_method_2(self):
        print("RUNNING METHOD 1-2")
