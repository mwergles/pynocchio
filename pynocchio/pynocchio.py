# -*- coding: utf-8 -*-
#
# Copyright (C) 2014-2016  Michell Stuttgart Faria

# This program is free software: you can redistribute it and/or modify it
# under the terms of the GNU General Public License as published by the Free
# Software Foundation, either version 3 of the License, or (at your option)
# any later version.

# This program is distributed in the hope that it will be useful, but WITHOUT
# ANY WARRANTY; without even the implied warranty of MERCHANTABILITY or
# FITNESS FOR A PARTICULAR PURPOSE.  See the GNU General Public License for
# more details.

# You should have received a copy of the GNU General Public License along
# with this program.  If not, see <http://www.gnu.org/licenses/>.

import sys
from PySide import QtGui, QtCore
import os

from main_window_model import MainWindowModel
from main_window_view import MainWindowView

DATADIRS = (
        os.path.abspath('./pynocchio'),
        '/usr/share/pynocchio',
        '/usr/local/share/pynocchio',
        os.path.join(QtCore.QDir.homePath(), '.local/share/pynocchio'),
    )

QLocale = QtCore.QLocale
QLibraryInfo = QtCore.QLibraryInfo
QTranslator = QtCore.QTranslator
QFileInfo = QtCore.QFileInfo
QFile = QtCore.QFile


class Pynocchio(QtGui.QApplication):

    def __init__(self):
        super(Pynocchio, self).__init__(sys.argv)
        self.setOrganizationName('Pynocchio')
        self.setApplicationName('Pynocchio')
        if hasattr(self, 'setApplicationDisplayName'):
            self.setApplicationDisplayName('Pynocchio')

        for path in DATADIRS:
            self.addLibraryPath(path)

        translator = QTranslator(self)
        language = 'pynocchio_' + QLocale.system().uiLanguages()[0]

        for path in DATADIRS:
            if translator.load(language, os.path.join(path, 'locale')):
                break
        qt_translator = QTranslator(self)
        qt_translator.load('qt_' + QLocale.system().name(),
                           QLibraryInfo.location(
                               QLibraryInfo.TranslationsPath))
        self.installTranslator(translator)
        self.installTranslator(qt_translator)

        self.model = MainWindowModel()
        self.view = MainWindowView(self.model)

    def run(self):

        self.view.show()

        if len(sys.argv) > 1:
            a = sys.argv
            filename = ''
            for s in sys.argv[1:]:
                filename += s

            filename = filename.replace('\\', ' ')

            if os.path.isfile(filename):
                self.view.open_comics(filename)

        sys.exit(self.exec_())
