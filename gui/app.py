# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'gui/app.ui'
#
# Created: Tue Dec 16 14:25:42 2014
#      by: PyQt4 UI code generator 4.11.3
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

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName(_fromUtf8("MainWindow"))
        MainWindow.resize(800, 716)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(_fromUtf8("test-tube-icon.png")), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        MainWindow.setWindowIcon(icon)
        self.centralwidget = QtGui.QWidget(MainWindow)
        self.centralwidget.setObjectName(_fromUtf8("centralwidget"))
        self.layoutWidget = QtGui.QWidget(self.centralwidget)
        self.layoutWidget.setGeometry(QtCore.QRect(0, 53, 781, 51))
        self.layoutWidget.setObjectName(_fromUtf8("layoutWidget"))
        self.gridLayout_2 = QtGui.QGridLayout(self.layoutWidget)
        self.gridLayout_2.setMargin(0)
        self.gridLayout_2.setObjectName(_fromUtf8("gridLayout_2"))
        self.le_query = QtGui.QLineEdit(self.layoutWidget)
        self.le_query.setMinimumSize(QtCore.QSize(200, 0))
        self.le_query.setObjectName(_fromUtf8("le_query"))
        self.gridLayout_2.addWidget(self.le_query, 2, 2, 1, 1)
        self.btn_start = QtGui.QPushButton(self.layoutWidget)
        icon = QtGui.QIcon.fromTheme(_fromUtf8("arrow-right"))
        self.btn_start.setIcon(icon)
        self.btn_start.setObjectName(_fromUtf8("btn_start"))
        self.gridLayout_2.addWidget(self.btn_start, 2, 4, 1, 1)
        self.label_2 = QtGui.QLabel(self.layoutWidget)
        self.label_2.setAlignment(QtCore.Qt.AlignBottom|QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft)
        self.label_2.setObjectName(_fromUtf8("label_2"))
        self.gridLayout_2.addWidget(self.label_2, 0, 0, 1, 1)
        self.label_4 = QtGui.QLabel(self.layoutWidget)
        self.label_4.setAlignment(QtCore.Qt.AlignBottom|QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft)
        self.label_4.setObjectName(_fromUtf8("label_4"))
        self.gridLayout_2.addWidget(self.label_4, 0, 2, 1, 1)
        self.le_curr_sdf = QtGui.QLineEdit(self.layoutWidget)
        self.le_curr_sdf.setMinimumSize(QtCore.QSize(150, 0))
        self.le_curr_sdf.setReadOnly(True)
        self.le_curr_sdf.setObjectName(_fromUtf8("le_curr_sdf"))
        self.gridLayout_2.addWidget(self.le_curr_sdf, 2, 0, 1, 1)
        self.combo_querytype = QtGui.QComboBox(self.layoutWidget)
        self.combo_querytype.setObjectName(_fromUtf8("combo_querytype"))
        self.combo_querytype.addItem(_fromUtf8(""))
        self.combo_querytype.addItem(_fromUtf8(""))
        self.combo_querytype.addItem(_fromUtf8(""))
        self.combo_querytype.addItem(_fromUtf8(""))
        self.gridLayout_2.addWidget(self.combo_querytype, 2, 1, 1, 1)
        self.label_5 = QtGui.QLabel(self.layoutWidget)
        self.label_5.setAlignment(QtCore.Qt.AlignBottom|QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft)
        self.label_5.setObjectName(_fromUtf8("label_5"))
        self.gridLayout_2.addWidget(self.label_5, 0, 3, 1, 1)
        self.label_3 = QtGui.QLabel(self.layoutWidget)
        self.label_3.setAlignment(QtCore.Qt.AlignBottom|QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft)
        self.label_3.setObjectName(_fromUtf8("label_3"))
        self.gridLayout_2.addWidget(self.label_3, 0, 1, 1, 1)
        self.le_out = QtGui.QLineEdit(self.layoutWidget)
        self.le_out.setMinimumSize(QtCore.QSize(150, 0))
        self.le_out.setObjectName(_fromUtf8("le_out"))
        self.gridLayout_2.addWidget(self.le_out, 2, 3, 1, 1)
        self.table_query_view = QtGui.QTableWidget(self.centralwidget)
        self.table_query_view.setGeometry(QtCore.QRect(-2, 109, 781, 111))
        self.table_query_view.setColumnCount(6)
        self.table_query_view.setObjectName(_fromUtf8("table_query_view"))
        self.table_query_view.setRowCount(0)
        self.table_query_view.horizontalHeader().setCascadingSectionResizes(False)
        self.layoutWidget_2 = QtGui.QWidget(self.centralwidget)
        self.layoutWidget_2.setGeometry(QtCore.QRect(8, 610, 541, 52))
        self.layoutWidget_2.setObjectName(_fromUtf8("layoutWidget_2"))
        self.gridLayout_3 = QtGui.QGridLayout(self.layoutWidget_2)
        self.gridLayout_3.setMargin(0)
        self.gridLayout_3.setObjectName(_fromUtf8("gridLayout_3"))
        self.btn_hist = QtGui.QPushButton(self.layoutWidget_2)
        self.btn_hist.setObjectName(_fromUtf8("btn_hist"))
        self.gridLayout_3.addWidget(self.btn_hist, 0, 0, 1, 1)
        self.label_6 = QtGui.QLabel(self.layoutWidget_2)
        self.label_6.setAlignment(QtCore.Qt.AlignBottom|QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft)
        self.label_6.setObjectName(_fromUtf8("label_6"))
        self.gridLayout_3.addWidget(self.label_6, 0, 1, 1, 1)
        self.label_7 = QtGui.QLabel(self.layoutWidget_2)
        self.label_7.setAlignment(QtCore.Qt.AlignBottom|QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft)
        self.label_7.setObjectName(_fromUtf8("label_7"))
        self.gridLayout_3.addWidget(self.label_7, 0, 3, 1, 1)
        self.btn_scatter = QtGui.QPushButton(self.layoutWidget_2)
        self.btn_scatter.setObjectName(_fromUtf8("btn_scatter"))
        self.gridLayout_3.addWidget(self.btn_scatter, 1, 0, 1, 1)
        self.combo_colorby = QtGui.QComboBox(self.layoutWidget_2)
        self.combo_colorby.setObjectName(_fromUtf8("combo_colorby"))
        self.gridLayout_3.addWidget(self.combo_colorby, 1, 1, 1, 1)
        self.btn_scatter2 = QtGui.QPushButton(self.layoutWidget_2)
        self.btn_scatter2.setObjectName(_fromUtf8("btn_scatter2"))
        self.gridLayout_3.addWidget(self.btn_scatter2, 1, 2, 1, 1)
        self.combo_compareto = QtGui.QComboBox(self.layoutWidget_2)
        self.combo_compareto.setObjectName(_fromUtf8("combo_compareto"))
        self.gridLayout_3.addWidget(self.combo_compareto, 1, 3, 1, 1)
        self.layoutWidget_3 = QtGui.QWidget(self.centralwidget)
        self.layoutWidget_3.setGeometry(QtCore.QRect(0, 1, 781, 51))
        self.layoutWidget_3.setObjectName(_fromUtf8("layoutWidget_3"))
        self.gridLayout = QtGui.QGridLayout(self.layoutWidget_3)
        self.gridLayout.setMargin(0)
        self.gridLayout.setObjectName(_fromUtf8("gridLayout"))
        self.le_sdf_name = QtGui.QLineEdit(self.layoutWidget_3)
        self.le_sdf_name.setMinimumSize(QtCore.QSize(200, 0))
        self.le_sdf_name.setBaseSize(QtCore.QSize(0, 0))
        self.le_sdf_name.setObjectName(_fromUtf8("le_sdf_name"))
        self.gridLayout.addWidget(self.le_sdf_name, 1, 0, 1, 1)
        self.btn_sdf_load = QtGui.QPushButton(self.layoutWidget_3)
        icon = QtGui.QIcon.fromTheme(_fromUtf8("document-open"))
        self.btn_sdf_load.setIcon(icon)
        self.btn_sdf_load.setObjectName(_fromUtf8("btn_sdf_load"))
        self.gridLayout.addWidget(self.btn_sdf_load, 1, 1, 1, 1)
        self.btn_load_prev_cluster = QtGui.QPushButton(self.layoutWidget_3)
        icon = QtGui.QIcon.fromTheme(_fromUtf8("go-previous-view"))
        self.btn_load_prev_cluster.setIcon(icon)
        self.btn_load_prev_cluster.setObjectName(_fromUtf8("btn_load_prev_cluster"))
        self.gridLayout.addWidget(self.btn_load_prev_cluster, 1, 2, 1, 1)
        self.btn_load_next_cluster = QtGui.QPushButton(self.layoutWidget_3)
        self.btn_load_next_cluster.setLayoutDirection(QtCore.Qt.RightToLeft)
        icon = QtGui.QIcon.fromTheme(_fromUtf8("go-next-view"))
        self.btn_load_next_cluster.setIcon(icon)
        self.btn_load_next_cluster.setObjectName(_fromUtf8("btn_load_next_cluster"))
        self.gridLayout.addWidget(self.btn_load_next_cluster, 1, 3, 1, 1)
        self.label = QtGui.QLabel(self.layoutWidget_3)
        self.label.setAlignment(QtCore.Qt.AlignBottom|QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft)
        self.label.setObjectName(_fromUtf8("label"))
        self.gridLayout.addWidget(self.label, 0, 0, 1, 2)
        self.layoutWidget_4 = QtGui.QWidget(self.centralwidget)
        self.layoutWidget_4.setGeometry(QtCore.QRect(10, 230, 791, 375))
        self.layoutWidget_4.setObjectName(_fromUtf8("layoutWidget_4"))
        self.horizontalLayout = QtGui.QHBoxLayout(self.layoutWidget_4)
        self.horizontalLayout.setMargin(0)
        self.horizontalLayout.setObjectName(_fromUtf8("horizontalLayout"))
        self.verticalLayout = QtGui.QVBoxLayout()
        self.verticalLayout.setObjectName(_fromUtf8("verticalLayout"))
        self.label_molimage = QtGui.QLabel(self.layoutWidget_4)
        self.label_molimage.setMinimumSize(QtCore.QSize(300, 300))
        self.label_molimage.setMaximumSize(QtCore.QSize(300, 300))
        self.label_molimage.setContextMenuPolicy(QtCore.Qt.CustomContextMenu)
        self.label_molimage.setAutoFillBackground(True)
        self.label_molimage.setStyleSheet(_fromUtf8("background-color : white;"))
        self.label_molimage.setFrameShape(QtGui.QFrame.Box)
        self.label_molimage.setFrameShadow(QtGui.QFrame.Plain)
        self.label_molimage.setText(_fromUtf8(""))
        self.label_molimage.setAlignment(QtCore.Qt.AlignCenter)
        self.label_molimage.setObjectName(_fromUtf8("label_molimage"))
        self.verticalLayout.addWidget(self.label_molimage)
        self.horizontalLayout_2 = QtGui.QHBoxLayout()
        self.horizontalLayout_2.setObjectName(_fromUtf8("horizontalLayout_2"))
        self.btn_prev = QtGui.QPushButton(self.layoutWidget_4)
        self.btn_prev.setText(_fromUtf8(""))
        icon = QtGui.QIcon.fromTheme(_fromUtf8("go-previous-view"))
        self.btn_prev.setIcon(icon)
        self.btn_prev.setObjectName(_fromUtf8("btn_prev"))
        self.horizontalLayout_2.addWidget(self.btn_prev)
        self.le_recnumber = QtGui.QLineEdit(self.layoutWidget_4)
        self.le_recnumber.setAlignment(QtCore.Qt.AlignCenter)
        self.le_recnumber.setReadOnly(True)
        self.le_recnumber.setObjectName(_fromUtf8("le_recnumber"))
        self.horizontalLayout_2.addWidget(self.le_recnumber)
        self.btn_next = QtGui.QPushButton(self.layoutWidget_4)
        self.btn_next.setText(_fromUtf8(""))
        icon = QtGui.QIcon.fromTheme(_fromUtf8("go-next-view"))
        self.btn_next.setIcon(icon)
        self.btn_next.setObjectName(_fromUtf8("btn_next"))
        self.horizontalLayout_2.addWidget(self.btn_next)
        self.check_rec_selected = QtGui.QCheckBox(self.layoutWidget_4)
        self.check_rec_selected.setObjectName(_fromUtf8("check_rec_selected"))
        self.horizontalLayout_2.addWidget(self.check_rec_selected)
        self.verticalLayout.addLayout(self.horizontalLayout_2)
        spacerItem = QtGui.QSpacerItem(20, 40, QtGui.QSizePolicy.Minimum, QtGui.QSizePolicy.Expanding)
        self.verticalLayout.addItem(spacerItem)
        self.horizontalLayout.addLayout(self.verticalLayout)
        self.verticalLayout_2 = QtGui.QVBoxLayout()
        self.verticalLayout_2.setObjectName(_fromUtf8("verticalLayout_2"))
        self.table_props = QtGui.QTableWidget(self.layoutWidget_4)
        self.table_props.setColumnCount(2)
        self.table_props.setObjectName(_fromUtf8("table_props"))
        self.table_props.setRowCount(0)
        self.verticalLayout_2.addWidget(self.table_props)
        self.check_lipinski = QtGui.QCheckBox(self.layoutWidget_4)
        self.check_lipinski.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.check_lipinski.setObjectName(_fromUtf8("check_lipinski"))
        self.verticalLayout_2.addWidget(self.check_lipinski)
        self.horizontalLayout.addLayout(self.verticalLayout_2)
        self.verticalLayout_3 = QtGui.QVBoxLayout()
        self.verticalLayout_3.setObjectName(_fromUtf8("verticalLayout_3"))
        self.btn_del_sdf = QtGui.QPushButton(self.layoutWidget_4)
        icon = QtGui.QIcon.fromTheme(_fromUtf8("edit-delete"))
        self.btn_del_sdf.setIcon(icon)
        self.btn_del_sdf.setObjectName(_fromUtf8("btn_del_sdf"))
        self.verticalLayout_3.addWidget(self.btn_del_sdf)
        self.btn_sdf_save = QtGui.QPushButton(self.layoutWidget_4)
        icon = QtGui.QIcon.fromTheme(_fromUtf8("document-save"))
        self.btn_sdf_save.setIcon(icon)
        self.btn_sdf_save.setObjectName(_fromUtf8("btn_sdf_save"))
        self.verticalLayout_3.addWidget(self.btn_sdf_save)
        self.btn_session_load = QtGui.QPushButton(self.layoutWidget_4)
        icon = QtGui.QIcon.fromTheme(_fromUtf8("document-open"))
        self.btn_session_load.setIcon(icon)
        self.btn_session_load.setObjectName(_fromUtf8("btn_session_load"))
        self.verticalLayout_3.addWidget(self.btn_session_load)
        self.btn_session_save = QtGui.QPushButton(self.layoutWidget_4)
        icon = QtGui.QIcon.fromTheme(_fromUtf8("document-save"))
        self.btn_session_save.setIcon(icon)
        self.btn_session_save.setObjectName(_fromUtf8("btn_session_save"))
        self.verticalLayout_3.addWidget(self.btn_session_save)
        self.btn_select_all = QtGui.QPushButton(self.layoutWidget_4)
        icon = QtGui.QIcon.fromTheme(_fromUtf8("list-add"))
        self.btn_select_all.setIcon(icon)
        self.btn_select_all.setObjectName(_fromUtf8("btn_select_all"))
        self.verticalLayout_3.addWidget(self.btn_select_all)
        self.btn_select_none = QtGui.QPushButton(self.layoutWidget_4)
        icon = QtGui.QIcon.fromTheme(_fromUtf8("list-remove"))
        self.btn_select_none.setIcon(icon)
        self.btn_select_none.setObjectName(_fromUtf8("btn_select_none"))
        self.verticalLayout_3.addWidget(self.btn_select_none)
        self.btn_select_invert = QtGui.QPushButton(self.layoutWidget_4)
        self.btn_select_invert.setObjectName(_fromUtf8("btn_select_invert"))
        self.verticalLayout_3.addWidget(self.btn_select_invert)
        self.btn_sdf_from_selection = QtGui.QPushButton(self.layoutWidget_4)
        icon = QtGui.QIcon.fromTheme(_fromUtf8("task-accepted"))
        self.btn_sdf_from_selection.setIcon(icon)
        self.btn_sdf_from_selection.setObjectName(_fromUtf8("btn_sdf_from_selection"))
        self.verticalLayout_3.addWidget(self.btn_sdf_from_selection)
        self.btn_copy_molids = QtGui.QPushButton(self.layoutWidget_4)
        icon = QtGui.QIcon.fromTheme(_fromUtf8("edit-copy"))
        self.btn_copy_molids.setIcon(icon)
        self.btn_copy_molids.setObjectName(_fromUtf8("btn_copy_molids"))
        self.verticalLayout_3.addWidget(self.btn_copy_molids)
        self.btn_browse = QtGui.QPushButton(self.layoutWidget_4)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Minimum, QtGui.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.btn_browse.sizePolicy().hasHeightForWidth())
        self.btn_browse.setSizePolicy(sizePolicy)
        icon = QtGui.QIcon.fromTheme(_fromUtf8("download"))
        self.btn_browse.setIcon(icon)
        self.btn_browse.setObjectName(_fromUtf8("btn_browse"))
        self.verticalLayout_3.addWidget(self.btn_browse)
        self.horizontalLayout.addLayout(self.verticalLayout_3)
        MainWindow.setCentralWidget(self.centralwidget)
        self.statusbar = QtGui.QStatusBar(MainWindow)
        self.statusbar.setObjectName(_fromUtf8("statusbar"))
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QObject.connect(self.le_sdf_name, QtCore.SIGNAL(_fromUtf8("returnPressed()")), self.btn_sdf_load.click)
        QtCore.QObject.connect(self.le_out, QtCore.SIGNAL(_fromUtf8("returnPressed()")), self.btn_start.click)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)
        MainWindow.setTabOrder(self.le_sdf_name, self.btn_sdf_load)
        MainWindow.setTabOrder(self.btn_sdf_load, self.btn_load_prev_cluster)
        MainWindow.setTabOrder(self.btn_load_prev_cluster, self.btn_load_next_cluster)
        MainWindow.setTabOrder(self.btn_load_next_cluster, self.le_curr_sdf)
        MainWindow.setTabOrder(self.le_curr_sdf, self.combo_querytype)
        MainWindow.setTabOrder(self.combo_querytype, self.le_query)
        MainWindow.setTabOrder(self.le_query, self.le_out)
        MainWindow.setTabOrder(self.le_out, self.btn_start)
        MainWindow.setTabOrder(self.btn_start, self.btn_prev)
        MainWindow.setTabOrder(self.btn_prev, self.le_recnumber)
        MainWindow.setTabOrder(self.le_recnumber, self.btn_next)
        MainWindow.setTabOrder(self.btn_next, self.check_lipinski)
        MainWindow.setTabOrder(self.check_lipinski, self.btn_hist)
        MainWindow.setTabOrder(self.btn_hist, self.btn_scatter)
        MainWindow.setTabOrder(self.btn_scatter, self.combo_colorby)
        MainWindow.setTabOrder(self.combo_colorby, self.btn_scatter2)
        MainWindow.setTabOrder(self.btn_scatter2, self.combo_compareto)
        MainWindow.setTabOrder(self.combo_compareto, self.btn_del_sdf)
        MainWindow.setTabOrder(self.btn_del_sdf, self.btn_sdf_save)
        MainWindow.setTabOrder(self.btn_sdf_save, self.btn_session_load)
        MainWindow.setTabOrder(self.btn_session_load, self.btn_session_save)
        MainWindow.setTabOrder(self.btn_session_save, self.table_props)
        MainWindow.setTabOrder(self.table_props, self.table_query_view)

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(_translate("MainWindow", "SDF Viewer", None))
        self.btn_start.setText(_translate("MainWindow", "start", None))
        self.label_2.setText(_translate("MainWindow", " current sdf", None))
        self.label_4.setText(_translate("MainWindow", " query", None))
        self.combo_querytype.setToolTip(_translate("MainWindow", "<html><head/><body><p>remember to prefix the fieldnames with &quot;s_&quot;, &quot;n_&quot; or &quot;k_&quot; in the factsearch and that string literals are lowercase, e.g.:</p><p>&quot;m.5&quot; in s_family <br/>n_pIC50 &gt;= 8</p></body></html>", None))
        self.combo_querytype.setItemText(0, _translate("MainWindow", "fact", None))
        self.combo_querytype.setItemText(1, _translate("MainWindow", "fact_inverted", None))
        self.combo_querytype.setItemText(2, _translate("MainWindow", "substruct", None))
        self.combo_querytype.setItemText(3, _translate("MainWindow", "substruct_inverted", None))
        self.label_5.setText(_translate("MainWindow", " store in", None))
        self.label_3.setText(_translate("MainWindow", " querytype", None))
        self.btn_hist.setText(_translate("MainWindow", "histogram", None))
        self.label_6.setText(_translate("MainWindow", " color by", None))
        self.label_7.setText(_translate("MainWindow", " compare to", None))
        self.btn_scatter.setText(_translate("MainWindow", "scattermatrix", None))
        self.btn_scatter2.setText(_translate("MainWindow", "scattermatrix2", None))
        self.btn_sdf_load.setText(_translate("MainWindow", "load", None))
        self.btn_load_prev_cluster.setText(_translate("MainWindow", "load prev", None))
        self.btn_load_next_cluster.setText(_translate("MainWindow", "load next", None))
        self.label.setText(_translate("MainWindow", " sd file", None))
        self.check_rec_selected.setText(_translate("MainWindow", "selected", None))
        self.check_lipinski.setText(_translate("MainWindow", "highlight Lipinski", None))
        self.btn_del_sdf.setText(_translate("MainWindow", "delete\n"
"current sdf", None))
        self.btn_sdf_save.setText(_translate("MainWindow", "save \n"
"current sdf", None))
        self.btn_session_load.setText(_translate("MainWindow", "load session", None))
        self.btn_session_save.setText(_translate("MainWindow", "save session", None))
        self.btn_select_all.setText(_translate("MainWindow", "select all", None))
        self.btn_select_none.setText(_translate("MainWindow", "select none", None))
        self.btn_select_invert.setText(_translate("MainWindow", "invert selection", None))
        self.btn_sdf_from_selection.setText(_translate("MainWindow", "create sdf \n"
"from selection", None))
        self.btn_copy_molids.setText(_translate("MainWindow", "copy selected \n"
"molids", None))
        self.btn_browse.setText(_translate("MainWindow", "open in\n"
" browser", None))

