'''
@author: m1tang
'''

import os
import xlrd
import sys
import logging
import shutil
import sqlite3

base_path =  os.getcwd()
tmp_file = None

EXCEL_MAX_LINE = 65533


def configLogger():
    global EXCEL_FILE_PATH
    log_path = os.path.join(EXCEL_FILE_PATH, 'log.txt')

    gLogConf = {
        'filename': log_path,
        'filemode': 'w',
        'level':    logging.INFO,
        'format':   '%(asctime)s %(levelname)s %(module)s:%(lineno)s : %(message)s',
        'stream':   sys.stdout,
    }
    
    logging.basicConfig(**gLogConf)

def get_excel2csv_column_map():
    global user_col_map_value, excel_col_value
    
    pos_csv = []
    for ele in excel_col_value:
        if not ele:
            continue
  
        if ele not in user_col_map_value:
            pos_csv.append('-')
        else:
            pos_csv.append(user_col_map_value.index(ele))
    
     
    return pos_csv[1:]

def open_db():
    global EXCEL_FILE_PATH
    base_path = os.path.join(EXCEL_FILE_PATH, '..')
    db_path = os.path.join(EXCEL_FILE_PATH, 'ttiTrace.db')
    if not os.path.exists(db_path):
        db_path = os.path.join(base_path, 'cmd', 'tmp_data', 'ttiTrace.db')
        if not os.path.exists(db_path):
            db_path = os.path.join(base_path, 'DATA', 'ttiTrace.db')
            if not os.path.exists(db_path):
                return None
    db = sqlite3.connect(db_path)
    return db.cursor()

def create_file_data():
    global db_cursor, cell_data_dict
    cell_data_dict = {}
    
    CELL_TABLE_NAME = r'cell_info'
    sql_str = 'select cellId, sfn, subFrameNbr, sequenceNo, * from %s' % CELL_TABLE_NAME
    rs = db_cursor.execute(sql_str)
    if not rs:
        return None

    while True:
        data = rs.fetchone()
        if not data:
            break
        
        if data[0] == 0:
            continue
        
        if not cell_data_dict.has_key(int(data[0])):
            cell_data_dict[int(data[0])] = {}
        if not cell_data_dict[int(data[0])].has_key(int(data[1])):
            cell_data_dict[int(data[0])][int(data[1])] = {}
        if not cell_data_dict[int(data[0])][int(data[1])].has_key(int(data[2])):
            cell_data_dict[int(data[0])][int(data[1])][int(data[2])] = {}
        if not cell_data_dict[int(data[0])][int(data[1])][int(data[2])].has_key(int(data[3])):
            cell_data_dict[int(data[0])][int(data[1])][int(data[2])][int(data[3])] = {}
        
        cell_data_dict[data[0]][data[1]][data[2]][data[3]]= data[4:]
    
def find_cell_data(sfn, sub_sfn, cellId, user_sequence):
#     global db_cursor
#     
#     if not db_cursor:
#         return None
#     
#     CELL_TABLE_NAME = r'cell_info'
#     sql_str = 'select * from %s where sfn = %d and subFrameNbr = %d and cellId=%d' % (CELL_TABLE_NAME, int(sfn), int(sub_sfn), int(cellId))
#     rs = db_cursor.execute(sql_str)
#     if not rs:
#         return None
#     return rs.fetchone()
    global cell_data_dict
    cellId = int(cellId)
    sfn = int(sfn)
    sub_sfn = int(sub_sfn)
    if not cell_data_dict.has_key(cellId):
        return None
    if not cell_data_dict[cellId].has_key(sfn):
        return None
    if not cell_data_dict[cellId][sfn].has_key(sub_sfn):
        return None
    
    # for sfn subframe revert 
    sequence_no_list = cell_data_dict[cellId][sfn][sub_sfn].keys()
    for i in range(0, len(sequence_no_list)):
        gap = int(user_sequence) - sequence_no_list[i]
        if gap > 0 and gap < 500:
            return cell_data_dict[cellId][sfn][sub_sfn][sequence_no_list[i]]
    return None

def write_cell_data(user_data):
    global db_cursor, cell_data
    
    if not db_cursor:
        return

    if not cell_data:
        return

    user_data[excel_col_value.index("Transmitted carrier power (mW)")] = cell_data[12+cell_col_map_value.index("Transmitted carrier power (mW)")]
    user_data[excel_col_value.index("Available PDSCH power (dBm)")] = round(cell_data[12+cell_col_map_value.index("Available PDSCH power (dBm)")] / 1000., 3)
    user_data[excel_col_value.index("Nbr Of Banned Users")] = cell_data[12+cell_col_map_value.index("Nbr Of Banned Users")]
    user_data[excel_col_value.index("No of users")] = cell_data[12+cell_col_map_value.index("No of users")]
    user_data[excel_col_value.index("Phase Offset")] = cell_data[12+cell_col_map_value.index("Phase Offset")]
    user_data[excel_col_value.index("K")] = cell_data[12+cell_col_map_value.index("K")]
    
#     user_data[58] = cell_data[19]
#     user_data[64] = cell_data[27]
#     user_data[63] = cell_data[24]
#     user_data[62] = cell_data[21]
    
def wirte_data_to_tmpfile(csv_data, pos_csv):
    
    write_data = []
    
    Timestamp = '%s:%s:%s:%s' % (csv_data[2], csv_data[3], csv_data[4], csv_data[5])
    write_data.append(Timestamp)
    
    for pos in pos_csv:
        if pos == '-':
            write_data.append('%s' % pos)
        else:
            write_data.append('%s' % (csv_data[pos]))
    
    return write_data

def export_tmp_file(csv_data, record_count, pos_csv):
    
    global tmp_file, EXCEL_FILE_PATH
    
    tmp_file_index = record_count / EXCEL_MAX_LINE + 1
    
    tmp_file_path = os.path.join(EXCEL_FILE_PATH, "TempFile_%s.txt" % tmp_file_index)
    if not os.path.exists(tmp_file_path):
        if tmp_file:
            tmp_file.close()
        tmp_file = open(tmp_file_path, 'w+')
    
    if not tmp_file:
        tmp_file = open(tmp_file_path, 'w+')
    
    user_data = wirte_data_to_tmpfile(csv_data, pos_csv)
    write_cell_data(user_data)
    
    tmp_data = ','.join(str(ele) for ele in user_data) + '\n'
    
    tmp_file.write(tmp_data)

def write_tmpfile(file_path):
    global db_cursor, user_col_map_value, excel_col_value, cell_col_map_value, EXCEL_FILE_PATH, cell_data
    
    db_cursor = open_db()
    create_file_data()
    EXCEL2CSV_PATH = os.path.join(EXCEL_FILE_PATH, 'bin', 'csv2excel.xlsx')
    xls_file = xlrd.open_workbook(EXCEL2CSV_PATH)
    sheet = xls_file.sheet_by_index(0)
    
    user_col_map_value = sheet.col_values(1)
    del user_col_map_value[0]
    
    excel_col_value = sheet.col_values(3)
    
    cell_col_map_value = sheet.col_values(6)
    del cell_col_map_value[0]
    
    pos_csv = get_excel2csv_column_map()
    user_file = open(file_path, "r")

    user_file.readline()  # skip the title
    record_count = 0
    
    old_sfn = -1
    old_sub_sfn = -1
    old_cellId = -1
    
    while True:
        user_data = user_file.readline()
        if not user_data:
            break

        record_count += 1
        
        csv_data = user_data.split(',')
        
        sfn = csv_data[user_col_map_value.index('SFN')]
        sub_sfn = csv_data[user_col_map_value.index('Subframe No')]
        cellId = csv_data[user_col_map_value.index('Cell ID')]
        user_sequence = csv_data[user_col_map_value.index('SEQ')]
        csv_data[user_col_map_value.index('T-put\n(bits/10ms)')] = int(csv_data[user_col_map_value.index('T-put\n(bits/10ms)')]) * 5

#         sfn = csv_data[7]
#         sub_sfn = csv_data[8]
#         cellId = csv_data[20]
        if sfn != old_sfn or sub_sfn != old_sub_sfn  or cellId != old_cellId:
            cell_data = find_cell_data(sfn, sub_sfn, cellId, user_sequence)
        
        export_tmp_file(csv_data, record_count, pos_csv)
        
        old_sfn = sfn
        old_sub_sfn = sub_sfn
        old_cellId = cellId
 
def remove_pre_tmp_file(): 
    if not os.path.exists(EXCEL_FILE_PATH):
        return
    for ele in os.listdir(EXCEL_FILE_PATH):
        if "TempFile_" in ele:
            os.remove(os.path.join(EXCEL_FILE_PATH, ele))
    
if __name__ == '__main__':
    global EXCEL_FILE_PATH, cell_data_dict

    user_file_path = sys.argv[1]
    EXCEL_FILE_PATH = sys.argv[2]
    #user_file_path = r'D:\software\workspace\CADC_tool_base\Export\user.csv'
    #EXCEL_FILE_PATH = r'D:\software\workspace\CADC_tool_base\r4_excel_trace_tool'
    remove_pre_tmp_file()
#     configLogger()
    logging.info(user_file_path)
    write_tmpfile(user_file_path)







