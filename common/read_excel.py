# encoding=utf-8
import xlrd
from xlutils.copy import copy
from config.config_set import Excel_path,sheet_id
class ReadExcel():
    def __init__(self):
        if Excel_path:
            self.file_name=Excel_path
            self.sheet_id=sheet_id
        else:
            self.file_name='F:\\python_Jiekou\\Auto\\data\\casedata.xls'
            self.sheet_id=0
        self.data=self.get_data()

    # 获取sheets的内容
    def get_data(self):
        data=xlrd.open_workbook(self.file_name)
        tables=data.sheets()[self.sheet_id]
        return tables

    #获取单元格的行数
    def get_lines(self):
        tables=self.data
        return tables.nrows

    #获取某一个单元格的内容
    def get_cell_value(self,row,col):
        return self.data.cell_value(row,col)

    # 写入数据
    def write_value(self, row, col, value):
        '''写入excel数据row,col,value'''
        read_data = xlrd.open_workbook(Excel_path)
        write_data = copy(read_data)
        sheet_data = write_data.get_sheet(sheet_id)
        sheet_data.write(row, col, value)
        write_data.save(Excel_path)


    # 根据行号，找到该行的内容
    def get_row_values(self, row):
        tables = self.data
        row_data = tables.row_values(row)
        return row_data

    # 获取某一列的内容
    def get_col_valuse(self, col_id=None):
        if col_id != None:
            col = self.data.col_values(col_id)
        else:
            col = self.data.col_values(0)
        return col

    # 根据对应的caseid找到对应行的行号
    def get_row_num(self, case_id):
            num = 0
            cols_data = self.get_col_valuse()
            for col_data in cols_data:
                print (col_data)
                if case_id in col_data:
                    return num
                else:
                   num = num + 1

    #根据对应的caseid找到对应行的内容
    def get_row_data(self,case_id):
        row_num=self.get_row_num(case_id)
        rows_data=self.get_row_values(row_num)
        return rows_data

if __name__=="__main__":
    read1 = ReadExcel()
    print (read1.get_cell_value(2,3))
    # read1.write_value(2,10,"fail")
    # row=read1.get_row_values(1)
    # print row
    # col=read1.get_col_valuse(0)
    # print col
    row_num=read1.get_row_num("test_001")
    print (row_num)
    row_data=read1.get_row_data("test_001")
    print (row_data)