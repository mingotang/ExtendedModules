# -*- encoding: UTF-8 -*-
import os
import shutil


class FolderPath(object):
    """文件夹路径对象"""
    def __init__(self, abs_path: str):
        if os.path.exists(abs_path):
            assert os.path.isfile(abs_path) is False, 'abs_path {} is a file instead of a folder'.format(abs_path)
            self.__path__ = abs_path
        else:
            RuntimeError('path {} not exists.'.format(abs_path))

    @property
    def folder_name(self):
        path_list = self.__path__.split(os.path.sep)
        return path_list[-1]

    def folder_path(self, move: int=0):
        assert move <= 0
        path_list = self.__path__.split(os.path.sep)
        folder_level = move
        try:
            while folder_level < 0:
                path_list.pop()
                folder_level += 1
            return os.path.sep.join(path_list)
        except IndexError:
            raise ValueError('No such super folder as level {}'.format(move))

    def move_to(self, folder_path: str):
        if not os.path.exists(folder_path):
            os.makedirs(folder_path)

        assert os.path.isfile(folder_path) is False
        target_path = os.path.join(folder_path, self.folder_name)
        if os.path.exists(target_path) is True:
            raise FileExistsError('target path {} already exists.'.format(target_path))
        else:
            shutil.move(self.__path__, folder_path)
            self.__path__ = target_path

    def copy_to(self, folder_path: str):
        if not os.path.exists(folder_path):
            os.makedirs(folder_path)

        assert os.path.isfile(folder_path) is False
        target_path = os.path.join(folder_path, self.folder_name)
        if os.path.exists(target_path) is True:
            raise FileExistsError('target path {} already exists.'.format(target_path))
        else:
            shutil.copy(self.__path__, folder_path)

    def delete(self):
        os.removedirs(self.__path__)


class FilePath(object):
    """文件路径对象"""
    def __init__(self, abs_path: str):
        if os.path.exists(abs_path):
            assert os.path.isfile(abs_path) is True, 'abs_path {} is a folder instead of a file'.format(abs_path)
            self.__path__ = abs_path
        else:
            RuntimeError('path {} not exists.'.format(abs_path))

    @property
    def full_name(self):
        return os.path.split(self.__path__)[-1]

    @property
    def name(self):
        file_name = self.full_name
        assert isinstance(file_name, str)
        file_name = file_name.split('.')
        file_name.pop()
        return '.'.join(file_name)

    @property
    def type(self):
        file_name = self.full_name
        assert isinstance(file_name, str)
        file_name = file_name.split('.')
        return file_name[-1]

    @property
    def folder_name(self):
        path_list = self.__path__.split(os.path.sep)
        path_list.pop()
        return path_list[-1]

    def folder_path(self, move: int=0):
        assert move <= 0
        path_list = self.__path__.split(os.path.sep)
        path_list.pop()
        folder_level = move
        try:
            while folder_level < 0:
                path_list.pop()
                folder_level += 1
            return os.path.sep.join(path_list)
        except IndexError:
            raise ValueError('No such super folder as level {}'.format(move))

    def move_to(self, folder_path: str):
        if not os.path.exists(folder_path):
            os.makedirs(folder_path)

        assert os.path.isfile(folder_path) is False
        target_path = os.path.join(folder_path, self.full_name)
        if os.path.exists(target_path) is True:
            raise FileExistsError('target path {} already exists.'.format(target_path))
        else:
            shutil.move(self.__path__, folder_path)
            self.__path__ = target_path

    def copy_to(self, folder_path: str):
        if not os.path.exists(folder_path):
            os.makedirs(folder_path)

        assert os.path.isfile(folder_path) is False
        target_path = os.path.join(folder_path, self.full_name)
        if os.path.exists(target_path) is True:
            raise FileExistsError('target path {} already exists.'.format(target_path))
        else:
            shutil.copy(self.__path__, folder_path)

    def delete(self):
        os.remove(self.__path__)


class StrPath(object):
    def __init__(self, string: str):
        self.__string__ = string

    def __repr__(self):
        return self.__string__

    def __str__(self):
        return self.__string__

    @property
    def str(self):
        return self.__string__

    @property
    def exists(self):
        return os.path.exists(self.str)

    @property
    def is_folder(self):
        return os.path.isdir(self.str)

    @property
    def is_legal_folder(self):
        if self.is_folder:
            if self.folder_name[0] in ('.', '@', '_'):
                return False
            else:
                return True
        else:
            return False

    @property
    def is_file(self):
        return os.path.isfile(self.str)

    @property
    def is_legal_file(self):
        if self.is_file:
            if self.file_full_name[0] in ('.', '$', '_'):
                return False
            else:
                return True
        else:
            return False

    @property
    def file_full_name(self):
        if self.is_file:
            full_name = os.path.split(self.str)[-1]
            assert isinstance(full_name, str)
            return full_name
        else:
            raise RuntimeError('folder has no file full name')

    @property
    def file_name(self):
        if self.is_file:
            file_name = self.file_full_name
            assert isinstance(file_name, str)
            file_name = file_name.split('.')
            file_name.pop()
            return '.'.join(file_name)
        else:
            raise RuntimeError('folder has no file name')

    @property
    def file_type(self):
        if self.is_file:
            file_name = self.file_full_name
            assert isinstance(file_name, str)
            file_name = file_name.split('.')
            return file_name[-1].lower()
        else:
            raise RuntimeError('folder has no file type')

    @property
    def msize(self):
        """size in MB"""
        return os.stat(self.str).st_size / MB_BYTES

    @property
    def gsize(self):
        return os.stat(self.str).st_size / GB_BYTES

    @property
    def last_visit_time(self):
        return datetime.datetime.fromtimestamp(os.stat(self.str).st_atime)

    @property
    def last_modify_time(self):
        return datetime.datetime.fromtimestamp(os.stat(self.str).st_mtime)

    @property
    def folder_name(self):
        if self.is_folder:
            path_list = self.str.split(os.path.sep)
            return path_list[-1]
        elif self.is_file:
            path_list = self.str.split(os.path.sep)
            path_list.pop()
            return path_list[-1]
        else:
            raise RuntimeError

    @property
    def folder_path(self):
        if self.is_folder:
            return self
        elif self.is_file:
            path_list = self.str.split(os.path.sep)
            path_list.pop()
            return StrPath(os.path.sep.join(path_list))
        else:
            raise RuntimeError

    @property
    def super_folder_name(self):
        if self.is_folder:
            path_list = self.str.split(os.path.sep)
            path_list.pop()
            if len(path_list) >= 1:
                return path_list[-1]
            else:
                raise RuntimeError('folder {} has no super folder')
        else:
            raise RuntimeError('file has no super folder')

    @property
    def super_folder_path(self):
        if self.is_folder:
            path_list = self.str.split(os.path.sep)
            path_list.pop()
            if len(path_list) >= 1:
                return StrPath(os.path.sep.join(path_list))
            else:
                raise RuntimeError('folder {} has no super folder')
        else:
            raise RuntimeError('file has no super folder')

    def move_to(self, folder_path):
        assert isinstance(folder_path, str)
        if not os.path.exists(folder_path):
            os.makedirs(folder_path)
        if os.path.isfile(folder_path) is True:
            raise ValueError('folder_path {} is a file instead of a folder.'.format(folder_path))

        if self.is_folder:
            target_path = os.path.join(folder_path, self.folder_name)
        elif self.is_file:
            target_path = os.path.join(folder_path, self.file_full_name)
        else:
            raise RuntimeError(self.str, folder_path)

        if os.path.exists(target_path) is True:
            raise FileExistsError('target path {} already exists.'.format(target_path))
        else:
            new_str_path = StrPath(shutil.move(self.str, folder_path))
            return new_str_path

    def copy_to(self, folder_path):
        assert isinstance(folder_path, str)
        if not os.path.exists(folder_path):
            os.makedirs(folder_path)
        if os.path.isfile(folder_path) is True:
            raise ValueError('folder_path {} is a file instead of a folder.'.format(folder_path))

        if self.is_folder:
            target_path = os.path.join(folder_path, self.folder_name)
        elif self.is_file:
            target_path = os.path.join(folder_path, self.file_full_name)
        else:
            raise RuntimeError

        if os.path.exists(target_path) is True:
            raise FileExistsError('target path {} already exists.'.format(target_path))
        else:
            new_str_path = StrPath(shutil.copy(self.str, folder_path))
            return new_str_path

    def sub_path(self, name: str):
        if self.is_file:
            raise RuntimeError('file has no sub_path')
        return StrPath(os.path.join(self.str, name))

    def list_folder(self):
        """list the folder -> folder_list, file_list"""
        if self.is_folder:
            folder_list, file_list = list(), list()
            for file_name in os.listdir(self.str):
                file_path = self.sub_path(file_name)
                if file_path.is_legal_file:
                    file_list.append(file_path.str)
                elif file_path.is_legal_folder:
                    folder_list.append(file_path.str)
                else:
                    continue
            folder_list.sort()
            for index in range(len(folder_list)):
                folder_list[index] = StrPath(folder_list[index])
            file_list.sort()
            for index in range(len(file_list)):
                file_list[index] = StrPath(file_list[index])

            return folder_list, file_list
        else:
            raise RuntimeError('None folder can not list folder.')

    def delete(self):
        if self.is_folder:
            os.removedirs(self.str)
        elif self.is_file:
            os.remove(self.str)
        else:
            raise RuntimeError
