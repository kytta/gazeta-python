import pytest

from gazeta.printer import Mode, Printer


def test_default_init():
    """Tests the initialization of a Printer with defaults."""
    default_printer = Printer()

    assert default_printer.mode == Mode.normal
    assert default_printer.colored


@pytest.mark.parametrize('color', [True, False])
@pytest.mark.parametrize('mode', ['verbose', 'normal', 'quiet'])
def test_init_with_params(color, mode):
    """Tests the initialization of a Printer with custom parameters."""
    printer = Printer(Mode[mode], color)

    assert printer.mode == Mode[mode]
    assert printer.colored == color
