# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'ui/Plot.ui'
#
# Created by: PyQt4 UI code generator 4.12.1
#
# WARNING! All changes made in this file will be lost!

from PyQt4 import QtCore, QtGui

try:
    _fromUtf8 = QtCore.QString.fromUtf8
except AttributeError:
    def _fromUtf8(s):
        return s

try:
    _encoding = QtGui.QApplication.UnicodeUTF8
    def _translate(context, text, disambig):
        return QtGui.QApplication.translate(context, text, disambig, _encoding)
except AttributeError:
    def _translate(context, text, disambig):
        return QtGui.QApplication.translate(context, text, disambig)

class Ui_PlotDialog(object):
    def setupUi(self, PlotDialog):
        PlotDialog.setObjectName(_fromUtf8("PlotDialog"))
        PlotDialog.resize(762, 550)
        PlotDialog.setMinimumSize(QtCore.QSize(762, 550))
        PlotDialog.setMaximumSize(QtCore.QSize(762, 550))
        self.buttonBox = QtGui.QDialogButtonBox(PlotDialog)
        self.buttonBox.setGeometry(QtCore.QRect(10, 510, 741, 32))
        self.buttonBox.setOrientation(QtCore.Qt.Horizontal)
        self.buttonBox.setStandardButtons(QtGui.QDialogButtonBox.Ok)
        self.buttonBox.setObjectName(_fromUtf8("buttonBox"))
        self.tabWidget = QtGui.QTabWidget(PlotDialog)
        self.tabWidget.setGeometry(QtCore.QRect(10, 10, 740, 491))
        self.tabWidget.setTabPosition(QtGui.QTabWidget.South)
        self.tabWidget.setTabShape(QtGui.QTabWidget.Rounded)
        self.tabWidget.setObjectName(_fromUtf8("tabWidget"))
        self.wave_tab = QtGui.QWidget()
        self.wave_tab.setObjectName(_fromUtf8("wave_tab"))
        self.verticalLayoutWidget_3 = QtGui.QWidget(self.wave_tab)
        self.verticalLayoutWidget_3.setGeometry(QtCore.QRect(0, 0, 731, 461))
        self.verticalLayoutWidget_3.setObjectName(_fromUtf8("verticalLayoutWidget_3"))
        self.plot0 = QtGui.QVBoxLayout(self.verticalLayoutWidget_3)
        self.plot0.setSizeConstraint(QtGui.QLayout.SetDefaultConstraint)
        self.plot0.setContentsMargins(5, 5, 2, 0)
        self.plot0.setObjectName(_fromUtf8("plot0"))
        self.tabWidget.addTab(self.wave_tab, _fromUtf8(""))
        self.spectrum_tab = QtGui.QWidget()
        self.spectrum_tab.setObjectName(_fromUtf8("spectrum_tab"))
        self.verticalLayoutWidget_2 = QtGui.QWidget(self.spectrum_tab)
        self.verticalLayoutWidget_2.setGeometry(QtCore.QRect(0, 0, 731, 461))
        self.verticalLayoutWidget_2.setObjectName(_fromUtf8("verticalLayoutWidget_2"))
        self.plot1 = QtGui.QVBoxLayout(self.verticalLayoutWidget_2)
        self.plot1.setSizeConstraint(QtGui.QLayout.SetDefaultConstraint)
        self.plot1.setContentsMargins(5, 5, 2, 0)
        self.plot1.setObjectName(_fromUtf8("plot1"))
        self.tabWidget.addTab(self.spectrum_tab, _fromUtf8(""))
        self.pitch_tab = QtGui.QWidget()
        self.pitch_tab.setObjectName(_fromUtf8("pitch_tab"))
        self.verticalLayoutWidget = QtGui.QWidget(self.pitch_tab)
        self.verticalLayoutWidget.setGeometry(QtCore.QRect(0, 0, 731, 461))
        self.verticalLayoutWidget.setObjectName(_fromUtf8("verticalLayoutWidget"))
        self.plot2 = QtGui.QVBoxLayout(self.verticalLayoutWidget)
        self.plot2.setSizeConstraint(QtGui.QLayout.SetDefaultConstraint)
        self.plot2.setContentsMargins(5, 5, 2, 0)
        self.plot2.setObjectName(_fromUtf8("plot2"))
        self.tabWidget.addTab(self.pitch_tab, _fromUtf8(""))
        self.tab = QtGui.QWidget()
        self.tab.setObjectName(_fromUtf8("tab"))
        self.verticalLayoutWidget_4 = QtGui.QWidget(self.tab)
        self.verticalLayoutWidget_4.setGeometry(QtCore.QRect(0, 0, 731, 461))
        self.verticalLayoutWidget_4.setObjectName(_fromUtf8("verticalLayoutWidget_4"))
        self.plot3 = QtGui.QVBoxLayout(self.verticalLayoutWidget_4)
        self.plot3.setSizeConstraint(QtGui.QLayout.SetDefaultConstraint)
        self.plot3.setContentsMargins(5, 5, 2, 0)
        self.plot3.setObjectName(_fromUtf8("plot3"))
        self.tabWidget.addTab(self.tab, _fromUtf8(""))
        self.tab_4 = QtGui.QWidget()
        self.tab_4.setObjectName(_fromUtf8("tab_4"))
        self.verticalLayoutWidget_5 = QtGui.QWidget(self.tab_4)
        self.verticalLayoutWidget_5.setGeometry(QtCore.QRect(0, 0, 731, 461))
        self.verticalLayoutWidget_5.setObjectName(_fromUtf8("verticalLayoutWidget_5"))
        self.plot4 = QtGui.QVBoxLayout(self.verticalLayoutWidget_5)
        self.plot4.setSizeConstraint(QtGui.QLayout.SetDefaultConstraint)
        self.plot4.setContentsMargins(5, 5, 2, 0)
        self.plot4.setObjectName(_fromUtf8("plot4"))
        self.tabWidget.addTab(self.tab_4, _fromUtf8(""))
        self.tab_2 = QtGui.QWidget()
        self.tab_2.setObjectName(_fromUtf8("tab_2"))
        self.label_file = QtGui.QTextBrowser(self.tab_2)
        self.label_file.setGeometry(QtCore.QRect(0, 0, 740, 461))
        self.label_file.setObjectName(_fromUtf8("label_file"))
        self.tabWidget.addTab(self.tab_2, _fromUtf8(""))
        self.tab_3 = QtGui.QWidget()
        self.tab_3.setObjectName(_fromUtf8("tab_3"))
        self.utt_file = QtGui.QTextBrowser(self.tab_3)
        self.utt_file.setGeometry(QtCore.QRect(0, 0, 740, 461))
        self.utt_file.setObjectName(_fromUtf8("utt_file"))
        self.tabWidget.addTab(self.tab_3, _fromUtf8(""))

        self.retranslateUi(PlotDialog)
        self.tabWidget.setCurrentIndex(4)
        QtCore.QObject.connect(self.buttonBox, QtCore.SIGNAL(_fromUtf8("accepted()")), PlotDialog.close)
        QtCore.QMetaObject.connectSlotsByName(PlotDialog)

    def retranslateUi(self, PlotDialog):
        PlotDialog.setWindowTitle(_translate("PlotDialog", "Analysis", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.wave_tab), _translate("PlotDialog", "Wave", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.spectrum_tab), _translate("PlotDialog", "Magnitude Spectrum", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.pitch_tab), _translate("PlotDialog", "Pitch Contour", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab), _translate("PlotDialog", "Spectrogram", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_4), _translate("PlotDialog", "MFCC Colormap", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_2), _translate("PlotDialog", "Label File", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_3), _translate("PlotDialog", "Utterance File", None))

