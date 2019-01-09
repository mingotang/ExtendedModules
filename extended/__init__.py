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

# include folder Package Modules
from .data.CountingDict import CountingDict
from .data.ObjectDict import ObjectDict

from .persist.Dict import TextDict, TextObjDict

from .wrapper.Shelve import ShelveWrapper
from .wrapper.Sqlite import SqliteWrapper

# include Package methods
from .Decoration import depreciated_method
from .Logger import get_logger
from .Path import Path

# ---- [depreciated] --- #
DataDict = ObjectDict