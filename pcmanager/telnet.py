import telnetlib


def telnet_remote(host):
    password = "btstest"
    user = "upl1-tester"
    print "host:", host
    try:
        tn = telnetlib.Telnet(host, timeout=3)
        #tn.set_debuglevel(2)
        tn.read_until("login:")
        tn.write(user + "\r\n")
        if password:
            tn.read_until("password:")
            tn.write(password + "\r\n")
        tn.read_until("tester>")
        tn.write("netstat -ano | find \"3389\"\r\n")
        ret_msg = tn.read_until("tester>")
        print ret_msg
        tn.write("exit\r\n")
        tn.close()
    except Exception as e:
        ret_msg = e
        print e

    return ret_msg

if __name__ == "__main__":
    telnet_remote("10.69.23.80")