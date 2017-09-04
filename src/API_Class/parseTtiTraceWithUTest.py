import ctypes as ct
import os
from hfile2sack import ret_sack

global MACHS_TTI_TRACE_BIT_FIELD_FOR_USER, MACHS_TTI_TRACE_BIT_FIELD_FOR_CELL_INFO, MACHS_TTI_TRACE_BIT_FIELD_FOR_CORE

MACHS_TTI_TRACE_BIT_FIELD_FOR_USER =       (("ueCategory", ct.c_uint, 5),
                                            ("nbrOfPdschCodes", ct.c_uint, 4),
                                            ("lchId", ct.c_uint, 16),
                                            ("SI", ct.c_uint, 2),
                                            ("modulation", ct.c_uint, 2),
                                            ("operatorID", ct.c_uint, 3),
                                            ("userId", ct.c_uint, 16),
                                            ("rnti", ct.c_uint, 16),
                                            ("cellId", ct.c_uint, 16),
                                            ("spiWeight", ct.c_uint, 8),
                                            ("edrxEnable", ct.c_uint, 1),
                                            ("averageCodeRate", ct.c_uint, 7),
                                            ("internalPrioQId", ct.c_uint, 9),
                                            ("tsn", ct.c_uint, 14),
                                            ("pdschPowerIndex", ct.c_uint, 9),
                                            ("t1Tsn", ct.c_uint, 14),
                                            ("harqIndex", ct.c_uint, 4),
                                            ("windowSize", ct.c_uint, 8),
                                            ("compensatedCqi", ct.c_uint, 6),
                                            ("recommendedTbs", ct.c_uint, 16),
                                            ("finalTbs", ct.c_uint, 16),
                                            ("scchPower", ct.c_uint, 16),
                                            ("pdschPower", ct.c_uint, 16),
                                            ("a", ct.c_uint, 15),
                                            ("bufferOccupancyInBits", ct.c_uint, 15),
                                            ("pciValue", ct.c_uint, 2),
                                            ("tpInBitsPerTTI", ct.c_uint, 19),
                                            ("cqi", ct.c_uint, 6),
                                            ("nbrOfMacDPdusInTb", ct.c_uint, 7),
                                            ("akNkReptFactor", ct.c_uint, 2),
                                            ("averageCqi", ct.c_uint, 7),
                                            ("ndi", ct.c_uint, 1),
                                            ("transmissionNbr", ct.c_uint, 3),
                                            ("carrierStreamIndex", ct.c_uint, 3),
                                            ("rv", ct.c_uint, 3),
                                            ("spi", ct.c_uint, 4),
                                            ("pading4", ct.c_uint, 9),
                                            ("scalingFactorQos", ct.c_uint, 32),
                                            ("activityFactor", ct.c_uint, 32),
                                            ("MaxPowerWithSharedRes", ct.c_uint, 16),
                                            ("neededPowerWithSharedResShared", ct.c_uint, 16),
                                            ("maxAllowedTBSWithSharedRes", ct.c_uint, 16),
                                            ("maxCRLimitedBlockSize", ct.c_uint, 16),
                                            ("paddingBits", ct.c_uint, 16),
                                            ("cqiVariance", ct.c_uint, 10),
                                            ("codeMuxIndex", ct.c_uint, 5),
                                            ("mimoModeInd", ct.c_uint, 1),
                                            ("neededCodes", ct.c_uint, 4),
                                            ("maxNeededCodes", ct.c_uint, 4),
                                            ("spiChangeIndication", ct.c_uint, 2),
                                            ("prioQType", ct.c_uint, 2),
                                            ("pdschCodeOffset", ct.c_uint, 4),
                                            ("machsAddress", ct.c_uint, 16))

MACHS_TTI_TRACE_BIT_FIELD_FOR_CELL_INFO =  (('cellID', ct.c_uint, 16),
                                            ('nbrofAgguser', ct.c_uint, 9),
                                            ('nbrofProposedLocalUser', ct.c_uint, 3),
                                            ('MoCNTrigger', ct.c_uint, 1),
                                            ('pading2', ct.c_uint, 3),
                                            ('nbrofSchAggUser', ct.c_uint, 3),
                                            ('transCarrierPower', ct.c_uint, 17),
                                            ('discardedCodes', ct.c_uint, 4),
                                            ('nbrofLocalUser', ct.c_uint, 8),
                                            ('nbrofLocalU', ct.c_uint, 9),
                                            ('k', ct.c_uint, 9),
                                            ('nbrOfBannedUsers', ct.c_uint, 9),
                                            ('nbrofReceiveAggUser', ct.c_uint, 4),
                                            ('calibrationOngoing', ct.c_uint, 1),
                                            ('availPdschPower', ct.c_uint, 16),
                                            ('maxUsablePower', ct.c_uint, 16),
                                            ('nonHSDPAPower', ct.c_uint, 16),
                                            ('nbrofLocalUOp1', ct.c_uint, 8),
                                            ('nbrofLocalUOp2', ct.c_uint, 8),
                                            ('nbrofLocalUOp3', ct.c_uint, 8),
                                            ('nbrofLocalUOp4', ct.c_uint, 8),
                                            ('phaseOffset', ct.c_uint, 9),
                                            ('proposedNodeNum2SELA', ct.c_uint, 3),
                                            ('proposedAggNodeNum2SELA', ct.c_uint, 3),
                                            ('pading6', ct.c_uint, 1))

MACHS_TTI_TRACE_BIT_FIELD_FOR_CELL = (("cell1", MACHS_TTI_TRACE_BIT_FIELD_FOR_CELL_INFO),
                                      ("cell2", MACHS_TTI_TRACE_BIT_FIELD_FOR_CELL_INFO),
                                      ("cell3", MACHS_TTI_TRACE_BIT_FIELD_FOR_CELL_INFO))

MACHS_TTI_TRACE_BIT_FIELD_FOR_CORE = (
                                       ('ackNack_u1s1', ct.c_uint, 4),
                                       ('ackNack_u2s1', ct.c_uint, 4),
                                       ('ackNack_u3s1', ct.c_uint, 4),
                                       ('ackNack_u4s1', ct.c_uint, 4),
                                       ('ackNack_u5s1', ct.c_uint, 4),
                                       ('ackNack_u6s1', ct.c_uint, 4),
                                       ('ackNack_u7s1', ct.c_uint, 4),
                                       ('ackNack_u8s1', ct.c_uint, 4),
                                       ('ackNack_u9s1', ct.c_uint, 4),
                                       ('ackNack_u10s1', ct.c_uint, 4),
                                       ('ackNack_u11s1', ct.c_uint, 4),
                                       ('ackNack_u12s1', ct.c_uint, 4),
                                       ('ackNack_u13s1', ct.c_uint, 4),
                                       ('ackNack_u14s1', ct.c_uint, 4),
                                       ('ackNack_u15s1', ct.c_uint, 4),
                                       ('ackNack_u16s1', ct.c_uint, 4),
                                       ('ackNack_u17s1', ct.c_uint, 4),
                                       ('ackNack_u18s1', ct.c_uint, 4),
                                       ('ackNack_u19s1', ct.c_uint, 4),
                                       ('ackNack_u20s1', ct.c_uint, 4),
                                       ('ackNack_u21s1', ct.c_uint, 4),
                                       ('ackNack_u22s1', ct.c_uint, 4),
                                       ('ackNack_u23s1', ct.c_uint, 4),
                                       ('ackNack_u24s1', ct.c_uint, 4),
                                       ('ackNack_u1s2', ct.c_uint, 4),
                                       ('ackNack_u2s2', ct.c_uint, 4),
                                       ('ackNack_u3s2', ct.c_uint, 4),
                                       ('ackNack_u4s2', ct.c_uint, 4),
                                       ('ackNack_u5s2', ct.c_uint, 4),
                                       ('ackNack_u6s2', ct.c_uint, 4),
                                       ('ackNack_u7s2', ct.c_uint, 4),
                                       ('ackNack_u8s2', ct.c_uint, 4),
                                       ('ackNack_u9s2', ct.c_uint, 4),
                                       ('ackNack_u10s2', ct.c_uint, 4),
                                       ('ackNack_u11s2', ct.c_uint, 4),
                                       ('ackNack_u12s2', ct.c_uint, 4),
                                       ('ackNack_u13s2', ct.c_uint, 4),
                                       ('ackNack_u14s2', ct.c_uint, 4),
                                       ('ackNack_u15s2', ct.c_uint, 4),
                                       ('ackNack_u16s2', ct.c_uint, 4),
                                       ('ackNack_u17s2', ct.c_uint, 4),
                                       ('ackNack_u18s2', ct.c_uint, 4),
                                       ('ackNack_u19s2', ct.c_uint, 4),
                                       ('ackNack_u20s2', ct.c_uint, 4),
                                       ('ackNack_u21s2', ct.c_uint, 4),
                                       ('ackNack_u22s2', ct.c_uint, 4),
                                       ('ackNack_u23s2', ct.c_uint, 4),
                                       ('ackNack_u24s2', ct.c_uint, 4),
                                       ('ackNack_u1s1Rep2', ct.c_uint, 4),
                                       ('ackNack_u2s1Rep2', ct.c_uint, 4),
                                       ('ackNack_u3s1Rep2', ct.c_uint, 4),
                                       ('ackNack_u4s1Rep2', ct.c_uint, 4),
                                       ('ackNack_u5s1Rep2', ct.c_uint, 4),
                                       ('ackNack_u6s1Rep2', ct.c_uint, 4),
                                       ('ackNack_u7s1Rep2', ct.c_uint, 4),
                                       ('ackNack_u8s1Rep2', ct.c_uint, 4),
                                       ('ackNack_u9s1Rep2', ct.c_uint, 4),
                                       ('ackNack_u10s1Rep2', ct.c_uint, 4),
                                       ('ackNack_u11s1Rep2', ct.c_uint, 4),
                                       ('ackNack_u12s1Rep2', ct.c_uint, 4),
                                       ('ackNack_u13s1Rep2', ct.c_uint, 4),
                                       ('ackNack_u14s1Rep2', ct.c_uint, 4),
                                       ('ackNack_u15s1Rep2', ct.c_uint, 4),
                                       ('ackNack_u16s1Rep2', ct.c_uint, 4),
                                       ('ackNack_u17s1Rep2', ct.c_uint, 4),
                                       ('ackNack_u18s1Rep2', ct.c_uint, 4),
                                       ('ackNack_u19s1Rep2', ct.c_uint, 4),
                                       ('ackNack_u20s1Rep2', ct.c_uint, 4),
                                       ('ackNack_u21s1Rep2', ct.c_uint, 4),
                                       ('ackNack_u22s1Rep2', ct.c_uint, 4),
                                       ('ackNack_u23s1Rep2', ct.c_uint, 4),
                                       ('ackNack_u24s1Rep2', ct.c_uint, 4),
                                       ('ackNack_u1s2Rep2', ct.c_uint, 4),
                                       ('ackNack_u2s2Rep2', ct.c_uint, 4),
                                       ('ackNack_u3s2Rep2', ct.c_uint, 4),
                                       ('ackNack_u4s2Rep2', ct.c_uint, 4),
                                       ('ackNack_u5s2Rep2', ct.c_uint, 4),
                                       ('ackNack_u6s2Rep2', ct.c_uint, 4),
                                       ('ackNack_u7s2Rep2', ct.c_uint, 4),
                                       ('ackNack_u8s2Rep2', ct.c_uint, 4),
                                       ('ackNack_u9s2Rep2', ct.c_uint, 4),
                                       ('ackNack_u10s2Rep2', ct.c_uint, 4),
                                       ('ackNack_u11s2Rep2', ct.c_uint, 4),
                                       ('ackNack_u12s2Rep2', ct.c_uint, 4),
                                       ('ackNack_u13s2Rep2', ct.c_uint, 4),
                                       ('ackNack_u14s2Rep2', ct.c_uint, 4),
                                       ('ackNack_u15s2Rep2', ct.c_uint, 4),
                                       ('ackNack_u16s2Rep2', ct.c_uint, 4),
                                       ('ackNack_u17s2Rep2', ct.c_uint, 4),
                                       ('ackNack_u18s2Rep2', ct.c_uint, 4),
                                       ('ackNack_u19s2Rep2', ct.c_uint, 4),
                                       ('ackNack_u20s2Rep2', ct.c_uint, 4),
                                       ('ackNack_u21s2Rep2', ct.c_uint, 4),
                                       ('ackNack_u22s2Rep2', ct.c_uint, 4),
                                       ('ackNack_u23s2Rep2', ct.c_uint, 4),
                                       ('ackNack_u24s2Rep2', ct.c_uint, 4),                                       
                                       ('usedSchedAlg', ct.c_uint, 2),
                                       ('cpuLoad', ct.c_uint, 7),
                                       ('nbrOfHarqs', ct.c_uint, 10),
                                       ('pading3', ct.c_uint, 13),
                                       ('coreid', ct.c_uint, 32)
                                       )

MACHS_TTI_TRACE_BIT_FIELD =  (("traceType", ct.c_uint, 3),
                               ("hour", ct.c_uint, 5),
                               ("minute", ct.c_uint, 6),
                               ("second", ct.c_uint, 6),
                               ("millisecond", ct.c_uint, 10),
                               ("pading1", ct.c_uint, 2),
                            
                                ("sfn", ct.c_uint, 12),
                                ("subFrameNbr", ct.c_uint,  4),
                                ("chipNbr", ct.c_uint,  12),
                                ("slotNbr", ct.c_uint,  4),
                                
                                ("sequenceNo",  ct.c_uint, 32))


class ParserError(Exception):
    """Raised when the msg file does not have the expected action"""

    def __init__(self, msg):
        Exception.__init__(self)
        self.msg = msg

    def __str__(self):
        return self.msg
    
class BlindParseMachsTtiTrace(object):
    ''' 
        if traceType changed, "self._trace_field_map" need to be modified.
        /*  traceType:
            0: core info; 
            1: local cell info; 
            2: mapping cell info; 
            3: local carrier scheduling info; 
            4: seconary carrier scheduling info, but secondary carrier is set up in remote machs;
            5: seconary carrier scheduling info, but primary carrier is set up in remote machs.
        */
    '''
    CORE_INFO = 0
    LOCAL_CELL_INFO = 1
    MAPPING_CELL_INFO = 2
    LOCAL_CA_SCH_INFO = 3
    SEC_CA_SCH_BUT_SEC_CA = 4
    SEC_CA_SCH_BUT_PR_CA =5
    
    def __init__(self, file_name, core_sack=None, cell_sack=None, user_sack=None):
        global MACHS_TTI_TRACE_BIT_FIELD_FOR_USER, MACHS_TTI_TRACE_BIT_FIELD_FOR_CELL, MACHS_TTI_TRACE_BIT_FIELD_FOR_CORE, MACHS_TTI_TRACE_BIT_FIELD_FOR_CELL_INFO
        self._file_name = file_name
        self.core_no = None
        
        if core_sack and cell_sack and user_sack:
            MACHS_TTI_TRACE_BIT_FIELD_FOR_USER = user_sack
            MACHS_TTI_TRACE_BIT_FIELD_FOR_CELL = cell_sack
            MACHS_TTI_TRACE_BIT_FIELD_FOR_CORE = core_sack
        
        self._get_parse_classes()
        
        base_name = os.path.basename(file_name).split('.')[0]
        common_path = os.path.abspath(os.path.join(os.getcwd(), "..")) + '\\DATA\\' + base_name
        core_file_path = common_path + "_core.csv"
        cell_file_path = common_path + "_cell.csv"
        user_file_path = common_path + "_user.csv"
        self._core_file = open(core_file_path, "wb")
        self._cell_file = open(cell_file_path, "wb")
        self._user_file = open(user_file_path, "wb")   
        
        self._get_title_info()
        
        self._parse_file()
        
    def _close_files(self):
        self._core_file.flush()
        self._cell_file.flush()
        self._user_file.flush()
        
        self._core_file.close()
        self._cell_file.close()
        self._user_file.close()
        
    def _write_to_result_file(self, msg, category):
        
        write_msg = ','.join([str(item) for item in msg]) + '\n'
        
        if category == BlindParseMachsTtiTrace.CORE_INFO:
            self._core_file.write(write_msg)
            self._core_file.flush()
        elif category == BlindParseMachsTtiTrace.LOCAL_CELL_INFO or \
             category == BlindParseMachsTtiTrace.MAPPING_CELL_INFO:
            self._cell_file.write(write_msg)
            self._cell_file.flush()
        elif category == BlindParseMachsTtiTrace.LOCAL_CA_SCH_INFO or \
             category == BlindParseMachsTtiTrace.SEC_CA_SCH_BUT_SEC_CA or \
             category == BlindParseMachsTtiTrace.SEC_CA_SCH_BUT_PR_CA:
            self._user_file.write(write_msg)
            self._user_file.flush()
            
    def _get_title_info(self):
        head_title = [field[0] for item in self._common_class_field_list for field in item[1]]
        core_title = [field[0] for item in self._core_class_field_list for field in item[1]]
        cell_title = [field[0] for item in self._cell_class_field_list for field in item[1]]
        user_title = [field[0] for item in self._user_class_field_list for field in item[1]]
        self.core_title =  core_title
        self._write_to_result_file(head_title + core_title, BlindParseMachsTtiTrace.CORE_INFO)
        self._write_to_result_file(head_title + cell_title, BlindParseMachsTtiTrace.LOCAL_CELL_INFO)
        self._write_to_result_file(head_title + user_title, BlindParseMachsTtiTrace.LOCAL_CA_SCH_INFO)
            
    def _parse_file(self):
        trace_file = open(self._file_name)
        
        line = trace_file.readline()  #skip 1st line
        while line:
            line = trace_file.readline()
            if not line:
                break
            line = line.strip()[:-1]
            line = line.strip().split(',')[16:]
            sliptIndex = len(self._common_class_field_list)      
            parse_common_result = self._parse_message_line(self._common_class_field_list, line[:sliptIndex])
            msg_type = parse_common_result[0]
            if msg_type == 0:
                msg_len = len(self._core_class_field_list)
            elif (msg_type == 1 or msg_type == 2):
                msg_len = len(self._cell_class_field_list)
            else:
                msg_len = len(self._user_class_field_list)
                
            parse_unique_result = self._parse_message_line(self._trace_field_map[msg_type], line[sliptIndex:sliptIndex+msg_len])
            if (msg_type == 0 and not self.core_no):
                self.core_no = parse_unique_result[self.core_title.index('coreid')]
            self._write_to_result_file(parse_common_result+parse_unique_result, msg_type)
                
        self._close_files()
        
    def _parse_message_line(self, class_fields_list, line):
        ''' '''
        if len(class_fields_list) != len(line):
            raise ParserError("Message length error, class_fields_list %d, msg %d. sack mismatch"%(len(class_fields_list), len(line)))
        
        parse_counter = 0
        parse_reslut = []
        for value in line:
            parse_class = class_fields_list[parse_counter][0]
            parse_instance = parse_class()
            parse_instance.value = int(value)
            for attr in class_fields_list[parse_counter][1]:
#                print attr[0], getattr(parse_instance.bits, attr[0])
                parse_reslut.append(getattr(parse_instance.bits, attr[0]))
            parse_counter += 1
            
        return parse_reslut
        
    def _get_parse_classes(self):
        global MACHS_TTI_TRACE_BIT_FIELD_FOR_USER, MACHS_TTI_TRACE_BIT_FIELD_FOR_CELL, MACHS_TTI_TRACE_BIT_FIELD_FOR_CORE

        self._common_class_field_list = self._create_parse_classes(MACHS_TTI_TRACE_BIT_FIELD)
        self._core_class_field_list = self._create_parse_classes(MACHS_TTI_TRACE_BIT_FIELD_FOR_CORE)
        self._cell_class_field_list = self._create_parse_classes(MACHS_TTI_TRACE_BIT_FIELD_FOR_CELL)
        self._user_class_field_list = self._create_parse_classes(MACHS_TTI_TRACE_BIT_FIELD_FOR_USER)
        
        self._trace_field_map = (self._core_class_field_list, 
                                 self._cell_class_field_list,
                                 self._cell_class_field_list,
                                 self._user_class_field_list,
                                 self._user_class_field_list,
                                 self._user_class_field_list)
        
#        print "self._common_class_field_list len:", len(self._common_class_field_list)
#        print "self._core_class_field_list len:", len(self._core_class_field_list)
#        print "self._cell_class_field_list len:", len(self._cell_class_field_list)
#        print "self._user_class_field_list len:", len(self._user_class_field_list)
        

    def _create_parse_classes(self, parse_field_list):
        ''' according to parse field struct, create union ctype classes which used to convert word to bitfield
            return ((class, filed), (class, filed),)
        '''
        bits_count = 0
        field_list = []
        class_fields_list = []
        for item in parse_field_list:
            if type(item[1]) is tuple:
                if field_list:
                    raise ParserError("field_list should be None")
                for innerItem in item[1]:
                    field_list.append((item[0]+'_'+innerItem[0], innerItem[1], innerItem[2])) #make name like this: cell3_transCarrierPower
                    bits_count = bits_count + innerItem[2]
                    if bits_count == 32:
                        bits_count = 0
                        ParseBits = type("ParseBits", (ct.Structure,), {"_fields_" : field_list})
                        BaseUnion = type("BaseUnion", (ct.Union,), {"_fields_":[('value', ct.c_uint), ('bits', ParseBits)]})
                        class_fields_list.append((BaseUnion, field_list))
                        field_list = []
            else:
                field_list.append(item)
                bits_count = bits_count + item[2]
                if bits_count == 32:
                    bits_count = 0
                    ParseBits = type("ParseBits", (ct.Structure,), {"_fields_" : field_list})
                    BaseUnion = type("BaseUnion", (ct.Union,), {"_fields_":[('value', ct.c_uint), ('bits', ParseBits)]})
                    class_fields_list.append((BaseUnion, field_list))
                    field_list = []
                
        if bits_count != 0:
            raise ParserError("Field bits error in struct.")
        
        return class_fields_list
    
if __name__ == "__main__":
    blind_parse = BlindParseMachsTtiTrace(r"D:\tti-trace-tool\workspace\ttitraceTool\traceFile\0x1252_MacHs_TTI_Trace_20150519_094839.txt")
            
            
            