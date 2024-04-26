# -*- coding: utf-8 -*-

from random import randint
from secrets import token_urlsafe
from logging import getLogger


# Создание пути для панели редактирования
class UrlCreate:
    def __init__(self):
        self.rand_token = randint(16, 32)
        self.logger = getLogger(__name__)
        self.url = token_urlsafe(self.rand_token)

    def get_url_create(self):
        return self.url

    def __del__(self):
        self.logger.warning('destruct urlsafe: {0}'.format(self.url))
