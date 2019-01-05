# -*- encoding: UTF-8 -*-
# ---------------------------------import------------------------------------
import os

from collections import Mapping, Sized


class BasePersistDict(Mapping, Sized):
    __postfix__ = None

    def __init__(self, path: str):
        Mapping.__init__(self)
        Sized.__init__(self)

        self.__path__ = path

    def __getitem__(self, key: str):
        raise NotImplementedError

    def __setitem__(self, key: str, value):
        raise NotImplementedError

    def get(self, k: str, default=None):
        try:
            return self.__getitem__(k)
        except KeyError or FileNotFoundError:
            if default is None:
                raise KeyError
            else:
                return default

    def __keys__(self):
        for tag in os.listdir(self.__path__):
            if tag.startswith('.'):
                continue
            elif tag.endswith(self.__postfix__):
                continue
            else:
                yield '.'.join(tag.split('.')[:-1])

    def __len__(self):
        return len(list(self.__keys__()))

    def to_dict(self):
        new_d = dict()
        for k, v in self.items():
            new_d[k] = v
        return new_d

    def keys(self):
        for key in self.__keys__():
            yield key

    def values(self):
        for key in self.__keys__():
            yield self.__getitem__(key)

    def items(self):
        for key in self.__keys__():
            yield key, self.__getitem__(key)

    def update(self, mapping):
        assert hasattr(mapping, 'items')
        for k, v in mapping.items():
            self.__setitem__(k, v)
