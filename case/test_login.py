#encoding=utf-8

import unittest
import json
from common.base import Base
from mock import mock
from mock_demo.demo1 import mock_demo1

class LoginCase(unittest.TestCase):


     # def test_001(self):
     #    url = r'http://127.0.0.1:8000/login'
     #    data = {"data": "eee", "username": "name0", "mobile": "189978798"}
     #    self.r = Base()
     #    res = self.r.run_main(url, "GET", data)
     #    run= json.loads(res)#将json格式转换为字典
     #    self.assertEqual(run['data'],'eee',"测试失败")

     def test_002(self):
        url = r'http://127.0.0.1:8000/login'
        request_data = {"data": "eee", "username": "name0", "mobile": "189978798"}
        response_data={"code":"200","data": "eee", "username": "name0", "mobile": "189978798"}
        self.r = Base()
        # res = self.r.run_main(url, "GET", data)
        res=mock_demo1(self.r.run_main,request_data,url,'GET',response_data)
        # run= json.loads(res)#将json格式转换为字典
        print res
        self.assertEqual(res['data'],'eee',"测试失败")

if __name__=="__main__":
    unittest.main()