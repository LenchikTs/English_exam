from tkinter import *
import os.path
m=0

def click1():
    global m
    m=1
    x=0
    entry_text = StringVar()
    check=os.path.exists('users.txt')
    if check==False:
        f=open('users.txt','w')
    else:
        f = open('users.txt', 'a')
        f1=open('users.txt', 'r')
        s=f1.read()
        exist_user=s.find(str(ent1.get()))
        if exist_user>0:
            x=1
        else:
            last = s.rfind(' :')
            last1=s.rfind('ля: ')
            y=''
            for i in s[last1+4:last]:
                y+=i
            m += int(y)
        f1.close()
    if x>0:
        l2['text']="Такой пользователь уже существует, введите другого!"
    else:
        l2['text']=''
        for j in 'ID Пользователя: '+str(m)+' : '+str(ent1.get()):
            f.write(j)
        f.write('\n')
        ent1['textvariable'] = entry_text
    f.close()

root=Tk()
root.title("Exam")

l1=Label(root,text="Введите ФИО пользователя:")
l1.grid(row=0, column=0, sticky=W)
ent1=Entry(root,width=100)
ent1.grid(row=0, column=1, sticky=W)
b1=Button(root,text="Сохранить пользователя")
b1.grid(row=1, column=0, sticky=E)
#b1['command']=b1.bind("<Button-1>",click1)
b1['command']=click1
l2=Label(root,fg='Red')
l2.grid(row=1, column=1, sticky=W)

root.mainloop()
from tkinter import *
import os.path
m=0

def click1():
    global m
    m=1
    x=0
    entry_text = StringVar()
    check=os.path.exists('users.txt')
    if check==False:
        f=open('users.txt','w')
    else:
        f = open('users.txt', 'a')
        f1=open('users.txt', 'r')
        s=f1.read()
        exist_user=s.find(str(ent1.get()))
        if exist_user>0:
            x=1
        else:
            last = s.rfind(' :')
            last1=s.rfind('ля: ')
            y=''
            for i in s[last1+4:last]:
                y+=i
            m += int(y)
        f1.close()
    if x>0:
        l2['text']="Такой пользователь уже существует, введите другого!"
    else:
        l2['text']=''
        for j in 'ID Пользователя: '+str(m)+' : '+str(ent1.get()):
            f.write(j)
        f.write('\n')
        ent1['textvariable'] = entry_text
    f.close()

root=Tk()
root.title("Exam")

l1=Label(root,text="Введите ФИО пользователя:")
l1.grid(row=0, column=0, sticky=W)
ent1=Entry(root,width=100)
ent1.grid(row=0, column=1, sticky=W)
b1=Button(root,text="Сохранить пользователя")
b1.grid(row=1, column=0, sticky=E)
#b1['command']=b1.bind("<Button-1>",click1)
b1['command']=click1
l2=Label(root,fg='Red')
l2.grid(row=1, column=1, sticky=W)

root.mainloop()