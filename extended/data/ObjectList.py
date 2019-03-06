# -*- encoding: UTF-8 -*-
# ---------------------------------import------------------------------------
from extended.Interface import AbstractDataStructure


class ObjectList(list, AbstractDataStructure):
    def __init__(self, *args, **kwargs):
        list.__init__(self, *args, **kwargs)

    def __repr__(self):
        content = '[\n'
        for value in self.__iter__():
            content += '\t{},\n'.format(value)
        content += ']'
        return content

    def copy(self):
        new_l = ObjectList()
        new_l.extend(self)
        return new_l

    def to_list(self):
        new_l = list()
        new_l.extend(self)
        return new_l

    def find_value_where(self, **kwargs):
        """
        find values by constrains -> ObjectDict
        :param kwargs:
        :return: DataList, list of stored value
        """
        target_list = ObjectList()
        for value in self.__iter__():
            all_check = True
            for c_key, c_value in kwargs.items():
                if getattr(value, c_key) != c_value:
                    all_check = False
                    break
            if all_check is True:
                target_list.append(value)
        return target_list

    def find_value(self, **kwargs):
        target_list = self.find_value_where(**kwargs)
        if len(target_list) == 1:
            return target_list[0]
        if len(target_list) == 0:
            raise ValueError('No value satisfy {}'.format(kwargs))
        else:
            raise RuntimeError('Unknown Error {}'.format(str(target_list)))

    def group_by_attr(self, attr_tag: str):
        """
        把内容对象按照 by_tag 属性分组，得到 { by_tag: {obj1, obj2, }} -> dict
        :param attr_tag: related attribute
        :return: dict( key: set())
        """
        grouped_dict = dict()

        for obj in self.__iter__():
            # obj = self.__getitem__(index)
            by_value = getattr(obj, attr_tag)

            if by_value is None:
                continue

            if not isinstance(by_value, str):
                by_value = str(by_value)

            if len(by_value) == 0:  # jump to next iteration if no content
                continue

            if by_value not in grouped_dict:
                grouped_dict[by_value] = ObjectList()

            grouped_dict[by_value].append(obj)

        return grouped_dict

    def group_attr_set_by(self, group_attr: str, by_attr: str):
        """
        建立属性之间映射的快速索引字典 -> dict( by_attr: set(group_attr, ))
        :param group_attr:
        :param by_attr:
        :return: dict( by_attr: set())
        """
        grouped_dict = dict()

        for obj in self.__iter__():
            key = getattr(obj, by_attr)
            if key not in grouped_dict:
                grouped_dict[key] = set()
            grouped_dict[key].add(getattr(obj, group_attr))

        return grouped_dict

    def collect_attr_set(self, attr_tag: str):
        """
        收集出现过的属性内容至一个集合 -> set
        :param attr_tag: str
        :return: set()
        """
        collected_set = set()

        for obj in self.__iter__():
            collected_set.add(getattr(obj, attr_tag))

        return collected_set

    def collect_attr_list(self, attr_tag: str):
        """ 收集出现过的属性内容至一个列表 -> list"""
        collected_list = list()

        for obj in self.__iter__():
            collected_list.append(getattr(obj, attr_tag))

        return collected_list
