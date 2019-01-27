# encoding=utf-8
from common.read_excel import ReadExcel
from common.read_json import ReadJson
from data.data_config import DataConfig
from common.connect_db import OperationMysql
from common.base import Base



class GetData():
    def __init__(self):
        self.read_excel=ReadExcel()
        self.dataconfig=DataConfig()

    #获取excel行数，case个数
    def get_case_lines(self):
        return self.read_excel.get_lines()

    #获取是否执行
    def get_run(self,row):
        res=None
        col=int(self.dataconfig.is_run())
        run=self.read_excel.get_cell_value(row,col)
        if run == "yes":
            res=True
        else:
            res=False
        return res

    #是否携带header
    def get_header(self,row):
        col=int(self.dataconfig.is_header())
        header=self.read_excel.get_cell_value(row,col)
        if header !="":
            return header
        else:
            return None

    #获取用例名称
    def get_case_name(self,row):
        col=int(self.dataconfig.is_request_name())
        case_name=self.read_excel.get_cell_value(row,col)
        return case_name

    #获取请求方式
    def get_request_method(self,row):
        col=int(self.dataconfig.is_request_method())
        request_method=self.read_excel.get_cell_value(row,col)
        return request_method

    #获取url
    def get_url(self,row):
        col=int(self.dataconfig.is_url())
        url=self.read_excel.get_cell_value(row,col)
        return url

    #获取请求数据
    def get_data(self,row):
        col=int(self.dataconfig.is_data())
        data=self.read_excel.get_cell_value(row,col)
        if data=="":
            return None
        return data

    #通过获取关键字拿到data数据
    def get_json_data(self,row):
        read_json=ReadJson()
        data=read_json.get_jsondata(self.get_data(row))
        return data

    #获取预期结果
    def get_expcet(self,row):
        col=int(self.dataconfig.is_expect())
        expect=self.read_excel.get_cell_value(row,col)
        if expect=="":
            return None
        return expect

    # 通过sql获取预期结果
    def get_expcet_data_for_mysql(self, row):
        op_mysql = OperationMysql()
        sql = self.get_expcet(row)
        res = op_mysql.search_one(sql)
        return res.decode('unicode-escape')

    #写入实际结果
    def write_result(self,row,value):
        col=int(self.dataconfig.is_result())
        self.read_excel.write_value(row,col,value)


    #获取依赖的数据的key
    def get_depend_key(self,row):
        col=int(self.dataconfig.is_data_depend())
        depend_key=self.read_excel.get_cell_value(row,col)
        if depend_key =="":
            return None
        else:
            return depend_key

    #判断是否有case依赖
    def is_depend(self,row):
        col=int(self.dataconfig.is_field_depend())
        depend_case_id=self.read_excel.get_cell_value(row,col)
        if depend_case_id=="":
            return None
        else:
            return depend_case_id

    #获取数据依赖字段
    def get_depend_field(self,row):
        col=int(self.dataconfig.is_field_depend())
        data=self.read_excel.get_cell_value(row,col)
        if data=="":
            return None
        else:
            return data







if __name__=="__main__":
    getdata=GetData()
    b=Base()
    # rows_count =getdata.get_case_lines()
    # for i in range(1, rows_count):
    #     url=getdata.get_url(i)
    #     run = getdata.get_run(i)
    #     header = getdata.get_header(i)
    #     method = getdata.get_request_method(i)
    #     data = getdata.get_data(i)
    #     json_data = getdata.get_json_data(i)
    #     print (i)
    #     print (url)
    #     print (run)
    #     print (",method:" + method)
    #     print (data)
    #     print (json_data)
    #     print type(json_data)
    #     res = b.run_main(url, method, json_data,header)
    #     print (res)
    y=getdata.get_expcet(1)
    print (y)
    t=getdata.get_expcet_data_for_mysql(1)
    print (t)



