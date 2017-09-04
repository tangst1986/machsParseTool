import sys
import traceback
import logging
from PyQt4.QtGui import QApplication
from ui_MainWindow import Ui_MainWindow

def configLogger():

    gLogConf = {
        'filename': 'stdout',
        'filemode': 'w',
        'level':    logging.INFO,
        'format':   '%(asctime)s %(levelname)s %(module)s:%(lineno)s : %(message)s',
        'stream':   sys.stdout,
    }
    
    logging.basicConfig(**gLogConf)

        
def startGui():
    try:
        app = QApplication(sys.argv)
        ui = Ui_MainWindow()
        ui.show()
        app.exec_()
    except Exception as e:
        print(e)
        logging.critical(traceback.format_exc())

if __name__ == '__main__':
    startGui()