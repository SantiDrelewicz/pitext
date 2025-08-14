from .text import process

import sys
del sys.modules[__name__ + ".text"]
del sys.modules[__name__ + ".token"]

__all__ = ["process"]
