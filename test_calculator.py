import subprocess
import sys

from calculator import add, main, parse_number


def test_add_integers():
    assert add(2, 3) == 5


def test_add_negative_numbers():
    assert add(-4, 1) == -3


def test_add_decimals():
    assert add(0.1, 0.2) == 0.30000000000000004


def test_parse_number():
    assert parse_number("7") == 7
    assert parse_number("2.5") == 2.5


def test_main_with_arguments():
    assert main(["5", "7"]) == 12


def test_run_from_command_line():
    result = subprocess.run(
        [sys.executable, "calculator.py", "5", "7"],
        capture_output=True,
        text=True,
    )
    assert result.returncode == 0
    assert "5 + 7 = 12" in result.stdout
