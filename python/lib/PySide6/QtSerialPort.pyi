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
PySide6.QtSerialPort, except for defaults which are replaced by "...".
"""

# Module `PySide6.QtSerialPort`

import PySide6.QtSerialPort
import PySide6.QtCore

from typing import Optional, List, overload
from shiboken6 import Shiboken


class QIntList(object): ...


class QSerialPort(PySide6.QtCore.QIODevice):

    Baud1200                 : QSerialPort.BaudRate = ... # 0x4b0
    Baud2400                 : QSerialPort.BaudRate = ... # 0x960
    Baud4800                 : QSerialPort.BaudRate = ... # 0x12c0
    Baud9600                 : QSerialPort.BaudRate = ... # 0x2580
    Baud19200                : QSerialPort.BaudRate = ... # 0x4b00
    Baud38400                : QSerialPort.BaudRate = ... # 0x9600
    Baud57600                : QSerialPort.BaudRate = ... # 0xe100
    Baud115200               : QSerialPort.BaudRate = ... # 0x1c200
    Data5                    : QSerialPort.DataBits = ... # 0x5
    Data6                    : QSerialPort.DataBits = ... # 0x6
    Data7                    : QSerialPort.DataBits = ... # 0x7
    Data8                    : QSerialPort.DataBits = ... # 0x8
    Input                    : QSerialPort.Direction = ... # 0x1
    Output                   : QSerialPort.Direction = ... # 0x2
    AllDirections            : QSerialPort.Direction = ... # 0x3
    NoFlowControl            : QSerialPort.FlowControl = ... # 0x0
    HardwareControl          : QSerialPort.FlowControl = ... # 0x1
    SoftwareControl          : QSerialPort.FlowControl = ... # 0x2
    NoParity                 : QSerialPort.Parity = ... # 0x0
    EvenParity               : QSerialPort.Parity = ... # 0x2
    OddParity                : QSerialPort.Parity = ... # 0x3
    SpaceParity              : QSerialPort.Parity = ... # 0x4
    MarkParity               : QSerialPort.Parity = ... # 0x5
    NoSignal                 : QSerialPort.PinoutSignal = ... # 0x0
    DataTerminalReadySignal  : QSerialPort.PinoutSignal = ... # 0x4
    DataCarrierDetectSignal  : QSerialPort.PinoutSignal = ... # 0x8
    DataSetReadySignal       : QSerialPort.PinoutSignal = ... # 0x10
    RingIndicatorSignal      : QSerialPort.PinoutSignal = ... # 0x20
    RequestToSendSignal      : QSerialPort.PinoutSignal = ... # 0x40
    ClearToSendSignal        : QSerialPort.PinoutSignal = ... # 0x80
    SecondaryTransmittedDataSignal: QSerialPort.PinoutSignal = ... # 0x100
    SecondaryReceivedDataSignal: QSerialPort.PinoutSignal = ... # 0x200
    NoError                  : QSerialPort.SerialPortError = ... # 0x0
    DeviceNotFoundError      : QSerialPort.SerialPortError = ... # 0x1
    PermissionError          : QSerialPort.SerialPortError = ... # 0x2
    OpenError                : QSerialPort.SerialPortError = ... # 0x3
    WriteError               : QSerialPort.SerialPortError = ... # 0x4
    ReadError                : QSerialPort.SerialPortError = ... # 0x5
    ResourceError            : QSerialPort.SerialPortError = ... # 0x6
    UnsupportedOperationError: QSerialPort.SerialPortError = ... # 0x7
    UnknownError             : QSerialPort.SerialPortError = ... # 0x8
    TimeoutError             : QSerialPort.SerialPortError = ... # 0x9
    NotOpenError             : QSerialPort.SerialPortError = ... # 0xa
    OneStop                  : QSerialPort.StopBits = ... # 0x1
    TwoStop                  : QSerialPort.StopBits = ... # 0x2
    OneAndHalfStop           : QSerialPort.StopBits = ... # 0x3

    class BaudRate(Shiboken.Enum):

        Baud1200                 : QSerialPort.BaudRate = ... # 0x4b0
        Baud2400                 : QSerialPort.BaudRate = ... # 0x960
        Baud4800                 : QSerialPort.BaudRate = ... # 0x12c0
        Baud9600                 : QSerialPort.BaudRate = ... # 0x2580
        Baud19200                : QSerialPort.BaudRate = ... # 0x4b00
        Baud38400                : QSerialPort.BaudRate = ... # 0x9600
        Baud57600                : QSerialPort.BaudRate = ... # 0xe100
        Baud115200               : QSerialPort.BaudRate = ... # 0x1c200

    class DataBits(Shiboken.Enum):

        Data5                    : QSerialPort.DataBits = ... # 0x5
        Data6                    : QSerialPort.DataBits = ... # 0x6
        Data7                    : QSerialPort.DataBits = ... # 0x7
        Data8                    : QSerialPort.DataBits = ... # 0x8

    class Direction(Shiboken.Enum):

        Input                    : QSerialPort.Direction = ... # 0x1
        Output                   : QSerialPort.Direction = ... # 0x2
        AllDirections            : QSerialPort.Direction = ... # 0x3

    class Directions(object): ...

    class FlowControl(Shiboken.Enum):

        NoFlowControl            : QSerialPort.FlowControl = ... # 0x0
        HardwareControl          : QSerialPort.FlowControl = ... # 0x1
        SoftwareControl          : QSerialPort.FlowControl = ... # 0x2

    class Parity(Shiboken.Enum):

        NoParity                 : QSerialPort.Parity = ... # 0x0
        EvenParity               : QSerialPort.Parity = ... # 0x2
        OddParity                : QSerialPort.Parity = ... # 0x3
        SpaceParity              : QSerialPort.Parity = ... # 0x4
        MarkParity               : QSerialPort.Parity = ... # 0x5

    class PinoutSignal(Shiboken.Enum):

        NoSignal                 : QSerialPort.PinoutSignal = ... # 0x0
        DataTerminalReadySignal  : QSerialPort.PinoutSignal = ... # 0x4
        DataCarrierDetectSignal  : QSerialPort.PinoutSignal = ... # 0x8
        DataSetReadySignal       : QSerialPort.PinoutSignal = ... # 0x10
        RingIndicatorSignal      : QSerialPort.PinoutSignal = ... # 0x20
        RequestToSendSignal      : QSerialPort.PinoutSignal = ... # 0x40
        ClearToSendSignal        : QSerialPort.PinoutSignal = ... # 0x80
        SecondaryTransmittedDataSignal: QSerialPort.PinoutSignal = ... # 0x100
        SecondaryReceivedDataSignal: QSerialPort.PinoutSignal = ... # 0x200

    class PinoutSignals(object): ...

    class SerialPortError(Shiboken.Enum):

        NoError                  : QSerialPort.SerialPortError = ... # 0x0
        DeviceNotFoundError      : QSerialPort.SerialPortError = ... # 0x1
        PermissionError          : QSerialPort.SerialPortError = ... # 0x2
        OpenError                : QSerialPort.SerialPortError = ... # 0x3
        WriteError               : QSerialPort.SerialPortError = ... # 0x4
        ReadError                : QSerialPort.SerialPortError = ... # 0x5
        ResourceError            : QSerialPort.SerialPortError = ... # 0x6
        UnsupportedOperationError: QSerialPort.SerialPortError = ... # 0x7
        UnknownError             : QSerialPort.SerialPortError = ... # 0x8
        TimeoutError             : QSerialPort.SerialPortError = ... # 0x9
        NotOpenError             : QSerialPort.SerialPortError = ... # 0xa

    class StopBits(Shiboken.Enum):

        OneStop                  : QSerialPort.StopBits = ... # 0x1
        TwoStop                  : QSerialPort.StopBits = ... # 0x2
        OneAndHalfStop           : QSerialPort.StopBits = ... # 0x3


    @overload
    def __init__(self, info:PySide6.QtSerialPort.QSerialPortInfo, parent:Optional[PySide6.QtCore.QObject]=...) -> None: ...
    @overload
    def __init__(self, name:str, parent:Optional[PySide6.QtCore.QObject]=...) -> None: ...
    @overload
    def __init__(self, parent:Optional[PySide6.QtCore.QObject]=...) -> None: ...

    def baudRate(self, directions:PySide6.QtSerialPort.QSerialPort.Directions=...) -> int: ...
    def bytesAvailable(self) -> int: ...
    def bytesToWrite(self) -> int: ...
    def canReadLine(self) -> bool: ...
    def clear(self, directions:PySide6.QtSerialPort.QSerialPort.Directions=...) -> bool: ...
    def clearError(self) -> None: ...
    def close(self) -> None: ...
    def dataBits(self) -> PySide6.QtSerialPort.QSerialPort.DataBits: ...
    def error(self) -> PySide6.QtSerialPort.QSerialPort.SerialPortError: ...
    def flowControl(self) -> PySide6.QtSerialPort.QSerialPort.FlowControl: ...
    def flush(self) -> bool: ...
    def handle(self) -> int: ...
    def isBreakEnabled(self) -> bool: ...
    def isDataTerminalReady(self) -> bool: ...
    def isRequestToSend(self) -> bool: ...
    def isSequential(self) -> bool: ...
    def open(self, mode:PySide6.QtCore.QIODeviceBase.OpenMode) -> bool: ...
    def parity(self) -> PySide6.QtSerialPort.QSerialPort.Parity: ...
    def pinoutSignals(self) -> PySide6.QtSerialPort.QSerialPort.PinoutSignals: ...
    def portName(self) -> str: ...
    def readBufferSize(self) -> int: ...
    def readData(self, data:bytes, maxSize:int) -> object: ...
    def readLineData(self, data:bytes, maxSize:int) -> object: ...
    def setBaudRate(self, baudRate:int, directions:PySide6.QtSerialPort.QSerialPort.Directions=...) -> bool: ...
    def setBreakEnabled(self, set:bool=...) -> bool: ...
    def setDataBits(self, dataBits:PySide6.QtSerialPort.QSerialPort.DataBits) -> bool: ...
    def setDataTerminalReady(self, set:bool) -> bool: ...
    def setFlowControl(self, flowControl:PySide6.QtSerialPort.QSerialPort.FlowControl) -> bool: ...
    def setParity(self, parity:PySide6.QtSerialPort.QSerialPort.Parity) -> bool: ...
    def setPort(self, info:PySide6.QtSerialPort.QSerialPortInfo) -> None: ...
    def setPortName(self, name:str) -> None: ...
    def setReadBufferSize(self, size:int) -> None: ...
    def setRequestToSend(self, set:bool) -> bool: ...
    def setStopBits(self, stopBits:PySide6.QtSerialPort.QSerialPort.StopBits) -> bool: ...
    def stopBits(self) -> PySide6.QtSerialPort.QSerialPort.StopBits: ...
    def waitForBytesWritten(self, msecs:int=...) -> bool: ...
    def waitForReadyRead(self, msecs:int=...) -> bool: ...
    def writeData(self, data:bytes, maxSize:int) -> int: ...


class QSerialPortInfo(Shiboken.Object):

    @overload
    def __init__(self) -> None: ...
    @overload
    def __init__(self, name:str) -> None: ...
    @overload
    def __init__(self, other:PySide6.QtSerialPort.QSerialPortInfo) -> None: ...
    @overload
    def __init__(self, port:PySide6.QtSerialPort.QSerialPort) -> None: ...

    @staticmethod
    def __copy__() -> None: ...
    @staticmethod
    def availablePorts() -> List[PySide6.QtSerialPort.QSerialPortInfo]: ...
    def description(self) -> str: ...
    def hasProductIdentifier(self) -> bool: ...
    def hasVendorIdentifier(self) -> bool: ...
    def isNull(self) -> bool: ...
    def manufacturer(self) -> str: ...
    def portName(self) -> str: ...
    def productIdentifier(self) -> int: ...
    def serialNumber(self) -> str: ...
    @staticmethod
    def standardBaudRates() -> List[int]: ...
    def swap(self, other:PySide6.QtSerialPort.QSerialPortInfo) -> None: ...
    def systemLocation(self) -> str: ...
    def vendorIdentifier(self) -> int: ...


# eof
