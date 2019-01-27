# encoding=utf-8
import json
from config.config_set import json_path,cookie_path

class ReadJson():

    # def __init__(self):
    #     if json_path:
    #           self.file_name=json_path
    #     else:
    #         self.file_name='F:\\python_Jiekou\\Auto\\data\\casejson.json'
    #     self.data=self.read_data()

    # 读取json文件
    def read_data(self,file_name):
        with open(file_name) as fp:
            data=json.load(fp)
            return data

    # 根据关键字获取数据
    def get_jsondata(self,id,):
        self.data = self.read_data(json_path)
        return self.data[id]

    #写json
    def write_jsondata(self,data):
        self.cookis_path = cookie_path
        with open(self.cookis_path,'w') as fp:
            fp.write(json.dumps(data))

    #获取cookie
    def read_cookie(self,id):
        self.data = self.read_data(cookie_path)
        return self.data[id]

if __name__=="__main__":
    read=ReadJson()
    r=read.get_jsondata("loginpost")
    print (type(r))
    print (r)


