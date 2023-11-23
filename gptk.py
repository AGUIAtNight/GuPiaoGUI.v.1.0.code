#!/usr/bin/python3
# -*- coding: utf-8 -*-
 
import threading
import time
import tkinter

from ttk import ttk1


class section:
    def onPaste(self):
        #print("显示AI机器人一天的工作")
 
        ''' def onCopy(self):
            print("如果要现在开始工作，就点开始，否则会根据日常的安排工作")
            ttk1()'''

    def create(self):
        top = tkinter.Toplevel()
        top.title('Python')

        v1 = tkinter.StringVar()
        e1 = tkinter.Text(top,textvariable=v1,width=10)
        e1.grid(row=1,column=0,padx=1,pady=1)

        tkinter.Button(top, text='完成').grid(row=1,column=1,padx=1,pady=1)
    '''————————————————
    版权声明：本文为CSDN博主「Popstar_」的原创文章，遵循CC 4.0 BY-SA版权协议，转载请附上原文出处链接及本声明。
    原文链接：https://blog.csdn.net/qq_35516165/article/details/81153535
    ''' 
    #def onCut(self):
        #print("学习新的工作技术，只要教过AI一次，就会了，以后的工作都可以交给他")
 
 
 
def move(event):
    global x,y,root
    new_x = (event.x-x)+root.winfo_x()
    new_y = (event.y-y)+root.winfo_y()
    s = "300x300+" + str(new_x)+"+" + str(new_y)
    root.geometry(s)
    '''#print("当把我放到左上角200*200的区域时我会走人的,当前是x:%s,y:%s"%(new_x,new_y))
    if new_x<50 and new_y<50:
        exit()'''
    
def button_1(event):
    global x,y
    x,y = event.x,event.y
    ##print("event.x, event.y = ",event.x,event.y)
'右键菜单设置'
def button_3(event):
    global menu
    #print(event.x_root, event.y_root)
    menu.post(event.x_root, event.y_root)
    '''
    global root
    root.Menu(root.abc,tearoff=0)
    root.Menu.post(event.x_root, event.y_root)
    '''
import json

import gp

global x,y,root,menu
def aiui():
    global root,menu,a
    root = tkinter.Tk()
    a=tkinter.StringVar() 
    
    
    
    #gp.gpmain('').trace('w',a.set(gp.gpmain('')))
    #root.after(1000,a.set(gp.gpmain('')))
    root.overrideredirect(True)
    root.wm_attributes('-topmost',1)
    sw=root.winfo_screenwidth()
    sh=root.winfo_screenheight()
    root_x=sw-500
    root_y=sh-500-50
    root.attributes("-alpha", 0.6)#窗口透明度60 %  0.4
    
    root.geometry("300x300+%d+%d"%(root_x,root_y))
    
    #canvas1 = tkinter.Canvas(root)
    canvas = tkinter.Label(root,textvariable = a,fg="red",
            font=("微软雅黑", 10))

    canvas.configure(width = 300)
    canvas.configure(height = 300)
    canvas.configure(bg = "white")
    #canvas.configure(highlightthickness = 0)
    
    
    #filename = tkinter.PhotoImage(file = "ai_1.gif")
    #canvas.create_image(150,150)#, image=filename)
    
    canvas.bind("<B1-Motion>",move)
    canvas.bind("<Button-1>",button_1)
    canvas.bind("<Button-3>",button_3)
    
    canvas.pack()
    
    
    section_obj = section()
    menu = tkinter.Menu(canvas,tearoff=0)
    menu.add_command(label="设置", command=ttk1)
    menu.add_separator()
    '''menu.add_command(label="开始工作", command=section_obj.onPaste)
    menu.add_separator()
    menu.add_command(label="技能学习", command=section_obj.onCut)
    menu.add_separator()'''
    menu.add_command(label="退出", command=root.quit)
      
    
    def jw():
        try:
            with open('data.json','r')as TxtFile:
                #print(str(json.load(TxtFile)))
                b=json.load(TxtFile)
                #print(b)
                a.set(b)
        except:pass
        root.after(500,jw)
        
    
    root.after(100,jw)
    root.mainloop()
 
 
    
'''线程控制'''
exitFlag = 0
class threadControl(threading.Thread):
    def __init__(self,threadID, name, counter):
        threading.Thread.__init__(self)
        self.threadID = threadID
        self.name = name
        self.counter = counter
        
    def run(self):
        #print ("开始线程：" + self.name)
        if self.name=='aiui':
            aiui()
        #print_time(self.name, self.counter, 5)
        #print ("退出线程：" + self.name)
        
def print_time(threadName, delay, counter):
    while counter:
        if exitFlag:
            threadName.exit()
        time.sleep(delay)
        #print ("%s: %s" % (threadName, time.ctime(time.time())))
        counter -= 1
        
    
if __name__ == '__main__':    
    thread1=threadControl(1,'thread_1',1)
    thread2=threadControl(2,'thread_2',2)
    aiui_obj=threadControl(3,'aiui',3)
    
    aiui_obj.start()
    

    def fun_timer():
        
        gp.gpmain('')
        global timer
        timer = threading.Timer(1, fun_timer)
        timer.start()

    timer = threading.Timer(1, fun_timer)
    timer.start()

    '''time.sleep(15) # 15秒后停止定时器
    timer.cancel()'''
    
    thread1.start()
    thread2.start()
    
    thread1.join()
    thread2.join()
    
    aiui_obj.join()
    
    #print ("退出主线程")
    