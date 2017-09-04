'''
Created on 2015/5/22

@author: m1tang
'''
from db_class import *  # @UnusedWildImport


class csv_class(object):
    def __init__(self, file_path, file_mode):
        '''
        Constructor
        '''
        self.file_path = file_path
        self.file_mode = file_mode
        self.openFile()
     
    def openFile(self):
        self.csv_file = open(self.file_path, self.file_mode)
        
    def getDBColumn(self):
        self.csv_file.seek(0)
        first_row  = self.csv_file.readline()
        return first_row.split(",")
        
    def getCsvFile(self):
        self.csv_file.seek(0)
        return self.csv_file
    
    def writeCsvFile(self, data_list):
        data_str = ",".join("%s" % ele for ele in data_list)
        self.csv_file.write(data_str)
    
    def closeFile(self):
        self.csv_file.close()  

        