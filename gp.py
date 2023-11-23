
import json
from unittest import expectedFailure


def know(a):  # 获取股票数据
    import requests
    # if 'sz' in a or 'sh' in a:
    gudaima = a  # "sz000001"
    headers = {'referer': 'http://finance.sina.com.cn'}
    resp = requests.get('http://hq.sinajs.cn/list=' +
                        gudaima, headers=headers, timeout=6)
    data = resp.text
    return data
    # else:

    '''TICKER_API_URL = 'https://api.coinmarketcap.com/v1/ticker/'

        def get_latest_crypto_price(crypto):

            response = requests.get(TICKER_API_URL+crypto)
            response_json = response.json()

            return float(response_json[0]['price_usd'])

        crypto = a
        price = get_latest_crypto_price(crypto)
        return price'''

    # print(data)
    '''
    var hq_str_sz000001="平安银行,17.450,17.330,17.350,17.560,17.210,17.350,17.360,148168295,2575115124.690,77830,17.350,69600,17.340,336500,17.330,321500,17.320,208200,17.310,370500,17.360,595600,17.370,497478,17.380,537000,17.390,815540,17.400,2022-01-21,15:00:03,00";

    输出内容含义，下面为各个数据的含义：

    0：”平安银行”，股票名字；
    1：”27.55″，今日开盘价；
    2：”27.25″，昨日收盘价；
    3：”26.91″，当前价格；
    4：”27.55″，今日最高价；
    5：”26.20″，今日最低价；
    6：”26.91″，竞买价，即“买一”报价；
    7：”26.92″，竞卖价，即“卖一”报价；
    8：”22114263″，成交的股票数，由于股票交易以一百股为基本单位，所以在使用时，通常把该值除以一百；
    9：”589824680″，成交金额，单位为“元”，为了一目了然，通常以“万元”为成交金额的单位，所以通常把该值除以一万；
    10：”4695″，“买一”申请4695股，即47手；
    11：”26.91″，“买一”报价；
    12：”57590″，“买二”
    13：”26.90″，“买二”
    14：”14700″，“买三”
    15：”26.89″，“买三”
    16：”14300″，“买四”
    17：”26.88″，“买四”
    18：”15100″，“买五”
    19：”26.87″，“买五”
    20：”3100″，“卖一”申报3100股，即31手；
    21：”26.92″，“卖一”报价
    (22, 23), (24, 25), (26,27), (28, 29)分别为“卖二”至“卖四的情况”
    30：”2008-01-11″，日期；
    31：”15:05:32″，时间；
    ————————————————
    版权声明：本文为CSDN博主「程序化交易」的原创文章，遵循CC 4.0 BY-SA版权协议，转载请附上原文出处链接及本声明。
    原文链接：https://blog.csdn.net/meiaoxue1234/article/details/122648757
    '''


'''def timenow():
    global tsw
    import time
    from datetime import datetime
    import pytz
    t = datetime.fromtimestamp(int(time.time()),pytz.timezone('Asia/Shanghai')).strftime('%H:%M')
    tz=t.split(':')
    ta=tb=tc=td=te=tf=0
    if int(tz[0])>=9 :ta=1 
    if int(tz[0])<11: tb=1
    if int(tz[0])<15: tc=1
    if int(tz[0])>13: td=1
    if int(tz[0])==9 and int(tz[1])>30:te=1
    if int(tz[0])==11 and int(tz[1])<30:tf=1
    if ta==tb==1 or tc==td==1 or te==tf==1:
        times= True
    else:
        times= False
        if t == '9:30' and tsw == False:
        send_msg({'msg_type':'group','number':'759734002','msg':'早盘开始'})
        tsw=True
        
    if t == '11:30' and tsw == False:
        send_msg({'msg_type':'group','number':'759734002','msg':'早盘结束'})
        tsw=True
    if t == '13:00' and tsw == False:
        send_msg({'msg_type':'group','number':'759734002','msg':'午盘开始'})
        tsw=True
    if t == '15:00' and tsw == False:
        send_msg({'msg_type':'group','number':'759734002','msg':'午盘结束'})
        tsw=True
    return times'''


'''def saver(n):
    with open('maintime.json', 'w') as f:
        json.dump(n, f)'''


def liangbi(name1, n2):

    n5 = ''

    try:
        with open('liangbi.json', 'r')as TxtFile:
            name = json.load(TxtFile)
    except Exception as e:
        print(e)
        name = {}
        with open('liangbi.json', 'w') as f:
            json.dump(name, f)
    try:
        n3 = float(name[n2])  # 上次
    except:
        name[n2] = name1
        with open('liangbi.json', 'w') as f:
            json.dump(name, f)
    name1 = float(name1)  # 现在
    n5 = name1/n3
    if name1/n3 > 10:
        n5 = str(n5) + '十倍'

    name[n2] = name1
    with open('liangbi.json', 'w') as f:
        json.dump(name, f)

    return n5


def gpmain(a):

    try:
        with open('name.json', 'r')as TxtFile:
            name = json.load(TxtFile)
    except:
        name = []
        with open('name.json', 'w') as f:
            json.dump(name, f)

    for n1 in name:
        #a += know(n)
        # print(know(n))
        try:
            n = n1.replace("\n", "")
            n2 = (know(n).split('=')[1].split(','))  # data
            n4 = liangbi(n2[9], n)

            # a+=1
            a += str(n2[0]) + \
                str(n2[3]) + ',,,' +\
                str(n4)+'\n'
            print(a)
        except Exception as e:
            print(e)
            continue
        # print(all)
    with open('data.json', 'w') as f:
        json.dump(a, f)
# gpmain('')
