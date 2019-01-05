# -*- encoding: UTF-8 -*-
# ---------------------------------import------------------------------------


class AbstractPersistObject:

    def get_state(self):
        """return the content of the object -> str"""
        raise NotImplementedError

    @classmethod
    def set_state(cls):
        """return the new object -> obj"""
        raise NotImplementedError
