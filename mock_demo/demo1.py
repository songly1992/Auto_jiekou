#encoding=utf-8
from mock import mock
#模拟mock封装
def mock_demo1(mock_method,request_data,url,method,response_data):
    mock_method=mock.Mock(return_value=response_data)
    res=mock_method(url,method,response_data)
    return res