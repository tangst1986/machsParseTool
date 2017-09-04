'''
@author: m1tang
'''
import zipfile
import os
import subprocess
import shutil

base_path = os.path.join(os.getcwd(), '..')

cmd_dir = os.path.join(base_path, 'cmd_exe')
gui_dir = os.path.join(base_path, 'gui_exe')
gui_cmd_dir = os.path.join(base_path, 'gui_cmd_exe')

def clean_build_dir():
    if os.path.exists(cmd_dir):
        shutil.rmtree(cmd_dir)
    if os.path.exists(gui_dir):
        shutil.rmtree(gui_dir)
    if os.path.exists(gui_cmd_dir):
        shutil.rmtree(gui_cmd_dir)
        
def mk_build_dir():
    if not os.path.exists(cmd_dir):
        os.mkdir(cmd_dir)
    if not os.path.exists(gui_dir):
        os.mkdir(gui_dir)
    if not os.path.exists(gui_cmd_dir):
        os.mkdir(gui_cmd_dir)
def build_exe(commond):
    try:
        subprocess.check_output(commond)
    except subprocess.CalledProcessError as e:
        print e.output
        print "err: build failed %s" % commond
        return False
    
    return True

def build_cmd_exe():
    cmd_exe_build = r'python cmd_setup.py py2exe'
    
    if not build_exe(cmd_exe_build):
        return False
    
    shutil.move('dist', cmd_dir)
    return True

def add_gui_library():
    wx_file = r'backend_wx.pyc'
    wxagg_file = r'backend_wxagg.pyc'
    
    src_path = r'C:\Python27\Lib\site-packages\matplotlib\backends'
    dest_path = r'matplotlib\backends'
    
    lib_file_path = os.path.join(gui_dir, 'dist', 'library.zip')
    lib_file = zipfile.ZipFile(lib_file_path, 'a')
    lib_file.write(os.path.join(src_path, wx_file), os.path.join(dest_path, wx_file))
    lib_file.write(os.path.join(src_path, wxagg_file), os.path.join(dest_path, wxagg_file))
    
    lib_file.close()

def build_gui_exe():
    gui_exe_build = r'python gui_setup.py py2exe'
        
    if not build_exe(gui_exe_build):
        return False
    
    shutil.move('dist', gui_dir)
    add_gui_library()
    return True

def build_gui_cmd_exe():
    gui_cmd_exe = r'python gui_cmd_setup.py py2exe'
    
    if not build_exe(gui_cmd_exe):
        return False
    shutil.move('dist', gui_cmd_dir)
    return True

if __name__ == '__main__':
    clean_build_dir()
    mk_build_dir()
    build_cmd_exe()
    build_gui_exe()
    build_gui_cmd_exe()