# encoding=utf-8
from common.base import Base
from common.getdata import GetData
from common.dependentdate import DepandentData
from common.send_email import SendEmail
from common.oparetion_header import OperationHeader
from common.read_json import ReadJson
import unittest
import json
from common.log import Log
log=Log()

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
               case_name=self.data.get_case_name(i)
               url=self.data.get_url(i)
               method=self.data.get_request_method(i)
               request_data=self.data.get_json_data(i)
               data=json.dumps(request_data)
               header=self.data.get_header(i)
               expect=self.data.get_expcet(i)
               depend_case=self.data.is_depend(i)
               depend_data = DepandentData(depend_case)
               log.info('------执行用例：%s'%case_name)
               log.info('inputdata> 参数:%s,预期结果:%s'%(data,expect))
               if depend_case != None:
                   # 获取的依赖响应数据
                   depend_response_data = depend_data.get_data_for_key(i)
                   # 获取依赖的key
                   depend_key = self.data.get_depend_field(i)
                   request_data[depend_key] = depend_response_data
               # self,url,method,data=None,header=None
               # res=self.base.run_main(url,method,request_data,header)
               if header == 'write':
                   res = self.base.run_main(url,method,request_data)
                   op_header = OperationHeader(res)
                   op_header.write_cookie()

               elif header == 'yes':
                   op_json = ReadJson()
                   cookie = op_json.read_cookie('apsid')
                   cookies = {
                       'apsid': cookie
                   }
                   res = self.base.run_main(url, method, request_data, cookies)
               else:
                   res = self.base.run_main(url, method, request_data)

               # print (type(res))
               if self.base.is_contain(expect,res):
                   self.data.write_result(i,"pass")
                   log.info('------用例测试通过,实际结果：%s'%res)
                   #统计通过的用例数
                   pass_count.append(1)

               else:
                   self.data.write_result(i,res)
                   log.info('----用例测试失败，返回结果：%s'%res)
                   #统计失败的用例数
                   fail_count.append(i)

        log.info('所有用例测试完成，成功数:%s,失败数：%s'%(len(pass_count),len(fail_count)))
        #发送邮件
        # self.send_email.send_main(pass_count,fail_count)
if __name__=="__main__":
    run=TestRun()
    print (run.test_on_run())
