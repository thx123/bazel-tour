import pytest

from unittest.mock import patch
from py3.hello_world import hello

# Test for the correct "Hello, World!" output
@patch('builtins.print')
def test_positive(mock_print):
    hello()
    mock_print.assert_called_once_with("\nHello, World!\n")

# Test for an incorrect output (for demonstration purposes)
@pytest.mark.skip(reason="meant-to-fail test")
@patch('builtins.print')
def test_negative(mock_print):
    hello()
    mock_print.assert_called_once_with("\nHola, Mundo!\n")

if __name__ == "__main__":
    raise SystemExit(pytest.main([__file__, "-vvv"]))
