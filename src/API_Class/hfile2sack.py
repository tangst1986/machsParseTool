'''
@author: m1tang
'''

import os
import sys
import re
import ctypes as ct
from config import S1_ACK_START_POSITION, S2_ACK_START_POSITION, S1_ACK_REP_START_POS, S2_ACK_REP_START_POS
import subprocess
import shutil

dirname, filename = os.path.split(os.path.abspath(sys.argv[0]))
os.chdir(dirname)
base_dir = os.path.abspath(os.path.join(os.getcwd(), ".."))

hfile_name = os.path.join(base_dir, 'sack', r'SMacHsTtiTraceBitField.h')
sack_name = os.path.join(base_dir, 'sack',  r'sack.txt')
pyfile_name = r'parseTtiTraceWithUTest.py'

user_ack_count = 0

def getBranchVersion(trace_file):
    if not os.path.exists(trace_file):
        return None, None
    r_file = open(trace_file, 'r')
    line = r_file.readline()
    if not line:
        return None, None

    branch_version_pattern = r'.*Span:[\d:/\.]*\s*(.*)@Revision:\W*(\d*).*'
    m = re.match(branch_version_pattern, line)
    if not m:
        r4_pattern = r'.*SWVersion:(.*)@Revision:\W*(\d*).*'
        m = m = re.match(r4_pattern, line)
        if not m:
            return None, None
    branch =  m.group(1)
    version = m.group(2)
    return branch.strip(), version.strip()

def checkHeadFileExist(branch, version):
    head_file_name = branch.replace(r'/', r'_') + '_' + version
    sack_dir = os.path.join(base_dir, r'sack')
    
    if head_file_name in os.listdir(sack_dir):
        return True, head_file_name
    
    return False, head_file_name


def getSvnHeadFile(branch, version):
    is_exist_head_file, head_file_name = checkHeadFileExist(branch, version)
    if is_exist_head_file:
        source_file = os.path.join(base_dir, r'sack', head_file_name)
        if os.path.exists(hfile_name):
            os.remove(hfile_name)
        shutil.copy(source_file, hfile_name)
        return True
    
    branch_map_file_path = os.path.join(base_dir, r'sack', r'branchSvnMap.txt')
    if not os.path.exists(branch_map_file_path):
        return False
    
    svn_path = None
    head_file = None
    is_read = False
    map_file = open(branch_map_file_path, 'r')
    while True:
        line = map_file.readline()
        if not line:
            break
        
        if is_read:
            head_file = line.split(r'=>')[1].strip()
            break
        
        if branch in line:
            svn_path = line.split(r'=>')[1].strip()
            is_read = True

    if not svn_path or not head_file:
        return False
    
    svn_head_file_path = svn_path + '/' + head_file
    head_save_path = os.path.join(base_dir, 'sack')
    try:
        cmd = r'svn export --force -r %s %s %s' % (version, svn_head_file_path, head_save_path)
        out_put = subprocess.check_output(cmd)
        print out_put
    except subprocess.CalledProcessError as e:
        print e.output
        return False
    print 'SMacHsTtiTraceBitField.h has been updated to branch %s, version %s!' % (branch, version) 
    shutil.copy(hfile_name, os.path.join(base_dir, r'sack', head_file_name))
    return True

def replace_sack():
    r_sack_file = open(sack_name, 'r')
    r_py_file = open(pyfile_name, 'r')
    core_rep_txt = find_txt(r_sack_file, "MACHS_TTI_TRACE_BIT_FIELD_FOR_CORE =")
    core_old_txt  = find_txt(r_py_file, "MACHS_TTI_TRACE_BIT_FIELD_FOR_CORE =")
    
    cell_rep_txt = find_txt(r_sack_file, "MACHS_TTI_TRACE_BIT_FIELD_FOR_CELL_INFO =")
    cell_old_txt  = find_txt(r_py_file, "MACHS_TTI_TRACE_BIT_FIELD_FOR_CELL_INFO =")
    
    user_rep_txt = find_txt(r_sack_file, "MACHS_TTI_TRACE_BIT_FIELD_FOR_USER =")
    user_old_txt  = find_txt(r_py_file, "MACHS_TTI_TRACE_BIT_FIELD_FOR_USER =")
    
    r_py_file.seek(0)
    w_txt = r_py_file.read()
    r_sack_file.close()
    r_py_file.close()
    
    w_py_file = open(pyfile_name, 'w')
    txt_1 = w_txt.replace(core_old_txt, core_rep_txt)
    txt_2 = txt_1.replace(cell_old_txt, cell_rep_txt)
    txt_3 = txt_2.replace(user_old_txt, user_rep_txt)
    w_py_file.write(txt_3)
    w_py_file.flush()
    w_py_file.close()

def find_txt(txt_file, pre_string):
    r_file = txt_file
    r_file.seek(0)
    old_txt = None
    while True:
        r_line = r_file.readline()
        if not r_line:
            break
        if pre_string in r_line:
            old_txt = r_line
            while True:
                r_line = r_file.readline()
                if not r_line:
                    break
                old_txt += r_line
                if ')' in r_line and '(' not in r_line:
                    break
                if '))' in r_line:
                    break
    
    return old_txt
    

def trans_hfile_to_sack():
    r_file = open(hfile_name, 'r')
    w_file = open(sack_name, 'w')

    while True:
        line = r_file.readline()
        if not line:
            break
        
        if re.match(r'^struct SMacHsTtiTraceBitFieldForCellInfo', line):
            output = r'MACHS_TTI_TRACE_BIT_FIELD_FOR_CELL_INFO = ('
        elif re.match(r'^struct SMacHsTtiTraceBitFieldForCore', line):
            output = r'MACHS_TTI_TRACE_BIT_FIELD_FOR_CORE = ('
        elif re.match(r'^struct SMacHsTtiTraceBitFieldForLocalUser', line):
            output = r'MACHS_TTI_TRACE_BIT_FIELD_FOR_USER = ('
        else:
            continue
        output += '\n'
        blank_len = len(output)
        pre_blank = ' ' * blank_len
        continue_flag = False
        while True:
            line = r_file.readline()
            line = line.strip().split(';')
            line_1 = ''
            if len(line) > 1:
                line_1 = line[1]
            line = line[0]
            if "{" in line:
                continue
            elif '/*' in line:
                continue_flag = True
                continue
            elif "}" in line:
                if '*/' in line_1:
                    continue_flag = False
                    continue
                else:
                    break
            elif continue_flag:
                continue
            else:
                w_txt = line.split(':')
                if len(w_txt) < 2:
                    continue
                w_txt[0] = w_txt[0].strip().split(' ')[-1]
                w_txt[1] = w_txt[1].strip()
                output += pre_blank +  '("%s", ct.c_unit, %s),' % (w_txt[0], w_txt[1])
                output += '\n'
        if output:
            output += pre_blank + ')\n'
            w_file.writelines(output)
            w_file.flush()
            
    w_file.close()
    r_file.close()

def calc_user_ack_count(field_str):
    global user_ack_count
    if re.match(r'.*s1$', field_str):
        user_ack_count += 1 

def calc_each_ack_start_position():
    global user_ack_count
    S1_ACK_START_POSITION = 12
    S2_ACK_START_POSITION = S1_ACK_START_POSITION + user_ack_count
    S1_ACK_REP_START_POS = S2_ACK_START_POSITION + user_ack_count
    S2_ACK_REP_START_POS = S1_ACK_REP_START_POS + user_ack_count
      
def ret_sack(trace_file):
    global user_ack_count
    user_ack_count = 0
    
    branch, version = getBranchVersion(trace_file)
    if not branch or not version:
        print "Can't get the branch or version, will use the default head file instead!"
    else:
        if not getSvnHeadFile(branch, version) :
            print "Svn can't get the head file, will use the default head file instead!"
    
      
    if not os.path.exists(hfile_name):
        print 'There is no head file'
        return None, None, None
    
    r_file = open(hfile_name, 'r')
    w_file = open(sack_name, 'w')

    core_sack = []
    cell_sack = []
    user_sack = []

    while True:
        line = r_file.readline()
        if not line:
            break
        
        if re.match(r'^struct SMacHsTtiTraceBitFieldForCellInfo', line):
            output = r'MACHS_TTI_TRACE_BIT_FIELD_FOR_CELL_INFO = ('
            out_sack = cell_sack
        elif re.match(r'^struct SMacHsTtiTraceBitFieldForCore', line):
            output = r'MACHS_TTI_TRACE_BIT_FIELD_FOR_CORE = ('
            out_sack = core_sack
        elif re.match(r'^struct SMacHsTtiTraceBitFieldForLocalUser', line):
            output = r'MACHS_TTI_TRACE_BIT_FIELD_FOR_USER = ('
            out_sack = user_sack
        else:
            continue
        output += '\n'
        blank_len = len(output)
        pre_blank = ' ' * blank_len
        continue_flag = False
        while True:
            line = r_file.readline()
            line = line.strip().split(';')
            line_1 = ''
            if len(line) > 1:
                line_1 = line[1]
            line = line[0]
            if "{" in line:
                continue
            elif '/*' in line:
                continue_flag = True
                continue
            elif "}" in line:
                if '*/' in line_1:
                    continue_flag = False
                    continue
                else:
                    break
            elif "*/" in line:
                continue_flag = False
                continue
            elif continue_flag:
                continue
            else:
                w_txt = line.split(':')
                if len(w_txt) < 2:
                    continue
                w_txt[0] = w_txt[0].strip().split(' ')[-1]
                calc_user_ack_count(w_txt[0])
                w_txt[1] = w_txt[1].strip()
                output += pre_blank +  '(%s, ct.c_uint, %s),' % (w_txt[0], w_txt[1])
                output += '\n'
                tmp_str = (w_txt[0], ct.c_uint, int(w_txt[1]))
                out_sack.append(tmp_str)
        if output:
            output += pre_blank + ')\n'
            w_file.writelines(output)
            w_file.flush()
            
    w_file.close()
    r_file.close()
    
    cell_info = (("cell1", tuple(cell_sack)),("cell2", tuple(cell_sack)),("cell3", tuple(cell_sack)))
    calc_each_ack_start_position()
    return tuple(core_sack), cell_info, tuple(user_sack)                  
                    
if __name__ == '__main__':
#     trans_hfile_to_sack()
#     replace_sack()
#     core_sack, cell_sack, user_sack = ret_sack()
#     print core_sack
#     print cell_sack
#     print user_sack
#     branch = r'BTS_SC_DSP/branches/p_nyquist'
#     version = r'84294'
#     b_flag = getSvnHeadFile(branch, version)
#     print b_flag
#                     
#    file_path = r'D:\userdata\m1tang\Desktop\rubbish\task\0x1252_MacHs_TTI_Trace_20160218_140446.txt'
    file_path = r'D:\userdata\m1tang\My Documents\MyJabberFiles\donghao.cao@nokia.com\TtiTrace_1471_531_CP4_20160328145029.txt'
    branch, version = getBranchVersion(file_path)
    if not branch or not version:
        print "Can't get the branch or version"
        exit(0)
    b_flag = getSvnHeadFile(branch, version) 
    if not b_flag:
        print "Svn can't get the head file, will use the default head file instead!"
    print branch, version
    exit(0)
    
