# encoding=utf-8
import requests
import json
import operator
from common.log import Log
log=Log()
class Base():
    def __init__(self):
        self.log=log
    def post_main(self,url,data,header=None):
        '''
        post请求
        # post请求入参data是字典类型，直接是data=data，如果入参是json类型为json=data
        # 入参需要传入header为headers=header
        '''
        try:
            res=None
            if header != None:
                res=requests.post(url,data,headers=header,verify=False)
            else:
                res=requests.post(url,data,verify=False)
            print (res.status_code)
            return (res.text.encode('utf-8').decode("unicode_escape"))
            # return (res.content.decode('unicode_escape'))

        except Exception as e:
            log.info('post请求出错，出错原因:%s' % e)
            return {'code': 1, 'result': 'post请求出错，出错原因:%s' % e}

    def get_main(self,url,data,header=None):
        '''
        get请求
        # 如果url是https开头的 ，需要加verify = False
        # params添加查询参数
        '''
        try:
            if header != None:
                res=requests.get(url,params=data,headers=header,verify=False)
            else:
                res=requests.get(url,params=data,verify=False)
            print (res.status_code)
            return (res.text.encode('utf-8').decode("unicode_escape"))

        except Exception as e:
            log.info('get请求出错，出错原因:%s' % e)
            return {'code': 1, 'result': 'get请求出错，出错原因:%s' % e}

    def run_main(self,url,method,data=None,header=None):
        '''
        请求的主要方法
        :param url:
        :param method:
        :param data:
        :param header:
        :return:
        '''
        if method == 'GET':
           res = self.get_main(url,data,header)
        else:
           res = self.post_main(url,data,header)
        # return json.dumps(res,ensure_ascii=False,indent=2,sort_keys=True)
        return res

    def is_contain(self,str1,str2):
        '''
        判断一个字符串是否在另一个字符串中
        :param str1:
        :param str2:
        :return:
        '''
        flag=None
        if isinstance(str1,str):
            str1=str1.encode('utf-8').decode("unicode_escape")
        if str1 in str2:
            flag = True
        else:
            flag = False
        return flag
        # flag = None
        # if str1 in str2:
        #     flag = True
        # else:
        #     flag = False
        # return flag

    def is_equal_dict(self, dict_one, dict_two):
        '''
        判断两个字典是否相等
        '''
        if isinstance(dict_one, str):
            dict_one = json.loads(dict_one)
        if isinstance(dict_two, str):
            dict_two = json.loads(dict_two)
        # return cmp(dict_one, dict_two) python2中使用
        return operator.eq(dict_one, dict_two)  # pyhon3中使用


if __name__=="__main__":

    # url= r'http://127.0.0.1:8000/login'
    # data ={"username":"name",
    #         "password":"189978798"
    #         }
    url = r'http://coding.imooc.com/class/ajaxsearchwords'
    data={"callback":"searchKeys","_":"1547087518961"}
    # data=''
    header= ""
    r=Base()
    # print type(data)
    # print(type(data))
    re1=r.run_main(url,'POST',data,header)
    print ("type%s"%type(re1))
    print (re1)
    # re2 = r.run_main(url2,"POST",data2,header)
    # print ("type%s"%type(re2))
    # # print re2
    # str1='"status":10001'
    # str2="{\"status\":10001,\"msg\":\"\\u6210\\u529f\",\"data\":{\"userInfo\":{\"uid\":\"3001774\"},\"url\":[\"http:\\/\\/www.imooc.com\\/user\\/ssologin?token=QcKLCeiTCGvo_qnpXVtC-NLk7fChyA7U7D7xf_vo8fyBGVjVbp-LFY0tIXgOSAfeJ3wGyX-WvPm87sXbW5l-qWgVIKZsg8GOLaxpYde9SH_ZNx0PLuDTZ6364dODfYhWRq8OM-29gHLtpK3xLiW_dmDrRwbFDRRlrUnQF-P9ph7z2LfQ-lzX4nVO_mpTUH1zxT1ejQ7G84LsebDE6c2Lbd9zAksJPg66C8LJRMYEOjGsPC_2rvbTkO4jWtepDvwAd_wcQTceQCiW0R2FZhAKPrac_fl-1brN-0EdQvm3OlYJ5L2Uy\",\"http:\\/\\/coding.imooc.com\\/user\\/ssologin?token=_aW2KYa911DR6c2-EkwLUhCOVPvubcH8M1o-20AiKMVBc5xZYxQuk-r91uCVn5ijlr8c1mtP9sl4f0z8pM6CZZw68RlbPjwwXI-6sadfzuKzxTsWFfBaJak8xq1zlXJPzrVcAHaq_Y9RooPKhroQ2RnEIK4VEFL0_iJK15nOR4S0LkogfxhejWnN-_hqXw9fXp8yMcWPG_4mquH2xprnhlX4Jb-n-2xE4X3GImAAZqbsGRXfjwVdqWARiJyYVCNGO_0NNwh5gGrcDy2jHi5FMsrrFczjvfvp-wrhsRCOBA\"]}}"
    # a=r.is_contain(str1,str2)
    # print (type(str1))
    # print (str1)
    # print (type(str2))
    # print (str2)
    # print (a)