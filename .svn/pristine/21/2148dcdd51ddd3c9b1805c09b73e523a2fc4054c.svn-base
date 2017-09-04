'''
Created on 2015\5\24

@author: m1tang
'''

import shutil
import os
from db_class import *  # @UnusedWildImport
from csv_class import csv_class
from parseTtiTraceWithUTest import BlindParseMachsTtiTrace, MACHS_TTI_TRACE_BIT_FIELD_FOR_CELL_INFO, MACHS_TTI_TRACE_BIT_FIELD, MACHS_TTI_TRACE_BIT_FIELD_FOR_CELL
from config import *
import subprocess
from hfile2sack import ret_sack

global BASE_PATH, DB_PATH, DB_FILE, BACKUP_PATH, EXPORT_PATH,  PIC_PATH

global is_support_cadc

is_support_cadc = False

def get_cell_sack(trace_file):
    global g_all_cell, g_one_cell
    tmp_core_sack, tmp_cell_sack, tmp_user_sack = ret_sack(trace_file)
    if tmp_cell_sack:
        g_all_cell = tmp_cell_sack
        g_one_cell =  g_all_cell[0][1]
    else:
        g_all_cell = MACHS_TTI_TRACE_BIT_FIELD_FOR_CELL
        g_one_cell = MACHS_TTI_TRACE_BIT_FIELD_FOR_CELL_INFO
    return tmp_core_sack, tmp_cell_sack, tmp_user_sack

def setup_path(is_cmd_mode):
    global BASE_PATH, DB_PATH, DB_FILE, BACKUP_PATH, EXPORT_PATH,  PIC_PATH
    global g_one_cell, g_all_cell
    
    if is_cmd_mode:
        BASE_PATH = os.path.join(os.getcwd(), 'tmp_data') + '\\'
        DB_PATH = BASE_PATH
        DB_FILE = DB_PATH  + 'ttiTrace.db'
        BACKUP_PATH = BASE_PATH
        EXPORT_PATH =BASE_PATH
        PIC_PATH = BASE_PATH
        g_one_cell = MACHS_TTI_TRACE_BIT_FIELD_FOR_CELL_INFO
        g_all_cell = MACHS_TTI_TRACE_BIT_FIELD_FOR_CELL
    else:
        BASE_PATH = os.path.abspath(os.path.join(os.getcwd(), ".."))
        DB_PATH = BASE_PATH + '\\DATA\\'
        DB_FILE = DB_PATH  + 'ttiTrace.db'
        BACKUP_PATH = BASE_PATH + '\\Backup\\'
        EXPORT_PATH = BASE_PATH + '\\Export\\'
        PIC_PATH = BASE_PATH + '\\Picture\\'
    

def getShowList():
    global DB_FILE
    
    core_list = None
    cell_list = None
    user_list = None
    
    db_obj = db_class(DB_FILE)
    rs = db_obj.findCore(CORE_TABLE_NAME)
    if rs:
        core_list = db_obj.translateCoreRsToList(rs)
        core_list = [str(item) for item in core_list]
        core_list.insert(0, 'all')
         
    rs = db_obj.findCell(CELL_TABLE_NAME)
    if rs:
        cell_list = db_obj.translateCellRsToList(rs)
        cell_list = [str(item) for item in cell_list]
        if '0' in cell_list:
            del cell_list[cell_list.index('0')]
         
    rs = db_obj.findUser(USER_TABLE_NAME)
    if rs:
        user_list = db_obj.translateUserRsToList(rs)
        user_list = [str(item) for item in user_list]
    
    return core_list, cell_list, user_list

def read_write(src_file, target_file):
    rd_file = open(src_file,'r')
    wr_file =  open(target_file, 'w')
    
    rd_file.readline()
    while True:
        data = rd_file.readline()
        if not data:
            break
        wr_file.write(data)
    rd_file.close()
    wr_file.close()
    
def useGTAParse(bin_file, gta_path, sack_path, config_path):
    global DB_PATH, EXPORT_PATH
    
    
    if sack_path == '' and config_path == '':
        cmd =  "%s -p -f %s -o %s --noassist --noupdate" % (gta_path, bin_file, EXPORT_PATH)
    elif sack_path == '':
        cmd =  "%s -p -f %s -c %s -o %s --noassist --noupdate" % (gta_path, bin_file, config_path, EXPORT_PATH)
    elif config_path == '':
        cmd =  "%s -p -f %s -d %s -o %s --noassist --noupdate" % (gta_path, bin_file, sack_path, EXPORT_PATH)
    else:
        cmd =  "%s -p -f %s -d %s -c %s -o %s --noassist --noupdate" % (gta_path, bin_file, sack_path, config_path, EXPORT_PATH)
    
    try:
        output = subprocess.check_output(cmd)
        print output
    except subprocess.CalledProcessError as e:
        print e.output
        print "err: please check the GTA cmd"
        return None
    
    base_name = os.path.basename(bin_file)[:-4]
    parse_file_path =  EXPORT_PATH + base_name
    for ele in os.listdir(parse_file_path):
        src_file = os.path.join(parse_file_path, ele)
            
        if "Core" in ele:
            target_file = DB_PATH + base_name + "_core.csv"
        elif "Cell" in ele:
            target_file = DB_PATH + base_name + "_cell.csv"
        elif "User" in ele:
            target_file = DB_PATH + base_name + "_user.csv"
        else:
            continue
        read_write(src_file, target_file)
    
    file_path =  DB_PATH + base_name + "_core.csv"
    core_file = open(file_path, 'r')
    core_file.readline()
    core_file.readline()
    core_data = core_file.readline().split(',')
    core_no = core_data[-1][:-1]
    core_file.close()    

    return core_no

def startParseBin(file_list, setText, showCoreList, showCellList, showUserList, gta_path, sack_path, config_path):
    global is_support_cadc
    
    core_no = None
    if not file_list:
        return 
    if len(file_list) < 1:
        return
    core_sack, cell_sack, user_sack = get_cell_sack(file_list[0])
    
    if len(file_list) > 1:
        is_support_cadc = True
    
    for ele in file_list:
        if ele[-4:] == '.txt':
            bp_obj = BlindParseMachsTtiTrace(ele, core_sack, cell_sack, user_sack)
            core_no = bp_obj.core_no
        elif ele[-4:] == '.bin':
            core_no = useGTAParse(ele, gta_path, sack_path, config_path)
        else:
            print "not support file type %s" % ele[-3:]
            return
        if not core_no:
            continue
        createTableFromFileList(int(core_no))
        
    core_list, cell_list, user_list = getShowList()
    if showCoreList and core_list:
        showCoreList(core_list)  
    if showCellList and cell_list:
        showCellList(cell_list)
    if showUserList and user_list:
        showUserList(user_list)  
   
    if setText:
        setText("parse file finish")   

def createTableFromFileList(core_no):
    global DB_PATH
    
    data_file_list = os.listdir(DB_PATH)
    for ele in data_file_list:
        if ele[-4:] != '.csv':
            continue
        data_file = DB_PATH + ele
        createTableInDB(data_file, core_no)

def getCellColumnToDB():
    global g_one_cell
    cell_column_list = []
    
    for ele in MACHS_TTI_TRACE_BIT_FIELD:
        cell_column_list.append(ele[0])
    
     
    for ele in g_one_cell:
        cell_column_list.append(ele[0])
        
    return cell_column_list
    

def createTableInDB(file_path, core_no):
    global DB_FILE, BACKUP_PATH
    
    file_name = os.path.basename(file_path)
    table_type = file_name.split(".")[0][-4:]
    
    csv_obj = csv_class(file_path, 'r+')
    table_column_list = csv_obj.getDBColumn()
    db_obj = db_class(DB_FILE)
    
    type_range = ['core', 'cell', 'user']
    if table_type not in type_range:
        print "file table can't create"
    
    if table_type == r"core":
        db_obj.createCoreTable(table_column_list)
        try:
            db_obj.createCoreIndex()
        except Exception as e:
            print e
        table_name = CORE_TABLE_NAME 
    elif table_type == r"cell":
        table_column_list = getCellColumnToDB()
        db_obj.createCellTable(table_column_list)
        table_name = CELL_TABLE_NAME
       
    else:
        db_obj.createUserTable(table_column_list)
        table_name = USER_TABLE_NAME
        
    insertCsvDataToDB(csv_obj, db_obj, core_no, table_name)
    csv_obj.closeFile()
    db_obj.commitDB()
    db_obj.closeDB()
        
    if os.path.dirname(file_path) == os.path.dirname(BACKUP_PATH):
        pass
    else:
        try:   
            shutil.move(file_path, BACKUP_PATH)
        except Exception as e:
            print "move failed: %s" % str(e)
 
def insertCellDataToDB(core_no, table_name, db_obj, read_line):
    global g_all_cell, g_one_cell
    common_title_len = len(MACHS_TTI_TRACE_BIT_FIELD)
    cell_data_len = len(g_one_cell)
    cell_num = len(g_all_cell)
    
    common_title_list = []
    cell_data_list = []
    
    data_list = read_line.split(',')
    common_title_list = data_list[:common_title_len ]
    
    for i in range(0, cell_num):
        start_pos = common_title_len + cell_data_len * i
        end_pos = start_pos + cell_data_len
        cell_data_list += common_title_list
        cell_data_list += data_list[start_pos:end_pos]
        if i != cell_num - 1:
            cell_data_list[-1] += '\n'
        db_obj.insertData(core_no, table_name, cell_data_list)
        cell_data_list = []
    
def insertCsvDataToDB(csv_obj, db_obj, core_no, table_name):
    csv_file = csv_obj.getCsvFile()
    line = csv_file.readline()  #skip first line
    while True:
        line = csv_file.readline()
        if not line:
            break
        
        if table_name == CELL_TABLE_NAME:
            insertCellDataToDB(core_no, table_name, db_obj, line)
        else:
            db_obj.insertData(core_no, table_name, line.split(','))

def write_db_column_to_csv_file(rs, csv_file):
    column_name_list = []
    
    if not rs:
        return
    
    rs_list = rs.fetchall()
    for ele in rs_list:
        column_name_list.append(ele[1])
           
    csv_file.writeCsvFile(column_name_list)
    csv_file.writeCsvFile("\n")
    
def write_db_data_to_csv_file(rs, csv_file):
    if not rs:
        return
    while True:
        data = rs.fetchone()
        if not data:
            break
        csv_file.writeCsvFile(data)    

def write_core_file(core_no):
    global DB_FILE, EXPORT_PATH
    db = db_class(DB_FILE)
    if core_no != '':
        core_file = EXPORT_PATH + "core_%s.csv" % core_no
    else:
        core_file = EXPORT_PATH + "core.csv"
    write_file = csv_class(core_file, 'w+')
    
    title_rs = db.getColumnNameFromCoreTable()
    write_db_column_to_csv_file(title_rs, write_file)
    
    data_rs = db.findCoreData(core_no)    
    write_db_data_to_csv_file(data_rs, write_file)
    write_file.closeFile()
    
    db.closeDB()


def write_cell_file(core_no, cell_no):
    global DB_FILE, EXPORT_PATH
    db = db_class(DB_FILE)
    
    if cell_no != '':
        cell_file = EXPORT_PATH + "cell_%s.csv" % cell_no
    else:
        cell_file = EXPORT_PATH + "cell.csv"
    write_file = csv_class(cell_file, 'w+')
         
    title_rs = db.getColumnNameFromCellTable()
    write_db_column_to_csv_file(title_rs, write_file)

    data_rs = db.findCellData(core_no, cell_no)
    write_db_data_to_csv_file(data_rs, write_file)
    write_file.closeFile()
    
    db.closeDB()
        

def write_user_file_title(rs, csv_file):
    column_name_list = []
    
    if not rs:
        return
    
    rs_list = rs.fetchall()
    for ele in rs_list:
        column_name_list.append(ele[1])
    
    insert_position = column_name_list.index("transmissionNbr");
    column_name_list.insert(insert_position + 1, "harqFeedBack")
    
    csv_file.writeCsvFile(column_name_list) 
    csv_file.writeCsvFile("\n")
    return column_name_list
    
def find_core_acknack(sfn, sub_sfn, rep_factor, user_id, core_db, user_seq_no):
    tmp = (sfn*5 + sub_sfn + 6 + rep_factor) % 20480
    
    acknack_sfn = tmp / 5
    acknack_sub_sfn = tmp % 5
    core_rs = core_db.getCoreDataBySfnAndSubsfn(acknack_sfn, acknack_sub_sfn)
    if not core_rs:
        print "user %s doesn't receive ack/nack" % user_id
        return
    
    core_data_list = core_rs.fetchall()
    
    if not core_data_list:
        return None
    
    core_list_len = len(core_data_list)
    if core_list_len <= 0:
        return None
    
    i = 0
    while True:
        core_data  = core_data_list[i]
        core_seq = int(core_data[11])
        
        # for sfn subframe revert 
        gap = core_seq - user_seq_no
        if gap > 0 and gap < 500:
            break
        i += 1
        if core_list_len < (i+1):
            return None   
    
    return core_data

def user_data_filter(user_title, write_data):
    t1Tsn_pos = user_title.index('t1Tsn')
    if write_data[t1Tsn_pos] == 16383:
        write_data[t1Tsn_pos] = -1
    
    averageCqi_pos = user_title.index('averageCqi')
    write_data[averageCqi_pos] =  round((write_data[averageCqi_pos] / 4.), 1)
    
    cqiVariance_pos = user_title.index('cqiVariance')
    write_data[cqiVariance_pos] =  round((write_data[cqiVariance_pos] / 8.), 1)
    
    a_pos = user_title.index('a')
    if write_data[a_pos] > 16383:
        write_data[a_pos] -= 32768
    
    rep_pos = user_title.index("akNkReptFactor")
    write_data[rep_pos] = write_data[rep_pos] + 1
    
    pdschPower_pos = user_title.index('pdschPower')
    if write_data[pdschPower_pos] > 55000:
        write_data[pdschPower_pos] = round((write_data[pdschPower_pos] - 65535 - 1)/1000., 3)
    else:
        write_data[pdschPower_pos] = round((write_data[pdschPower_pos])/1000., 3) 
    
    scchPower_pos = user_title.index('scchPower')
    write_data[scchPower_pos] = round((write_data[scchPower_pos])/1000., 3)
    
    averageCodeRate_pos = user_title.index('averageCodeRate')
    write_data[averageCodeRate_pos] = round((write_data[averageCodeRate_pos])/10., 1)
    
    scalingFactorQos_pos = user_title.index('scalingFactorQos')
    write_data[scalingFactorQos_pos] = round((write_data[scalingFactorQos_pos])/4194304., 5)
    
    activityFactor_pos = user_title.index('activityFactor')
    write_data[activityFactor_pos] = round((write_data[activityFactor_pos])/4194304., 5)
    
    bufferOccupancyInBits_pos = user_title.index('bufferOccupancyInBits')
    if write_data[bufferOccupancyInBits_pos] == 32767:
        write_data[bufferOccupancyInBits_pos] = '< 1'

def write_user_data_to_file(rs, csv_file, user_title_list):
    global DB_FILE
    if not rs:
        return
    
    core_db = db_class(DB_FILE)
    insert_pos = user_title_list.index("harqFeedBack")
    user_id_pos = user_title_list.index("userId") 
    rep_pos = user_title_list.index("akNkReptFactor")
    seq_no = user_title_list.index("sequenceNo")
    
    old_sfn = -1
    old_sub_sfn = -1
    old_rep_factor = -1
    acknack_pos = 0
    rep_acknack_pos = 0
    use_s2_ack_nack =False
    user_ack_nack_s1 = ACK_NACK_INVAILD_VALUE
    user_ack_nack_s2 = ACK_NACK_INVAILD_VALUE
    
    invalid_feedback = '0'
    
    data = rs.fetchone()
    while True:
        if not data:
            break
        
        user_id = data[user_id_pos]
        sfn = data[SFN_POSITION]
        sub_sfn = data[SUB_SFN_POSITION]
        rep_factor = data[rep_pos]
        
        write_data = list(data)
        
        if user_id == 0:
            write_data.insert(insert_pos, invalid_feedback)
            data = rs.fetchone()
            if not data:
                write_data[insert_pos] = '88'
            csv_file.writeCsvFile(write_data)
            continue
        
        if use_s2_ack_nack:
            write_data.insert(insert_pos, '%s' % user_ack_nack_s2)
            if rep_factor == 0:
                acknack_pos += 1
            else:
                rep_acknack_pos += 1
            use_s2_ack_nack = False
            
        else:
            if sfn == old_sfn and sub_sfn == old_sub_sfn:
                if old_rep_factor == rep_factor:
                    if rep_factor == 0:
                        acknack_pos += 1
                    else:
                        rep_acknack_pos += 1
            else:
                acknack_pos = 0
                rep_acknack_pos = 0
            
            if sfn != old_sfn or sub_sfn != old_sub_sfn or rep_factor != old_rep_factor:
                core_data = find_core_acknack(sfn, sub_sfn, rep_factor, user_id, core_db, int(data[seq_no]))
       
            
            if not core_data:
                write_data.insert(insert_pos, '88')
            
            else:
                if rep_factor == 0:
                    user_ack_nack_s1 = core_data[S1_ACK_START_POSITION + acknack_pos]
                    user_ack_nack_s2 = core_data[S2_ACK_START_POSITION + acknack_pos]
                else:
                    user_ack_nack_s1 = core_data[S1_ACK_REP_START_POS + rep_acknack_pos]
                    user_ack_nack_s2 = core_data[S2_ACK_REP_START_POS + rep_acknack_pos]
                
                if user_ack_nack_s1 != ACK_NACK_INVAILD_VALUE and user_ack_nack_s2 != ACK_NACK_INVAILD_VALUE:
                    write_data.insert(insert_pos, '%s' % user_ack_nack_s1)
                    use_s2_ack_nack = True
                elif user_ack_nack_s1 != ACK_NACK_INVAILD_VALUE:
                    write_data.insert(insert_pos, '%s' % user_ack_nack_s1)
                elif user_ack_nack_s2 != ACK_NACK_INVAILD_VALUE:
                    write_data.insert(insert_pos, '%s' % user_ack_nack_s2)
                else:
                    write_data.insert(insert_pos, invalid_feedback)
        
        old_sfn = sfn
        old_sub_sfn = sub_sfn
        old_rep_factor = rep_factor
        
        user_data_filter(user_title_list, write_data)
        
        data = rs.fetchone()
        if not data:
            write_data[insert_pos] = '88'
        
        csv_file.writeCsvFile(write_data) 
    
    core_db.closeDB()

def write_user_file(core_no, cell_no, user_no):
    global DB_FILE, EXPORT_PATH
    db = db_class(DB_FILE)
    if user_no != '':
        user_file = EXPORT_PATH  + "user_%s.csv" % user_no
    else:
        user_file = EXPORT_PATH  + "user.csv"
    write_file = csv_class(user_file, 'w+')
    
    title_rs = db.getColumnNameFromUserTable()
    user_title_list = write_user_file_title(title_rs, write_file)
    
    data_rs = db.findUserData(core_no, cell_no, user_no)
    write_user_data_to_file(data_rs, write_file, user_title_list)
    
    write_file.closeFile()
    
    db.closeDB()

def click_export_btn(core_no, cell_no, user_no):
    global BASE_PATH, DB_PATH, DB_FILE
    global is_support_cadc

    
    if is_support_cadc:
        import sys
        sys.path.append(os.path.join(BASE_PATH, r'CADC_Feature'))
        from cadcFeature import cadc_merge        
        import xlrd
        cadc_merge(DB_FILE)
    
    write_core_file(core_no)
    write_cell_file(core_no, cell_no)
    write_user_file(core_no, cell_no, user_no)
 
def clickCoreItem(core_no, showCellList, showUserList):
    global DB_FILE
    db = db_class(DB_FILE)
    if not core_no:
        cell_rs = db.findCell(CELL_TABLE_NAME)
        cell_list = db.translateCellRsToList(cell_rs)
        user_rs = db.findUser(USER_TABLE_NAME)
        user_list = db.translateUserRsToList(user_rs)
    else:
        cell_rs = db.findCellByCore(CELL_TABLE_NAME, core_no)
        cell_list = db.translateCellRsToList(cell_rs)
        user_rs = db.findUserByCore(USER_TABLE_NAME, core_no)
        user_list = db.translateUserRsToList(user_rs)
    
    cell_list = [str(item) for item in cell_list]
    showCellList(cell_list) 
     
    user_list = [str(item) for item in user_list]
    showUserList(user_list)
    db.closeDB()

def clickCellItem(core_no, cell_no, showUserList): 
    global DB_FILE
    if not cell_no:
        return
    db = db_class(DB_FILE)

    user_rs = db.findUserByCoreAndCell(USER_TABLE_NAME, core_no, cell_no)
    user_list = db.translateUserRsToList(user_rs)
    user_list = [str(item) for item in user_list]
    showUserList(user_list)
    db.closeDB()

def click_check_tracefile():
    global DB_FILE
    db = db_class(DB_FILE)
    
    sequence_no = set()
    
    rs = db.getSequenceNoFromCore()
    if not rs:
        return False
    
    sequence_list = rs.fetchall()
    for ele in sequence_list:
        sequence_no.add(ele[0])
        
    min_sequence = sequence_list[0][0]
    max_sequence = sequence_list[-1][0]
    
    rs = db.getSequenceNoFromCell()
    if not rs:
        return False
     
    sequence_list = rs.fetchall()
    for ele in sequence_list:
        sequence_no.add(ele[0])
        
    if sequence_list[0][0] < min_sequence:
        min_sequence = sequence_list[0][0]
    if sequence_list[-1][0] > max_sequence:
        max_sequence = sequence_list[-1][0]
     
    rs = db.getSequenceNoFromUser()
    if not rs:
        return False
     
    sequence_list = rs.fetchall()
    for ele in sequence_list:
        sequence_no.add(ele[0])
        
    if sequence_list[0][0] < min_sequence:
        min_sequence = sequence_list[0][0]
    if sequence_list[-1][0] > max_sequence:
        max_sequence = sequence_list[-1][0]

    expect_len = max_sequence - min_sequence + 1
    if expect_len == len(sequence_no):
        return True

    return False

def setup_dir(dir_name):
    if not os.path.exists(dir_name):
        os.mkdir(dir_name)

def setup_dirs(): 
    global DB_PATH, BACKUP_PATH, EXPORT_PATH, PIC_PATH
    setup_dir(DB_PATH)
    setup_dir(BACKUP_PATH)
    setup_dir(PIC_PATH)
    setup_dir(EXPORT_PATH)      

def cleanDir(dir_name):
    if not os.path.exists(dir_name):
        return
    shutil.rmtree(dir_name)

def cleanDirs():
    global DB_PATH, BACKUP_PATH, EXPORT_PATH, PIC_PATH
    cleanDir(DB_PATH)
    cleanDir(BACKUP_PATH)
    cleanDir(PIC_PATH)
    cleanDir(EXPORT_PATH)

def cleanupResource():
    global DB_FILE
    if not os.path.exists(DB_FILE):
        return
    db_obj = db_class(DB_FILE)
    db_obj.dropAllTable()
