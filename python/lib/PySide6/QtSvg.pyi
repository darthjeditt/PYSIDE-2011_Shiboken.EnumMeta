#############################################################################
##
## Copyright (C) 2021 The Qt Company Ltd.
## Contact: https://www.qt.io/licensing/
##
## This file is part of Qt for Python.
##
## $QT_BEGIN_LICENSE:LGPL$
## Commercial License Usage
## Licensees holding valid commercial Qt licenses may use this file in
## accordance with the commercial license agreement provided with the
## Software or, alternatively, in accordance with the terms contained in
## a written agreement between you and The Qt Company. For licensing terms
## and conditions see https://www.qt.io/terms-conditions. For further
## information use the contact form at https://www.qt.io/contact-us.
##
## GNU Lesser General Public License Usage
## Alternatively, this file may be used under the terms of the GNU Lesser
## General Public License version 3 as published by the Free Software
## Foundation and appearing in the file LICENSE.LGPL3 included in the
## packaging of this file. Please review the following information to
## ensure the GNU Lesser General Public License version 3 requirements
## will be met: https://www.gnu.org/licenses/lgpl-3.0.html.
##
## GNU General Public License Usage
## Alternatively, this file may be used under the terms of the GNU
## General Public License version 2.0 or (at your option) the GNU General
## Public license version 3 or any later version approved by the KDE Free
## Qt Foundation. The licenses are as published by the Free Software
## Foundation and appearing in the file LICENSE.GPL2 and LICENSE.GPL3
## included in the packaging of this file. Please review the following
## information to ensure the GNU General Public License requirements will
## be met: https://www.gnu.org/licenses/gpl-2.0.html and
## https://www.gnu.org/licenses/gpl-3.0.html.
##
## $QT_END_LICENSE$
##
#############################################################################
"""
This file contains the exact signatures for all functions in module
PySide6.QtSvg, except for defaults which are replaced by "...".
"""

# Module `PySide6.QtSvg`

import PySide6.QtSvg
import PySide6.QtCore
import PySide6.QtGui

from typing import Optional, Union, overload


class QIntList(object): ...


class QSvgGenerator(PySide6.QtGui.QPaintDevice):

    def __init__(self) -> None: ...

    def description(self) -> str: ...
    def fileName(self) -> str: ...
    def metric(self, metric:PySide6.QtGui.QPaintDevice.PaintDeviceMetric) -> int: ...
    def outputDevice(self) -> PySide6.QtCore.QIODevice: ...
    def paintEngine(self) -> PySide6.QtGui.QPaintEngine: ...
    def resolution(self) -> int: ...
    def setDescription(self, description:str) -> None: ...
    def setFileName(self, fileName:str) -> None: ...
    def setOutputDevice(self, outputDevice:PySide6.QtCore.QIODevice) -> None: ...
    def setResolution(self, dpi:int) -> None: ...
    def setSize(self, size:PySide6.QtCore.QSize) -> None: ...
    def setTitle(self, title:str) -> None: ...
    @overload
    def setViewBox(self, viewBox:PySide6.QtCore.QRect) -> None: ...
    @overload
    def setViewBox(self, viewBox:Union[PySide6.QtCore.QRectF, PySide6.QtCore.QRect]) -> None: ...
    def size(self) -> PySide6.QtCore.QSize: ...
    def title(self) -> str: ...
    def viewBox(self) -> PySide6.QtCore.QRect: ...
    def viewBoxF(self) -> PySide6.QtCore.QRectF: ...


class QSvgRenderer(PySide6.QtCore.QObject):

    @overload
    def __init__(self, contents:PySide6.QtCore.QXmlStreamReader, parent:Optional[PySide6.QtCore.QObject]=...) -> None: ...
    @overload
    def __init__(self, contents:Union[PySide6.QtCore.QByteArray, bytes], parent:Optional[PySide6.QtCore.QObject]=...) -> None: ...
    @overload
    def __init__(self, filename:str, parent:Optional[PySide6.QtCore.QObject]=...) -> None: ...
    @overload
    def __init__(self, parent:Optional[PySide6.QtCore.QObject]=...) -> None: ...

    def animated(self) -> bool: ...
    def animationDuration(self) -> int: ...
    def aspectRatioMode(self) -> PySide6.QtCore.Qt.AspectRatioMode: ...
    def boundsOnElement(self, id:str) -> PySide6.QtCore.QRectF: ...
    def currentFrame(self) -> int: ...
    def defaultSize(self) -> PySide6.QtCore.QSize: ...
    def elementExists(self, id:str) -> bool: ...
    def framesPerSecond(self) -> int: ...
    def isValid(self) -> bool: ...
    @overload
    def load(self, contents:PySide6.QtCore.QXmlStreamReader) -> bool: ...
    @overload
    def load(self, contents:Union[PySide6.QtCore.QByteArray, bytes]) -> bool: ...
    @overload
    def load(self, filename:str) -> bool: ...
    @overload
    def render(self, p:PySide6.QtGui.QPainter) -> None: ...
    @overload
    def render(self, p:PySide6.QtGui.QPainter, bounds:Union[PySide6.QtCore.QRectF, PySide6.QtCore.QRect]) -> None: ...
    @overload
    def render(self, p:PySide6.QtGui.QPainter, elementId:str, bounds:Union[PySide6.QtCore.QRectF, PySide6.QtCore.QRect]=...) -> None: ...
    def setAspectRatioMode(self, mode:PySide6.QtCore.Qt.AspectRatioMode) -> None: ...
    def setCurrentFrame(self, arg__1:int) -> None: ...
    def setFramesPerSecond(self, num:int) -> None: ...
    @overload
    def setViewBox(self, viewbox:PySide6.QtCore.QRect) -> None: ...
    @overload
    def setViewBox(self, viewbox:Union[PySide6.QtCore.QRectF, PySide6.QtCore.QRect]) -> None: ...
    def transformForElement(self, id:str) -> PySide6.QtGui.QTransform: ...
    def viewBox(self) -> PySide6.QtCore.QRect: ...
    def viewBoxF(self) -> PySide6.QtCore.QRectF: ...


# eof
