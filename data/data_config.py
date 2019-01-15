# encoding=utf-8
class DataConfig:
    id='0'
    request_name = '1'
    url = '2'
    run = '3'
    request_method = '4'
    header = '5'
    case_depend = '6'
    data_depend = '7'
    field_depend = '8'
    data = '9'
    expect = '10'
    result = '11'

    #获取id
    def is_id(self):
        return DataConfig.id
    #获取用例名称
    def is_request_name(self):
        return DataConfig.request_name
    #获取url
    def is_url(self):
        return DataConfig.url
    #获取是否执行
    def is_run(self):
        return DataConfig.run
    #获取请求方式
    def is_request_method(self):
        return DataConfig.request_method
    #获取header
    def is_header(self):
        return DataConfig.header
    #获取依赖ID
    def is_case_depend(self):
        return DataConfig.case_depend
    #获取返回的依赖数据
    def is_data_depend(self):
        return DataConfig.data_depend
    #获取依赖数据所属字段
    def is_field_depend(self):
        return DataConfig.field_depend
    #获取请求数据
    def is_data(self):
        return DataConfig.data
    #获取预期结果
    def is_expect(self):
        return DataConfig.expect
    #获取实际结果
    def is_result(self):
        return DataConfig.result