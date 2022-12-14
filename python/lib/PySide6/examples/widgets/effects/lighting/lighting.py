
#############################################################################
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

import math
import sys

from PySide6.QtCore import QPointF, QTimer, Qt
from PySide6.QtGui import (QBrush, QColor, QLinearGradient, QPainter, QPen,
                           QPixmap, QRadialGradient)
from PySide6.QtWidgets import (QApplication, QFrame, QGraphicsDropShadowEffect,
                               QGraphicsEllipseItem, QGraphicsRectItem,
                               QGraphicsScene, QGraphicsView, QWidget)


class Lighting(QGraphicsView):
    def __init__(self, parent=None):
        super().__init__(parent)

        self.angle = 0.0
        self.m_scene = QGraphicsScene()
        self.m_lightSource = None
        self.m_items = []

        self.setScene(self.m_scene)

        self.setup_scene()

        timer = QTimer(self)
        timer.timeout.connect(self.animate)
        timer.setInterval(30)
        timer.start()

        self.setRenderHint(QPainter.Antialiasing)
        self.setFrameStyle(QFrame.NoFrame)

    def setup_scene(self):
        self.m_scene.setSceneRect(-300, -200, 600, 460)

        linear_grad = QLinearGradient(QPointF(-100, -100),
                QPointF(100, 100))
        linear_grad.setColorAt(0, QColor(255, 255, 255))
        linear_grad.setColorAt(1, QColor(192, 192, 255))
        self.setBackgroundBrush(linear_grad)

        radial_grad = QRadialGradient(30, 30, 30)
        radial_grad.setColorAt(0, Qt.yellow)
        radial_grad.setColorAt(0.2, Qt.yellow)
        radial_grad.setColorAt(1, Qt.transparent)

        pixmap = QPixmap(60, 60)
        pixmap.fill(Qt.transparent)

        with QPainter(pixmap) as painter:
            painter.setPen(Qt.NoPen)
            painter.setBrush(radial_grad)
            painter.drawEllipse(0, 0, 60, 60)

        self.m_lightSource = self.m_scene.addPixmap(pixmap)
        self.m_lightSource.setZValue(2)

        for i in range(-2, 3):
            for j in range(-2, 3):
                if (i + j) & 1:
                    item = QGraphicsEllipseItem(0, 0, 50, 50)
                else:
                    item = QGraphicsRectItem(0, 0, 50, 50)

                item.setPen(QPen(Qt.black, 1))
                item.setBrush(QBrush(Qt.white))

                effect = QGraphicsDropShadowEffect(self)
                effect.setBlurRadius(8)
                item.setGraphicsEffect(effect)
                item.setZValue(1)
                item.setPos(i * 80, j * 80)
                self.m_scene.addItem(item)
                self.m_items.append(item)

    def animate(self):
        self.angle += (math.pi / 30)
        xs = 200 * math.sin(self.angle) - 40 + 25
        ys = 200 * math.cos(self.angle) - 40 + 25
        self.m_lightSource.setPos(xs, ys)

        for item in self.m_items:
            effect = item.graphicsEffect()

            delta = QPointF(item.x() - xs, item.y() - ys)
            effect.setOffset(QPointF(delta.toPoint() / 30))

            dd = math.hypot(delta.x(), delta.y())
            color = effect.color()
            color.setAlphaF(max(0.4, min(1 - dd / 200.0, 0.7)))
            effect.setColor(color)

        self.m_scene.update()


if __name__ == '__main__':
    app = QApplication(sys.argv)

    lighting = Lighting()
    lighting.setWindowTitle("Lighting and Shadows")
    lighting.resize(640, 480)
    lighting.show()

    sys.exit(app.exec())
