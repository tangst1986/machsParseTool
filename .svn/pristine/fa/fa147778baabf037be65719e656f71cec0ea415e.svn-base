'''
Created on 2015/5/25

@author: m1tang
'''
import numpy as np
import matplotlib

matplotlib.use('WXAgg')
import matplotlib.pyplot as plt
import os



class draw_class(object):
    '''
    classdocs
    '''


    def __init__(self, pic_name, metric):
        '''
        Constructor
        '''
        self.pic_name = pic_name
        self.metric = metric
        
        BASE_PATH = os.path.abspath(os.path.join(os.getcwd(), ".."))
        PIC_PATH = BASE_PATH + '\\Picture\\'
        self.save_path = PIC_PATH
    
    def drawOneColumn(self, x_data_list, y_data_list, seq_no):
        x_ind = np.arange(len(x_data_list))
        x_column_width = 0.5  # bar's width
        
        fig, ax = plt.subplots()  # @UnusedVariable
        rects = ax.bar(x_ind, y_data_list, x_column_width, color = "r", yerr=x_data_list)
        
        x_tick_lables = [str(ele) for ele in x_data_list]
        ax.set_ylabel("througput(%s)" % self.metric)
        ax.set_xticks(x_ind + x_column_width/2)
        ax.set_xticklabels(x_tick_lables)
        
        for rect in rects:
            height = rect.get_height()
            ax.text(rect.get_x()+rect.get_width()/2., 1.05*height, height,
                    ha='center', va='bottom')
            
        plt.savefig('%s%s_%d' % (self.save_path, self.pic_name,seq_no), dpi=300)
        plt.show()

    def drawColumn(self, x_data_list, y_data_list):
        seq_no = 1
        index = 0
        num_data_in_one_pic = 10
         
        x_data_list_sub = []
        y_data_list_sub = []
         
        for ele in x_data_list:
            x_data_list_sub.append(ele)
            y_data_list_sub.append(y_data_list[index])
            index += 1
            if (index % num_data_in_one_pic == 0):
                self.drawOneColumn(x_data_list_sub, y_data_list_sub, seq_no)
                seq_no += 1
                x_data_list_sub = []
                y_data_list_sub = []
          
          
        if len(x_data_list_sub):
            self.drawOneColumn(x_data_list_sub, y_data_list_sub, seq_no)
        
if __name__ == '__main__':
    draw_obj =draw_class("test", "mb")
    
    x_data_list = [1, 2, 3, 4, 5, 6]
    y_data_list = [100,200, 1000, 2000, 10, 20]
    draw_obj.drawColumn(x_data_list, y_data_list)
        