'''
@author: m1tang
'''

import sys
import os
import time
import logging
import subprocess
import shutil
from business import *


TMP_DATA_DIR = r'tmp_data'

SRC_PATH = os.path.join(os.getcwd(), TMP_DATA_DIR) + '\\'

global file_name, core_no, cell_no, user_no, GTA_PATH, export_path, sack_path, config_path
sack_path = None
config_path = None

def configLogger():

    gLogConf = {
        'filename': 'debug.txt',
        'filemode': 'w',
        'level':    logging.INFO,
        'format':   '%(asctime)s %(levelname)s %(module)s:%(lineno)s : %(message)s',
        'stream':   sys.stdout,
    }
    
    logging.basicConfig(**gLogConf)

def parse_args(arg_list):
    global file_name, core_no, cell_no, user_no, GTA_PATH, export_path, sack_path, config_path
    
    file_exist = False
    for ele in arg_list:
        if ele.startswith('file='):
            file_name = ele[5:]
            file_exist = True
        elif ele.startswith('core='):
            core_no = ele[5:]
        elif ele.startswith('cell='):
            cell_no = ele[5:]
        elif ele.startswith('user='):
            user_no = ele[5:]
        elif ele.startswith('export='):
            export_path = ele[7:]

        else:
            print "invalid parameter '%s'" % ele
            return False
        
    return file_exist


def main_run():
    global file_name, core_no, cell_no, user_no, GTA_PATH, export_path, sack_path, config_path
    core_no = ''
    cell_no = ''
    user_no = ''
    
    file_list = []
    file_list.append(file_name)
    
    setup_path(False)
    
    cleanDirs()
    
    setup_dirs()
        
    startParseBin(file_list, None, None, None, None, None, None, None)
    click_export_btn(core_no, cell_no, user_no)

def cmd_parse():
    
    if len(sys.argv) < 2:
        return
    
    else:
        is_continue = parse_args(sys.argv[1:])
        if not is_continue:
            return
    dirname, filename = os.path.split(os.path.abspath(sys.argv[0]))
    os.chdir(dirname)
    print os.curdir, os.getcwd()
    
    start_time = time.clock()
    print "start parse & export..."
    configLogger()
    main_run()
    
    msg = "task complete, cost %.3f seconds" %(time.clock() - start_time)
    logging.info(msg)
    print msg
    
if __name__=='__main__':
    cmd_parse()
    
    
        