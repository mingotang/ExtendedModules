# -*- encoding: UTF-8 -*-
# ---------------------------------import------------------------------------
import warnings


def depreciated(new_name: str):
    def __depreciated__(func):
        def wrapper(*args, **kwargs):
            warnings.warn(
                """
                method {} is depreciated and will be removed in the future,
                please use {} instead.
                """.format(getattr(func, '__name__', str(func)), new_name))
            func(*args, **kwargs)
        return wrapper
    return __depreciated__
