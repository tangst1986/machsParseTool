# -*- coding: utf-8 -*-


from PyQt4 import QtCore, QtGui
from PyQt4.QtGui import *  # @UnusedWildImport
from PyQt4.QtCore import QThread, SIGNAL
import logging
import time
from business import *  # @UnusedWildImport
from config import *  # @UnusedWildImport
from draw_business import *


BinFileList = None
core_no = ''
cell_no = ''
user_no = ''
operation = ''
gta_path = ''
sack_path = ''
config_path = ''

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


class Operation_Thread(QThread):
    def SendText(self, text):
        self.emit(SIGNAL("setText(QString)"), text)
        
    def pbShowCoreList(self, core_list):
        self.emit(SIGNAL("showCoreList(QStringList)"), core_list)

    def pbShowCellList(self, cell_list):
        self.emit(SIGNAL("showCellList(QStringList)"), cell_list)
        
    def pbShowUserList(self, user_list):
        self.emit(SIGNAL("showUserList(QStringList)"), user_list)
         
    def run(self):
        global core_no, cell_no, user_no, operation, BinFileList, gta_path, sack_path, config_path
        
        if operation == r'export':
            click_export_btn(core_no, cell_no, user_no)
            
        elif operation == r'parse':
            startParseBin(BinFileList, self.SendText, self.pbShowCoreList, self.pbShowCellList, self.pbShowUserList,
                          gta_path, sack_path, config_path)
            
        else:
            self.SendText("fail: %s operation not defined" % operation)            
            
        self.SendText("finish")

class Timer(QThread):
    def SendText(self, text):
        self.emit(SIGNAL("setText(QString)"), text)
        
    def run(self):
        while True:
            self.SendText('.')
            self.sleep(2)


class Ui_MainWindow(QMainWindow):
    def __init__(self):
        super(Ui_MainWindow,self).__init__()
        MainWindow = self
        self.setupUi(MainWindow)
        self.addControlEvent()

        self.threadInit()
        
        self.check_tracefile_btn.setEnabled(False)
        
        self.setComponetInit()
        
        setup_path(False)
    
    def setupUi(self, MainWindow):
        MainWindow.setObjectName(_fromUtf8("MainWindow"))
        MainWindow.resize(890, 679)
        self.centralwidget = QtGui.QWidget(MainWindow)
        self.centralwidget.setObjectName(_fromUtf8("centralwidget"))
        self.groupBox_selectBin = QtGui.QGroupBox(self.centralwidget)
        self.groupBox_selectBin.setGeometry(QtCore.QRect(10, 20, 841, 281))
        self.groupBox_selectBin.setObjectName(_fromUtf8("groupBox_selectBin"))
        self.label_address = QtGui.QLabel(self.groupBox_selectBin)
        self.label_address.setGeometry(QtCore.QRect(20, 20, 91, 16))
        self.label_address.setObjectName(_fromUtf8("label_address"))
        self.listWidget_binAddress = QtGui.QListWidget(self.groupBox_selectBin)
        self.listWidget_binAddress.setGeometry(QtCore.QRect(60, 40, 641, 111))
        self.listWidget_binAddress.setObjectName(_fromUtf8("listWidget_binAddress"))
        self.pButton_addAddress = QtGui.QPushButton(self.groupBox_selectBin)
        self.pButton_addAddress.setGeometry(QtCore.QRect(720, 40, 93, 28))
        self.pButton_addAddress.setObjectName(_fromUtf8("pButton_addAddress"))
        self.pButton_removeAddr = QtGui.QPushButton(self.groupBox_selectBin)
        self.pButton_removeAddr.setGeometry(QtCore.QRect(720, 80, 93, 28))
        self.pButton_removeAddr.setObjectName(_fromUtf8("pButton_removeAddr"))
        self.pushButton_parse = QtGui.QPushButton(self.groupBox_selectBin)
        self.pushButton_parse.setGeometry(QtCore.QRect(720, 120, 93, 28))
        self.pushButton_parse.setObjectName(_fromUtf8("pushButton_parse"))
        self.label_address_2 = QtGui.QLabel(self.groupBox_selectBin)
        self.label_address_2.setGeometry(QtCore.QRect(20, 170, 91, 16))
        self.label_address_2.setObjectName(_fromUtf8("label_address_2"))
        self.gta_path_text = QtGui.QTextEdit(self.groupBox_selectBin)
        self.gta_path_text.setGeometry(QtCore.QRect(20, 190, 201, 41))
        self.gta_path_text.setObjectName(_fromUtf8("gta_path_text"))
        self.label_address_3 = QtGui.QLabel(self.groupBox_selectBin)
        self.label_address_3.setGeometry(QtCore.QRect(270, 170, 91, 16))
        self.label_address_3.setObjectName(_fromUtf8("label_address_3"))
        self.sack_path_text = QtGui.QTextEdit(self.groupBox_selectBin)
        self.sack_path_text.setGeometry(QtCore.QRect(260, 190, 201, 41))
        self.sack_path_text.setObjectName(_fromUtf8("sack_path_text"))
        self.config_path_text = QtGui.QTextEdit(self.groupBox_selectBin)
        self.config_path_text.setGeometry(QtCore.QRect(500, 190, 201, 41))
        self.config_path_text.setObjectName(_fromUtf8("config_path_text"))
        self.label_address_4 = QtGui.QLabel(self.groupBox_selectBin)
        self.label_address_4.setGeometry(QtCore.QRect(510, 170, 91, 16))
        self.label_address_4.setObjectName(_fromUtf8("label_address_4"))
        self.select_type_comboBox = QtGui.QComboBox(self.groupBox_selectBin)
        self.select_type_comboBox.setGeometry(QtCore.QRect(250, 241, 261, 31))
        self.select_type_comboBox.setObjectName(_fromUtf8("select_type_comboBox"))
        self.pushButton_gta_path = QtGui.QPushButton(self.groupBox_selectBin)
        self.pushButton_gta_path.setGeometry(QtCore.QRect(90, 160, 81, 28))
        self.pushButton_gta_path.setObjectName(_fromUtf8("pushButton_gta_path"))
        self.pushButton_sack_path = QtGui.QPushButton(self.groupBox_selectBin)
        self.pushButton_sack_path.setGeometry(QtCore.QRect(350, 160, 71, 28))
        self.pushButton_sack_path.setObjectName(_fromUtf8("pushButton_sack_path"))
        self.pushButton_config_path = QtGui.QPushButton(self.groupBox_selectBin)
        self.pushButton_config_path.setGeometry(QtCore.QRect(600, 160, 71, 28))
        self.pushButton_config_path.setObjectName(_fromUtf8("pushButton_config_path"))
        self.groupBox_display = QtGui.QGroupBox(self.centralwidget)
        self.groupBox_display.setGeometry(QtCore.QRect(10, 320, 351, 201))
        self.groupBox_display.setObjectName(_fromUtf8("groupBox_display"))
        self.lw_core = QtGui.QListWidget(self.groupBox_display)
        self.lw_core.setGeometry(QtCore.QRect(20, 60, 71, 121))
        self.lw_core.setObjectName(_fromUtf8("lw_core"))
        self.label_address_5 = QtGui.QLabel(self.groupBox_display)
        self.label_address_5.setGeometry(QtCore.QRect(20, 40, 91, 16))
        self.label_address_5.setObjectName(_fromUtf8("label_address_5"))
        self.label_address_6 = QtGui.QLabel(self.groupBox_display)
        self.label_address_6.setGeometry(QtCore.QRect(130, 40, 71, 16))
        self.label_address_6.setObjectName(_fromUtf8("label_address_6"))
        self.lw_cell = QtGui.QListWidget(self.groupBox_display)
        self.lw_cell.setGeometry(QtCore.QRect(120, 60, 71, 121))
        self.lw_cell.setObjectName(_fromUtf8("lw_cell"))
        self.label_address_7 = QtGui.QLabel(self.groupBox_display)
        self.label_address_7.setGeometry(QtCore.QRect(240, 40, 71, 16))
        self.label_address_7.setObjectName(_fromUtf8("label_address_7"))
        self.lw_user = QtGui.QListWidget(self.groupBox_display)
        self.lw_user.setGeometry(QtCore.QRect(230, 60, 71, 121))
        self.lw_user.setObjectName(_fromUtf8("lw_user"))
        self.groupBox_query = QtGui.QGroupBox(self.centralwidget)
        self.groupBox_query.setGeometry(QtCore.QRect(390, 320, 461, 201))
        self.groupBox_query.setObjectName(_fromUtf8("groupBox_query"))
        self.label_address_11 = QtGui.QLabel(self.groupBox_query)
        self.label_address_11.setGeometry(QtCore.QRect(20, 40, 91, 16))
        self.label_address_11.setObjectName(_fromUtf8("label_address_11"))
        self.label_address_12 = QtGui.QLabel(self.groupBox_query)
        self.label_address_12.setGeometry(QtCore.QRect(120, 40, 71, 16))
        self.label_address_12.setObjectName(_fromUtf8("label_address_12"))
        self.label_address_13 = QtGui.QLabel(self.groupBox_query)
        self.label_address_13.setGeometry(QtCore.QRect(240, 40, 71, 16))
        self.label_address_13.setObjectName(_fromUtf8("label_address_13"))
        self.core_query_no = QtGui.QTextEdit(self.groupBox_query)
        self.core_query_no.setGeometry(QtCore.QRect(20, 60, 81, 31))
        self.core_query_no.setObjectName(_fromUtf8("core_query_no"))
        self.cell_query_no = QtGui.QTextEdit(self.groupBox_query)
        self.cell_query_no.setGeometry(QtCore.QRect(120, 60, 91, 31))
        self.cell_query_no.setObjectName(_fromUtf8("cell_query_no"))
        self.user_query_no = QtGui.QTextEdit(self.groupBox_query)
        self.user_query_no.setGeometry(QtCore.QRect(240, 60, 91, 31))
        self.user_query_no.setObjectName(_fromUtf8("user_query_no"))
        self.cell_throughput_btn = QtGui.QPushButton(self.groupBox_query)
        self.cell_throughput_btn.setGeometry(QtCore.QRect(20, 130, 141, 28))
        self.cell_throughput_btn.setObjectName(_fromUtf8("cell_throughput_btn"))
        self.user_throughput_btn = QtGui.QPushButton(self.groupBox_query)
        self.user_throughput_btn.setGeometry(QtCore.QRect(200, 130, 141, 28))
        self.user_throughput_btn.setObjectName(_fromUtf8("user_throughput_btn"))
        self.export_btn = QtGui.QPushButton(self.groupBox_query)
        self.export_btn.setGeometry(QtCore.QRect(350, 60, 91, 28))
        self.export_btn.setObjectName(_fromUtf8("export_btn"))
        self.groupBox_logs = QtGui.QGroupBox(self.centralwidget)
        self.groupBox_logs.setGeometry(QtCore.QRect(20, 530, 831, 121))
        self.groupBox_logs.setObjectName(_fromUtf8("groupBox_logs"))
        self.textBrowser_logs = QtGui.QTextBrowser(self.groupBox_logs)
        self.textBrowser_logs.setGeometry(QtCore.QRect(20, 30, 471, 81))
        self.textBrowser_logs.setObjectName(_fromUtf8("textBrowser_logs"))
        self.check_tracefile_btn = QtGui.QPushButton(self.groupBox_logs)
        self.check_tracefile_btn.setGeometry(QtCore.QRect(560, 50, 141, 28))
        self.check_tracefile_btn.setObjectName(_fromUtf8("check_tracefile_btn"))
        MainWindow.setCentralWidget(self.centralwidget)
        self.statusbar = QtGui.QStatusBar(MainWindow)
        self.statusbar.setObjectName(_fromUtf8("statusbar"))
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow  (V%s)" % SOFT_VERSION, None))
        self.groupBox_selectBin.setTitle(_translate("MainWindow", "Select File", None))
        self.label_address.setText(_translate("MainWindow", "TraceFile", None))
        self.pButton_addAddress.setText(_translate("MainWindow", "Add", None))
        self.pButton_removeAddr.setText(_translate("MainWindow", "remove", None))
        self.pushButton_parse.setText(_translate("MainWindow", "parse", None))
        self.label_address_2.setText(_translate("MainWindow", "GTA_PATH", None))
        self.label_address_3.setText(_translate("MainWindow", "SACK_PATH", None))
        self.label_address_4.setText(_translate("MainWindow", "CONFIG_PATH", None))
        self.pushButton_gta_path.setText(_translate("MainWindow", "...", None))
        self.pushButton_sack_path.setText(_translate("MainWindow", "...", None))
        self.pushButton_config_path.setText(_translate("MainWindow", "...", None))
        self.groupBox_display.setTitle(_translate("MainWindow", "Select display info", None))
        self.label_address_5.setText(_translate("MainWindow", "Core_list", None))
        self.label_address_6.setText(_translate("MainWindow", "Cell_list", None))
        self.label_address_7.setText(_translate("MainWindow", "User_list", None))
        self.groupBox_query.setTitle(_translate("MainWindow", "Query", None))
        self.label_address_11.setText(_translate("MainWindow", "Core_no", None))
        self.label_address_12.setText(_translate("MainWindow", "Cell_no", None))
        self.label_address_13.setText(_translate("MainWindow", "User_no", None))
        self.cell_throughput_btn.setText(_translate("MainWindow", "Cell Throughput", None))
        self.user_throughput_btn.setText(_translate("MainWindow", "User Throughput", None))
        self.export_btn.setText(_translate("MainWindow", "export", None))
        self.groupBox_logs.setTitle(_translate("MainWindow", "Log", None))
        self.check_tracefile_btn.setText(_translate("MainWindow", "check trace file", None))
    
    
    def setComponetInit(self):
        self.controlGTAComponet(True)
        self.select_type_comboBox.addItem("bin trace file")
        self.select_type_comboBox.addItem("text trace file")
        self.gta_path_text.setPlainText(r"D:\CI\CI_TOOL\GTA_Plugin_Giant\Bin\GTA_Plugin_Giant.exe")
    
    def controlGTAComponet(self, is_enable):
        self.gta_path_text.setEnabled(is_enable)
        self.sack_path_text.setEnabled(is_enable)
        self.config_path_text.setEnabled(is_enable)
        if is_enable:
            self.pushButton_gta_path.setHidden(False)
            self.pushButton_config_path.setHidden(False)
            self.pushButton_sack_path.setHidden(False)
        else:
            self.pushButton_gta_path.setHidden(True)
            self.pushButton_config_path.setHidden(True)
            self.pushButton_sack_path.setHidden(True)
    
    def threadInit(self):
        self.timer = Timer()
        self.connect(self.timer, SIGNAL("setText(QString)"), self.addTimerText)
        
        self.operation_thread = Operation_Thread()
        self.connect(self.operation_thread, SIGNAL("setText(QString)"),    self.DisplayText)
        self.connect(self.operation_thread, SIGNAL("showCoreList(QStringList)"),    self.showCoreList)
        self.connect(self.operation_thread, SIGNAL("showCellList(QStringList)"), self.showCellList)
        self.connect(self.operation_thread, SIGNAL("showUserList(QStringList)"),    self.showUserList)
    
    def addTimerText(self, text):
        new_text = self.textBrowser_logs.toPlainText() + text
        self.textBrowser_logs.setText(new_text)
        
    def actionSelectBinFile(self):
        global BinFileList
        directory = "/"
        binFile = QFileDialog.getOpenFileName(None,
                                              'Select a TTI-Trace bin file',
                                              directory)
        if binFile == "":
            return
        
        BinFileList = [str(self.listWidget_binAddress.item(x).text()) for x in range(self.listWidget_binAddress.count())]
        BinFileList.append(str(binFile))
        BinFileList = list(set(BinFileList))
        self.listWidget_binAddress.clear()
        self.listWidget_binAddress.addItems(BinFileList)
    
    def actionBinFileRemove(self):
        global BinFileList
        
        select_list = self.listWidget_binAddress.selectedItems()
        if not select_list:
            return
        for ele in select_list:
            BinFileList.remove(ele.text())

        self.listWidget_binAddress.takeItem(self.listWidget_binAddress.currentRow())
  
    def addControlEvent(self):
        self.pButton_addAddress.clicked.connect(self.actionSelectBinFile)
        self.pButton_removeAddr.clicked.connect(self.actionBinFileRemove)
        self.pushButton_parse.clicked.connect(self.actionParse)
        self.user_throughput_btn.clicked.connect(self.user_throughput_btn_click)
        self.cell_throughput_btn.clicked.connect(self.cell_throughput_btn_click)
        self.export_btn.clicked.connect(self.export_btn_click)
        self.lw_core.itemClicked.connect(self.coreItemClick)
        self.lw_cell.itemClicked.connect(self.cellItemClick)
        self.lw_user.itemClicked.connect(self.userItemClick)
        
        self.check_tracefile_btn.clicked.connect(self.check_tracefile_btn_click)
        
        self.select_type_comboBox.currentIndexChanged.connect(self.select_type_parse)
        
        self.pushButton_gta_path.clicked.connect(self.click_gta_path_btn)
        self.pushButton_config_path.clicked.connect(self.click_config_path_btn)
        self.pushButton_sack_path.clicked.connect(self.click_sack_path_btn)
        
    def click_gta_path_btn(self):
        directory = r'/'
        gta_exe_path = QFileDialog.getOpenFileName(None,
                                              'Select the gta exe path',
                                              directory, "*.exe")
        self.gta_path_text.setPlainText(gta_exe_path)
    
    def click_config_path_btn(self):
        directory = r'/'
        config_file_path = QFileDialog.getOpenFileName(None,
                                              'Select the config file path',
                                              directory)
        self.config_path_text.setPlainText(config_file_path)
        
    def click_sack_path_btn(self):
        directory = r'/'
        sack_file_path = QFileDialog.getOpenFileName(None,
                                              'Select the sack file path',
                                              directory)
        self.sack_path_text.setPlainText(sack_file_path)
        
    
    def select_type_parse(self):
        file_type = self.select_type_comboBox.currentText()
        if file_type == 'text trace file':
            self.controlGTAComponet(False)
        else:
            self.controlGTAComponet(True)
            
        
      
    def check_tracefile_btn_click(self):
        self.textBrowser_logs.clear()
        is_right = click_check_tracefile()
        if not is_right:
            self.DisplayText("fail: trace file is not correct!")
        else:
            self.DisplayText("the trace file is OK")
 
    def queryInfoClear(self):
        self.cell_query_no.clear()
        self.core_query_no.clear()
        self.user_query_no.clear()
 
    def listInfoClear(self):
        self.lw_cell.clear()
        self.lw_core.clear()
        self.lw_user.clear()
 
    def coreItemClick(self):
        self.lw_cell.clear()
        self.lw_user.clear()
        core_no = self.lw_core.currentItem().text()
        if core_no == 'all':
            core_no = ''
        self.core_query_no.setText(core_no)
        clickCoreItem(core_no, self.showCellList, self.showUserList)        
 
    def cellItemClick(self):
        self.lw_user.clear()
        core_no = ''
        if self.lw_core.currentItem():
            core_no = self.lw_core.currentItem().text()
            if core_no == 'all':
                core_no = ''
        cell_no = self.lw_cell.currentItem().text()
        if cell_no == 'all':
            cell_no = ''
        self.cell_query_no.setText(cell_no)
        clickCellItem(core_no, cell_no, self.showUserList)
    
    def userItemClick(self):
        user_no = self.lw_user.currentItem().text()
        if user_no == 'all':
            user_no = ''
        self.user_query_no.setText(user_no)
 
    def set_enable_components(self, is_enable):
        self.pButton_addAddress.setEnabled(is_enable)
        self.pButton_removeAddr.setEnabled(is_enable)
        self.pushButton_parse.setEnabled(is_enable)
        self.user_throughput_btn.setEnabled(is_enable)
        self.cell_throughput_btn.setEnabled(is_enable)
        self.export_btn.setEnabled(is_enable)
        self.check_tracefile_btn.setEnabled(is_enable)
    
    def actionParse(self):
        global operation, gta_path, sack_path, config_path
        
        cleanDirs()
        cleanupResource()
        
        
        setup_dirs()
        self.listInfoClear()
        operation = r'parse'
        
        gta_path = self.gta_path_text.toPlainText()
        sack_path = self.sack_path_text.toPlainText()
        config_path = self.config_path_text.toPlainText()
        
        self.operation_func()
    
    def showOperationInfo(self, start_time, end_time):
        global operation
        text_str = operation + ' finish: cost %.3f seconds' % (end_time - start_time)
        self.textBrowser_logs.append(text_str)
    
    def operation_func(self):
        global operation
        
        self.textBrowser_logs.clear()
        self.start_time = time.clock()
        self.DisplayText("start %s" % operation)
   
        self.set_enable_components(False)
         
        self.operation_thread.start()
        self.timer.start()
    
    def user_throughput_btn_click(self):
        self.textBrowser_logs.clear()
        self.DisplayText("start draw user")
        
        core_no = self.core_query_no.toPlainText()
        cell_no = self.cell_query_no.toPlainText()
        user_no = self.user_query_no.toPlainText()
        
        rs = click_user_throughput_btn(core_no, cell_no, user_no)
        if not rs:
            self.DisplayText("fail to draw user: not find selected data")
        
        self.DisplayText("draw user finish")
        
    def cell_throughput_btn_click(self):
        self.textBrowser_logs.clear()
        self.DisplayText("start draw cell")
    
        core_no = self.core_query_no.toPlainText()
        cell_no = self.cell_query_no.toPlainText()
        user_no = self.user_query_no.toPlainText()
        
        rs = click_cell_throughput_btn(core_no, cell_no, user_no)
        if not rs:
            self.DisplayText("fail to draw cell: not find selected data")
        
        self.DisplayText("draw cell finish")
    
    def export_btn_click(self):
        global core_no, cell_no, user_no, operation
        operation = r'export'

        core_no = self.core_query_no.toPlainText()
        cell_no = self.cell_query_no.toPlainText()
        user_no = self.user_query_no.toPlainText()
        self.operation_func()
        
    def DisplayText(self, text):
        logging.info(text)
        
        fail_set = False
        if "fail" in text:
            self.textBrowser_logs.setTextColor(QColor(255,0,0))
            fail_set = True
        
        if text == r'finish':
            self.set_enable_components(True)
            self.timer.terminate()
            self.showOperationInfo(self.start_time, time.clock())
        else:
            self.textBrowser_logs.append(text)
        
        if fail_set:
            self.textBrowser_logs.setTextColor(QColor(0))

    def showCoreList(self, core_list):
        self.lw_core.addItems(core_list)
        
    def showCellList(self, cell_list):
        self.lw_cell.addItems(cell_list)
        
    def showUserList(self, user_list):
        self.lw_user.addItems(user_list)