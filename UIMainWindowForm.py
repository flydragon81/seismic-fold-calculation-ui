# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'ui/UIMainWindowForm.ui'
#
# Created by: PyQt5 UI code generator 5.15.2
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(800, 600)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 800, 22))
        self.menubar.setObjectName("menubar")
        self.menuFile = QtWidgets.QMenu(self.menubar)
        self.menuFile.setObjectName("menuFile")
        self.menuHelp = QtWidgets.QMenu(self.menubar)
        self.menuHelp.setObjectName("menuHelp")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)
        self.actionNew_project = QtWidgets.QAction(MainWindow)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(":/sfc-ui/icons/folder--plus-24.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.actionNew_project.setIcon(icon)
        self.actionNew_project.setObjectName("actionNew_project")
        self.actionOpen_project = QtWidgets.QAction(MainWindow)
        icon1 = QtGui.QIcon()
        icon1.addPixmap(QtGui.QPixmap(":/sfc-ui/icons/folder-open-document-24.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.actionOpen_project.setIcon(icon1)
        self.actionOpen_project.setObjectName("actionOpen_project")
        self.actionSave_project = QtWidgets.QAction(MainWindow)
        icon2 = QtGui.QIcon()
        icon2.addPixmap(QtGui.QPixmap(":/sfc-ui/icons/disk-24.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.actionSave_project.setIcon(icon2)
        self.actionSave_project.setObjectName("actionSave_project")
        self.actionSave_as_project = QtWidgets.QAction(MainWindow)
        self.actionSave_as_project.setIcon(icon2)
        self.actionSave_as_project.setObjectName("actionSave_as_project")
        self.actionQuit = QtWidgets.QAction(MainWindow)
        icon3 = QtGui.QIcon()
        icon3.addPixmap(QtGui.QPixmap(":/sfc-ui/icons/cross-24.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.actionQuit.setIcon(icon3)
        self.actionQuit.setObjectName("actionQuit")
        self.actionLicense = QtWidgets.QAction(MainWindow)
        icon4 = QtGui.QIcon()
        icon4.addPixmap(QtGui.QPixmap(":/sfc-ui/icons/key-16.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.actionLicense.setIcon(icon4)
        self.actionLicense.setObjectName("actionLicense")
        self.actionAbout = QtWidgets.QAction(MainWindow)
        icon5 = QtGui.QIcon()
        icon5.addPixmap(QtGui.QPixmap(":/sfc-ui/icons/information-button-24.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.actionAbout.setIcon(icon5)
        self.actionAbout.setObjectName("actionAbout")
        self.menuFile.addAction(self.actionNew_project)
        self.menuFile.addAction(self.actionOpen_project)
        self.menuFile.addAction(self.actionSave_project)
        self.menuFile.addAction(self.actionSave_as_project)
        self.menuFile.addSeparator()
        self.menuFile.addAction(self.actionQuit)
        self.menuHelp.addAction(self.actionLicense)
        self.menuHelp.addAction(self.actionAbout)
        self.menubar.addAction(self.menuFile.menuAction())
        self.menubar.addAction(self.menuHelp.menuAction())

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.menuFile.setTitle(_translate("MainWindow", "File"))
        self.menuHelp.setTitle(_translate("MainWindow", "Help"))
        self.actionNew_project.setText(_translate("MainWindow", "New project"))
        self.actionOpen_project.setText(_translate("MainWindow", "Open project"))
        self.actionSave_project.setText(_translate("MainWindow", "Save project"))
        self.actionSave_as_project.setText(_translate("MainWindow", "Save as project"))
        self.actionQuit.setText(_translate("MainWindow", "Quit"))
        self.actionLicense.setText(_translate("MainWindow", "License"))
        self.actionAbout.setText(_translate("MainWindow", "About"))
import resources_rc