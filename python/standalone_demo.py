#!/usr/bin/env python
import os
import sys


def bootstrap():
    this = os.path.realpath(__file__)
    parent = os.path.dirname(this)

    paths = [
        parent,
        os.path.join(parent, 'lib')
    ]

    for i, path in enumerate(paths):
        print(f'Bootstrapping {path}')
        sys.path.insert(i, path)


def main():
    bootstrap()

    from PySide6.QtWidgets import QApplication, QWidget
    from PySide6.QtCore import QLibraryInfo, qVersion
    from proxi.ui import debugSystemTime

    print('Python {}.{}'.format(sys.version_info[0], sys.version_info[1]))
    print(QLibraryInfo.build())

    app = QApplication.instance() or QApplication(sys.argv)
    window = debugSystemTime.Window()

    window.setWindowTitle(qVersion())
    window.showAndActivate()

    sys.exit(app.exec_())


if __name__ == '__main__':
    print('Executing in standalone mode')
    main()