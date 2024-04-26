# -*- coding: utf-8 -*-

from ui.py_ui.Uploads_MTS import (
    UI_SendMessagePage,
    successWindow,
    errorWindow,
    findErrorWindow,
    pathDialogWindow,
)

from json import load, dump, decoder
from requests import post, exceptions
from os import remove

from logging import getLogger, INFO, FileHandler, basicConfig, error, info

from PyQt5.QtWidgets import QWidget
from PyQt5.QtWidgets import QApplication

from datetime import datetime

import sys
