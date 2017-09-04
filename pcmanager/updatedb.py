from multiprocessing.dummy import Pool as ThreadPool
from telnet import telnet_remote
import re
import MySQLdb
from Queue import Queue
import os

host_pattern = re.compile(r'(.*3389\s+)(\d+.\d+.\d+.\d+)(:\d+)', re.DOTALL)
user_pattern = re.compile(r'(.*\d+.\d+.\d+.\d+\s+)(.*?(?=\s))(\s+.*)')

compute_name_map = {"5CG4511HRK": "hu weikang",
                    "CNU321BN45": "chen fei",
                    "CNU403921K": "cheng hongwu",
                    "CNU403922C": "zhang jiafang",
                    "CNU2489ZG3": "He Luting",
                    "5CG4511HWD": "Li xiaofeng",
                    "CNU321BNXC": "zhang peng",
                    "5CG4511HXX": "zhang yulong",
                    "CNU401B6M1": "li fugui",
                    "5CG4511HQ3": "wang yucheng",
                    "CNU249BPNF": "sou jianming",
                    "CNU40391YK": "tang miao",
                    "5CG446372L": "sun kun",
                    "GWFL5S1":    "Hong Shaojun",
                    "5CG4511HVW": "jiang xiao",
                    "CNU423BSPD": "ma ye",
                    "5CG44647LZ": "zhang jianbo",
                    "5CG4413M99": "chen yi",
                    "CNU3169ZP7": "ma xiaonan",
                    "5CG4511HRR": "wang qian",
                    "CNU321BN0N": "jin feng",
                    "5CG5010H14": "zhong shu ting",
                    "CNU4289Q6H": "liu yanyan",
                    "5CG4511HX9": "wang zhenglin",
                    "CNU251B88Q": "tang xiaohu",
                    "CNU401B6LQ": "cao donghao"
                    }

""" ###################################################### """
from runningTb import RunningTb, engine
from sqlalchemy.orm import sessionmaker, scoped_session

def get_user_from_host(host):
    """ get user from host """
    out = os.popen('nbtscan %s'%host)
    out = out.readlines()
    if len(list(out)) == 5:
        m = user_pattern.match(out[4])
        if m:
            return m.group(2)
    return None

def update_db(host, ret_msg):
    session_factory = sessionmaker(bind=engine)
    Session = scoped_session(session_factory)
    session = Session()
    instance = session.query(RunningTb).filter_by(ip=host).first()

    print "LRLZ ret_msg", host, ret_msg


    if "timed out" in ret_msg:
        status = "poweroff"
    elif "telnet connection closed" in ret_msg:
        status = "telnet closed"
    else:
        status = "running"

    if "Connection refused" in ret_msg:
        status = "telnet refused"

    user = 'None'
    if "ESTABLISHED" in ret_msg:
        match = host_pattern.match(ret_msg)
        if match:
            remote_host = match.group(2)

        user = get_user_from_host(remote_host)
        if user is None:
            user = remote_host

        if user in compute_name_map:
            user = compute_name_map[user]

    if instance.status != status:
        instance.status = status

    username = instance.username
    if username != user:
        if username is not "None":
            instance.lastuser = username
            instance.lastlogintime = time.ctime()
        instance.username = user


    session.commit()
    session.close()
    Session.remove()

def remote_status_update(host):
    msg = telnet_remote(host)
    update_db(host, msg)

def main():
    pool = ThreadPool(20)
    from createdb import select_db
    hosts = select_db()
    hosts.remove("10.69.23.198")
    result = pool.map(remote_status_update, hosts)
    #print "result:", result
    pool.close()
    pool.join()

import threading
import time

def perodic_task():
    main()
    print "LRLZ 30s perodic task", time.ctime()
    global timer
    timer = threading.Timer(30, perodic_task,[])
    timer.start()

if __name__ == "__main__":
    timer = threading.Timer(30, perodic_task,[])
    timer.start()

