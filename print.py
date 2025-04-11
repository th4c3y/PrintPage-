# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'print.ui'
##
## Created by: Qt User Interface Compiler version 6.8.1
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
from PySide6.QtWidgets import (QAbstractButton, QApplication, QCheckBox, QComboBox,
    QDialogButtonBox, QDockWidget, QDoubleSpinBox, QGridLayout,
    QGroupBox, QHBoxLayout, QLabel, QLineEdit,
    QListWidget, QListWidgetItem, QPushButton, QSizePolicy,
    QSlider, QSpacerItem, QTextEdit, QToolButton,
    QVBoxLayout, QWidget)

class Ui_PrintForm(object):
    def setupUi(self, PrintForm):
        if not PrintForm.objectName():
            PrintForm.setObjectName(u"PrintForm")
        PrintForm.resize(563, 481)
        PrintForm.setAcceptDrops(True)
        icon = QIcon(QIcon.fromTheme(QIcon.ThemeIcon.Printer))
        PrintForm.setWindowIcon(icon)
        self.horizontalLayout = QHBoxLayout(PrintForm)
        self.horizontalLayout.setSpacing(8)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.horizontalLayout.setContentsMargins(-1, 8, -1, 8)
        self.listWidget = QListWidget(PrintForm)
        self.listWidget.setObjectName(u"listWidget")

        self.horizontalLayout.addWidget(self.listWidget)

        self.verticalLayout_2 = QVBoxLayout()
        self.verticalLayout_2.setSpacing(9)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.pushButton_2 = QPushButton(PrintForm)
        self.pushButton_2.setObjectName(u"pushButton_2")

        self.verticalLayout_2.addWidget(self.pushButton_2)

        self.pushButton_3 = QPushButton(PrintForm)
        self.pushButton_3.setObjectName(u"pushButton_3")

        self.verticalLayout_2.addWidget(self.pushButton_3)

        self.pushButton_4 = QPushButton(PrintForm)
        self.pushButton_4.setObjectName(u"pushButton_4")

        self.verticalLayout_2.addWidget(self.pushButton_4)

        self.pushButton = QPushButton(PrintForm)
        self.pushButton.setObjectName(u"pushButton")

        self.verticalLayout_2.addWidget(self.pushButton)

        self.label_8 = QLabel(PrintForm)
        self.label_8.setObjectName(u"label_8")

        self.verticalLayout_2.addWidget(self.label_8)

        self.groupBox = QGroupBox(PrintForm)
        self.groupBox.setObjectName(u"groupBox")
        self.gridLayout = QGridLayout(self.groupBox)
        self.gridLayout.setObjectName(u"gridLayout")
        self.gridLayout.setHorizontalSpacing(3)
        self.gridLayout.setVerticalSpacing(4)
        self.gridLayout.setContentsMargins(4, 2, 4, 3)
        self.label_4 = QLabel(self.groupBox)
        self.label_4.setObjectName(u"label_4")
        self.label_4.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.gridLayout.addWidget(self.label_4, 4, 1, 1, 1)

        self.verticalSpacer = QSpacerItem(20, 40, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.gridLayout.addItem(self.verticalSpacer, 3, 0, 1, 1)

        self.verticalSpacer_5 = QSpacerItem(20, 40, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.gridLayout.addItem(self.verticalSpacer_5, 0, 0, 1, 1)

        self.label_5 = QLabel(self.groupBox)
        self.label_5.setObjectName(u"label_5")
        self.label_5.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.gridLayout.addWidget(self.label_5, 7, 1, 1, 1)

        self.label_3 = QLabel(self.groupBox)
        self.label_3.setObjectName(u"label_3")
        self.label_3.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.gridLayout.addWidget(self.label_3, 10, 1, 1, 1)

        self.doubleSpinBox = QDoubleSpinBox(self.groupBox)
        self.doubleSpinBox.setObjectName(u"doubleSpinBox")
        self.doubleSpinBox.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.doubleSpinBox.setDecimals(0)
        self.doubleSpinBox.setMinimum(1.000000000000000)
        self.doubleSpinBox.setMaximum(10000.000000000000000)
        self.doubleSpinBox.setValue(1.000000000000000)

        self.gridLayout.addWidget(self.doubleSpinBox, 12, 0, 1, 1)

        self.checkBox_3 = QCheckBox(self.groupBox)
        self.checkBox_3.setObjectName(u"checkBox_3")

        self.gridLayout.addWidget(self.checkBox_3, 15, 1, 1, 1)

        self.label_2 = QLabel(self.groupBox)
        self.label_2.setObjectName(u"label_2")
        self.label_2.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.gridLayout.addWidget(self.label_2, 10, 0, 1, 1)

        self.label_6 = QLabel(self.groupBox)
        self.label_6.setObjectName(u"label_6")
        self.label_6.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.gridLayout.addWidget(self.label_6, 1, 0, 1, 2)

        self.comboBox = QComboBox(self.groupBox)
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.setObjectName(u"comboBox")
        self.comboBox.setMaxVisibleItems(12)
        self.comboBox.setMaxCount(12)
        self.comboBox.setInsertPolicy(QComboBox.InsertPolicy.InsertBeforeCurrent)
        self.comboBox.setSizeAdjustPolicy(QComboBox.SizeAdjustPolicy.AdjustToMinimumContentsLengthWithIcon)
        self.comboBox.setMinimumContentsLength(4)
        self.comboBox.setFrame(True)

        self.gridLayout.addWidget(self.comboBox, 5, 0, 1, 1)

        self.verticalSpacer_6 = QSpacerItem(20, 40, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.gridLayout.addItem(self.verticalSpacer_6, 18, 0, 1, 1)

        self.comboBox_6 = QComboBox(self.groupBox)
        self.comboBox_6.addItem("")
        self.comboBox_6.addItem("")
        self.comboBox_6.addItem("")
        self.comboBox_6.setObjectName(u"comboBox_6")
        self.comboBox_6.setEnabled(False)
        self.comboBox_6.setDuplicatesEnabled(False)

        self.gridLayout.addWidget(self.comboBox_6, 8, 0, 1, 1)

        self.checkBox_4 = QCheckBox(self.groupBox)
        self.checkBox_4.setObjectName(u"checkBox_4")

        self.gridLayout.addWidget(self.checkBox_4, 14, 0, 1, 1)

        self.label_7 = QLabel(self.groupBox)
        self.label_7.setObjectName(u"label_7")

        self.gridLayout.addWidget(self.label_7, 7, 0, 1, 1, Qt.AlignmentFlag.AlignHCenter)

        self.dockWidget_2 = QDockWidget(self.groupBox)
        self.dockWidget_2.setObjectName(u"dockWidget_2")
        self.dockWidget_2.setMinimumSize(QSize(1, 1))
        self.dockWidget_2.setMaximumSize(QSize(140, 140))
        self.dockWidget_2.setInputMethodHints(Qt.InputMethodHint.ImhDigitsOnly)
        self.dockWidget_2.setFloating(True)
        self.dockWidget_2.setAllowedAreas(Qt.DockWidgetArea.TopDockWidgetArea)
        self.dockWidgetContents_2 = QWidget()
        self.dockWidgetContents_2.setObjectName(u"dockWidgetContents_2")
        self.dockWidgetContents_2.setInputMethodHints(Qt.InputMethodHint.ImhDigitsOnly)
        self.verticalLayout = QVBoxLayout(self.dockWidgetContents_2)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.label_9 = QLabel(self.dockWidgetContents_2)
        self.label_9.setObjectName(u"label_9")
        self.label_9.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.verticalLayout.addWidget(self.label_9, 0, Qt.AlignmentFlag.AlignHCenter)

        self.lineEdit = QLineEdit(self.dockWidgetContents_2)
        self.lineEdit.setObjectName(u"lineEdit")
        self.lineEdit.setMaximumSize(QSize(100, 20))
        self.lineEdit.setInputMethodHints(Qt.InputMethodHint.ImhDigitsOnly)
        self.lineEdit.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.verticalLayout.addWidget(self.lineEdit, 0, Qt.AlignmentFlag.AlignHCenter)

        self.verticalSpacer_7 = QSpacerItem(2, 10, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.verticalLayout.addItem(self.verticalSpacer_7)

        self.label_10 = QLabel(self.dockWidgetContents_2)
        self.label_10.setObjectName(u"label_10")
        self.label_10.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.verticalLayout.addWidget(self.label_10, 0, Qt.AlignmentFlag.AlignHCenter)

        self.lineEdit_2 = QLineEdit(self.dockWidgetContents_2)
        self.lineEdit_2.setObjectName(u"lineEdit_2")
        self.lineEdit_2.setMaximumSize(QSize(100, 20))
        self.lineEdit_2.setInputMethodHints(Qt.InputMethodHint.ImhDigitsOnly)
        self.lineEdit_2.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.verticalLayout.addWidget(self.lineEdit_2, 0, Qt.AlignmentFlag.AlignHCenter)

        self.buttonBox = QDialogButtonBox(self.dockWidgetContents_2)
        self.buttonBox.setObjectName(u"buttonBox")
        self.buttonBox.setMaximumSize(QSize(100, 16777215))
        self.buttonBox.setStandardButtons(QDialogButtonBox.StandardButton.Ok)
        self.buttonBox.setCenterButtons(True)

        self.verticalLayout.addWidget(self.buttonBox, 0, Qt.AlignmentFlag.AlignHCenter)

        self.dockWidget_2.setWidget(self.dockWidgetContents_2)

        self.gridLayout.addWidget(self.dockWidget_2, 16, 1, 1, 1)

        self.comboBox_3 = QComboBox(self.groupBox)
        self.comboBox_3.addItem("")
        self.comboBox_3.addItem("")
        self.comboBox_3.addItem("")
        self.comboBox_3.addItem("")
        self.comboBox_3.setObjectName(u"comboBox_3")

        self.gridLayout.addWidget(self.comboBox_3, 5, 1, 1, 1)

        self.comboBox_5 = QComboBox(self.groupBox)
        self.comboBox_5.setObjectName(u"comboBox_5")
        self.comboBox_5.setMaxVisibleItems(100)
        self.comboBox_5.setSizeAdjustPolicy(QComboBox.SizeAdjustPolicy.AdjustToMinimumContentsLengthWithIcon)
        self.comboBox_5.setMinimumContentsLength(5)

        self.gridLayout.addWidget(self.comboBox_5, 2, 0, 1, 2)

        self.dockWidget = QDockWidget(self.groupBox)
        self.dockWidget.setObjectName(u"dockWidget")
        self.dockWidget.setMinimumSize(QSize(1, 1))
        self.dockWidget.setFloating(True)
        self.dockWidget.setAllowedAreas(Qt.DockWidgetArea.BottomDockWidgetArea|Qt.DockWidgetArea.TopDockWidgetArea)
        self.dockWidgetContents = QWidget()
        self.dockWidgetContents.setObjectName(u"dockWidgetContents")
        self.verticalLayout_3 = QVBoxLayout(self.dockWidgetContents)
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.textEdit = QTextEdit(self.dockWidgetContents)
        self.textEdit.setObjectName(u"textEdit")
        self.textEdit.setTabletTracking(False)
        self.textEdit.setTabChangesFocus(False)
        self.textEdit.setLineWrapMode(QTextEdit.LineWrapMode.NoWrap)
        self.textEdit.setTabStopDistance(500.000000000000000)
        self.textEdit.setAcceptRichText(False)
        self.textEdit.setCursorWidth(2)

        self.verticalLayout_3.addWidget(self.textEdit)

        self.dockWidget.setWidget(self.dockWidgetContents)

        self.gridLayout.addWidget(self.dockWidget, 16, 0, 1, 1)

        self.label = QLabel(self.groupBox)
        self.label.setObjectName(u"label")
        self.label.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.gridLayout.addWidget(self.label, 4, 0, 1, 1)

        self.comboBox_2 = QComboBox(self.groupBox)
        self.comboBox_2.addItem("")
        self.comboBox_2.addItem("")
        self.comboBox_2.addItem("")
        self.comboBox_2.setObjectName(u"comboBox_2")

        self.gridLayout.addWidget(self.comboBox_2, 12, 1, 1, 1)

        self.verticalSpacer_4 = QSpacerItem(20, 40, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.gridLayout.addItem(self.verticalSpacer_4, 9, 1, 1, 1)

        self.checkBox = QCheckBox(self.groupBox)
        self.checkBox.setObjectName(u"checkBox")

        self.gridLayout.addWidget(self.checkBox, 15, 0, 1, 1)

        self.checkBox_2 = QCheckBox(self.groupBox)
        self.checkBox_2.setObjectName(u"checkBox_2")

        self.gridLayout.addWidget(self.checkBox_2, 14, 1, 1, 1)

        self.comboBox_4 = QComboBox(self.groupBox)
        self.comboBox_4.addItem("")
        self.comboBox_4.addItem("")
        self.comboBox_4.addItem("")
        self.comboBox_4.addItem("")
        self.comboBox_4.setObjectName(u"comboBox_4")

        self.gridLayout.addWidget(self.comboBox_4, 8, 1, 1, 1)

        self.verticalSpacer_2 = QSpacerItem(20, 40, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.gridLayout.addItem(self.verticalSpacer_2, 6, 0, 1, 1)

        self.verticalSpacer_3 = QSpacerItem(20, 40, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.gridLayout.addItem(self.verticalSpacer_3, 13, 0, 1, 1)

        self.horizontalSlider = QSlider(self.groupBox)
        self.horizontalSlider.setObjectName(u"horizontalSlider")
        self.horizontalSlider.setMaximumSize(QSize(200, 4))
        self.horizontalSlider.setMinimum(90)
        self.horizontalSlider.setMaximum(100)
        self.horizontalSlider.setPageStep(10)
        self.horizontalSlider.setValue(100)
        self.horizontalSlider.setOrientation(Qt.Orientation.Horizontal)
        self.horizontalSlider.setTickPosition(QSlider.TickPosition.TicksBelow)
        self.horizontalSlider.setTickInterval(1)

        self.gridLayout.addWidget(self.horizontalSlider, 19, 0, 1, 2)

        self.comboBox.raise_()
        self.label.raise_()
        self.label_4.raise_()
        self.comboBox_5.raise_()
        self.label_6.raise_()
        self.doubleSpinBox.raise_()
        self.label_2.raise_()
        self.comboBox_3.raise_()
        self.label_7.raise_()
        self.comboBox_6.raise_()
        self.label_5.raise_()
        self.comboBox_4.raise_()
        self.label_3.raise_()
        self.comboBox_2.raise_()
        self.checkBox_2.raise_()
        self.dockWidget.raise_()
        self.dockWidget_2.raise_()
        self.checkBox_3.raise_()
        self.checkBox.raise_()
        self.checkBox_4.raise_()
        self.horizontalSlider.raise_()

        self.verticalLayout_2.addWidget(self.groupBox)

        self.toolButton = QToolButton(PrintForm)
        self.toolButton.setObjectName(u"toolButton")
        self.toolButton.setStyleSheet(u"color: rgb(95, 95, 95);")
        self.toolButton.setAutoRaise(True)

        self.verticalLayout_2.addWidget(self.toolButton, 0, Qt.AlignmentFlag.AlignHCenter)


        self.horizontalLayout.addLayout(self.verticalLayout_2)

        self.horizontalLayout.setStretch(0, 9)
        self.horizontalLayout.setStretch(1, 2)
        QWidget.setTabOrder(self.pushButton_2, self.pushButton_3)
        QWidget.setTabOrder(self.pushButton_3, self.pushButton)
        QWidget.setTabOrder(self.pushButton, self.comboBox_5)
        QWidget.setTabOrder(self.comboBox_5, self.comboBox)
        QWidget.setTabOrder(self.comboBox, self.comboBox_3)
        QWidget.setTabOrder(self.comboBox_3, self.comboBox_6)
        QWidget.setTabOrder(self.comboBox_6, self.comboBox_4)
        QWidget.setTabOrder(self.comboBox_4, self.doubleSpinBox)
        QWidget.setTabOrder(self.doubleSpinBox, self.comboBox_2)
        QWidget.setTabOrder(self.comboBox_2, self.checkBox_2)
        QWidget.setTabOrder(self.checkBox_2, self.toolButton)
        QWidget.setTabOrder(self.toolButton, self.listWidget)


        self.retranslateUi(PrintForm)

        self.comboBox_2.setCurrentIndex(1)


        QMetaObject.connectSlotsByName(PrintForm)
    # setupUi

    def retranslateUi(self, PrintForm):
        PrintForm.setWindowTitle(QCoreApplication.translate("PrintForm", u"\u6253\u5370 \uff08\u543e\u7231\u7834\u89e3 by th4c3y\uff09", None))
        self.pushButton_2.setText(QCoreApplication.translate("PrintForm", u"\u6dfb\u52a0\u6587\u4ef6", None))
        self.pushButton_3.setText(QCoreApplication.translate("PrintForm", u"\u6e05\u7a7a", None))
        self.pushButton_4.setText(QCoreApplication.translate("PrintForm", u"\u6253\u5370\u9884\u89c8", None))
        self.pushButton.setText(QCoreApplication.translate("PrintForm", u"\u6253\u5370", None))
        self.label_8.setText(QCoreApplication.translate("PrintForm", u"\u51c6\u5907\u5c31\u7eea......", None))
        self.groupBox.setTitle(QCoreApplication.translate("PrintForm", u"\u6253\u5370\u9009\u9879", None))
        self.label_4.setText(QCoreApplication.translate("PrintForm", u"\u53cc\u9762\u6253\u5370", None))
        self.label_5.setText(QCoreApplication.translate("PrintForm", u"\u5c45\u4e2d\u65b9\u5f0f", None))
        self.label_3.setText(QCoreApplication.translate("PrintForm", u"\u6253\u5370\u5206\u8fa8\u7387", None))
        self.doubleSpinBox.setPrefix("")
        self.doubleSpinBox.setSuffix(QCoreApplication.translate("PrintForm", u"\u4efd", None))
        self.checkBox_3.setText(QCoreApplication.translate("PrintForm", u"\u88c1\u526a\u7ebf", None))
        self.label_2.setText(QCoreApplication.translate("PrintForm", u"\u6253\u5370\u4efd\u6570", None))
        self.label_6.setText(QCoreApplication.translate("PrintForm", u"\u6253\u5370\u673a\u9009\u62e9", None))
        self.comboBox.setItemText(0, QCoreApplication.translate("PrintForm", u"A4", None))
        self.comboBox.setItemText(1, QCoreApplication.translate("PrintForm", u"A4\u4e24\u7248", None))
        self.comboBox.setItemText(2, QCoreApplication.translate("PrintForm", u"A4\u4e09\u7248", None))
        self.comboBox.setItemText(3, QCoreApplication.translate("PrintForm", u"A4\u56db\u7248-2*2", None))
        self.comboBox.setItemText(4, QCoreApplication.translate("PrintForm", u"A4\u516d\u7248-2*3", None))
        self.comboBox.setItemText(5, QCoreApplication.translate("PrintForm", u"A5", None))
        self.comboBox.setItemText(6, QCoreApplication.translate("PrintForm", u"A5\u4e24\u7248", None))
        self.comboBox.setItemText(7, QCoreApplication.translate("PrintForm", u"A5\u56db\u7248-2*2", None))
        self.comboBox.setItemText(8, QCoreApplication.translate("PrintForm", u"\u81ea\u5b9a\u4e49\u7eb8\u5f20", None))

        self.comboBox_6.setItemText(0, QCoreApplication.translate("PrintForm", u"\u81ea\u52a8\u65cb\u8f6c", None))
        self.comboBox_6.setItemText(1, QCoreApplication.translate("PrintForm", u"\u7eb5\u5411", None))
        self.comboBox_6.setItemText(2, QCoreApplication.translate("PrintForm", u"\u6a2a\u5411", None))

        self.checkBox_4.setText(QCoreApplication.translate("PrintForm", u"\u590d\u5236\u9875\u9762*2", None))
        self.label_7.setText(QCoreApplication.translate("PrintForm", u"\u9875\u9762\u65b9\u5411", None))
        self.dockWidget_2.setWindowTitle(QCoreApplication.translate("PrintForm", u"\u81ea\u5b9a\u4e49\u7eb8\u5f20\u5927\u5c0f", None))
        self.label_9.setText(QCoreApplication.translate("PrintForm", u"\u8f93\u5165\u7eb8\u5f20\u5bbd\u5ea6mm", None))
        self.label_10.setText(QCoreApplication.translate("PrintForm", u"\u8f93\u5165\u7eb8\u5f20\u9ad8\u5ea6mm", None))
        self.comboBox_3.setItemText(0, QCoreApplication.translate("PrintForm", u"\u5355\u9762\u6253\u5370", None))
        self.comboBox_3.setItemText(1, QCoreApplication.translate("PrintForm", u"\u957f\u8fb9\u7ffb\u8f6c", None))
        self.comboBox_3.setItemText(2, QCoreApplication.translate("PrintForm", u"\u77ed\u8fb9\u7ffb\u8f6c", None))
        self.comboBox_3.setItemText(3, QCoreApplication.translate("PrintForm", u"\u81ea\u52a8\u9009\u62e9", None))

        self.dockWidget.setWindowTitle(QCoreApplication.translate("PrintForm", u"\u8def\u5f84\u7c98\u8d34", None))
        self.textEdit.setPlaceholderText(QCoreApplication.translate("PrintForm", u"\u7c98\u8d34\u8def\u5f84\u5230\u6b64\u5904\uff0c\u4e00\u884c\u4e00\u4e2a", None))
        self.label.setText(QCoreApplication.translate("PrintForm", u"\u7eb8\u5f20\u5927\u5c0f", None))
        self.comboBox_2.setItemText(0, QCoreApplication.translate("PrintForm", u"150dpi", None))
        self.comboBox_2.setItemText(1, QCoreApplication.translate("PrintForm", u"300dpi", None))
        self.comboBox_2.setItemText(2, QCoreApplication.translate("PrintForm", u"600dpi", None))

        self.checkBox.setText(QCoreApplication.translate("PrintForm", u"\u7070\u5ea6\u6253\u5370", None))
        self.checkBox_2.setText(QCoreApplication.translate("PrintForm", u"\u5408\u5e76\u9875\u9762", None))
        self.comboBox_4.setItemText(0, QCoreApplication.translate("PrintForm", u"\u6c34\u5e73\u5c45\u4e2d", None))
        self.comboBox_4.setItemText(1, QCoreApplication.translate("PrintForm", u"\u9760\u53f3\u5c45\u4e2d", None))
        self.comboBox_4.setItemText(2, QCoreApplication.translate("PrintForm", u"\u5782\u76f4\u4e24\u7aef", None))
        self.comboBox_4.setItemText(3, QCoreApplication.translate("PrintForm", u"\u65e0", None))

#if QT_CONFIG(tooltip)
        self.horizontalSlider.setToolTip(QCoreApplication.translate("PrintForm", u"<html><head/><body><p>\u9875\u9762\u7f29\u653e</p></body></html>", None))
#endif // QT_CONFIG(tooltip)
        self.toolButton.setText(QCoreApplication.translate("PrintForm", u"\u4f7f\u7528\u7cfb\u7edf\u5bf9\u8bdd\u6846\u8fdb\u884c\u6253\u5370..", None))
    # retranslateUi

