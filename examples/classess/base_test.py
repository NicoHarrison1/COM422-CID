class BaseTest:

    def setup_class(cls):
        # pylint: disable=no-self-argument,no-member
        print(
            f"\nsetting up CLASS {format(cls.__name__)}")

    def teardown_class(cls):
        # pylint: disable=no-self-argument,no-member
        print(
            f"tearing down CLASS {format(cls.__name__)}\n")

    def setup_method(self, method):
        print(
            f"\nsetting up METHOD {format(method.__name__)}")

    def teardown_method(self, method):
        print(
            f"\ntearing down METHOD {format(method.__name__)}")
