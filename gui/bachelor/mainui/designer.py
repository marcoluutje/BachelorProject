# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'designer.ui'
#
# Created by: PyQt5 UI code generator 5.12.1
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(1072, 952)
        MainWindow.setMinimumSize(QtCore.QSize(836, 558))
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.gridLayout = QtWidgets.QGridLayout(self.centralwidget)
        self.gridLayout.setObjectName("gridLayout")
        self.frame_5 = QtWidgets.QFrame(self.centralwidget)
        self.frame_5.setMaximumSize(QtCore.QSize(350, 16777215))
        self.frame_5.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_5.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_5.setObjectName("frame_5")
        self.gridLayout_2 = QtWidgets.QGridLayout(self.frame_5)
        self.gridLayout_2.setObjectName("gridLayout_2")
        self.label_11 = QtWidgets.QLabel(self.frame_5)
        self.label_11.setObjectName("label_11")
        self.gridLayout_2.addWidget(self.label_11, 0, 0, 1, 1)
        self.frame_7 = QtWidgets.QFrame(self.frame_5)
        self.frame_7.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_7.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_7.setObjectName("frame_7")
        self.gridLayout_10 = QtWidgets.QGridLayout(self.frame_7)
        self.gridLayout_10.setObjectName("gridLayout_10")
        self.label = QtWidgets.QLabel(self.frame_7)
        self.label.setMaximumSize(QtCore.QSize(132, 17))
        self.label.setObjectName("label")
        self.gridLayout_10.addWidget(self.label, 0, 0, 1, 1)
        self.superpixelSpinBox = QtWidgets.QSpinBox(self.frame_7)
        self.superpixelSpinBox.setMinimum(1)
        self.superpixelSpinBox.setMaximum(9999)
        self.superpixelSpinBox.setProperty("value", 100)
        self.superpixelSpinBox.setObjectName("superpixelSpinBox")
        self.gridLayout_10.addWidget(self.superpixelSpinBox, 1, 0, 1, 1)
        self.label_5 = QtWidgets.QLabel(self.frame_7)
        self.label_5.setObjectName("label_5")
        self.gridLayout_10.addWidget(self.label_5, 2, 1, 1, 1)
        self.sigmaSpinBox = QtWidgets.QSpinBox(self.frame_7)
        self.sigmaSpinBox.setMaximum(9999)
        self.sigmaSpinBox.setProperty("value", 5)
        self.sigmaSpinBox.setObjectName("sigmaSpinBox")
        self.gridLayout_10.addWidget(self.sigmaSpinBox, 3, 1, 1, 1)
        self.iterationsSpinBox = QtWidgets.QSpinBox(self.frame_7)
        self.iterationsSpinBox.setMaximum(999)
        self.iterationsSpinBox.setProperty("value", 10)
        self.iterationsSpinBox.setObjectName("iterationsSpinBox")
        self.gridLayout_10.addWidget(self.iterationsSpinBox, 1, 1, 1, 1)
        self.superpixelButton = QtWidgets.QPushButton(self.frame_7)
        self.superpixelButton.setObjectName("superpixelButton")
        self.gridLayout_10.addWidget(self.superpixelButton, 4, 0, 1, 1)
        self.label_3 = QtWidgets.QLabel(self.frame_7)
        self.label_3.setObjectName("label_3")
        self.gridLayout_10.addWidget(self.label_3, 0, 1, 1, 1)
        self.label_4 = QtWidgets.QLabel(self.frame_7)
        self.label_4.setObjectName("label_4")
        self.gridLayout_10.addWidget(self.label_4, 2, 0, 1, 1)
        self.compactnessSpinBox = QtWidgets.QDoubleSpinBox(self.frame_7)
        self.compactnessSpinBox.setDecimals(5)
        self.compactnessSpinBox.setProperty("value", 10.0)
        self.compactnessSpinBox.setObjectName("compactnessSpinBox")
        self.gridLayout_10.addWidget(self.compactnessSpinBox, 3, 0, 1, 1)
        self.gridLayout_2.addWidget(self.frame_7, 4, 0, 1, 1)
        self.clusteringBox = QtWidgets.QComboBox(self.frame_5)
        self.clusteringBox.setObjectName("clusteringBox")
        self.clusteringBox.addItem("")
        self.clusteringBox.addItem("")
        self.clusteringBox.addItem("")
        self.gridLayout_2.addWidget(self.clusteringBox, 3, 0, 1, 1)
        self.frame_8 = QtWidgets.QFrame(self.frame_5)
        self.frame_8.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_8.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_8.setObjectName("frame_8")
        self.gridLayout_12 = QtWidgets.QGridLayout(self.frame_8)
        self.gridLayout_12.setObjectName("gridLayout_12")
        self.siftlabel = QtWidgets.QLabel(self.frame_8)
        self.siftlabel.setObjectName("siftlabel")
        self.gridLayout_12.addWidget(self.siftlabel, 3, 0, 1, 1)
        self.siftSpinBox = QtWidgets.QSpinBox(self.frame_8)
        self.siftSpinBox.setMinimum(1)
        self.siftSpinBox.setProperty("value", 32)
        self.siftSpinBox.setObjectName("siftSpinBox")
        self.gridLayout_12.addWidget(self.siftSpinBox, 4, 0, 1, 1)
        self.colorlabel2 = QtWidgets.QLabel(self.frame_8)
        self.colorlabel2.setObjectName("colorlabel2")
        self.gridLayout_12.addWidget(self.colorlabel2, 0, 1, 1, 1)
        self.histogramButton = QtWidgets.QPushButton(self.frame_8)
        self.histogramButton.setObjectName("histogramButton")
        self.gridLayout_12.addWidget(self.histogramButton, 6, 0, 1, 1)
        self.label_8 = QtWidgets.QLabel(self.frame_8)
        self.label_8.setText("")
        self.label_8.setObjectName("label_8")
        self.gridLayout_12.addWidget(self.label_8, 5, 0, 1, 1)
        self.SSpinBox = QtWidgets.QSpinBox(self.frame_8)
        self.SSpinBox.setProperty("value", 20)
        self.SSpinBox.setObjectName("SSpinBox")
        self.gridLayout_12.addWidget(self.SSpinBox, 1, 1, 1, 1)
        self.frame_2 = QtWidgets.QFrame(self.frame_8)
        self.frame_2.setStyleSheet("border:0")
        self.frame_2.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_2.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_2.setObjectName("frame_2")
        self.gridLayout_12.addWidget(self.frame_2, 2, 0, 1, 1)
        self.HspinBox = QtWidgets.QSpinBox(self.frame_8)
        self.HspinBox.setMinimum(2)
        self.HspinBox.setMaximum(360)
        self.HspinBox.setProperty("value", 20)
        self.HspinBox.setObjectName("HspinBox")
        self.gridLayout_12.addWidget(self.HspinBox, 1, 0, 1, 1)
        self.colorlabel1 = QtWidgets.QLabel(self.frame_8)
        self.colorlabel1.setObjectName("colorlabel1")
        self.gridLayout_12.addWidget(self.colorlabel1, 0, 0, 1, 1)
        self.pushButton = QtWidgets.QPushButton(self.frame_8)
        self.pushButton.setObjectName("pushButton")
        self.gridLayout_12.addWidget(self.pushButton, 6, 1, 1, 1)
        self.gridLayout_2.addWidget(self.frame_8, 5, 0, 1, 1)
        self.kmeansFrame = QtWidgets.QFrame(self.frame_5)
        self.kmeansFrame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.kmeansFrame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.kmeansFrame.setObjectName("kmeansFrame")
        self.gridLayout_17 = QtWidgets.QGridLayout(self.kmeansFrame)
        self.gridLayout_17.setObjectName("gridLayout_17")
        self.kmeansButton = QtWidgets.QPushButton(self.kmeansFrame)
        self.kmeansButton.setObjectName("kmeansButton")
        self.gridLayout_17.addWidget(self.kmeansButton, 1, 0, 1, 1)
        self.kclustervalue = QtWidgets.QSpinBox(self.kmeansFrame)
        self.kclustervalue.setMinimum(2)
        self.kclustervalue.setMaximum(12)
        self.kclustervalue.setObjectName("kclustervalue")
        self.gridLayout_17.addWidget(self.kclustervalue, 1, 1, 1, 1)
        self.label_10 = QtWidgets.QLabel(self.kmeansFrame)
        self.label_10.setObjectName("label_10")
        self.gridLayout_17.addWidget(self.label_10, 0, 1, 1, 1)
        self.gridLayout_2.addWidget(self.kmeansFrame, 9, 0, 1, 1)
        self.label_2 = QtWidgets.QLabel(self.frame_5)
        self.label_2.setObjectName("label_2")
        self.gridLayout_2.addWidget(self.label_2, 2, 0, 1, 1)
        self.spectralFrame = QtWidgets.QFrame(self.frame_5)
        self.spectralFrame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.spectralFrame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.spectralFrame.setObjectName("spectralFrame")
        self.gridLayout_9 = QtWidgets.QGridLayout(self.spectralFrame)
        self.gridLayout_9.setObjectName("gridLayout_9")
        self.spectralButton = QtWidgets.QPushButton(self.spectralFrame)
        self.spectralButton.setObjectName("spectralButton")
        self.gridLayout_9.addWidget(self.spectralButton, 1, 0, 1, 1)
        self.Sclustervalue = QtWidgets.QSpinBox(self.spectralFrame)
        self.Sclustervalue.setMinimum(2)
        self.Sclustervalue.setMaximum(12)
        self.Sclustervalue.setObjectName("Sclustervalue")
        self.gridLayout_9.addWidget(self.Sclustervalue, 1, 1, 1, 1)
        self.label_9 = QtWidgets.QLabel(self.spectralFrame)
        self.label_9.setObjectName("label_9")
        self.gridLayout_9.addWidget(self.label_9, 0, 1, 1, 1)
        self.gridLayout_2.addWidget(self.spectralFrame, 8, 0, 1, 1)
        self.extractionBox = QtWidgets.QComboBox(self.frame_5)
        self.extractionBox.setObjectName("extractionBox")
        self.extractionBox.addItem("")
        self.extractionBox.addItem("")
        self.extractionBox.addItem("")
        self.gridLayout_2.addWidget(self.extractionBox, 1, 0, 1, 1)
        self.graphFrame = QtWidgets.QFrame(self.frame_5)
        self.graphFrame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.graphFrame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.graphFrame.setObjectName("graphFrame")
        self.gridLayout_7 = QtWidgets.QGridLayout(self.graphFrame)
        self.gridLayout_7.setObjectName("gridLayout_7")
        self.frame_9 = QtWidgets.QFrame(self.graphFrame)
        self.frame_9.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_9.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_9.setObjectName("frame_9")
        self.gridLayout_18 = QtWidgets.QGridLayout(self.frame_9)
        self.gridLayout_18.setObjectName("gridLayout_18")
        self.bwRadioButton = QtWidgets.QRadioButton(self.frame_9)
        self.bwRadioButton.setObjectName("bwRadioButton")
        self.gridLayout_18.addWidget(self.bwRadioButton, 0, 0, 1, 1)
        self.bRadioButton = QtWidgets.QRadioButton(self.frame_9)
        self.bRadioButton.setObjectName("bRadioButton")
        self.gridLayout_18.addWidget(self.bRadioButton, 0, 1, 1, 1)
        self.gridLayout_7.addWidget(self.frame_9, 9, 0, 1, 2)
        self.frame_6 = QtWidgets.QFrame(self.graphFrame)
        self.frame_6.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_6.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_6.setObjectName("frame_6")
        self.gridLayout_11 = QtWidgets.QGridLayout(self.frame_6)
        self.gridLayout_11.setObjectName("gridLayout_11")
        self.edgeRadioButton = QtWidgets.QRadioButton(self.frame_6)
        self.edgeRadioButton.setObjectName("edgeRadioButton")
        self.gridLayout_11.addWidget(self.edgeRadioButton, 0, 0, 1, 1)
        self.nodeRadioButton = QtWidgets.QRadioButton(self.frame_6)
        self.nodeRadioButton.setObjectName("nodeRadioButton")
        self.gridLayout_11.addWidget(self.nodeRadioButton, 0, 1, 1, 1)
        self.gridLayout_7.addWidget(self.frame_6, 5, 0, 1, 2)
        self.label_12 = QtWidgets.QLabel(self.graphFrame)
        self.label_12.setObjectName("label_12")
        self.gridLayout_7.addWidget(self.label_12, 6, 0, 1, 1)
        self.pushButton_2 = QtWidgets.QPushButton(self.graphFrame)
        self.pushButton_2.setObjectName("pushButton_2")
        self.gridLayout_7.addWidget(self.pushButton_2, 4, 0, 1, 2)
        self.doubleSpinBox_2 = QtWidgets.QDoubleSpinBox(self.graphFrame)
        self.doubleSpinBox_2.setDecimals(5)
        self.doubleSpinBox_2.setMaximum(999999999.0)
        self.doubleSpinBox_2.setProperty("value", 1.0)
        self.doubleSpinBox_2.setObjectName("doubleSpinBox_2")
        self.gridLayout_7.addWidget(self.doubleSpinBox_2, 7, 1, 1, 1)
        self.componentMin = QtWidgets.QSpinBox(self.graphFrame)
        self.componentMin.setProperty("value", 5)
        self.componentMin.setObjectName("componentMin")
        self.gridLayout_7.addWidget(self.componentMin, 1, 0, 1, 1)
        self.componentMax = QtWidgets.QSpinBox(self.graphFrame)
        self.componentMax.setObjectName("componentMax")
        self.gridLayout_7.addWidget(self.componentMax, 1, 1, 1, 1)
        self.label_13 = QtWidgets.QLabel(self.graphFrame)
        self.label_13.setObjectName("label_13")
        self.gridLayout_7.addWidget(self.label_13, 6, 1, 1, 1)
        self.n_init = QtWidgets.QSpinBox(self.graphFrame)
        self.n_init.setObjectName("n_init")
        self.gridLayout_7.addWidget(self.n_init, 3, 0, 1, 1)
        self.label_6 = QtWidgets.QLabel(self.graphFrame)
        self.label_6.setObjectName("label_6")
        self.gridLayout_7.addWidget(self.label_6, 2, 0, 1, 1)
        self.label_7 = QtWidgets.QLabel(self.graphFrame)
        self.label_7.setObjectName("label_7")
        self.gridLayout_7.addWidget(self.label_7, 0, 0, 1, 2)
        self.doubleSpinBox = QtWidgets.QDoubleSpinBox(self.graphFrame)
        self.doubleSpinBox.setDecimals(5)
        self.doubleSpinBox.setMaximum(999999999.0)
        self.doubleSpinBox.setObjectName("doubleSpinBox")
        self.gridLayout_7.addWidget(self.doubleSpinBox, 7, 0, 1, 1)
        self.graphcomputeButton = QtWidgets.QPushButton(self.graphFrame)
        self.graphcomputeButton.setObjectName("graphcomputeButton")
        self.gridLayout_7.addWidget(self.graphcomputeButton, 8, 0, 1, 2)
        self.gridLayout_2.addWidget(self.graphFrame, 7, 0, 1, 1)
        self.gridLayout.addWidget(self.frame_5, 0, 0, 1, 1)
        self.frame = QtWidgets.QFrame(self.centralwidget)
        self.frame.setMaximumSize(QtCore.QSize(350, 350))
        self.frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame.setObjectName("frame")
        self.gridLayout_4 = QtWidgets.QGridLayout(self.frame)
        self.gridLayout_4.setObjectName("gridLayout_4")
        self.treeView = QtWidgets.QTreeView(self.frame)
        self.treeView.setObjectName("treeView")
        self.gridLayout_4.addWidget(self.treeView, 0, 0, 1, 1)
        self.gridLayout.addWidget(self.frame, 2, 0, 1, 1)
        self.tabWidget = QtWidgets.QTabWidget(self.centralwidget)
        self.tabWidget.setObjectName("tabWidget")
        self.drawTab = QtWidgets.QWidget()
        self.drawTab.setObjectName("drawTab")
        self.gridLayout_5 = QtWidgets.QGridLayout(self.drawTab)
        self.gridLayout_5.setObjectName("gridLayout_5")
        self.scrollArea = QtWidgets.QScrollArea(self.drawTab)
        self.scrollArea.setWidgetResizable(True)
        self.scrollArea.setObjectName("scrollArea")
        self.scrollAreaWidgetContents = QtWidgets.QWidget()
        self.scrollAreaWidgetContents.setGeometry(QtCore.QRect(0, 0, 533, 733))
        self.scrollAreaWidgetContents.setObjectName("scrollAreaWidgetContents")
        self.gridLayout_6 = QtWidgets.QGridLayout(self.scrollAreaWidgetContents)
        self.gridLayout_6.setObjectName("gridLayout_6")
        self.image = QtWidgets.QLabel(self.scrollAreaWidgetContents)
        self.image.setText("")
        self.image.setObjectName("image")
        self.gridLayout_6.addWidget(self.image, 0, 0, 1, 1)
        self.scrollArea.setWidget(self.scrollAreaWidgetContents)
        self.gridLayout_5.addWidget(self.scrollArea, 0, 0, 1, 1)
        self.tabWidget.addTab(self.drawTab, "")
        self.superpixelTab = QtWidgets.QWidget()
        self.superpixelTab.setObjectName("superpixelTab")
        self.gridLayout_15 = QtWidgets.QGridLayout(self.superpixelTab)
        self.gridLayout_15.setObjectName("gridLayout_15")
        self.scrollArea_3 = QtWidgets.QScrollArea(self.superpixelTab)
        self.scrollArea_3.setWidgetResizable(True)
        self.scrollArea_3.setObjectName("scrollArea_3")
        self.scrollAreaWidgetContents_2 = QtWidgets.QWidget()
        self.scrollAreaWidgetContents_2.setGeometry(QtCore.QRect(0, 0, 533, 733))
        self.scrollAreaWidgetContents_2.setObjectName("scrollAreaWidgetContents_2")
        self.gridLayout_16 = QtWidgets.QGridLayout(self.scrollAreaWidgetContents_2)
        self.gridLayout_16.setObjectName("gridLayout_16")
        self.superImage = QtWidgets.QLabel(self.scrollAreaWidgetContents_2)
        self.superImage.setText("")
        self.superImage.setObjectName("superImage")
        self.gridLayout_16.addWidget(self.superImage, 0, 0, 1, 1)
        self.scrollArea_3.setWidget(self.scrollAreaWidgetContents_2)
        self.gridLayout_15.addWidget(self.scrollArea_3, 0, 0, 1, 1)
        self.tabWidget.addTab(self.superpixelTab, "")
        self.tab = QtWidgets.QWidget()
        self.tab.setObjectName("tab")
        self.tabWidget.addTab(self.tab, "")
        self.resultsTab = QtWidgets.QWidget()
        self.resultsTab.setObjectName("resultsTab")
        self.gridLayout_8 = QtWidgets.QGridLayout(self.resultsTab)
        self.gridLayout_8.setObjectName("gridLayout_8")
        self.scrollArea_2 = QtWidgets.QScrollArea(self.resultsTab)
        self.scrollArea_2.setWidgetResizable(True)
        self.scrollArea_2.setObjectName("scrollArea_2")
        self.scrollAreaWidgetContents_3 = QtWidgets.QWidget()
        self.scrollAreaWidgetContents_3.setGeometry(QtCore.QRect(0, 0, 533, 733))
        self.scrollAreaWidgetContents_3.setObjectName("scrollAreaWidgetContents_3")
        self.gridLayout_14 = QtWidgets.QGridLayout(self.scrollAreaWidgetContents_3)
        self.gridLayout_14.setObjectName("gridLayout_14")
        self.result_image = QtWidgets.QLabel(self.scrollAreaWidgetContents_3)
        self.result_image.setText("")
        self.result_image.setObjectName("result_image")
        self.gridLayout_14.addWidget(self.result_image, 0, 0, 1, 1)
        self.scrollArea_2.setWidget(self.scrollAreaWidgetContents_3)
        self.gridLayout_8.addWidget(self.scrollArea_2, 0, 0, 1, 1)
        self.tabWidget.addTab(self.resultsTab, "")
        self.gridLayout.addWidget(self.tabWidget, 0, 1, 1, 1)
        self.frame_4 = QtWidgets.QFrame(self.centralwidget)
        self.frame_4.setMaximumSize(QtCore.QSize(16777215, 350))
        self.frame_4.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_4.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_4.setObjectName("frame_4")
        self.gridLayout_3 = QtWidgets.QGridLayout(self.frame_4)
        self.gridLayout_3.setObjectName("gridLayout_3")
        self.listWidget = QtWidgets.QListWidget(self.frame_4)
        self.listWidget.setMaximumSize(QtCore.QSize(16777215, 16777215))
        self.listWidget.setObjectName("listWidget")
        self.gridLayout_3.addWidget(self.listWidget, 0, 0, 1, 1)
        self.gridLayout.addWidget(self.frame_4, 2, 1, 1, 2)
        self.frame_3 = QtWidgets.QFrame(self.centralwidget)
        self.frame_3.setMaximumSize(QtCore.QSize(178, 16777215))
        self.frame_3.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_3.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_3.setObjectName("frame_3")
        self.gridLayout_13 = QtWidgets.QGridLayout(self.frame_3)
        self.gridLayout_13.setObjectName("gridLayout_13")
        self.bgRadioButton = QtWidgets.QRadioButton(self.frame_3)
        self.bgRadioButton.setObjectName("bgRadioButton")
        self.gridLayout_13.addWidget(self.bgRadioButton, 1, 0, 1, 1)
        self.fgRadioButton = QtWidgets.QRadioButton(self.frame_3)
        self.fgRadioButton.setObjectName("fgRadioButton")
        self.gridLayout_13.addWidget(self.fgRadioButton, 0, 0, 1, 1)
        self.clearMarkingsButton = QtWidgets.QPushButton(self.frame_3)
        self.clearMarkingsButton.setObjectName("clearMarkingsButton")
        self.gridLayout_13.addWidget(self.clearMarkingsButton, 4, 0, 1, 1)
        self.radioButton = QtWidgets.QRadioButton(self.frame_3)
        self.radioButton.setObjectName("radioButton")
        self.gridLayout_13.addWidget(self.radioButton, 2, 0, 1, 1)
        self.markingsButton = QtWidgets.QPushButton(self.frame_3)
        self.markingsButton.setObjectName("markingsButton")
        self.gridLayout_13.addWidget(self.markingsButton, 3, 0, 1, 1)
        self.gridLayout.addWidget(self.frame_3, 0, 2, 1, 1)
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 1072, 25))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        self.tabWidget.setCurrentIndex(2)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.label_11.setText(_translate("MainWindow", "Feature extraction"))
        self.label.setText(_translate("MainWindow", "Superpixel quantity"))
        self.label_5.setText(_translate("MainWindow", "Sigma"))
        self.superpixelButton.setText(_translate("MainWindow", "Calculate superpixels"))
        self.label_3.setText(_translate("MainWindow", "Iterations"))
        self.label_4.setText(_translate("MainWindow", "Compactness"))
        self.clusteringBox.setItemText(0, _translate("MainWindow", "Graph Cut"))
        self.clusteringBox.setItemText(1, _translate("MainWindow", "kmeans clustering"))
        self.clusteringBox.setItemText(2, _translate("MainWindow", "Spectral clustering"))
        self.siftlabel.setText(_translate("MainWindow", "keypoint size"))
        self.colorlabel2.setText(_translate("MainWindow", "bins_S"))
        self.histogramButton.setText(_translate("MainWindow", "Calculate histograms"))
        self.colorlabel1.setText(_translate("MainWindow", "bins_H"))
        self.pushButton.setText(_translate("MainWindow", "PushButton"))
        self.kmeansButton.setText(_translate("MainWindow", "kmeans clustering"))
        self.label_10.setText(_translate("MainWindow", "Clusters"))
        self.label_2.setText(_translate("MainWindow", "Clustering"))
        self.spectralButton.setText(_translate("MainWindow", "Spectral clustering"))
        self.label_9.setText(_translate("MainWindow", "Clusters"))
        self.extractionBox.setItemText(0, _translate("MainWindow", "Color"))
        self.extractionBox.setItemText(1, _translate("MainWindow", "hsv"))
        self.extractionBox.setItemText(2, _translate("MainWindow", "Sift"))
        self.bwRadioButton.setText(_translate("MainWindow", "black white mode"))
        self.bRadioButton.setText(_translate("MainWindow", "border mode"))
        self.edgeRadioButton.setText(_translate("MainWindow", "Edge"))
        self.nodeRadioButton.setText(_translate("MainWindow", "Node"))
        self.label_12.setText(_translate("MainWindow", "pairwise term scale"))
        self.pushButton_2.setText(_translate("MainWindow", "Compute GMM and uncertainties"))
        self.label_13.setText(_translate("MainWindow", "scale parameters"))
        self.label_6.setText(_translate("MainWindow", "Number of restarts"))
        self.label_7.setText(_translate("MainWindow", "Component range"))
        self.graphcomputeButton.setText(_translate("MainWindow", "Graph cut"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.drawTab), _translate("MainWindow", "Draw"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.superpixelTab), _translate("MainWindow", "Superpixel"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab), _translate("MainWindow", "Uncertainty"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.resultsTab), _translate("MainWindow", "results"))
        self.bgRadioButton.setText(_translate("MainWindow", "Background"))
        self.fgRadioButton.setText(_translate("MainWindow", "Foreground"))
        self.clearMarkingsButton.setText(_translate("MainWindow", "clear markings"))
        self.radioButton.setText(_translate("MainWindow", "Eraser"))
        self.markingsButton.setText(_translate("MainWindow", "Set Markings"))


