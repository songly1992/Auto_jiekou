# encoding=utf-8
from common.read_excel import ReadExcel
from common.base import Base
from common.getdata import GetData
from jsonpath_rw import jsonpath,parse
import json
class DepandentData():
    def __init__(self,case_id):
        self.case_id=case_id
        self.read_excel=ReadExcel()
        self.data=GetData()


    #通过case_id去获取该case_id的整行数据
    def get_case_line_data(self,row):
        rows_data=self.read_excel.get_row_values(row)
        return rows_data

    #执行依赖测试，获取结果
    def run_depandent(self):
        base=Base()
        row_num=self.read_excel.get_row_num(self.case_id)
        request_data=self.data.get_json_data(row_num)
        header=self.data.get_header(row_num)
        method=self.data.get_request_method(row_num)
        url=self.data.get_url(row_num)
        res=base.run_main(url,method,request_data,header)
        return json.loads(res)

    #根据依赖的key去获取执行依赖测试case的响应，然后返回
    def get_data_for_key(self,row):
        depend_data=self.data.get_depend_key(row) # 获取响应返回的字段
        response_data=self.run_depandent()# 获取依赖返回的响应数据
        json_exe=parse(depend_data)
        madle=json_exe.find(response_data)
        return [math.value for math in madle][0]

if __name__ == '__main__':
    # order = {
    #     "data": {
    #         "_input_charset": "utf-8",
    #         "body": "京东订单-1710141907182334",
    #         "it_b_pay": "1d",
    #         "notify_url": "http://order.imooc.com/pay/notifyalipay",
    #         "out_trade_no": "1710141907182334",
    #         "partner": "2088002966755334",
    #         "payment_type": "1",
    #         "seller_id": "yangyan01@tcl.com",
    #         "service": "mobile.securitypay.pay",
    #         "sign": "kZBV53KuiUf5HIrVLBCcBpWDg%2FnzO%2BtyEnBqgVYwwBtDU66Xk8VQUTbVOqDjrNymCupkVhlI%2BkFZq1jOr8C554KsZ7Gk7orC9dDbQlpr%2BaMmdjO30JBgjqjj4mmM%2Flphy9Xwr0Xrv46uSkDKdlQqLDdGAOP7YwOM2dSLyUQX%2Bo4%3D",
    #         "sign_type": "RSA",
    #         "string": "_input_charset=utf-8&body=京东订单-1710141907182334&it_b_pay=1d&notify_url=http://order.imooc.com/pay/notifyalipay&out_trade_no=1710141907182334&partner=2088002966755334&payment_type=1&seller_id=yangyan01@tcl.com&service=mobile.securitypay.pay&subject=京东订单-1710141907182334&total_fee=299&sign=kZBV53KuiUf5HIrVLBCcBpWDg%2FnzO%2BtyEnBqgVYwwBtDU66Xk8VQUTbVOqDjrNymCupkVhlI%2BkFZq1jOr8C554KsZ7Gk7orC9dDbQlpr%2BaMmdjO30JBgjqjj4mmM%2Flphy9Xwr0Xrv46uSkDKdlQqLDdGAOP7YwOM2dSLyUQX%2Bo4%3D&sign_type=RSA",
    #         "subject": "京东订单-1710141907182334",
    #         "total_fee": 299
    #         },
    #         "errorCode": 1000,
    #         "errorDesc": "成功",
    #         "status": 1,
    #         "timestamp": 1507979239100
    #     }
    # res = "data.out_trade_no"
    # # res = "errorDesc"
    # json_exe = parse(res)
    # madle = json_exe.find(order)
    # print [math.value for math in madle][0]

    r=DepandentData("test_002")
    t=r.run_depandent()
    print(t)