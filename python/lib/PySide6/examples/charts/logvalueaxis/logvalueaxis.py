#############################################################################
##
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

"""PySide6 port of the Logarithmic Axis Example from Qt v5.x"""


import sys
from PySide6.QtCore import Qt, QPointF
from PySide6.QtGui import QPainter
from PySide6.QtWidgets import QMainWindow, QApplication
from PySide6.QtCharts import (QChart, QChartView, QLineSeries, QLogValueAxis,
                              QValueAxis)


class TestChart(QMainWindow):
    def __init__(self):
        super().__init__()

        self.series = QLineSeries()
        self.series.append([
            QPointF(1.0, 1.0), QPointF(2.0, 73.0), QPointF(3.0, 268.0),
            QPointF(4.0, 17.0), QPointF(5.0, 4325.0), QPointF(6.0, 723.0)])

        self.chart = QChart()
        self.chart.addSeries(self.series)
        self.chart.legend().hide()
        self.chart.setTitle("Logarithmic axis example")

        self._axis_x = QValueAxis()
        self._axis_x.setTitleText("Data point")
        self._axis_x.setLabelFormat("%i")
        self._axis_x.setTickCount(self.series.count())
        self.chart.addAxis(self._axis_x, Qt.AlignBottom)
        self.series.attachAxis(self._axis_x)

        self._axis_y = QLogValueAxis()
        self._axis_y.setTitleText("Values")
        self._axis_y.setLabelFormat("%g")
        self._axis_y.setBase(8.0)
        self._axis_y.setMinorTickCount(-1)
        self.chart.addAxis(self._axis_y, Qt.AlignLeft)
        self.series.attachAxis(self._axis_y)

        self._chart_view = QChartView(self.chart)
        self._chart_view.setRenderHint(QPainter.Antialiasing)

        self.setCentralWidget(self._chart_view)


if __name__ == "__main__":
    app = QApplication(sys.argv)

    window = TestChart()
    window.show()
    window.resize(800, 600)

    sys.exit(app.exec())
