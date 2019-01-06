# -*- encoding: UTF-8 -*-
# ---------------------------------import------------------------------------


class AbstractPersistObject:
    __get_state_attribute__ = 'get_state'
    __set_state_attribute__ = 'set_state'

    def get_state(self):
        """return the content of the object -> str"""
        raise NotImplementedError

    @classmethod
    def set_state(cls, state: str):
        """return the new object -> obj"""
        raise NotImplementedError
