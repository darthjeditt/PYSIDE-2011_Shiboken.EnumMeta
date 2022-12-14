
############################################################################
##
## Copyright (C) 2013 Riverbank Computing Limited.
## Copyright (C) 2021 The Qt Company Ltd.
## Contact: https://www.qt.io/licensing/
##
## This file is part of the Qt for Python examples of the Qt Toolkit.
##
## $QT_BEGIN_LICENSE:BSD$
## You may use this file under the terms of the BSD license as follows:
##
## "Redistribution and use in source and binary forms, with or without
## modification, are permitted provided that the following conditions are
## met:
##   * Redistributions of source code must retain the above copyright
##     notice, this list of conditions and the following disclaimer.
##   * Redistributions in binary form must reproduce the above copyright
##     notice, this list of conditions and the following disclaimer in
##     the documentation and/or other materials provided with the
##     distribution.
##   * Neither the name of The Qt Company Ltd nor the names of its
##     contributors may be used to endorse or promote products derived
##     from this software without specific prior written permission.
##
##
## THIS SOFTWARE IS PROVIDED BY THE COPYRIGHT HOLDERS AND CONTRIBUTORS
## "AS IS" AND ANY EXPRESS OR IMPLIED WARRANTIES, INCLUDING, BUT NOT
## LIMITED TO, THE IMPLIED WARRANTIES OF MERCHANTABILITY AND FITNESS FOR
## A PARTICULAR PURPOSE ARE DISCLAIMED. IN NO EVENT SHALL THE COPYRIGHT
## OWNER OR CONTRIBUTORS BE LIABLE FOR ANY DIRECT, INDIRECT, INCIDENTAL,
## SPECIAL, EXEMPLARY, OR CONSEQUENTIAL DAMAGES (INCLUDING, BUT NOT
## LIMITED TO, PROCUREMENT OF SUBSTITUTE GOODS OR SERVICES; LOSS OF USE,
## DATA, OR PROFITS; OR BUSINESS INTERRUPTION) HOWEVER CAUSED AND ON ANY
## THEORY OF LIABILITY, WHETHER IN CONTRACT, STRICT LIABILITY, OR TORT
## (INCLUDING NEGLIGENCE OR OTHERWISE) ARISING IN ANY WAY OUT OF THE USE
## OF THIS SOFTWARE, EVEN IF ADVISED OF THE POSSIBILITY OF SUCH DAMAGE."
##
## $QT_END_LICENSE$
##
#############################################################################

"""PySide6 port of the widgets/richtext/syntaxhighlighter example from Qt v5.x"""

import os
from pathlib import Path
import sys
import re
from PySide6.QtCore import (QFile, Qt, QTextStream)
from PySide6.QtGui import (QColor, QFont, QFontDatabase, QKeySequence,
                           QSyntaxHighlighter, QTextCharFormat)
from PySide6.QtWidgets import (QApplication, QFileDialog, QMainWindow,
    QPlainTextEdit)


class MainWindow(QMainWindow):
    def __init__(self, parent=None):
        QMainWindow.__init__(self, parent)

        self._highlighter = Highlighter()

        self.setup_file_menu()
        self.setup_editor()

        self.setCentralWidget(self._editor)
        self.setWindowTitle(self.tr("Syntax Highlighter"))

    def new_file(self):
        self._editor.clear()

    def open_file(self, path=""):
        file_name = path

        if not file_name:
            file_name, _ = QFileDialog.getOpenFileName(self, self.tr("Open File"), "",
                                                       "Python Files (*.py)")

        if file_name:
            in_file = QFile(file_name)
            if in_file.open(QFile.ReadOnly | QFile.Text):
                stream = QTextStream(in_file)
                self._editor.setPlainText(stream.readAll())

    def setup_editor(self):
        class_format = QTextCharFormat()
        class_format.setFontWeight(QFont.Bold)
        class_format.setForeground(Qt.blue)
        pattern = r'^\s*class\s+\w+\(.*$'
        self._highlighter.add_mapping(pattern, class_format)

        function_format = QTextCharFormat()
        function_format.setFontItalic(True)
        function_format.setForeground(Qt.blue)
        pattern = r'^\s*def\s+\w+\s*\(.*\)\s*:\s*$'
        self._highlighter.add_mapping(pattern, function_format)

        comment_format = QTextCharFormat()
        comment_format.setBackground(QColor("#77ff77"))
        self._highlighter.add_mapping(r'^\s*#.*$', comment_format)

        font = QFontDatabase.systemFont(QFontDatabase.FixedFont)
        self._editor = QPlainTextEdit()
        self._editor.setFont(font)
        self._highlighter.setDocument(self._editor.document())

    def setup_file_menu(self):
        file_menu = self.menuBar().addMenu(self.tr("&File"))

        new_file_act = file_menu.addAction(self.tr("&New..."))
        new_file_act.setShortcut(QKeySequence(QKeySequence.New))
        new_file_act.triggered.connect(self.new_file)

        open_file_act = file_menu.addAction(self.tr("&Open..."))
        open_file_act.setShortcut(QKeySequence(QKeySequence.Open))
        open_file_act.triggered.connect(self.open_file)

        quit_act = file_menu.addAction(self.tr("E&xit"))
        quit_act.setShortcut(QKeySequence(QKeySequence.Quit))
        quit_act.triggered.connect(self.close)

        help_menu = self.menuBar().addMenu("&Help")
        help_menu.addAction("About &Qt", qApp.aboutQt)


class Highlighter(QSyntaxHighlighter):
    def __init__(self, parent=None):
        QSyntaxHighlighter.__init__(self, parent)

        self._mappings = {}

    def add_mapping(self, pattern, format):
        self._mappings[pattern] = format

    def highlightBlock(self, text):
        for pattern, format in self._mappings.items():
            for match in re.finditer(pattern, text):
                start, end = match.span()
                self.setFormat(start, end - start, format)


if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = MainWindow()
    window.resize(640, 512)
    window.show()
    window.open_file(os.fspath(Path(__file__).resolve()))
    sys.exit(app.exec())
