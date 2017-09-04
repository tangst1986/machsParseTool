'''
@author: m1tang
'''

import os
from db_class import *  # @UnusedWildImport
from draw_class import draw_class
from config import *

BASE_PATH = os.path.abspath(os.path.join(os.getcwd(), ".."))
DB_PATH = BASE_PATH + '\\DATA\\'
DB_FILE = DB_PATH  + 'ttiTrace.db'

def calculateUserThroughput(rs):
    db_data = rs.fetchall()

    user_dict = {}
    for ele in db_data:
        if user_dict.has_key(ele[0]):
            user_dict[ele[0]] += ele[1] - ele[2]  #user throughput: finalTbs - paddingBits
        else:
            user_dict[ele[0]] = ele[1] - ele[2]

    return user_dict

def drawUserThoughput(user_dict):
    draw_obj = draw_class("user_throughput")

    x_data_list = [key for key in user_dict]
    y_data_list = [user_dict[key] for key in user_dict]
    
    draw_obj.drawColumn(x_data_list, y_data_list)
        

def get_time(table_type, search_no):
    global DB_FILE
    
    db = db_class(DB_FILE)
    if table_type == CORE_TABLE_NAME:
        rs = db.findUserDataByCore(search_no)

    elif table_type == CELL_TABLE_NAME:
        rs = db.findUserDataByCell(search_no)
    else:
        rs = None
    if not rs:
        return None
    data_list = rs.fetchall()
    first_record = data_list[0]
    last_record = data_list[len(data_list) - 1]
    
    start_time = time_gap(first_record)
    end_time = time_gap(last_record)
    ret_time = end_time - start_time
    if ret_time == 0:
        ret_time = get_time_from_sfn(first_record, last_record)
    return ret_time

def draw_cell(data_list):
    x_data_list = []
    y_data_list = []
    
    cell_dict = {}
    time_dict = {}
    for ele in data_list:
        if cell_dict.has_key(ele[4]):
            cell_dict[ele[4]] += ele[1] - ele[2]
        else:
            cell_dict[ele[4]] = ele[1] - ele[2]
            time_dict[ele[4]] = get_cell_time(ele[4])
    
    for key in cell_dict:
        cell_dict[key] = (cell_dict[key]/time_dict[key]) / (1024*1024) #change to MB
        cell_dict[key] = round(cell_dict[key], 2)
        x_data_list.append(key)
        y_data_list.append(cell_dict[key])
    
    draw_obj = draw_class("cell_throughput", "Mbits/s")
    draw_obj.drawColumn(x_data_list, y_data_list)
    return True

def draw_cell_user(data_list, cell_no):
    x_data_list = []
    y_data_list = []
    
    time = get_cell_time(cell_no)

    user_dict = {}  #use userID as the key
    
    for ele in data_list:
        if user_dict.has_key(ele[0]):
            user_dict[ele[0]] += ele[1] - ele[2]
        else:
            user_dict[ele[0]] = ele[1] - ele[2]
    
    for key in user_dict:
        user_dict[key] = ((user_dict[key]/time) / 1024) #change to KB
        user_dict[key] = round(user_dict[key], 2)
        x_data_list.append(key)
        y_data_list.append(user_dict[key])
    
    draw_obj = draw_class("cell_%s_user_throughput" % cell_no, "Kbits/s")
    draw_obj.drawColumn(x_data_list, y_data_list)
    return True
 
def draw_no_cell_user(data_list, user_no):
    x_data_list = []
    y_data_list = []
    
    user_dict = {}  #use the cellId as the key
    time_dict = {}
    for ele in data_list:
        if user_dict.has_key(ele[4]):
            user_dict[ele[4]] += ele[1] - ele[2]
        else:
            user_dict[ele[4]] = ele[1] - ele[2]
            time_dict[ele[4]] = get_cell_time(ele[4])
    
    for key in user_dict:
        user_dict[key] = (user_dict[key]/time_dict[key]) / 1024#change to KB
        user_dict[key] = round(user_dict[key], 2)
        x_data_list.append(key)
        y_data_list.append(user_dict[key])
    
    draw_obj = draw_class("user_%s_throughput" % user_no, "Kbits/s")
    draw_obj.drawColumn(x_data_list, y_data_list)
    return True

def time_gap(rs_data):
    return rs_data[HOUR_POSITION] * 3600 + rs_data[MINUTE_POSITION] * 60 + rs_data[SECOND_POSITION] + rs_data[MILLISECOND_POSITION] / 1000.

def get_core_time(core_no):
    return get_time(CORE_TABLE_NAME, core_no)

def get_cell_time(cell_no):
    return get_time(CELL_TABLE_NAME, cell_no)

def get_time_from_sfn(first_record, last_record):
    first_sfn = first_record[SFN_POSITION]
    first_sub_sfn = first_record[SUB_SFN_POSITION]
    
    last_sfn = last_record[SFN_POSITION]
    last_sub_sfn = last_record[SUB_SFN_POSITION]
    
    if first_sfn > last_sfn:
        num_sfn = 20479 - first_sfn + last_sfn - 1
        ret_time = num_sfn * 10 + (5 - first_sub_sfn + last_sub_sfn + 1) * 2
    elif first_sfn == last_sfn:
        ret_time = (5 - first_sub_sfn + last_sub_sfn + 1) * 2
    else:
        num_sfn = last_sfn - first_sfn - 1
        ret_time = num_sfn * 10 + (5 - first_sub_sfn + last_sub_sfn + 1) * 2
    return  ret_time / 1000.


def click_cell_throughput_btn(core_no, cell_no, user_no):
    global DB_FILE

    if not core_no:
        return False
    
    db_obj = db_class(DB_FILE)
    rs = db_obj.getUserThroughputData(core_no, cell_no, user_no)
    if not rs:
        return False
    
    data_list = rs.fetchall()
    draw_cell(data_list)
    
    db_obj.closeDB()
    return True

def click_user_throughput_btn(core_no, cell_no, user_no):
    global DB_FILE
    if not core_no and not user_no:
        return False
    
    db_obj = db_class(DB_FILE)
    rs = db_obj.getUserThroughputData(core_no, cell_no, user_no)
    if not rs:
        return False
    
    data_list = rs.fetchall()
    if cell_no:
        draw_cell_user(data_list, cell_no)
    else:
        draw_no_cell_user(data_list, user_no)
    
    db_obj.closeDB()
    return True