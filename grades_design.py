# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'grades_design.ui'
#
# Created by: PyQt5 UI code generator 5.13.2
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(1712, 963)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(1)
        sizePolicy.setVerticalStretch(1)
        sizePolicy.setHeightForWidth(MainWindow.sizePolicy().hasHeightForWidth())
        MainWindow.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setPointSize(12)
        MainWindow.setFont(font)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")

        self.verticalLayoutWidget = QtWidgets.QWidget(self.centralwidget)
        self.verticalLayoutWidget.setGeometry(QtCore.QRect(10, 150, 320, 500))
        self.verticalLayoutWidget.setObjectName("verticalLayoutWidget")

        self.verticalLayout_10 = QtWidgets.QVBoxLayout(self.verticalLayoutWidget)
        self.verticalLayout_10.setContentsMargins(5, 50, 10, 100)
        self.verticalLayout_10.setSpacing(13)
        self.verticalLayout_10.setObjectName("verticalLayout_10")
        self.formLayout_10 = QtWidgets.QFormLayout()
        self.formLayout_10.setVerticalSpacing(9)
        self.formLayout_10.setObjectName("formLayout_10")
        self.label_40 = QtWidgets.QLabel(self.verticalLayoutWidget)
        self.label_40.setObjectName("label_40")
        self.formLayout_10.setWidget(0, QtWidgets.QFormLayout.LabelRole, self.label_40)
        self.label_41 = QtWidgets.QLabel(self.verticalLayoutWidget)
        self.label_41.setObjectName("label_41")
        self.formLayout_10.setWidget(1, QtWidgets.QFormLayout.LabelRole, self.label_41)
        self.label_42 = QtWidgets.QLabel(self.verticalLayoutWidget)
        self.label_42.setObjectName("label_42")
        self.formLayout_10.setWidget(2, QtWidgets.QFormLayout.LabelRole, self.label_42)
        self.label_43 = QtWidgets.QLabel(self.verticalLayoutWidget)
        self.label_43.setObjectName("label_43")
        self.formLayout_10.setWidget(3, QtWidgets.QFormLayout.LabelRole, self.label_43)
        self.lineEdit_20 = QtWidgets.QLineEdit(self.verticalLayoutWidget)
        self.lineEdit_20.setObjectName("lineEdit_20")
        self.formLayout_10.setWidget(1, QtWidgets.QFormLayout.FieldRole, self.lineEdit_20)
        self.lineEdit_21 = QtWidgets.QLineEdit(self.verticalLayoutWidget)
        self.lineEdit_21.setObjectName("lineEdit_21")
        self.formLayout_10.setWidget(2, QtWidgets.QFormLayout.FieldRole, self.lineEdit_21)
        self.lineEdit_22 = QtWidgets.QLineEdit(self.verticalLayoutWidget)
        self.lineEdit_22.setObjectName("lineEdit_22")
        self.formLayout_10.setWidget(3, QtWidgets.QFormLayout.FieldRole, self.lineEdit_22)
        self.spinBox = QtWidgets.QSpinBox(self.verticalLayoutWidget)
        self.spinBox.setMinimum(2)
        self.spinBox.setMaximum(15)
        self.spinBox.setProperty("value", 8)
        self.spinBox.setObjectName("spinBox")
        self.formLayout_10.setWidget(0, QtWidgets.QFormLayout.FieldRole, self.spinBox)
        self.verticalLayout_10.addLayout(self.formLayout_10)
        self.pushButton_10 = QtWidgets.QPushButton(self.verticalLayoutWidget)
        self.pushButton_10.setObjectName("pushButton_10")
        self.verticalLayout_10.addWidget(self.pushButton_10)
        self.label_44 = QtWidgets.QLabel(self.verticalLayoutWidget)
        self.label_44.setObjectName("label_44")
        self.verticalLayout_10.addWidget(self.label_44)
        self.label_45 = QtWidgets.QLabel(self.verticalLayoutWidget)
        self.label_45.setObjectName("label_45")
        self.verticalLayout_10.addWidget(self.label_45)
        self.label_46 = QtWidgets.QLabel(self.verticalLayoutWidget)
        self.label_46.setObjectName("label_46")
        self.verticalLayout_10.addWidget(self.label_46)

        self.verticalLayoutWidget_2 = QtWidgets.QWidget(self.centralwidget)
        self.verticalLayoutWidget_2.setGeometry(QtCore.QRect(10, 600, 320, 250))
        self.verticalLayoutWidget_2.setObjectName("verticalLayoutWidget_2")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout(self.verticalLayoutWidget_2)
        self.verticalLayout_2.setContentsMargins(5, 10, 5, 10)
        self.verticalLayout_2.setSpacing(10)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.textEdit = QtWidgets.QTextEdit(self.verticalLayoutWidget_2)
        self.textEdit.setPlaceholderText("1")
        self.textEdit.setObjectName("textEdit")
        self.verticalLayout_2.addWidget(self.textEdit)
        self.comboBox = QtWidgets.QComboBox(self.verticalLayoutWidget_2)
        self.comboBox.setObjectName("comboBox")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.verticalLayout_2.addWidget(self.comboBox)
        self.label = QtWidgets.QLabel(self.verticalLayoutWidget_2)
        self.label.setText("")
        self.label.setObjectName("label")
        self.verticalLayout_2.addWidget(self.label)
        self.comboBox_2 = QtWidgets.QComboBox(self.verticalLayoutWidget_2)
        self.comboBox_2.setObjectName("comboBox_2")
        self.comboBox_2.addItem("")
        self.comboBox_2.addItem("")
        self.comboBox_2.addItem("")
        self.comboBox_2.addItem("")
        self.verticalLayout_2.addWidget(self.comboBox_2)
        self.horizontalLayoutWidget = QtWidgets.QWidget(self.centralwidget)
        self.horizontalLayoutWidget.setGeometry(QtCore.QRect(330, 30, 1300, 40))
        self.horizontalLayoutWidget.setObjectName("horizontalLayoutWidget")
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.horizontalLayoutWidget)
        self.horizontalLayout.setContentsMargins(10, 0, 10, 0)
        self.horizontalLayout.setSpacing(10)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.pushButton = QtWidgets.QPushButton(self.horizontalLayoutWidget)
        self.pushButton.setObjectName("pushButton")
        self.horizontalLayout.addWidget(self.pushButton)
        self.pushButton_2 = QtWidgets.QPushButton(self.horizontalLayoutWidget)
        self.pushButton_2.setObjectName("pushButton_2")
        self.horizontalLayout.addWidget(self.pushButton_2)
        self.pushButton_3 = QtWidgets.QPushButton(self.horizontalLayoutWidget)
        self.pushButton_3.setObjectName("pushButton_3")
        self.horizontalLayout.addWidget(self.pushButton_3)
        self.pushButton_4 = QtWidgets.QPushButton(self.horizontalLayoutWidget)
        self.pushButton_4.setObjectName("pushButton_4")
        self.horizontalLayout.addWidget(self.pushButton_4)
        self.horizontalLayout.setStretch(0, 1)
        self.horizontalLayout.setStretch(1, 1)
        self.horizontalLayout.setStretch(2, 2)
        self.horizontalLayout.setStretch(3, 2)

        self.widget = QtWidgets.QWidget(self.centralwidget)
        self.widget.setGeometry(QtCore.QRect(330, 100, 1350, 850))
        self.widget.setObjectName("widget")

        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 800, 22))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Grades"))

        self.label_40.setText(_translate("MainWindow", "grade=(max-min) /"))
        self.label_41.setText(_translate("MainWindow", "Фамилия"))
        self.label_42.setText(_translate("MainWindow", "Имя"))
        self.label_43.setText(_translate("MainWindow", "Отчество"))
        self.pushButton_10.setText(_translate("MainWindow", "Отобразить"))
        self.label_44.setText(_translate("MainWindow", "Коэф. Зн. :"))
        self.label_45.setText(_translate("MainWindow", "Зар. плата :"))
        self.label_46.setText(_translate("MainWindow", "Отчет :"))

        self.comboBox.setItemText(0, _translate("MainWindow", "RUB"))
        self.comboBox.setItemText(1, _translate("MainWindow", "USD"))
        self.comboBox.setItemText(2, _translate("MainWindow", "EUR"))
        self.comboBox.setItemText(3, _translate("MainWindow", "GBP"))
        self.comboBox_2.setItemText(0, _translate("MainWindow", "USD"))
        self.comboBox_2.setItemText(1, _translate("MainWindow", "EUR"))
        self.comboBox_2.setItemText(2, _translate("MainWindow", "GBP"))
        self.comboBox_2.setItemText(3, _translate("MainWindow", "RUB"))
        self.pushButton.setText(_translate("MainWindow", "Построить"))
        self.pushButton_2.setText(_translate("MainWindow", "Отчет"))
        self.pushButton_3.setText(_translate("MainWindow", "Добавить сотрудника"))
        self.pushButton_4.setText(_translate("MainWindow", "Добавить должность"))
