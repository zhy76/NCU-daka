import requests
from io import StringIO
import pytz
import datetime
import json

class Daka:
    def __init__(self):
        self.url ='http://jc.ncu.edu.cn/gate/student/signIn'
        self.userId = *
        self.token =*
        self.In = StringIO()
        self.In.write('打卡日志\n')
        self.tz = pytz.timezone('Asia/Shanghai')
        self.nowtime = datetime.datetime.now(self.tz).strftime("%Y-%m-%d %H:%M:%S")
        self.In.write('运行日期：'+self.nowtime+'\n')
    def sendmessages(self):
        headers = {
            'Host': 'jc.ncu.edu.cn',
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/88.0.4324.182 Safari/537.36 Edg/88.0.705.81',
            'token': self.token
        }
        data = {
            'addressCity': "南昌市",
            'addressInfo': "南昌大学前湖校区",
            'addressProvince': "江西省",
            'closeHb': "否",
            'closeIll': "否",
            'healthDetail': "无异常",
            'healthStatus': "无异常",
            'inChina': "是",
            'isGraduate': "否",
            'isIll': "否",
            'isIsolate': "否",
            'isIsolation': "否",
            'isolatePlace': "无",
            'isolationPlace': "无",
            'temperature': 0,
            'temperatureStatus': "正常",
            'userId': self.userId
        }
        req = requests.post(self.url, data=data, headers=headers)
        result = req.json()
        code = result["code"]
        message = result["message"]
        self.In.write('姓名：学号:'+str(self.userId)+'\n')
        self.In.write('code：')
        self.In.write(code + '\n')
        self.In.write('打卡状态：')
        self.In.write(message)

    def return_(self):
        return self.In.getvalue()

class Weisend:
    def __init__(self,):
        self.corpid = *
        self.agentid = *
        self.secret = *
        self.touser = *
    def get_access_token(self):
        url = " https://qyapi.weixin.qq.com/cgi-bin/gettoken?corpid=" + self.corpid + "&corpsecret=" + self.secret
        req = requests.get(url=url)
        self.token = json.loads(req.text)["access_token"]
    def send_new(self):
        url = "https://qyapi.weixin.qq.com/cgi-bin/message/send?access_token=" + self.token
        req = requests.post(url=url, data=json.dumps(self.date))
        if json.loads(req.text)["errcode"] == 0:
            print("成功！")
        else:
            print("失败！")
    def date_(self,news):
        date = {
            "touser": self.touser,
            "msgtype": "text",
            "agentid": self.agentid,
            "text": {
                "content": news
            }
        }
        self.date = date
    def send_messages(self,news):
        daka = Weisend()
        daka.date_(news)
        daka.get_access_token()
        daka.send_new()
daka = Daka()
daka.sendmessages()
Weisend().send_messages('{}'.format(daka.return_()))
