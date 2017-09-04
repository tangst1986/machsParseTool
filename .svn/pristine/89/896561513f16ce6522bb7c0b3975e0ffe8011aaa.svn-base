'''
@author: m1tang
'''

import xlrd
import sys
import os

LOAD_PATH = os.path.join(os.getcwd(), '..', 'API_Class')
sys.path.append(LOAD_PATH)
from db_class import *


CADC_FILE_NAME = os.path.join(os.getcwd(), '..', r'CADC_Map', r'ttitrace_for_cadc_user_2.2.xlsx')
DATA_START_INDEX = 2
USER_FILED_INDEX = 0
USE_INDEX = 1

global db_file, user_title_list

def get_user_title():
    global db_file, user_title_list  
    user_title_list = []
    
    db = db_class(db_file)
    user_title_rs = db.getColumnNameFromUserTable()
    if not user_title_rs:
        print 'err: get user column failed'
        return None
    
    rs_list = user_title_rs.fetchall()
    for ele in rs_list:
        user_title_list.append(ele[1])
    
    db.closeDB()
    
def make_cadc_map():
    global user_title_list
    user_field2_cadc_map = []
    cadc_excel_file = xlrd.open_workbook(CADC_FILE_NAME)
    sheet = cadc_excel_file.sheet_by_name(u'User')
    nrows = sheet.nrows
    get_user_title()
    if not user_title_list:
        return None
    for i in range(DATA_START_INDEX, nrows):
        read_data = sheet.row_values(i)
        if 'Secondary Mac-hs' in read_data[1]:
            user_field2_cadc_map.append(user_title_list.index(read_data[0].strip()))
        
    return user_field2_cadc_map
   
def cadc_merge(db_path):
    global db_file, user_title_list
    db_file = db_path
    user_filed2_cadc_map = make_cadc_map()
    if not user_filed2_cadc_map:
        print "err: CADC merge failed"
        return
    
    trace_type_index = user_title_list.index('traceType')
    sfn_index = user_title_list.index('sfn')
    sub_sfn_index = user_title_list.index('subFrameNbr')
    userId_index = user_title_list.index('userId')
    cellId_index = user_title_list.index('cellId')
     
    db = db_class(db_file)
    create_user_index_sql_str =  r'create index cadc_user_index on %s(%s, %s, %s, %s, %s)' %\
                                 (USER_TABLE_NAME, 'traceType', 'sfn', 'subFrameNbr', 'userId', 'cellId')
    try:
        db.excuteSelfSql(create_user_index_sql_str)
    except Exception as e:
        print e
        
    local_user_type = 4
    remote_user_type = 5
    sql_str = r'select * from %s where traceType=%d' % (USER_TABLE_NAME, remote_user_type)
    remote_user_rs = db.excuteSelfSql(sql_str)
    if not remote_user_rs:
        db.closeDB()
        return 
    remote_user_list = remote_user_rs.fetchall()
     
    for ele in remote_user_list:
        update_sql_str = r'update %s set ' % USER_TABLE_NAME
        for map_ele in user_filed2_cadc_map:
            update_sql_str += '%s=%s,' % (user_title_list[map_ele], ele[map_ele])
        update_sql_str = update_sql_str[:-1]
        update_sql_str += ' '
        update_sql_str += 'where traceType=%d and sfn=%d and subFrameNbr=%d and userId=%d and cellId=%d' %\
                          (local_user_type, ele[sfn_index], ele[sub_sfn_index], ele[userId_index], ele[cellId_index])
        try:
            db.excuteSelfSql(update_sql_str)
        except Exception as e:
            print e

        del_sql_str = 'delete from %s where traceType=%d and sfn=%d and subFrameNbr=%d and userId=%d and cellId=%d' %\
                      (USER_TABLE_NAME, ele[trace_type_index], ele[sfn_index], ele[sub_sfn_index], ele[userId_index], ele[cellId_index]) 
        try:         
            db.excuteSelfSql(del_sql_str)
        except Exception as e:
            print e
    db.commitDB()
    db.closeDB()
    
    
if __name__ == '__main__':
    db_file = os.path.join(os.getcwd(), '..', 'DATA', 'ttiTrace.db')
    cadc_merge(db_file)
