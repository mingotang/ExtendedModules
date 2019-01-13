# -*- encoding: UTF-8 -*-
# ---------------------------------import------------------------------------


class CountingDict(dict):
    def __init__(self):
        dict.__init__(self)

    def __mul__(self, other):
        if isinstance(other, dict):
            result = 0
            for self_element in self.keys():
                if self_element in other:
                    result += self.__getitem__(self_element) * other[self_element]
            return result
        else:
            raise TypeError()

    @classmethod
    def init_from(cls, obj):
        from collections.abc import Iterable
        assert isinstance(obj, Iterable)
        new_cd = cls()
        for item in obj:
            new_cd.count(item)
        return new_cd

    def set(self, element, value):
        self.__setitem__(element, value)
        return self

    def count(self, element, step=1):
        try:
            self.__setitem__(element, self.__getitem__(element) + step)
        except KeyError:
            self.__setitem__(element, step)

    def sort(self, inverse=False):
        """ 按照值从小到大排序 """
        stored_list = sorted(self.keys(), key=lambda x: self.__getitem__(x), reverse=inverse)
        return stored_list
        # stored_list = list(self.keys())
        # for index_x in range(len(stored_list)):
        #     for index_y in range(index_x + 1, len(stored_list)):
        #         if self[stored_list[index_x]] > self[stored_list[index_y]]:
        #             stored_list[index_x], stored_list[index_y] = stored_list[index_y], stored_list[index_x]
        # if inverse is True:
        #     stored_list.reverse()
        #     return stored_list
        # else:
        #     return stored_list

    def weights(self, tag_or_list=None):
        """根据 tag_or_list 的标签收集权重信息"""
        from collections import Iterable
        total_num = 0
        if isinstance(tag_or_list, Iterable):
            for tag in tag_or_list:
                total_num += self.__getitem__(tag)
        elif isinstance(tag_or_list, type(None)):
            for tag in self.keys():
                total_num += self.__getitem__(tag)
        else:
            raise TypeError()
        return total_num

    def trim(self, lower_limit=None, higher_limit=None):
        """修剪值不符合要求的标签"""
        if lower_limit is not None:
            for tag in list(self.keys()):
                if self.__getitem__(tag) < lower_limit:
                    self.__delitem__(tag)

        if higher_limit is not None:
            for tag in list(self.keys()):
                if self.__getitem__(tag) > higher_limit:
                    self.__delitem__(tag)

        return self

    @property
    def sum(self):
        result = 0
        for value in self.values():
            result += value
        return result
