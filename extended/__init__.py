#!/usr/bin/env python

# The version as used in the setup.py and the docs conf.py
__version__ = "0.0.1"

# include Package Modules
from .CountingDict import CountingDict
from .DataDict import DataDict
from .EventEngine import EventEngine, EventObject
from .Exceptions import (
    ParamMissingError, ParamNoContentError, ParamOutOfRangeError, ParamTypeError,
    ValueTypeError,
)
from .Persist import Pdict, Plist, Pset, PqueueFIFO, PqueueLIFO
from .ShelveDict import ShelveDict

# include Package methods
from .Logger import get_logger
