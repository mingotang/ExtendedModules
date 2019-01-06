# -*- encoding: UTF-8 -*-
# ---------------------------------import------------------------------------
import os

from collections import Mapping, Sized

from extended.Interface import AbstractPersistObject as APO


class BasePersistDict(Mapping, Sized):
    __postfix__ = None

    def __init__(self, path: str):
        Mapping.__init__(self)
        Sized.__init__(self)

        os.makedirs(path, exist_ok=True)
        self.__path__ = path

    def __getitem__(self, key: str):
        raise NotImplementedError

    def __setitem__(self, key: str, value):
        raise NotImplementedError

    def __check_postfix__(self, key: str):
        if '.' in key:
            if key.split('.')[-1] == self.__postfix__:
                return key
            else:
                return '{}.{}'.format(key, self.__postfix__)
        else:
            return '{}.{}'.format(key, self.__postfix__)

    def __sub_file__(self, file_name: str):
        return os.path.join(self.__path__, file_name)

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
            elif not tag.endswith(self.__postfix__):
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


class TextDict(BasePersistDict):
    __postfix__ = 'txt'

    def __init__(self, path: str, encoding: str = 'utf-8'):
        BasePersistDict.__init__(self, path)

        self.__encoding__ = encoding

    def __setitem__(self, key: str, value):
        full_key = self.__check_postfix__(key)
        with open(self.__sub_file__(full_key), mode='w', encoding=self.__encoding__) as f:
            f.write(value)

    def __getitem__(self, key: str):
        full_key = self.__check_postfix__(key)
        try:
            with open(self.__sub_file__(full_key), mode='r', encoding=self.__encoding__) as f:
                return f.read()
        except FileNotFoundError:
            raise KeyError('no such key as {}'.format(key))


class TextObjDict(TextDict):

    def __init__(self, path: str, obj_type: type, encoding: str = 'utf-8'):
        BasePersistDict.__init__(self, path)

        assert hasattr(obj_type, APO.__get_state_attribute__)
        assert hasattr(obj_type, APO.__set_state_attribute__)
        self.__obj_type__ = obj_type
        self.__encoding__ = encoding

    def __setitem__(self, key: str, value):
        full_key = self.__check_postfix__(key)
        with open(self.__sub_file__(full_key), mode='w', encoding=self.__encoding__) as f:
            f.write(getattr(value, APO.__get_state_attribute__))

    def __getitem__(self, key: str):
        full_key = self.__check_postfix__(key)
        try:
            with open(self.__sub_file__(full_key), mode='r', encoding=self.__encoding__) as f:
                return getattr(self.__obj_type__, APO.__set_state_attribute__).__call__(f.read())
        except FileNotFoundError:
            raise KeyError('no such key as {}'.format(key))
