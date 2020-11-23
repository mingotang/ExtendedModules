# -*- encoding: UTF-8 -*-
# ---------------------------------import------------------------------------
import os


class FileDataBase(object):
    """文档型简易json数据库"""

    def __init__(self, db_path: str):
        self.__path__ = db_path

    def show_data_bases(self):
        # 搜寻文档目录
        db_list = list()
        for item_name in os.listdir(self.__path__):
            if os.path.isdir(os.path.join(self.__path__, item_name)) and os.path.exists(
                os.path.join(self.__path__, item_name, '__db_index__.json')
            ):
                db_list.append(os.path.join(self.__path__, item_name))
            else:
                pass
        return db_list


class BaseSector(object):

    def __init__(self, sector_path: str):
        self.__path__ = sector_path
