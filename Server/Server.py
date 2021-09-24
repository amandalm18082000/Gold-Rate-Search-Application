#SOCKET
from socket import AF_INET, socket, SOCK_STREAM
from threading import Thread
from socket import *
import threading
import socket
from threading import Thread

#GUI
from tkinter import messagebox 
from tkinter import *
from tkinter import *
from tkinter import font
import tkinter as tk
from tkinter import messagebox

#HTTP
import requests

#from bs4 import BeautifulSoup
#HTTPs
import codecs
import json
#TIME UPDATE FILE
import schedule
import time
#DUMPLE DICTIONARY TO SEEN FOR CLIENT
import pickle
#TODAY
from datetime import date

#GLOBALS
today = date.today()
# YYmmDD
todayis = today.strftime("%Y%m%d")

#import pandas as pd

def writeDataForDay(day):
    #import xlsxwriter
    def api():
        url = 'https://tygia.com/json.php?ran=0&rate=0&gold=1&bank=VIETCOM&date=' + day
        # Search GitHub's repositories for requests
        resp = requests.get(url)
        #print(resp.content.decode('utf-8'))
        resp.encoding='utf-8-sig'
        content = resp.text.encode().decode('utf-8-sig')
        return json.loads(content)
    linkjson = day + ".json"
    a = api()
    with open(linkjson, 'w') as f:
        json.dump(a, f)
    with open(linkjson, 'r') as f:
        sed = json.load(f)
    b = sed["golds"]
    #print(type(b[0])) => dict
    c = b[0]
    d = c['value']
    with open(linkjson, 'w') as f:
        json.dump(d, f, indent = 4)

def writeData():
    #import xlsxwriter
    def api():
        url = 'https://tygia.com/json.php?ran=0&rate=0&gold=1&bank=VIETCOM&date=now'
        # Search GitHub's repositories for requests
        resp = requests.get(url)
        #print(resp.content.decode('utf-8'))
        resp.encoding='utf-8-sig'
        content = resp.text.encode().decode('utf-8-sig')
        return json.loads(content)
 
    a = api()
    with open('data.json', 'w') as f:
        json.dump(a, f)
    with open('data.json', 'r') as f:
        sed = json.load(f)
    b = sed["golds"]
    #print(type(b[0])) => dict
    c = b[0]
    d = c['value']
    with open('data.json', 'w') as f:
        json.dump(d, f, indent = 4)

def writeType(client, filename, typeGold):
    with open(filename, 'r') as f:
        seed = json.load(f)
    lists = []
    Gold = {}
    for types in seed:
        if (typeGold == types['type']):
            Gold = types.copy()
            lists.append(Gold)
    client.sendall(bytes(str(len(lists)),"utf-8"))
    data = pickle.dumps(lists)
    client.sendall(data)

def writeCompany(client, filename, companyGold):
    with open(filename, 'r') as f:
        seed = json.load(f)
    lists = []
    Gold = {}
    for companies in seed:
        if (companyGold == companies['company']):
            Gold = companies.copy()
            lists.append(Gold)
    client.sendall(bytes(str(len(lists)),"utf-8"))
    data = pickle.dumps(lists)
    client.sendall(data)

def writeBrand(client, filename, brandGold):
    with open(filename, 'r') as f:
        seed = json.load(f)
    lists = []
    Gold = {}
    for world in seed:
        if (brandGold == world['brand']):
            Gold = world.copy()
            lists.append(Gold)
    client.sendall(bytes(str(len(lists)),"utf-8"))
    data = pickle.dumps(lists)
    client.sendall(data)

def writeDay(client, filename, dayUpdate):
    with open(filename, 'r') as f:
        seed = json.load(f)
    lists = []
    Gold = {}
    for city in seed:
        Gold = city.copy()
        lists.append(Gold)
    client.sendall(bytes(str(len(lists)),"utf-8"))
    data = pickle.dumps(lists)
    client.sendall(data)

def readRequest (client):
    request =""
    client.settimeout(60)
    try:
        request = client.recv(1024).decode('utf-8')
        # recieve request from client
    except timeout:
        print("No reveive data from client")
        client.close()
    finally:
        return request


def checkSignIn (filename,user):
    f = open(filename, mode = 'r', encoding = 'utf-8')
    with open(filename, 'r') as f:
        for s_line in f:
            a = s_line.strip()
            if a == user:
                return True
    f.close()
    return False

def checkSignUp(filename, user):
    username = user.split('&')
    print(username[0])
    f = open(filename, mode = 'r', encoding = 'utf-8')
    with open(filename, 'r') as f:
        for s_line in f:
            a = s_line.strip()
            if username[0] in a:
                return True
    f.close()
    return False
 #ACCEPT_THREAD = Thread(target = waitingConnection())
# Choose a port that is free

#def broadcast(msg, prefix=""):  
#    for sock in clients:
#        sock.send(bytes(prefix, "utf-8") + msg)

def checkYear(strs):
    year = int(strs)
    if (((year % 4 == 0) and (year % 100 != 0)) or (year % 400 == 0)):
        return True
    return False

def checkMonth(strs):
    month = int(strs)
    if (month == 2):
        return -1
    elif (month == 1) or (month == 3) or (month == 5) or (month == 7) or (month == 8) or (month == 10) or (month == 12):
        return 1
    return 0

def takeRequest (client):
    while True:
        client.settimeout(120)
        try:
            Request=""
            Request = readRequest(client)
            print(Request)
            if Request == "":
                client.close()
                break
            print("--> Got a request\n")
            if "InUsername" in Request:
                user = Request.replace('In', '')
                if checkSignIn('user.txt', user) == True:
                    client.sendall(bytes("usernamecorrect", "utf-8"))
                    print("usernamecorrect")
                else:
                    client.sendall(bytes("usernameincorrect", "utf-8"))  
                
            elif "UpUsername" in Request:
                user = Request.replace('Up', '')
                if checkSignUp('user.txt', user) == True:
                    client.sendall(bytes("nosignupsuccess", 'utf-8'))
                else:
                    f = open('user.txt', mode = 'a+', encoding = 'utf-8')
                    with open('user.txt', mode='a+') as f:
                        f.write(user)
                        f.write('\n')
                    f.close()
                    print ("success")
                    client.send(bytes("signupsuccess", "utf-8"))
            elif "Type" == Request:
                client.sendall(bytes("OK", 'utf-8'))
                typeGold = client.recv(1024).decode('utf-8')
                writeType(client, 'data.json', typeGold)
            elif "Company" == Request:
                client.sendall(bytes("OK", 'utf-8'))
                companyGold = client.recv(1024).decode('utf-8')
                writeCompany(client, 'data.json', companyGold)
            elif "Brands" == Request:
                client.sendall(bytes("OK", 'utf-8'))
                brandGold = client.recv(1024).decode('utf-8')
                writeBrand(client, 'data.json', brandGold)
            elif "Day" == Request:
                client.sendall(bytes("OK", 'utf-8'))
                dayUpdate = client.recv(1024).decode('utf-8')
                new_search = dayUpdate 
                new_year = new_search[0:4]
                print(new_year)
                new_month = new_search[4:6]
                print(new_month)
                new_day = new_search[6:8]
                print(new_day)
                if dayUpdate > todayis:
                    filename = todayis + ".json"
                    writeDataForDay(todayis)
                    writeDay(client, filename, todayis)
                elif(new_month >= "01" and new_month <= "12"):
                    if (checkYear(new_year) == True and new_month == "02" and new_day >= "01" and new_day <= "29"):
                        filename = dayUpdate + ".json"
                        writeDataForDay(dayUpdate)
                        writeDay(client, filename, dayUpdate)
                    elif (checkYear(new_year) == False and new_month == "02" and new_day >= "01" and new_day <= "28"):
                        filename = dayUpdate + ".json"
                        writeDataForDay(dayUpdate)
                        writeDay(client, filename, dayUpdate)
                    elif (checkMonth(new_month) == 1 and new_day >= "01" and new_day <= "31"):
                        filename = dayUpdate + ".json"
                        writeDataForDay(dayUpdate)
                        writeDay(client, filename, dayUpdate)
                    elif (checkMonth(new_month) == 0 and new_day >= "01" and new_day <= "30"):
                        filename = dayUpdate + ".json"
                        writeDataForDay(dayUpdate)
                        writeDay(client, filename, dayUpdate)
                    else:
                        filename = todayis + ".json"
                        writeDataForDay(todayis)
                        writeDay(client, filename, todayis)
                else:
                    filename = todayis + ".json"
                    writeDataForDay(todayis)
                    writeDay(client, filename, todayis)
            elif "Exit" == Request:
            #client.sendall(bytes("Da tat may", "utf-8"))
                print("client yêu cầu rời khỏi dịch vụ")
                client.close()
            schedule.run_pending()
        except timeout:
            print("Không nhận được thông tin từ client")
            client.close()
            break

       
def control (SERVER):
    window = Tk()
    window.tat = Button (text = "Ngắt toàn bộ kết nối đến client")
    window.tat.pack()
    window.mainloop()

def waitingConnection():
    #SERVER.listen()
    print("Waiting for client")
    lists = {}
    while True:
        client, Address = SERVER.accept()
        addresses[client] = Address
        print("client", Address, "connected!")
        
        threading.Thread(target = takeRequest, args = (client,)).start()
        #takeRequest(client)
def broadcast():
    for sock in clients:
            #print(sock)
        sock.sendall(bytes("Exit", "utf-8"))
        print("Ngắt kết nôi với client")
        sock.close()
    #except:
    #    SERVER.close()


def action():
    try:
        #to
        print("server is working on ", (socket.gethostbyname(socket.gethostname())))
        SERVER.listen()
        ACCEPT_THREAD = threading.Thread(target = waitingConnection())
        ACCEPT_THREAD.start()
        ACCEPT_THREAD.join()
    except:
        print("Error occured!")
        SERVER.close()
    #finally:
        #SERVER.close()
def GUIcontrol():
    top = Tk()
    top.title("Clients")
    messages_frame = Frame(top)
    my_msg = StringVar() 
    my_msg.set("Update")
    scrollbar = Scrollbar(messages_frame)  
    msg_list = Listbox(messages_frame, height=15, width=50, yscrollcommand=scrollbar.set)
    scrollbar.pack(side=RIGHT, fill=Y)
    msg_list.pack(side=LEFT, fill=BOTH)
    msg_list.pack()
    messages_frame.pack()

    def update():
        msg_list.delete(0,'end')
        for sock in addresses:
            msg_list.insert(END, addresses[sock])
            print(addresses[sock])

    send_button = Button(top, text="Cập nhật",bg = "#FFFACD", width =40, font=('Helvetica 10 bold'), bd = 5, activebackground='#F4A460', command= update)
    send_button.pack()
    msg_list.insert("123")
    nut = Button(top, text = "Đóng Client",bg = "#EEA2AD", width =40, font=('Helvetica 10 bold'), bd = 5, activebackground='#F4A460', command = lambda: broadcast())
    nut.pack()
    top.mainloop() 

def divideAction(top):
    top.destroy()#ĐỂ cho mở server bị mất đi
    threading.Thread(target = action, args = ()).start()
    GUIcontrol()


def main():
    writeData()
    top = Tk()
    top.title("Server")
    top.geometry("200x200+30+30")
    top.button = Button(top, text ="Mở Server",font=('Helvetica Bold', 11), command = lambda: divideAction(top), bd = 10, activebackground='#F4A460' )
    top.button.pack(fill=BOTH, pady=10, padx=10, expand=True)
    top.mainloop()


clients = {}
addresses = {}
SERVER =socket.socket(socket.AF_INET,socket.SOCK_STREAM)
SERVER.bind((socket.gethostbyname(socket.gethostname()), 5656))
schedule.every(30).minutes.do(writeData)

if __name__ == "__main__":
    main()
    #control(SERVER)
   