'''
Created on 2015\5\22

@author: m1tang
'''
import sqlite3 as db

CORE_TABLE_NAME = r'core_info'
CELL_TABLE_NAME = r'cell_info'
USER_TABLE_NAME = r'user_info'

SFN_COL_NAME = r'sfn'
SUBFRMAE_COL_NAME = r'subFrameNbr'

class db_class(object):
    '''
    classdocs
    '''


    def __init__(self, db_path):
        '''
        Constructor
        '''
        self.db_path = db_path
        self.db = db.connect(db_path)
        self.cur_db = self.db.cursor()
    
    def createCoreTable(self, table_column_list):
        self.__createTable(CORE_TABLE_NAME, table_column_list)
    
    def createCoreIndex(self):
        sql_str = r'create index sfn_subframe on %s(%s, %s)' % (CORE_TABLE_NAME, SFN_COL_NAME, SUBFRMAE_COL_NAME)
        
        self.cur_db.execute(sql_str)
        
        self.commitDB()
        
    def createCellTable(self, table_column_list):
        self.__createTable(CELL_TABLE_NAME, table_column_list)
    
    def createUserTable(self, table_column_list):
        self.__createTable(USER_TABLE_NAME, table_column_list)
    
    def __isTalbeExist(self, table_name):
        sql_str = r'select count(*) from sqlite_master where type = "table" and name = "%s"' % (table_name)

        rs = self.cur_db.execute(sql_str)
        
        count = rs.fetchall()[0][0]
        return count
            
    
    def __createTable(self, table_name, table_column_list):
        if self.__isTalbeExist(table_name):
            print "table %s exist" % table_name
            return
        
        sql_str = r"create table %s (core_no INTEGER, " % table_name
        
        for ele in table_column_list:
            sql_str += r"%s INTEGER, " % ele
            
        sql_str = sql_str[:-2]
        sql_str += r")"
        
        self.cur_db.execute(sql_str)
        
        self.db.commit()
     
    def insertData(self, core_no, table_name, value_list):
        sql_str = r'insert into %s values (%d, %s)' % (table_name, core_no, ', '.join('"%s"' % ele for ele in value_list))
        self.cur_db.execute(sql_str)
#        self.db.commit()
        
    def findData(self, table_name):
        if not self.__isTalbeExist(table_name):
            return
        
        sql_str = r'select * from %s' % table_name
        rs = self.cur_db.execute(sql_str)
        return rs
     
    def findCore(self, table_name):
        if not self.__isTalbeExist(table_name):
            return
        
        sql_str = r'select distinct(core_no) from %s' %(table_name)
        rs = self.cur_db.execute(sql_str)
        return rs
     
    def findCell(self, table_name):
        if not self.__isTalbeExist(table_name):
            return 
               
        sql_str = r'select distinct cellID from %s' %(table_name)
        rs = self.cur_db.execute(sql_str)
        return rs
    
    def findCellByCore(self, table_name, core_no):
        if not self.__isTalbeExist(table_name):
            return 
               
        sql_str = r'select distinct cellID from %s where core_no = %s' %(table_name, core_no)
        rs = self.cur_db.execute(sql_str)
        return rs
    
    def findUserByCore(self, table_name, core_no):
        if not self.__isTalbeExist(table_name):
            return
                
        sql_str = r'select distinct userId from %s where core_no = %s' %(table_name, core_no)
        rs = self.cur_db.execute(sql_str)
        return rs        
    
    def findUserByCoreAndCell(self, table_name, core_no, cell_no):
        if not self.__isTalbeExist(table_name):
            return  
        sql_str = r'select distinct userId from %s where ' %(table_name)
        if core_no:
            sql_str += r'core_no = %s and ' % core_no
        if cell_no:
            sql_str += r'cellId = %s and ' % cell_no
        
        if sql_str[-5:] == ' and ':
            sql_str = sql_str[:-5]
        else:
            sql_str = sql_str[:-7]
        return self.cur_db.execute(sql_str) 
    
    def findUser(self, table_name):
        if not self.__isTalbeExist(table_name):
            return
                
        sql_str = r'select distinct userId from %s' %(table_name)
        rs = self.cur_db.execute(sql_str)
        return rs
    
    def translateCoreRsToList(self, rs):
        return self.translateRsToList(rs, 1)
    
    def translateCellRsToList(self, rs):
        return self.translateRsToList(rs, 1)
    
    def translateUserRsToList(self, rs):
        return self.translateRsToList(rs, 1)
    
    def translateRsToList(self, rs, rs_data_len):
        value = []
        while True:
            data = rs.fetchone()
            if not data:
                break
            for i in range(0, rs_data_len):
                value.append(data[i])
        value = set(value)  
        return list(value)
    
    def getColumnNameFromTable(self, table_name):
        if not self.__isTalbeExist(table_name):
            return
        sql_str = "PRAGMA table_info(%s)" % table_name
        return self.cur_db.execute(sql_str)
    
    def getColumnNameFromCoreTable(self):
        return self.getColumnNameFromTable(CORE_TABLE_NAME)
    
    def getColumnNameFromCellTable(self):
        return self.getColumnNameFromTable(CELL_TABLE_NAME)    
    
    def getColumnNameFromUserTable(self):
        return self.getColumnNameFromTable(USER_TABLE_NAME)
    
    def findCoreDataByCore(self, core_no):
        sql_str = r'select * from %s where core_no = %s' % (CORE_TABLE_NAME, core_no)
        return self.cur_db.execute(sql_str)
    
#     def findCoreData(self):
#         sql_str = r'select * from %s' % (CORE_TABLE_NAME)
#         return self.cur_db.execute(sql_str)
    
#     def findCellData(self):
#         sql_str = r'select * from %s' % (CELL_TABLE_NAME)
#         return self.cur_db.execute(sql_str)
    
    def findCellDataByCell(self, cell_no):
        sql_str = r'select * from %s where cellID = %s' % (CELL_TABLE_NAME, cell_no)
        return self.cur_db.execute(sql_str)    
    
    def findCellDataByCoreAndCell(self, core_no, cell_no):
        sql_str = r'select * from %s where core_no = %s and cellID = %s' % (CELL_TABLE_NAME, core_no, cell_no)
        return self.cur_db.execute(sql_str)     

    def findCellDataByCore(self, core_no):
        sql_str = r'select * from %s where core_no = %s' % (CELL_TABLE_NAME, core_no)
        return self.cur_db.execute(sql_str)
    
    def findUserDataByCoreAndCellAndUser(self, core_no, cell_no, user_no):
        sql_str = r'select * from %s where core_no = %s and cellId = %s and userId = %s' % (USER_TABLE_NAME, core_no, cell_no, user_no)
        return self.cur_db.execute(sql_str)
    
    def findUserDataByCoreAndUser(self, core_no, user_no):
        sql_str = r'select * from %s where core_no = %s and userId = %s' % (USER_TABLE_NAME, core_no, user_no)
        return self.cur_db.execute(sql_str)
    
    def findUserDataByCoreAndCell(self, core_no, cell_no):
        sql_str = r'select * from %s where core_no = %s and cellId = %s' % (USER_TABLE_NAME, core_no, cell_no)
        return self.cur_db.execute(sql_str)
    
    def findUserDataByCore(self, core_no):
        sql_str = r'select * from %s where core_no = %s' % (USER_TABLE_NAME, core_no)
        return self.cur_db.execute(sql_str)
    
    def findUserDataByCell(self, cell_no):
        sql_str = r'select * from %s where cellId = %s' % (USER_TABLE_NAME, cell_no)
        return self.cur_db.execute(sql_str)
    
    def findUserDataByCellAndUser(self, cell_no, user_no):
        sql_str = r'select * from %s where cellId = %s and userId = %s' % (USER_TABLE_NAME, cell_no, user_no)
        return self.cur_db.execute(sql_str)
    
    def findUserDataByUser(self, user_no):
        sql_str = r'select * from %s where userId = %s' % (USER_TABLE_NAME, user_no)
        return self.cur_db.execute(sql_str)
    
    def findCoreData(self, core_no):
        if not self.__isTalbeExist(CORE_TABLE_NAME):
            return
        
        sql_str = r'select * from %s where ' % CORE_TABLE_NAME 
        if core_no:
            sql_str += r'core_no = %s and ' % core_no
        
        if sql_str[-5:] == ' and ':
            sql_str = sql_str[:-5]
        else:
            sql_str = sql_str[:-7]
        return self.cur_db.execute(sql_str)     
    
    def findCellData(self, core_no, cell_no):
        if not self.__isTalbeExist(CELL_TABLE_NAME):
            return
    
        sql_str = r'select * from %s where ' % CELL_TABLE_NAME 
        if core_no:
            sql_str += r'core_no = %s and ' % core_no
        if cell_no:
            sql_str += r'cellID = %s and ' % cell_no
            
        if sql_str[-5:] == ' and ':
            sql_str = sql_str[:-5]
        else:
            sql_str = sql_str[:-7]
        return self.cur_db.execute(sql_str)         
    
    def findUserData(self, core_no, cell_no, user_no):
        if not self.__isTalbeExist(USER_TABLE_NAME):
            return    

        sql_str = r'select * from %s where ' % USER_TABLE_NAME 
        if core_no:
            sql_str += r'core_no = %s and ' % core_no
        if cell_no:
            sql_str += r'cellId = %s and ' % cell_no
        if user_no:
            sql_str += r'userId = %s and ' % user_no
            
        if sql_str[-5:] == ' and ':
            sql_str = sql_str[:-5]
        else:
            sql_str = sql_str[:-7]
        return self.cur_db.execute(sql_str) 
    
    
    def getUserThroughputData(self, core_no, cell_no, user_no):
        sql_str = r"select userId, finalTbs, paddingBits, core_no, cellId, hour, minute, second, millisecond from %s where transmissionNbr = 1 and " % USER_TABLE_NAME
        if core_no:
            sql_str += r"core_no = %d and " % int(core_no)
        if cell_no:
            sql_str += r"cellId = %d and " % int(cell_no)
        if user_no:
            sql_str += r"userId = %d and " % int(user_no)
    
        sql_str = sql_str[:-5]
        return self.cur_db.execute(sql_str) 
    
    def getCoreDataBySfnAndSubsfn(self, sfn, sub_sfn):
        sql_str = r'select * from %s where sfn = %d and subFrameNbr = %d' % (CORE_TABLE_NAME, sfn, sub_sfn)
        return self.cur_db.execute(sql_str)
    
    def getSequenceNoFromCore(self):
        sql_str = r'select distinct sequenceNo from %s' % CORE_TABLE_NAME
        return self.cur_db.execute(sql_str)
    
    def getSequenceNoFromCell(self):
        sql_str = r'select distinct sequenceNo from %s' % CELL_TABLE_NAME
        return self.cur_db.execute(sql_str)
    
    def getSequenceNoFromUser(self):
        sql_str = r'select distinct sequenceNo from %s' % USER_TABLE_NAME
        return self.cur_db.execute(sql_str)
    
    def excuteSelfSql(self, sql_str):
        return self.cur_db.execute(sql_str)
    
    def dropAllTable(self):
        self.dropTable(CORE_TABLE_NAME)
        self.dropTable(CELL_TABLE_NAME)
        self.dropTable(USER_TABLE_NAME)
    
    def dropTable(self, table_name):
        rs = self.cur_db.execute("SELECT name FROM sqlite_master where type='table' and name='%s'" % table_name)
        if rs.fetchone():
            sql_str = r'drop table %s' % table_name
            self.cur_db.execute(sql_str)
            self.db.commit()
        else:
            print 'no table'
    
    def commitDB(self):
        self.db.commit()
    
    def closeDB(self):
#         self.db.commit()
        self.db.close()
