import os
import sys
import urllib.request
import json
from tkinter.ttk import *
import tkinter as tk
window = tk.Tk()
window.title("papago")
window.geometry("640x400+450+200")
window.resizable(True,True)
combo = Combobox(window)
combo2 = Combobox(window)
combo['values'] = ("일본어","한국어","영어")
combo2['values'] = ("일본어","한국어","영어")
combo.config(state="readonly")
combo2.config(state="readonly")
combo.set("언어선택")
combo2.set("언어선택")
combo.pack()
combo2.pack()
input_text = Entry(window, width=30)
input_text.pack()
def translator(a,b,c):
    #Massage = str(input("변역할 문자열을 입력해 주세요"))
    client_id = "HtRq75QBgv_Qw44yTZQQ" # 개발자센터에서 발급받은 Client ID 값
    client_secret = "Z7wU_x7szl" # 개발자센터에서 발급받은 Client Secret 값
    encText = urllib.parse.quote(c)
    #data = f"source=ko&target=en&text=" + encText
    data = f"source={a}&target={b}&text=" + encText
    url = "https://openapi.naver.com/v1/papago/n2mt"
    request = urllib.request.Request(url)
    request.add_header("X-Naver-Client-Id",client_id)
    request.add_header("X-Naver-Client-Secret",client_secret)
    response = urllib.request.urlopen(request, data=data.encode("utf-8"))
    rescode = response.getcode()
    if(rescode==200):
        response_body = response.read()
        response_body = json.loads(response_body.decode('utf-8'))
        response_body = response_body.get("message")
        response_body = response_body.get("result")
        print("translatedText = {},".format(response_body.get("translatedText")))
        result = response_body.get("translatedText")
    else:
        print("Error Code:" + rescode)
    return result_show(result)

def bt_press():
    a = combo.get()
    b = combo2.get()
    c = input_text.get()
    if(a == '일본어'):
        a = "ja"
    elif(a == "한국어"):
        a = "ko"
    elif(a == "영어"):
        a = "en"
    if(b == '일본어'):
        b = "ja"
    elif(b == "한국어"):
        b = "ko"
    elif(b == "영어"):
        b = "en"
    
    return translator(a,b,c)

def result_show(result):
    text.insert(0,result)

btn = tk.Button(window,text="변역하기",width= 50,height= 2, bg="gray",font=(30), command= bt_press).pack()
text = Entry(window, width=30).pack()

window.mainloop()