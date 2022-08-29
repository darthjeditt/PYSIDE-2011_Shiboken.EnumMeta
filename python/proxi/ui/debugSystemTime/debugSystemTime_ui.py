# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'debugSystemTime.ui'
##
## Created by: Qt User Interface Compiler version 6.3.1
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import (QCoreApplication, QDate, QDateTime, QLocale,
    QMetaObject, QObject, QPoint, QRect,
    QSize, QTime, QUrl, Qt)
from PySide6.QtGui import (QAction, QBrush, QColor, QConicalGradient,
    QCursor, QFont, QFontDatabase, QGradient,
    QIcon, QImage, QKeySequence, QLinearGradient,
    QPainter, QPalette, QPixmap, QRadialGradient,
    QTransform)
from PySide6.QtWidgets import (QApplication, QHBoxLayout, QLabel, QMainWindow,
    QMenu, QMenuBar, QPlainTextEdit, QPushButton,
    QSizePolicy, QSpacerItem, QStatusBar, QVBoxLayout,
    QWidget)

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(941, 711)
        self.menuActionBatch = QAction(MainWindow)
        self.menuActionBatch.setObjectName(u"menuActionBatch")
        self.menuActionBatch.setEnabled(False)
        self.menuActionRefresh = QAction(MainWindow)
        self.menuActionRefresh.setObjectName(u"menuActionRefresh")
        self.menu_view_reset = QAction(MainWindow)
        self.menu_view_reset.setObjectName(u"menu_view_reset")
        self.menuActionSelectProject = QAction(MainWindow)
        self.menuActionSelectProject.setObjectName(u"menuActionSelectProject")
        self.menuViewReloadStylesheet = QAction(MainWindow)
        self.menuViewReloadStylesheet.setObjectName(u"menuViewReloadStylesheet")
        self.menuViewReloadStylesheet.setEnabled(False)
        self.menu_developer_reload_stylesheet = QAction(MainWindow)
        self.menu_developer_reload_stylesheet.setObjectName(u"menu_developer_reload_stylesheet")
        self.menu_actions_select_project = QAction(MainWindow)
        self.menu_actions_select_project.setObjectName(u"menu_actions_select_project")
        self.menu_actions_refresh = QAction(MainWindow)
        self.menu_actions_refresh.setObjectName(u"menu_actions_refresh")
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.verticalLayout = QVBoxLayout(self.centralwidget)
        self.verticalLayout.setSpacing(3)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.verticalLayout.setContentsMargins(20, 10, 20, 15)
        self.main = QWidget(self.centralwidget)
        self.main.setObjectName(u"main")
        sizePolicy = QSizePolicy(QSizePolicy.Preferred, QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.main.sizePolicy().hasHeightForWidth())
        self.main.setSizePolicy(sizePolicy)
        self.verticalLayout_2 = QVBoxLayout(self.main)
        self.verticalLayout_2.setSpacing(15)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.verticalLayout_2.setContentsMargins(0, 20, 0, 0)
        self.label_10 = QLabel(self.main)
        self.label_10.setObjectName(u"label_10")
        self.label_10.setMinimumSize(QSize(200, 0))
        self.label_10.setAlignment(Qt.AlignCenter)

        self.verticalLayout_2.addWidget(self.label_10)

        self.horizontalLayout_6 = QHBoxLayout()
        self.horizontalLayout_6.setObjectName(u"horizontalLayout_6")
        self.verticalLayout_3 = QVBoxLayout()
        self.verticalLayout_3.setSpacing(4)
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.verticalLayout_3.setContentsMargins(-1, 0, -1, 0)
        self.horizontalLayout_2 = QHBoxLayout()
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.label = QLabel(self.main)
        self.label.setObjectName(u"label")
        sizePolicy1 = QSizePolicy(QSizePolicy.Fixed, QSizePolicy.Preferred)
        sizePolicy1.setHorizontalStretch(0)
        sizePolicy1.setVerticalStretch(0)
        sizePolicy1.setHeightForWidth(self.label.sizePolicy().hasHeightForWidth())
        self.label.setSizePolicy(sizePolicy1)
        self.label.setMinimumSize(QSize(100, 0))

        self.horizontalLayout_2.addWidget(self.label)

        self.system_time = QLabel(self.main)
        self.system_time.setObjectName(u"system_time")

        self.horizontalLayout_2.addWidget(self.system_time)


        self.verticalLayout_3.addLayout(self.horizontalLayout_2)

        self.horizontalLayout_3 = QHBoxLayout()
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.label_2 = QLabel(self.main)
        self.label_2.setObjectName(u"label_2")
        sizePolicy1.setHeightForWidth(self.label_2.sizePolicy().hasHeightForWidth())
        self.label_2.setSizePolicy(sizePolicy1)
        self.label_2.setMinimumSize(QSize(100, 0))

        self.horizontalLayout_3.addWidget(self.label_2)

        self.unreal_time = QLabel(self.main)
        self.unreal_time.setObjectName(u"unreal_time")

        self.horizontalLayout_3.addWidget(self.unreal_time)


        self.verticalLayout_3.addLayout(self.horizontalLayout_3)

        self.horizontalLayout_4 = QHBoxLayout()
        self.horizontalLayout_4.setObjectName(u"horizontalLayout_4")
        self.label_3 = QLabel(self.main)
        self.label_3.setObjectName(u"label_3")
        sizePolicy1.setHeightForWidth(self.label_3.sizePolicy().hasHeightForWidth())
        self.label_3.setSizePolicy(sizePolicy1)
        self.label_3.setMinimumSize(QSize(100, 0))

        self.horizontalLayout_4.addWidget(self.label_3)

        self.difference = QLabel(self.main)
        self.difference.setObjectName(u"difference")

        self.horizontalLayout_4.addWidget(self.difference)


        self.verticalLayout_3.addLayout(self.horizontalLayout_4)

        self.horizontalLayout_5 = QHBoxLayout()
        self.horizontalLayout_5.setObjectName(u"horizontalLayout_5")
        self.label_4 = QLabel(self.main)
        self.label_4.setObjectName(u"label_4")
        sizePolicy1.setHeightForWidth(self.label_4.sizePolicy().hasHeightForWidth())
        self.label_4.setSizePolicy(sizePolicy1)
        self.label_4.setMinimumSize(QSize(100, 0))

        self.horizontalLayout_5.addWidget(self.label_4)

        self.running_time = QLabel(self.main)
        self.running_time.setObjectName(u"running_time")

        self.horizontalLayout_5.addWidget(self.running_time)


        self.verticalLayout_3.addLayout(self.horizontalLayout_5)

        self.verticalSpacer_2 = QSpacerItem(0, 40, QSizePolicy.Minimum, QSizePolicy.Fixed)

        self.verticalLayout_3.addItem(self.verticalSpacer_2)

        self.horizontalLayout = QHBoxLayout()
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.reset = QPushButton(self.main)
        self.reset.setObjectName(u"reset")

        self.horizontalLayout.addWidget(self.reset)

        self.horizontalSpacer_2 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout.addItem(self.horizontalSpacer_2)


        self.verticalLayout_3.addLayout(self.horizontalLayout)

        self.verticalSpacer = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.verticalLayout_3.addItem(self.verticalSpacer)


        self.horizontalLayout_6.addLayout(self.verticalLayout_3)

        self.verticalLayout_4 = QVBoxLayout()
        self.verticalLayout_4.setSpacing(2)
        self.verticalLayout_4.setObjectName(u"verticalLayout_4")
        self.label_9 = QLabel(self.main)
        self.label_9.setObjectName(u"label_9")

        self.verticalLayout_4.addWidget(self.label_9)

        self.ticks = QPlainTextEdit(self.main)
        self.ticks.setObjectName(u"ticks")
        sizePolicy2 = QSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)
        sizePolicy2.setHorizontalStretch(0)
        sizePolicy2.setVerticalStretch(0)
        sizePolicy2.setHeightForWidth(self.ticks.sizePolicy().hasHeightForWidth())
        self.ticks.setSizePolicy(sizePolicy2)
        self.ticks.setVerticalScrollBarPolicy(Qt.ScrollBarAlwaysOff)
        self.ticks.setHorizontalScrollBarPolicy(Qt.ScrollBarAlwaysOff)

        self.verticalLayout_4.addWidget(self.ticks)


        self.horizontalLayout_6.addLayout(self.verticalLayout_4)

        self.horizontalLayout_6.setStretch(0, 5)
        self.horizontalLayout_6.setStretch(1, 5)

        self.verticalLayout_2.addLayout(self.horizontalLayout_6)


        self.verticalLayout.addWidget(self.main)

        self.verticalLayout.setStretch(0, 10)
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QMenuBar(MainWindow)
        self.menubar.setObjectName(u"menubar")
        self.menubar.setGeometry(QRect(0, 0, 941, 22))
        self.menu_view = QMenu(self.menubar)
        self.menu_view.setObjectName(u"menu_view")
        self.menu_developer = QMenu(self.menubar)
        self.menu_developer.setObjectName(u"menu_developer")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QStatusBar(MainWindow)
        self.statusbar.setObjectName(u"statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.menubar.addAction(self.menu_view.menuAction())
        self.menubar.addAction(self.menu_developer.menuAction())
        self.menu_view.addAction(self.menu_view_reset)
        self.menu_developer.addAction(self.menu_developer_reload_stylesheet)

        self.retranslateUi(MainWindow)

        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"PROXi Animation Clip Generator", None))
        self.menuActionBatch.setText(QCoreApplication.translate("MainWindow", u"Batch: Link and sync with ShotGrid", None))
#if QT_CONFIG(statustip)
        self.menuActionBatch.setStatusTip(QCoreApplication.translate("MainWindow", u"Batch tool for linking cameras to ShotGrid shots and syncing all data", None))
#endif // QT_CONFIG(statustip)
        self.menuActionRefresh.setText(QCoreApplication.translate("MainWindow", u"Refresh server data", None))
        self.menu_view_reset.setText(QCoreApplication.translate("MainWindow", u"Reset window", None))
        self.menuActionSelectProject.setText(QCoreApplication.translate("MainWindow", u"Select ShotGrid project", None))
        self.menuViewReloadStylesheet.setText(QCoreApplication.translate("MainWindow", u"Reload stylesheet", None))
        self.menu_developer_reload_stylesheet.setText(QCoreApplication.translate("MainWindow", u"Reload stylesheet", None))
        self.menu_actions_select_project.setText(QCoreApplication.translate("MainWindow", u"Select ShotGrid project", None))
        self.menu_actions_refresh.setText(QCoreApplication.translate("MainWindow", u"Refresh server data", None))
        self.label_10.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p><span style=\" font-size:16pt;\">System time debug</span></p></body></html>", None))
        self.label.setText(QCoreApplication.translate("MainWindow", u"System time:", None))
        self.system_time.setText("")
        self.label_2.setText(QCoreApplication.translate("MainWindow", u"Unreal time:", None))
        self.unreal_time.setText("")
        self.label_3.setText(QCoreApplication.translate("MainWindow", u"Difference:", None))
        self.difference.setText("")
        self.label_4.setText(QCoreApplication.translate("MainWindow", u"Running time:", None))
        self.running_time.setText("")
        self.reset.setText(QCoreApplication.translate("MainWindow", u"Reset", None))
        self.label_9.setText(QCoreApplication.translate("MainWindow", u"Incoming unreal ticks (delta time):", None))
        self.menu_view.setTitle(QCoreApplication.translate("MainWindow", u"View", None))
        self.menu_developer.setTitle(QCoreApplication.translate("MainWindow", u"Developer", None))
    # retranslateUi




import typing
if typing.TYPE_CHECKING:

    class _TypeHint:
        """Auto-generated type hinting class"""

        MainWindow: QMainWindow = QMainWindow()
        menuActionBatch: QAction = QAction(MainWindow)
        menuActionRefresh: QAction = QAction(MainWindow)
        menu_view_reset: QAction = QAction(MainWindow)
        menuActionSelectProject: QAction = QAction(MainWindow)
        menuViewReloadStylesheet: QAction = QAction(MainWindow)
        menu_developer_reload_stylesheet: QAction = QAction(MainWindow)
        menu_actions_select_project: QAction = QAction(MainWindow)
        menu_actions_refresh: QAction = QAction(MainWindow)
        centralwidget: QWidget = QWidget(MainWindow)
        verticalLayout: QVBoxLayout = QVBoxLayout(centralwidget)
        main: QWidget = QWidget(centralwidget)
        verticalLayout_2: QVBoxLayout = QVBoxLayout(main)
        label_10: QLabel = QLabel(main)
        horizontalLayout_6: QHBoxLayout = QHBoxLayout()
        verticalLayout_3: QVBoxLayout = QVBoxLayout()
        horizontalLayout_2: QHBoxLayout = QHBoxLayout()
        label: QLabel = QLabel(main)
        system_time: QLabel = QLabel(main)
        horizontalLayout_3: QHBoxLayout = QHBoxLayout()
        label_2: QLabel = QLabel(main)
        unreal_time: QLabel = QLabel(main)
        horizontalLayout_4: QHBoxLayout = QHBoxLayout()
        label_3: QLabel = QLabel(main)
        difference: QLabel = QLabel(main)
        horizontalLayout_5: QHBoxLayout = QHBoxLayout()
        label_4: QLabel = QLabel(main)
        running_time: QLabel = QLabel(main)
        verticalSpacer_2: QSpacerItem = QSpacerItem(0, 40, QSizePolicy.Minimum, QSizePolicy.Fixed)
        horizontalLayout: QHBoxLayout = QHBoxLayout()
        reset: QPushButton = QPushButton(main)
        horizontalSpacer_2: QSpacerItem = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)
        verticalSpacer: QSpacerItem = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)
        verticalLayout_4: QVBoxLayout = QVBoxLayout()
        label_9: QLabel = QLabel(main)
        ticks: QPlainTextEdit = QPlainTextEdit(main)
        menubar: QMenuBar = QMenuBar(MainWindow)
        menu_view: QMenu = QMenu(menubar)
        menu_developer: QMenu = QMenu(menubar)
        statusbar: QStatusBar = QStatusBar(MainWindow)
