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
CORE_FILE_NAME = r'TtiTrace_MacHsTtiTrace_CoreTrace.csv'
CELL_FILE_NAME = r'TtiTrace_MacHsTtiTrace_LocalCellTrace.csv'
USER_FILE_NAME = r'TtiTrace_MacHsTtiTrace_LocalUserTrace.csv'

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
        elif ele.startswith('GTA='):
            GTA_PATH = ele[4:]
        elif ele.startswith('export='):
            export_path = ele[7:]
        elif ele.startswith('sack='):
            sack_path = ele[5:]
        elif ele.startswith('config='):
            config_path = ele[7:]
        else:
            print "invalid parameter '%s'" % ele
            return False
        
    if not file_exist:
        display_helpinfo()
        print 'please input the right trace_file'
        
    return file_exist


def display_helpinfo():
    help_str = '''parse TXT trace file: cmdParse.exe file=trace_file [core=core_no cell=cell_no user=user_no export=export_path]
    parse BIN trace file: cmdParse.exe file=trace_file GTA=GTA_path export=export_path sack=sack_path config=config_path'''
    
    print '*'*80
    print '    %s' % help_str
    print '*'*80

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

def main_run():
    global file_name, core_no, cell_no, user_no, GTA_PATH, export_path, sack_path, config_path
    core_no = ''
    cell_no =''
    user_no = ''
    
    file_list = []
    file_list.append(file_name)
    
    setup_path(True)
    
    if not os.path.exists(TMP_DATA_DIR):
        os.mkdir(TMP_DATA_DIR)
        
    if os.path.exists(TMP_DATA_DIR):
        for ele in os.listdir(TMP_DATA_DIR):
            os.remove(TMP_DATA_DIR + '\\' + ele)

    if file_name[-4:] == '.bin':
        if not GTA_PATH or not export_path:
            print 'err: GTA parse need GTA_path and export_path'
            return
        
        if not sack_path and not config_path:
            cmd =  "%s -p -f %s -o %s --noassist --noupdate" % (GTA_PATH, file_name, export_path)
        elif not sack_path:
            cmd =  "%s -p -f %s -c %s -o %s --noassist --noupdate" % (GTA_PATH, file_name, config_path, export_path)
        elif not config_path:
            cmd =  "%s -p -f %s -d %s -o %s --noassist --noupdate" % (GTA_PATH, file_name, sack_path, export_path)
        else:
            cmd =  "%s -p -f %s -d %s -c %s -o %s --noassist --noupdate" % (GTA_PATH, file_name, sack_path, config_path, export_path)
        try:
            out_put = subprocess.check_output(cmd)
            print out_put
        except subprocess.CalledProcessError as e:
            print e.output
            logging.error(e.output)
            return
        
        base_name = os.path.basename(file_name)[:-4]
        src_file_path = os.path.join(export_path, base_name)
        sleep_count = 0
        while True:
            if not os.path.exists(src_file_path):
                logging.debug("check path %s" % src_file_path)
                time.sleep(10)
                sleep_count += 1
                if sleep_count == 12:
                    logging.error("%s is not exists" % src_file_path)
                    return
                continue
            break
        for ele in os.listdir(src_file_path):
            src_file = os.path.join(src_file_path, ele)
            
            if "Core" in ele:
                target_file = SRC_PATH + base_name + "_core.csv"
            elif "Cell" in ele:
                target_file = SRC_PATH + base_name + "_cell.csv"
            elif "User" in ele:
                target_file = SRC_PATH + base_name + "_user.csv"
            else:
                continue
            read_write(src_file, target_file)
        
        file_path =  SRC_PATH + base_name + "_core.csv"
        core_file = open(file_path, 'r')
        core_file.readline()
        core_file.readline()
        core_data = core_file.readline().split(',')
        core_no = core_data[-1][:-1]
        core_file.close()
        
        
        createTableFromFileList(int(core_no))
        core_no = ''
        click_export_btn(core_no, cell_no, user_no)
        
        for ele in os.listdir(src_file_path):
            shutil.move(os.path.join(src_file_path, ele), TMP_DATA_DIR)
         
        for ele in os.listdir(SRC_PATH):
            if ele == "user.csv":
                shutil.move(os.path.join(SRC_PATH, ele), os.path.join(src_file_path, USER_FILE_NAME))
            elif ele == "core.csv":
                shutil.move(os.path.join(SRC_PATH, ele), os.path.join(src_file_path, CORE_FILE_NAME))
            elif ele == "cell.csv":
                shutil.move(os.path.join(SRC_PATH, ele), os.path.join(src_file_path, CELL_FILE_NAME))
            else:
                pass
        
#         
#     elif file_name[-4:] == '.txt':
#         cleanDirs()
#         cleanupResource()
#         startParseBin(file_list, '', '', '', '')
#         click_export_btn(core_no, cell_no, user_no)
#         if export_path:
#             cleanDir(export_path)
#             for ele in os.listdir(SRC_PATH):
#                 shutil.move(SRC_PATH + ele, export_path)
    else:
        pass  
    

def cmd_parse():
    
    if len(sys.argv) < 2:
        display_helpinfo()
        return
    
    else:
        is_continue = parse_args(sys.argv[1:])
        if not is_continue:
            return
    
    start_time = time.clock()
    print "start parse & export..."
    configLogger()
    main_run()
    
    msg = "task complete, cost %.3f seconds" %(time.clock() - start_time)
    logging.info(msg)
    print msg
    
if __name__=='__main__':
    cmd_parse()
    
    
        