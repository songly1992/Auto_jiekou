#encoding=utf-8
from common.base import Base
from common.getdata import GetData
from common.dependentdate import DepandentData
from  common.send_email import SendEmail
import unittest

class TestRun(unittest.TestCase):

    #程序执行
    def test_on_run(self):
        self.base= Base()
        self.data = GetData()
        self.send_email=SendEmail()
        pass_count = []
        fail_count = []
        rows_count=self.data.get_case_lines()
        for i in range(1,rows_count):
            is_run = self.data.get_run(i)
            if is_run:
               url=self.data.get_url(i)
               method=self.data.get_request_method(i)
               request_data=self.data.get_json_data(i)
               header=self.data.get_header(i)
               expect=self.data.get_expcet(i)
               depend_case=self.data.is_depend(i)
               depend_data = DepandentData(depend_case)
               if depend_case != None:
                   # 获取的依赖响应数据
                   depend_response_data = depend_data.get_data_for_key(i)
                   # 获取依赖的key
                   depend_key = self.data.get_depend_field(i)
                   request_data[depend_key] = depend_response_data
               # self,url,method,data=None,header=None
               res=self.base.run_main(url,method,request_data,header)
               print (res)


               if self.base.is_contain(expect,res):
                   self.data.write_result(i,"pass")
                   print "测试通过"
                   #统计通过的用例数
                   pass_count.append(1)

               else:
                   self.data.write_result(i,res)
                   print "测试失败"
                   #统计失败的用例数
                   fail_count.append(i)
        print len(pass_count)
        print len(fail_count)
        self.send_email.send_main(pass_count,fail_count)
if __name__=="__main__":
    run=TestRun()
    print run.test_on_run()
