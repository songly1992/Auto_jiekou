#encoding=utf-8
import requests
import json

class Base():

    def post_main(self,url,data,header=None):
        '''
        post请求
        # post请求入参data是字典类型，直接是data=data，如果入参是json类型为json=data
        # 入参需要传入header为headers=header
        '''
        res=None
        if header != None:
            res=requests.post(url,data,headers=header)
        else:
            res=requests.post(url,data)
        print res.status_code
        return res.text

    def get_main(self,url,data,header=None):
        '''
        get请求
        # 如果url是https开头的 ，需要加verify = False
        # params添加查询参数
        '''
        res=None
        if header != None:
            res=requests.get(url,params=data,headers=header,verify=False)
        else:
            res=requests.get(url,params=data,verify=False)
        print res.status_code
        return res.text

    def run_main(self,url,method,data=None,header=None):
        '''
        请求的主要方法
        :param url:
        :param method:
        :param data:
        :param header:
        :return:
        '''
        res=None
        if method=='GET':
           res = self.get_main(url,data,header)
        else:
           res=self.post_main(url,data,header)
        return json.dumps(res,ensure_ascii=False,indent=2,sort_keys=True).encode("gbk","ignore")

    def is_contain(self,str1,str2):
        '''
        判断一个字符串是否在另一个字符串中
        :param str1:
        :param str2:
        :return:
        '''
        flag=None
        if isinstance(str1,unicode):
            str1=str1.encode("unicode-escape").encode("utf-8")
        if str1 in str2:
            flag = True
        else:
            flag = False
        return flag


if __name__=="__main__":
    url=r'http://127.0.0.1:8000/login'
    data={"data": "eee", "username":"name0", "mobile":"189978798"}
    url2 = r'http://127.0.0.1:8000/loginpost'
    data2 ={"username":"lilihahah",
            "password":"189978798"
            }
    # url=r'http://coding.imooc.com/class/ajaxsearchwords'
    # data={"callback":"searchKeys","_":"1547087518961"}
    header=None
    r=Base()
    print type(data)
    re1=r.run_main(url,"GET",data,header)
    print ("type%s"%type(re1))
    print re1
    re2 = r.run_main(url2,"POST",data2,header)
    print ("type%s"%type(re2))
    print re2