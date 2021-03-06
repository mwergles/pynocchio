# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file '/home/michell/Documents/Projects/pynocchio-comic-reader/forms/go_to_page_dialog.ui'
#
# Created: Thu May  5 13:07:39 2016
#      by: pyside-uic 0.2.15 running on PySide 1.2.1
#
# WARNING! All changes made in this file will be lost!

from PySide import QtCore, QtGui

class Ui_GoPageDialog(object):
    def setupUi(self, GoPageDialog):
        GoPageDialog.setObjectName("GoPageDialog")
        GoPageDialog.resize(283, 513)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(":/icons/elementary3-icon-theme/actions/48/search.svg"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        GoPageDialog.setWindowIcon(icon)
        GoPageDialog.setLocale(QtCore.QLocale(QtCore.QLocale.English, QtCore.QLocale.UnitedStates))
        GoPageDialog.setModal(True)
        self.verticalLayout = QtGui.QVBoxLayout(GoPageDialog)
        self.verticalLayout.setObjectName("verticalLayout")
        self.verticalLayout_2 = QtGui.QVBoxLayout()
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.groupBox = QtGui.QGroupBox(GoPageDialog)
        self.groupBox.setTitle("")
        self.groupBox.setAlignment(QtCore.Qt.AlignCenter)
        self.groupBox.setFlat(True)
        self.groupBox.setObjectName("groupBox")
        self.vertical_layout_3 = QtGui.QVBoxLayout(self.groupBox)
        self.vertical_layout_3.setContentsMargins(0, 0, 9, 0)
        self.vertical_layout_3.setObjectName("vertical_layout_3")
        self.scrollArea = QtGui.QScrollArea(self.groupBox)
        self.scrollArea.setStyleSheet("background-color: rgb(0, 0, 0);")
        self.scrollArea.setFrameShape(QtGui.QFrame.NoFrame)
        self.scrollArea.setFrameShadow(QtGui.QFrame.Sunken)
        self.scrollArea.setVerticalScrollBarPolicy(QtCore.Qt.ScrollBarAlwaysOff)
        self.scrollArea.setHorizontalScrollBarPolicy(QtCore.Qt.ScrollBarAlwaysOff)
        self.scrollArea.setWidgetResizable(True)
        self.scrollArea.setAlignment(QtCore.Qt.AlignCenter)
        self.scrollArea.setObjectName("scrollArea")
        self.scrollAreaWidgetContents_2 = QtGui.QWidget()
        self.scrollAreaWidgetContents_2.setGeometry(QtCore.QRect(0, 0, 258, 378))
        self.scrollAreaWidgetContents_2.setObjectName("scrollAreaWidgetContents_2")
        self.horizontalLayout = QtGui.QHBoxLayout(self.scrollAreaWidgetContents_2)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.label_icon = QtGui.QLabel(self.scrollAreaWidgetContents_2)
        self.label_icon.setText("")
        self.label_icon.setAlignment(QtCore.Qt.AlignCenter)
        self.label_icon.setObjectName("label_icon")
        self.horizontalLayout.addWidget(self.label_icon)
        self.scrollArea.setWidget(self.scrollAreaWidgetContents_2)
        self.vertical_layout_3.addWidget(self.scrollArea)
        self.verticalLayout_2.addWidget(self.groupBox)
        self.formLayout = QtGui.QFormLayout()
        self.formLayout.setFieldGrowthPolicy(QtGui.QFormLayout.ExpandingFieldsGrow)
        self.formLayout.setObjectName("formLayout")
        self.label_num_pages = QtGui.QLabel(GoPageDialog)
        self.label_num_pages.setLocale(QtCore.QLocale(QtCore.QLocale.English, QtCore.QLocale.UnitedStates))
        self.label_num_pages.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignVCenter)
        self.label_num_pages.setObjectName("label_num_pages")
        self.formLayout.setWidget(0, QtGui.QFormLayout.LabelRole, self.label_num_pages)
        self.line_edit_num_page = QtGui.QLineEdit(GoPageDialog)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.line_edit_num_page.sizePolicy().hasHeightForWidth())
        self.line_edit_num_page.setSizePolicy(sizePolicy)
        self.line_edit_num_page.setMaximumSize(QtCore.QSize(16777214, 16777215))
        self.line_edit_num_page.setFrame(True)
        self.line_edit_num_page.setAlignment(QtCore.Qt.AlignCenter)
        self.line_edit_num_page.setReadOnly(True)
        self.line_edit_num_page.setObjectName("line_edit_num_page")
        self.formLayout.setWidget(0, QtGui.QFormLayout.FieldRole, self.line_edit_num_page)
        self.label_current_page = QtGui.QLabel(GoPageDialog)
        self.label_current_page.setLocale(QtCore.QLocale(QtCore.QLocale.English, QtCore.QLocale.UnitedStates))
        self.label_current_page.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignVCenter)
        self.label_current_page.setObjectName("label_current_page")
        self.formLayout.setWidget(1, QtGui.QFormLayout.LabelRole, self.label_current_page)
        self.line_edit_current_page = QtGui.QLineEdit(GoPageDialog)
        self.line_edit_current_page.setFrame(True)
        self.line_edit_current_page.setAlignment(QtCore.Qt.AlignCenter)
        self.line_edit_current_page.setReadOnly(True)
        self.line_edit_current_page.setObjectName("line_edit_current_page")
        self.formLayout.setWidget(1, QtGui.QFormLayout.FieldRole, self.line_edit_current_page)
        self.label_go_page = QtGui.QLabel(GoPageDialog)
        self.label_go_page.setLocale(QtCore.QLocale(QtCore.QLocale.English, QtCore.QLocale.UnitedStates))
        self.label_go_page.setObjectName("label_go_page")
        self.formLayout.setWidget(2, QtGui.QFormLayout.LabelRole, self.label_go_page)
        self.spin_box_go_page = QtGui.QSpinBox(GoPageDialog)
        self.spin_box_go_page.setWrapping(False)
        self.spin_box_go_page.setAlignment(QtCore.Qt.AlignCenter)
        self.spin_box_go_page.setButtonSymbols(QtGui.QAbstractSpinBox.UpDownArrows)
        self.spin_box_go_page.setAccelerated(True)
        self.spin_box_go_page.setCorrectionMode(QtGui.QAbstractSpinBox.CorrectToNearestValue)
        self.spin_box_go_page.setSuffix("")
        self.spin_box_go_page.setPrefix("")
        self.spin_box_go_page.setMinimum(1)
        self.spin_box_go_page.setSingleStep(1)
        self.spin_box_go_page.setObjectName("spin_box_go_page")
        self.formLayout.setWidget(2, QtGui.QFormLayout.FieldRole, self.spin_box_go_page)
        self.verticalLayout_2.addLayout(self.formLayout)
        self.verticalLayout.addLayout(self.verticalLayout_2)
        self.buttonBox = QtGui.QDialogButtonBox(GoPageDialog)
        self.buttonBox.setLocale(QtCore.QLocale(QtCore.QLocale.English, QtCore.QLocale.UnitedStates))
        self.buttonBox.setOrientation(QtCore.Qt.Horizontal)
        self.buttonBox.setStandardButtons(QtGui.QDialogButtonBox.Cancel|QtGui.QDialogButtonBox.Ok)
        self.buttonBox.setCenterButtons(False)
        self.buttonBox.setObjectName("buttonBox")
        self.verticalLayout.addWidget(self.buttonBox)

        self.retranslateUi(GoPageDialog)
        QtCore.QObject.connect(self.buttonBox, QtCore.SIGNAL("accepted()"), GoPageDialog.accept)
        QtCore.QObject.connect(self.buttonBox, QtCore.SIGNAL("rejected()"), GoPageDialog.reject)
        QtCore.QObject.connect(self.spin_box_go_page, QtCore.SIGNAL("valueChanged(int)"), GoPageDialog.update)
        QtCore.QMetaObject.connectSlotsByName(GoPageDialog)

    def retranslateUi(self, GoPageDialog):
        GoPageDialog.setWindowTitle(QtGui.QApplication.translate("GoPageDialog", "Go to Page", None, QtGui.QApplication.UnicodeUTF8))
        self.label_num_pages.setText(QtGui.QApplication.translate("GoPageDialog", "Number of pages: ", None, QtGui.QApplication.UnicodeUTF8))
        self.label_current_page.setText(QtGui.QApplication.translate("GoPageDialog", "Current page:        ", None, QtGui.QApplication.UnicodeUTF8))
        self.label_go_page.setText(QtGui.QApplication.translate("GoPageDialog", "Go to page:           ", None, QtGui.QApplication.UnicodeUTF8))

from . import main_window_view_rc
