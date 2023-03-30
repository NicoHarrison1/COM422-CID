"""
Example of setup and tear down
"""
def setup_module(module):
    """
    Run this with 
    """
    print(
        f'\nSetting up MODULE {format(module.__name__)}')


def teardown_module(module):
    print(f'\nTearing down MODULE {format(module.__name__)}')



def test_a_function():
    print('Running test function')
