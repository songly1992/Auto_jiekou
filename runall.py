# coding=utf-8
import unittest
import HTMLTestRunner
from config.config_set import case_path,report_path
# 将默认编码设置为utf-8
import sys
reload(sys)
sys.setdefaultencoding('utf-8')


rule="test*.py"
discover=unittest.defaultTestLoader.discover(start_dir=case_path,pattern=rule)
print (discover)

fp=file(report_path,'wb')
runner=HTMLTestRunner.HTMLTestRunner(stream=fp,
                                    title='接口自动化测试报告',
                                    description='接口测试报告')
runner.run(discover)