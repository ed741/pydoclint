
def _test_private_function() -> int:
    """test function

    Returns:
        bool: With incorrect argument
    """
    return 2

class TestClass:
    """
    Docstring for TestClass, this will still be checked if skip-checking-short-docstrings is False
    """

    def __init__(self) -> None:
        """This init will still be checked if skip-checking-short-docstrings is False"""

    def _private_method(self, i: int) -> bool:
        """Test method

        Args:
            i (bool): With incorrect argument type

        Returns:
            bool: Always returns False
        """
        return False
