from enum import Enum


class Mode(Enum):
    """Output mode of the library.

    This enum defines three output types that gazeta supports:

    - **verbose:** everything gets output to the console.
    - **normal:** only warnings and errors get output to the console
    - **quiet:** nothing gets output to the console
    """

    verbose = 0
    normal = 30
    quiet = 100


class Printer(object):
    """Printer class, which is responsible for the console output.

    This class contains the actual methods that output messages to the console.
    gazeta also exports a "default" instance of Printer.

    Parameters
    ----------
    mode : Mode, optional
        defines the verbosity level of output, by default Mode.normal
    colored : bool, optional
        whether to color the messages, by default True
    """

    def __init__(
        self,
        mode: Mode = Mode.normal,
        colored: bool = True,
    ) -> None:
        """Creates an instance of Printer."""
        self.mode = mode
        self.colored = colored
