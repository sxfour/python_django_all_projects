# -*- coding: utf-8 -*-

# Добавление папок при сохранении
def name_file(instance, filename):
    return '/'.join(['files_teploset', str(instance.name), filename])
