
#############################################################################
##
## Copyright (C) 2010 velociraptor Genjix <aphidia@hotmail.com>
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

import sys

from PySide6.QtCore import QCoreApplication, QObject, Qt, Property, Signal
from PySide6.QtStateMachine import (QFinalState, QSignalTransition, QState,
                                    QStateMachine)


class Factorial(QObject):
    x_changed = Signal(int)

    def __init__(self):
        super().__init__()
        self.xval = -1
        self.facval = 1

    def get_x(self):
        return self.xval

    def set_x(self, x):
        if self.xval == x:
            return
        self.xval = x
        self.x_changed.emit(x)
    x = Property(int, get_x, set_x)

    def get_fact(self):
        return self.facval

    def set_fact(self, fac):
        self.facval = fac

    fac = Property(int, get_fact, set_fact)


class FactorialLoopTransition(QSignalTransition):
    def __init__(self, fact):
        super().__init__(fact.x_changed)
        self.fact = fact

    def eventTest(self, e):
        if not super(FactorialLoopTransition, self).eventTest(e):
            return False
        return e.arguments()[0] > 1

    def onTransition(self, e):
        x = e.arguments()[0]
        fac = self.fact.fac
        self.fact.fac = x * fac
        self.fact.x = x - 1


class FactorialDoneTransition(QSignalTransition):
    def __init__(self, fact):
        super().__init__(fact.x_changed)
        self.fact = fact

    def eventTest(self, e):
        if not super(FactorialDoneTransition, self).eventTest(e):
            return False
        return e.arguments()[0] <= 1

    def onTransition(self, e):
        print(self.fact.fac)


if __name__ == '__main__':
    app = QCoreApplication(sys.argv)
    factorial = Factorial()
    machine = QStateMachine()

    compute = QState(machine)
    compute.assignProperty(factorial, 'fac', 1)
    compute.assignProperty(factorial, 'x', 6)
    compute.addTransition(FactorialLoopTransition(factorial))

    done = QFinalState(machine)
    done_transition = FactorialDoneTransition(factorial)
    done_transition.setTargetState(done)
    compute.addTransition(done_transition)

    machine.setInitialState(compute)
    machine.finished.connect(app.quit)
    machine.start()

    sys.exit(app.exec())
