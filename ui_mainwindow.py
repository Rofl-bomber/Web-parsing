# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'window.ui'
##
## Created by: Qt User Interface Compiler version 6.7.2
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import (QCoreApplication, QDate, QDateTime, QLocale,
    QMetaObject, QObject, QPoint, QRect,
    QSize, QTime, QUrl, Qt)
from PySide6.QtGui import (QBrush, QColor, QConicalGradient, QCursor,
    QFont, QFontDatabase, QGradient, QIcon,
    QImage, QKeySequence, QLinearGradient, QPainter,
    QPalette, QPixmap, QRadialGradient, QTransform)
from PySide6.QtWidgets import (QApplication, QCheckBox, QGridLayout, QGroupBox,
    QMainWindow, QPushButton, QSizePolicy, QSpacerItem,
    QVBoxLayout, QWidget)

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(293, 287)
        MainWindow.setMinimumSize(QSize(293, 287))
        MainWindow.setMaximumSize(QSize(293, 287))
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.gridLayout = QGridLayout(self.centralwidget)
        self.gridLayout.setObjectName(u"gridLayout")
        self.groupBox = QGroupBox(self.centralwidget)
        self.groupBox.setObjectName(u"groupBox")
        self.groupBox.setCheckable(False)
        self.gridLayout_2 = QGridLayout(self.groupBox)
        self.gridLayout_2.setObjectName(u"gridLayout_2")
        self.all_button = QCheckBox(self.groupBox)
        self.all_button.setObjectName(u"all_button")

        self.gridLayout_2.addWidget(self.all_button, 0, 0, 1, 1)

        self.verticalLayout_3 = QVBoxLayout()
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.button_2 = QCheckBox(self.groupBox)
        self.button_2.setObjectName(u"button_2")

        self.verticalLayout_3.addWidget(self.button_2)

        self.button_4 = QCheckBox(self.groupBox)
        self.button_4.setObjectName(u"button_4")

        self.verticalLayout_3.addWidget(self.button_4)

        self.button_6 = QCheckBox(self.groupBox)
        self.button_6.setObjectName(u"button_6")

        self.verticalLayout_3.addWidget(self.button_6)

        self.button_3 = QCheckBox(self.groupBox)
        self.button_3.setObjectName(u"button_3")

        self.verticalLayout_3.addWidget(self.button_3)

        self.button_5 = QCheckBox(self.groupBox)
        self.button_5.setObjectName(u"button_5")

        self.verticalLayout_3.addWidget(self.button_5)

        self.button_1 = QCheckBox(self.groupBox)
        self.button_1.setObjectName(u"button_1")
        self.button_1.setTristate(False)

        self.verticalLayout_3.addWidget(self.button_1)


        self.gridLayout_2.addLayout(self.verticalLayout_3, 3, 0, 1, 1)

        self.verticalSpacer = QSpacerItem(20, 10, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Fixed)

        self.gridLayout_2.addItem(self.verticalSpacer, 1, 0, 1, 1)


        self.gridLayout.addWidget(self.groupBox, 0, 0, 1, 1)

        self.open_button = QPushButton(self.centralwidget)
        self.open_button.setObjectName(u"open_button")
        self.open_button.setEnabled(False)
        self.open_button.setAutoDefault(False)
        self.open_button.setFlat(False)

        self.gridLayout.addWidget(self.open_button, 2, 0, 1, 1)

        self.parser_button = QPushButton(self.centralwidget)
        self.parser_button.setObjectName(u"parser_button")

        self.gridLayout.addWidget(self.parser_button, 1, 0, 1, 1)

        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)
        self.all_button.clicked["bool"].connect(self.button_2.setChecked)
        self.all_button.clicked["bool"].connect(self.button_4.setChecked)
        self.all_button.clicked["bool"].connect(self.button_6.setChecked)
        self.all_button.clicked["bool"].connect(self.button_3.setChecked)
        self.all_button.clicked["bool"].connect(self.button_5.setChecked)
        self.all_button.clicked["bool"].connect(self.button_1.setChecked)

        self.open_button.setDefault(False)


        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"\u041f\u043e\u043b\u0443\u0447\u0435\u043d\u0438\u0435 \u0441\u043a\u0438\u0434\u043e\u043a", None))
        self.groupBox.setTitle(QCoreApplication.translate("MainWindow", u"\u041c\u0430\u0433\u0430\u0437\u0438\u043d\u044b", None))
        self.all_button.setText(QCoreApplication.translate("MainWindow", u"\u0412\u044b\u0431\u0440\u0430\u0442\u044c \u0432\u0441\u0435 \u043c\u0430\u0433\u0430\u0437\u0438\u043d\u044b", None))
        self.button_2.setText(QCoreApplication.translate("MainWindow", u"\u041b\u0430\u043c\u043e\u0434\u0430", None))
        self.button_4.setText(QCoreApplication.translate("MainWindow", u"\u041c\u0435\u0433\u0430\u043c\u0430\u0440\u043a\u0435\u0442", None))
        self.button_6.setText(QCoreApplication.translate("MainWindow", u"\u0410\u043b\u0438\u042d\u043a\u0441\u043f\u0440\u0435\u0441\u0441", None))
        self.button_3.setText(QCoreApplication.translate("MainWindow", u"\u042f\u043d\u0434\u0435\u043a\u0441 \u041c\u0430\u0440\u043a\u0435\u0442", None))
        self.button_5.setText(QCoreApplication.translate("MainWindow", u"\u042d\u043b\u044c\u0434\u043e\u0440\u0430\u0434\u043e", None))
        self.button_1.setText(QCoreApplication.translate("MainWindow", u"\u041c.\u0412\u0438\u0434\u0435\u043e", None))
        self.open_button.setText(QCoreApplication.translate("MainWindow", u"\u041e\u0442\u043a\u0440\u044b\u0442\u044c \u0444\u0430\u0439\u043b", None))
        self.parser_button.setText(QCoreApplication.translate("MainWindow", u"\u041e\u0431\u0440\u0430\u0431\u043e\u0442\u0430\u0442\u044c \u0441\u0430\u0439\u0442", None))
    # retranslateUi

