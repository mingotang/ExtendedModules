#!/usr/bin/env python

# The version as used in the setup.py and the docs conf.py
__version__ = "0.0.1"

# include Package Modules
from .EventEngine import EventEngine, EventObject
from .Exceptions import (
    ParamMissingError, ParamNoContentError, ParamOutOfRangeError, ParamTypeError,
    ValueTypeError,
)
from .Interface import AbstractPersistObject

from .data.CountingDict import CountingDict
from .data.ObjectDict import ObjectDict

from .persist.ShelveWrapper import ShelveWrapper

# include Package methods
from .Logger import get_logger

# ---- [depreciated] --- #
DataDict = ObjectDict
