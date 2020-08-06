# ------------------------------------------------------
# Created and developed by Pawel Gasiewski
# Politechnika Poznanska, WIiT, EiT 17/18, August 2020
# Under supervision of Ph.D. Adrian Dziembowski
# ------------------------------------------------------

# Importing necessary libraries and modules for PyQt5 GUI Framework
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QFileDialog, QMessageBox
from PyQt5.QtGui import *
import os
# Importing necessary libraries (np, opencv) and functions from filtering.py to work on
# filtering.py script-file was also created by me, before GUI development.
from filtering import np, cv, rgb_conv, kernels


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(1003, 578)
        MainWindow.setStyleSheet("background-color: rgb(170,170,170);")
        self.img = cv.imread('basic.jpg') # Image in an OpenCV format - necessary for filtering
        self.img_path = 'basic.jpg'
        self.temp = 'basic.jpg'
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")

        # ------------------------- BUTTONS ----------------------------
        self.hpf1Button = QtWidgets.QPushButton(self.centralwidget)
        self.hpf1Button.setGeometry(QtCore.QRect(655, 60, 151, 71))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.hpf1Button.setFont(font)
        self.hpf1Button.setObjectName("hpf1Button")
        self.hpf1Button.setStyleSheet("border:2px solid rgb(0,0,0);"
                                      "background-color: rgb(210,210,210);")

        self.hpf2Button = QtWidgets.QPushButton(self.centralwidget)
        self.hpf2Button.setGeometry(QtCore.QRect(835, 60, 151, 71))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.hpf2Button.setFont(font)
        self.hpf2Button.setObjectName("hpf2Button")
        self.hpf2Button.setStyleSheet("border:2px solid rgb(0,0,0);"
                                      "background-color: rgb(210,210,210);")

        self.lpf1Button = QtWidgets.QPushButton(self.centralwidget)
        self.lpf1Button.setGeometry(QtCore.QRect(655, 140, 151, 71))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.lpf1Button.setFont(font)
        self.lpf1Button.setObjectName("lpf1Button")
        self.lpf1Button.setStyleSheet("border:2px solid rgb(0,0,0);"
                                      "background-color: rgb(210,210,210);")

        self.lpf2Button = QtWidgets.QPushButton(self.centralwidget)
        self.lpf2Button.setGeometry(QtCore.QRect(835, 140, 151, 71))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.lpf2Button.setFont(font)
        self.lpf2Button.setObjectName("lpf2Button")
        self.lpf2Button.setStyleSheet("border:2px solid rgb(0,0,0);"
                                      "background-color: rgb(210,210,210);")

        self.vsobelButton = QtWidgets.QPushButton(self.centralwidget)
        self.vsobelButton.setGeometry(QtCore.QRect(655, 220, 151, 71))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.vsobelButton.setFont(font)
        self.vsobelButton.setObjectName("vsobelButton")
        self.vsobelButton.setStyleSheet("border:2px solid rgb(0,0,0);"
                                        "background-color: rgb(210,210,210);")

        self.hsobelButton = QtWidgets.QPushButton(self.centralwidget)
        self.hsobelButton.setGeometry(QtCore.QRect(835, 220, 151, 71))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.hsobelButton.setFont(font)
        self.hsobelButton.setObjectName("hsobelButton")
        self.hsobelButton.setStyleSheet("border:2px solid rgb(0,0,0);"
                                        "background-color: rgb(210,210,210);")

        self.edge1Button = QtWidgets.QPushButton(self.centralwidget)
        self.edge1Button.setGeometry(QtCore.QRect(655, 300, 151, 71))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.edge1Button.setFont(font)
        self.edge1Button.setObjectName("edge1Button")
        self.edge1Button.setStyleSheet("border:2px solid rgb(0,0,0);"
                                       "background-color: rgb(210,210,210);")

        self.edge2Button = QtWidgets.QPushButton(self.centralwidget)
        self.edge2Button.setGeometry(QtCore.QRect(835, 300, 151, 71))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.edge2Button.setFont(font)
        self.edge2Button.setObjectName("edge2Button")
        self.edge2Button.setStyleSheet("border:2px solid rgb(0,0,0);"
                                       "background-color: rgb(210,210,210);")

        self.gaussButton = QtWidgets.QPushButton(self.centralwidget)
        self.gaussButton.setGeometry(QtCore.QRect(745, 380, 151, 71))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.gaussButton.setFont(font)
        self.gaussButton.setObjectName("gaussButton")
        self.gaussButton.setStyleSheet("border:2px solid rgb(0,0,0);"
                                       "background-color: rgb(210,210,210);")

        self.resetButton = QtWidgets.QPushButton(self.centralwidget)
        self.resetButton.setGeometry(QtCore.QRect(210, 490, 191, 41))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.resetButton.setFont(font)
        self.resetButton.setObjectName("resetButton")
        self.resetButton.setStyleSheet("border:2px solid rgb(0,0,0);"
                                       "background-color: rgb(210,210,210);")

        # ------------------------- LABELS----------------------------
        self.filter_type = QtWidgets.QLabel(self.centralwidget)
        self.filter_type.setGeometry(QtCore.QRect(765, 20, 121, 31))
        font = QtGui.QFont()
        font.setPointSize(14)
        self.filter_type.setFont(font)
        self.filter_type.setObjectName("filter_type")

        self.image_pix = QtWidgets.QLabel(self.centralwidget)
        self.image_pix.setGeometry(QtCore.QRect(30, 22, 591, 451))
        self.image_pix.setText("")
        self.image_pix.setPixmap(QtGui.QPixmap("{}".format('basic.jpg')))
        self.image_pix.setObjectName("image_pix")
        self.image_pix.setScaledContents(True)
        self.image_pix.setStyleSheet("border:2px solid rgb(0,0,0)")

        # ------------------------- MENU ----------------------------
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 1003, 21))
        self.menubar.setObjectName("menubar")
        self.menubar.setStyleSheet("border:1px solid rgb(0,0,0);"
                                   "background-color: rgb(200,200,200);")
        self.menu_INFO = QtWidgets.QMenu(self.menubar)
        self.menu_INFO.setObjectName("menu_INFO")
        self.menuFile = QtWidgets.QMenu(self.menubar)
        self.menuFile.setObjectName("menuFile")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)
        self.actionOpen = QtWidgets.QAction(MainWindow)
        self.actionOpen.setObjectName("actionOpen")
        self.actionSave = QtWidgets.QAction(MainWindow)
        self.actionSave.setObjectName("actionSave")
        self.actionShow = QtWidgets.QAction(MainWindow)
        self.actionShow.setObjectName("actionShow")
        self.menuFile.addAction(self.actionOpen)
        self.menuFile.addAction(self.actionSave)
        self.menu_INFO.addAction(self.actionShow)
        self.menubar.addAction(self.menuFile.menuAction())
        self.menubar.addAction(self.menu_INFO.menuAction())

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

        self.hpf1Button.clicked.connect(lambda: self.clicked_filter(self.img, kernels['hpf1']))
        self.hpf2Button.clicked.connect(lambda: self.clicked_filter(self.img, kernels['hpf2']))
        self.lpf1Button.clicked.connect(lambda: self.clicked_filter(self.img, kernels['lpf1']))
        self.lpf2Button.clicked.connect(lambda: self.clicked_filter(self.img, kernels['lpf2']))
        self.hsobelButton.clicked.connect(lambda: self.clicked_filter(self.img, kernels['sobelx']))
        self.vsobelButton.clicked.connect(lambda: self.clicked_filter(self.img, kernels['sobely']))
        self.edge1Button.clicked.connect(lambda: self.clicked_filter(self.img, kernels['edge1']))
        self.edge2Button.clicked.connect(lambda: self.clicked_filter(self.img, kernels['edge2']))
        self.gaussButton.clicked.connect(lambda: self.clicked_filter(self.img, kernels['gauss']))
        self.resetButton.clicked.connect(self.reset_img)
        self.actionShow.triggered.connect(self.show_info)
        self.actionOpen.triggered.connect(self.file_open)
        self.actionSave.triggered.connect(self.file_save)
        #self.actionZapisz.triggered.connect(self.file_save)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Filtering - Pawel Gasiewski"))
        self.hpf1Button.setText(_translate("MainWindow", "HPF - weaker"))
        self.hpf2Button.setText(_translate("MainWindow", "HPF - stronger"))
        self.vsobelButton.setText(_translate("MainWindow", "Sobel - vertical"))
        self.hsobelButton.setText(_translate("MainWindow", "Sobel - horizontal"))
        self.edge1Button.setText(_translate("MainWindow", "Edge - weaker"))
        self.edge2Button.setText(_translate("MainWindow", "Edge - stronger"))
        self.gaussButton.setText(_translate("MainWindow", "Gaussian"))
        self.filter_type.setText(_translate("MainWindow", "Filter type : "))
        self.lpf1Button.setText(_translate("MainWindow", "LPF - weaker"))
        self.lpf2Button.setText(_translate("MainWindow", "LPF - stronger"))
        self.resetButton.setText(_translate("MainWindow", "Reset"))
        self.menu_INFO.setTitle(_translate("MainWindow", "INFO"))
        self.menuFile.setTitle(_translate("MainWindow", "File"))
        self.actionOpen.setText(_translate("MainWindow", "Open"))
        self.actionOpen.setShortcut(_translate("MainWindow", "Ctrl+O"))
        self.actionSave.setText(_translate("MainWindow", "Save"))
        self.actionSave.setShortcut(_translate("MainWindow", "Ctrl+S"))
        self.actionShow.setText(_translate("MainWindow", "Show"))
        self.actionShow.setShortcut(_translate("MainWindow", "Ctrl+I"))

    # Method projected for filtering an image after clicking one of buttons available
    def clicked_filter(self, image, mask):
        output = rgb_conv(image, mask)
        filename = 'temp.jpg'
        cv.imwrite(filename, output)
        fn = 'temp.jpg'
        p = os.popen('attrib +h' + fn)
        t = p.read()
        p.close()
        self.temp = output
        self.image_pix.setPixmap(QtGui.QPixmap('temp.jpg'))

    # Just resetting the normal image (for comparison or smth)
    def reset_img(self):
        self.temp = self.img
        self.image_pix.setPixmap(QtGui.QPixmap('{}'.format(self.img_path)))

    # Function projected to open an image file from the computer to work on
    def file_open(self):
        try:
            filename = QFileDialog.getOpenFileName()
            path = filename[0]
            self.img = cv.imread('{}'.format(path))
            self.img_path = path
            self.image_pix.setPixmap(QtGui.QPixmap('{}'.format(path)))
        except:
            msg = QMessageBox()
            msg.setIcon(QMessageBox.Error)
            msg.setText("Please select an image file!.")
            msg.setWindowTitle("Something went wrong...")
            msg.exec()

    # Meant to save the currently viewed image
    def file_save(self):
        try:
            filename = QFileDialog.getSaveFileName()
            path = filename[0]
            cv.imwrite((path+'.jpg'), self.temp)
        except:
            print('error')

    # Shows developer info
    def show_info(self):
        msg = QMessageBox()
        msg.setIcon(QMessageBox.Information)
        msg.setText("Created by Pawel Gasiewski.\nPolitechnika Poznanska\nWIiT, EiT 17/18\nAll cpr. reserved.")
        msg.setWindowTitle("INFO")
        msg.exec()

# Window construction - core part of programme
if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
