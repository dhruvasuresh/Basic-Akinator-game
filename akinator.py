from tkinter import *
from PIL import Image,ImageTk
database =[
     {"name":"Iron man","human":True,"youtuber":False,"movie":True,"original":False,"inventor":True,"indian":False,"athlete":False,"superpowers":True,"beard":False,"alive":False,"MCU":True,"football":False,"cricket":False,"bald":False},
     {"name":"Erling Haaland","human":True,"youtuber":False,"movie":False,"original":True,"inventor":False,"indian":False,"athlete":True,"superpowers":False,"beard":False,"alive":True,"MCU":False,"football":True,"cricket":False,"bald":False},
     {"name":"Virat Kohli","human":True,"youtuber":False,"movie":False,"original":True,"inventor":False,"indian":True,"athlete":True,"superpowers":False,"beard":True,"alive":True,"MCU":False,"football":False,"cricket":True,"bald":False},
     {"name":"Albert Einstein","human":True,"youtuber":False,"movie":False,"original":True,"inventor":True,"indian":False,"athlete":False,"superpowers":False,"beard":False,"alive":False,"MCU":False,"football":False,"cricket":False,"bald":False},
     {"name":"Andrew Tate","human":True,"youtuber":False,"movie":False,"original":True,"inventor":False,"indian":False,"athlete":True,"superpowers":False,"beard":True,"alive":True,"MCU":False,"football":False,"cricket":False,"bald":True},
     {"name":"Annabelle","human":False,"youtuber":False,"movie":True,"original":False,"inventor":False,"indian":False,"athlete":False,"superpowers":True,"beard":False,"alive":False,"MCU":False,"football":False,"cricket":False,"bald":False},
     {"name":"Walter White","human":True,"youtuber":False,"movie":True,"original":False,"inventor":True,"indian":False,"athlete":False,"superpowers":False,"beard":True,"alive":False,"MCU":False,"football":False,"cricket":False,"bald":True},
     {"name":"Soldier Boy","human":True,"youtuber":False,"movie":True,"original":False,"inventor":False,"indian":False,"athlete":False,"superpowers":True,"beard":True,"alive":False,"MCU":False,"football":False,"cricket":False,"bald":False},
     {"name":"Carryminati","human":True,"youtuber":True,"movie":True,"original":True,"inventor":False,"indian":True,"athlete":False,"superpowers":False,"beard":True,"alive":True,"MCU":False,"football":False,"cricket":False,"bald":False},
     {"name":"Don Corleone","human":True,"youtuber":False,"movie":True,"original":False,"inventor":False,"indian":False,"athlete":False,"superpowers":False,"beard":False,"alive":False,"MCU":False,"football":False,"cricket":False,"bald":False},
     {"name":"Drake","human":True,"youtuber":False,"movie":False,"original":True,"inventor":False,"indian":False,"athlete":False,"superpowers":False,"beard":True,"alive":True,"MCU":False,"football":False,"cricket":False,"bald":False},
     {"name":"Jordan Belfort","human":True,"youtuber":False,"movie":True,"original":True,"inventor":False,"indian":False,"athlete":False,"superpowers":False,"beard":False,"alive":True,"MCU":False,"football":False,"cricket":False,"bald":False},
     {"name":"Peter Parker","human":True,"youtuber":False,"movie":True,"original":False,"inventor":True,"indian":False,"athlete":False,"superpowers":True,"beard":False,"alive":True,"MCU":True,"football":False,"cricket":False,"bald":False},
     {"name":"hulk","human":False,"youtuber":False,"movie":True,"original":False,"inventor":True,"indian":False,"athlete":False,"superpowers":True,"beard":False,"alive":True,"MCU":True,"football":False,"cricket":False,"bald":False},
     {"name":"captain marvel","human":True,"youtuber":False,"movie":True,"original":False,"inventor":False,"indian":False,"athlete":False,"superpowers":True,"beard":False,"alive":True,"MCU":True,"football":False,"cricket":False,"bald":False},
     {"name":"aquaman","human":True,"youtuber":False,"movie":True,"original":False,"inventor":False,"indian":False,"athlete":False,"superpowers":True,"beard":True,"alive":True,"MCU":False,"football":False,"cricket":False,"bald":False},
     {"name":"antman","human":True,"youtuber":False,"movie":True,"original":False,"inventor":False,"indian":False,"athlete":False,"superpowers":True,"beard":False,"alive":True,"MCU":True,"football":False,"cricket":False,"bald":False},
     {"name":"neeraj chopra","human":True,"youtuber":False,"movie":False,"original":True,"inventor":False,"indian":True,"athlete":True,"superpowers":False,"beard":False,"alive":True,"MCU":False,"football":False,"cricket":False,"bald":False},
     {"name":"usain bolt","human":True,"youtuber":False,"movie":False,"original":True,"inventor":False,"indian":False,"athlete":True,"superpowers":False,"beard":True,"alive":True,"MCU":False,"football":False,"cricket":False,"bald":False},
     {"name":"lionel messi","human":True,"youtuber":False,"movie":False,"original":True,"inventor":False,"indian":False,"athlete":True,"superpowers":False,"beard":True,"alive":True,"MCU":False,"football":True,"cricket":False,"bald":False},
     {"name":"neymar jr","human":True,"youtuber":False,"movie":True,"original":True,"inventor":False,"indian":False,"athlete":True,"superpowers":False,"beard":True,"alive":True,"MCU":False,"football":True,"cricket":False,"bald":False},
     {"name":"ab devillers","human":True,"youtuber":False,"movie":False,"original":True,"inventor":False,"indian":False,"athlete":True,"superpowers":False,"beard":True,"alive":True,"MCU":False,"football":False,"cricket":True,"bald":False},
     {"name":"amitabh bachchan","human":True,"youtuber":False,"movie":True,"original":True,"inventor":False,"indian":True,"athlete":False,"superpowers":False,"beard":True,"alive":False,"MCU":False,"football":False,"cricket":False,"bald":False},
     {"name":"thor","human":False,"youtuber":False,"movie":True,"original":False,"inventor":False,"indian":False,"athlete":False,"superpowers":True,"beard":True,"alive":True,"MCU":True,"football":False,"cricket":False,"bald":False},
     {"name":"captain america","human":True,"youtuber":False,"movie":True,"original":False,"inventor":False,"indian":False,"athlete":False,"superpowers":True,"beard":True,"alive":True,"MCU":True,"football":False,"cricket":False,"bald":False},
     {"name":"shah rukh khan","human":True,"youtuber":False,"movie":True,"original":True,"inventor":False,"indian":True,"athlete":False,"superpowers":False,"beard":False,"alive":True,"MCU":False,"football":False,"cricket":False,"bald":False},
    ]

def take_chance(answer,property):
    print("Initial DB values count")
    print(len(database))
    if answer == "y":
        ans= True
    else:
        ans= False

    character_guess="no value"
    to_remove=[]
    for d in database:
        if d[property] != ans:
            to_remove.append(d)
    for i in to_remove:
        database.remove(i)
    print(len(database))
    if len(database) == 1:
        character_guess = "your character is "+ database[0]["name"]#final result
        return character_guess


root=Tk()
root.geometry("900x950")
title=root.title("AKINATOR")
l1=Label(root,text="WELCOME TO",font=("Courier",20),bg="red").place(x=275,y=145)
i=0
def kick():
    global i,l1
    if(i>64):
        i=14
    else:
        i=i+14
        l1=Label(root,text="AKINATOR",font=("Courier",i),bg="red")
        l1.place(x=375,y=195)
    root.after(500,kick)
kick()
def start1():
    root.destroy() 
img1=Image.open(r"D:\Users\Dhruva\Desktop\python mini projec\start.png")
resize1=img1.resize((120,120))
img11=ImageTk.PhotoImage(resize1)
start=Button(root,text="",image=img11,command=lambda:start1()).place(x=375,y=305)
root.mainloop()#1st window

q1=Tk()#2nd window
q1.geometry("900x950")
l1=Label(q1,text="IS YOUR CHARACTER HUMAN?",font=("Courier,25"),fg="blue").place(x=275,y=210)
def yes():
    global character_guess
    character_guess=take_chance("y","human")
    print("out",character_guess)
    q1.destroy()
def no():
    global character_guess
    take_chance("n","human")
    q1.destroy()

img2=Image.open(r"D:\Users\Dhruva\Desktop\python mini projec\yes.png")
resize2=img2.resize((80,80))
img12=ImageTk.PhotoImage(resize2)
start=Button(q1,text="",image=img12,command=lambda:yes()).place(x=305,y=305)
img3=Image.open(r"D:\Users\Dhruva\Desktop\python mini projec\no.png")
resize3=img3.resize((80,80))
img13=ImageTk.PhotoImage(resize3)
start=Button(q1,text="",image=img13,command=lambda:yes()).place(x=435,y=305)
q1.mainloop()#close of 2nd window
q2=Tk()
q2.geometry("900x950")
l2=Label(q2,text="IS YOUR CHARACTER YOUTUBER?",font=("Courier",15),fg="blue").place(x=275,y=210)
def yes():
    global character_guess
    character_guess=take_chance("y","youtuber")
    print(character_guess)
    q2.destroy()
def no():
    global character_guess
    character_guess=take_chance("n","youtuber")
    print(character_guess)
    q2.destroy()
img4=Image.open(r"D:\Users\Dhruva\Desktop\python mini projec\yes.png")
resize4=img4.resize((80,80))
img14=ImageTk.PhotoImage(resize4)
start=Button(q2,text="",image=img14,command=lambda:yes()).place(x=305,y=305)
img5=Image.open(r"D:\Users\Dhruva\Desktop\python mini projec\no.png")
resize5=img5.resize((80,80))
img15=ImageTk.PhotoImage(resize5)
start=Button(q2,text="",image=img15,command=lambda:no()).place(x=435,y=305)
q2.mainloop()#close of 2nd window

q4=Tk()
q4.geometry("900x950")
l4=Label(q4,text="is ur character in a movie/tv series",font=("Courier",15),fg="blue").place(x=275,y=210)
def yes():
    global character_guess
    character_guess=take_chance("y","movie")
    print(character_guess)
    q4.destroy()
def no():
    global character_guess
    character_guess=take_chance("n","movie")
    print(character_guess)
    q4.destroy()  
img6=Image.open(r"D:\Users\Dhruva\Desktop\python mini projec\yes.png")
resize6=img6.resize((80,80))
img16=ImageTk.PhotoImage(resize6)
start=Button(q4,text="",image=img16,command=lambda:yes()).place(x=305,y=305)
img7=Image.open(r"D:\Users\Dhruva\Desktop\python mini projec\no.png")
resize7=img7.resize((80,80))
img17=ImageTk.PhotoImage(resize7)
start=Button(q4,text="",image=img17,command=lambda:no()).place(x=435,y=305)

q4.mainloop()

q5=Tk()
q5.geometry("900x950")
l5=Label(q5,text="is ur character original",font=("Courier",15),fg="blue").place(x=275,y=210)
def yes():
    global character_guess
    character_guess=take_chance("y","original")
    print(character_guess)
    q5.destroy()
def no():
    global character_guess
    character_guess=take_chance("n","original")
    print(character_guess)
    q5.destroy()

img8=Image.open(r"D:\Users\Dhruva\Desktop\python mini projec\yes.png")
resize8=img8.resize((80,80))
img18=ImageTk.PhotoImage(resize8)
start=Button(q5,text="",image=img18,command=lambda:yes()).place(x=305,y=305)
img9=Image.open(r"D:\Users\Dhruva\Desktop\python mini projec\no.png")
resize9=img9.resize((80,80))
img19=ImageTk.PhotoImage(resize9)
start=Button(q5,text="",image=img19,command=lambda:no()).place(x=435,y=305)
q5.mainloop()

q6=Tk()
q6.geometry("900x950")
l6=Label(q6,text="is ur character an inventor",font=("Courier",15),fg="blue").place(x=275,y=210)
def yes():
    global character_guess
    character_guess=take_chance("y","inventor")
    print(character_guess)

    q6.destroy()
def no():
    global character_guess
    character_guess=take_chance("n","inventor")
    print(character_guess)
    q6.destroy()

img88=Image.open(r"D:\Users\Dhruva\Desktop\python mini projec\yes.png")
resize88=img88.resize((80,80))
img188=ImageTk.PhotoImage(resize88)
start=Button(q6,text="",image=img188,command=lambda:yes()).place(x=305,y=305)
img92=Image.open(r"D:\Users\Dhruva\Desktop\python mini projec\no.png")
resize92=img92.resize((80,80))
img192=ImageTk.PhotoImage(resize92)
start=Button(q6,text="",image=img192,command=lambda:no()).place(x=435,y=305)
q6.mainloop()

q7=Tk()
q7.geometry("900x950")
l7=Label(q7,text="is ur character indian",font=("Courier",15),fg="blue").place(x=275,y=210)
def yes():
    global character_guess
    character_guess=take_chance("y","indian")
    print(character_guess)
    q7.destroy()
def no():
    global character_guess
    character_guess=take_chance("n","indian")
    print(character_guess)
    q7.destroy()

img87=Image.open(r"D:\Users\Dhruva\Desktop\python mini projec\yes.png")
resize87=img87.resize((80,80))
img187=ImageTk.PhotoImage(resize87)
start=Button(q7,text="",image=img187,command=lambda:yes()).place(x=305,y=305)
img91=Image.open(r"D:\Users\Dhruva\Desktop\python mini projec\no.png")
resize91=img91.resize((80,80))
img191=ImageTk.PhotoImage(resize91)
start=Button(q7,text="",image=img191,command=lambda:no()).place(x=435,y=305)
q7.mainloop()

q8=Tk()
q8.geometry("900x950")
l8=Label(q8,text="is ur character an athlete",font=("Courier",15),fg="blue").place(x=275,y=210)
def yes():
    global character_guess
    character_guess=take_chance("y","athlete")
    print(character_guess)
    q8.destroy()
def no():
    global character_guess
    character_guess=take_chance("n","athlete")
    print(character_guess)
    q8.destroy()

img86=Image.open(r"D:\Users\Dhruva\Desktop\python mini projec\yes.png")
resize86=img86.resize((80,80))
img186=ImageTk.PhotoImage(resize86)
start=Button(q8,text="",image=img186,command=lambda:yes()).place(x=305,y=305)
img93=Image.open(r"D:\Users\Dhruva\Desktop\python mini projec\no.png")
resize93=img93.resize((80,80))
img193=ImageTk.PhotoImage(resize93)
start=Button(q8,text="",image=img193,command=lambda:no()).place(x=435,y=305)
q8.mainloop()

q9=Tk()
q9.geometry("900x950")
l9=Label(q9,text="does your character have superpowers"
,font=("Courier",15),fg="blue").place(x=275,y=210)
def yes():
    global character_guess
    character_guess=take_chance("y","superpowers")
    print(character_guess)
    q9.destroy()
def no():
    global character_guess
    character_guess=take_chance("n","superpowers")
    print(character_guess)
    q9.destroy()

img85=Image.open(r"D:\Users\Dhruva\Desktop\python mini projec\yes.png")
resize85=img85.resize((80,80))
img185=ImageTk.PhotoImage(resize85)
start=Button(q9,text="",image=img185,command=lambda:yes()).place(x=305,y=305)
img96=Image.open(r"D:\Users\Dhruva\Desktop\python mini projec\no.png")
resize96=img96.resize((80,80))
img196=ImageTk.PhotoImage(resize96)
start=Button(q9,text="",image=img196,command=lambda:no()).place(x=435,y=305)
q9.mainloop()

q10=Tk()
q10.geometry("900x950")
l10=Label(q10,text="does your character have a beard",font=("Courier",15),fg="blue").place(x=275,y=210)
def yes():
    global character_guess
    character_guess=take_chance("y","beard")
    print(character_guess)
    q10.destroy()
def no():
    global character_guess
    character_guess=take_chance("n","beard")
    print(character_guess)
    q10.destroy()

img86=Image.open(r"D:\Users\Dhruva\Desktop\python mini projec\yes.png")
resize86=img86.resize((80,80))
img186=ImageTk.PhotoImage(resize86)
start=Button(q10,text="",image=img186,command=lambda:yes()).place(x=305,y=305)
img94=Image.open(r"D:\Users\Dhruva\Desktop\python mini projec\no.png")
resize94=img94.resize((80,80))
img194=ImageTk.PhotoImage(resize94)
start=Button(q10,text="",image=img194,command=lambda:no()).place(x=435,y=305)
q10.mainloop()

q11=Tk()
q11.geometry("900x950")
l11=Label(q11,text="is ur character alive",font=("Courier",15),fg="blue").place(x=275,y=210)
def yes():
    global character_guess
    character_guess=take_chance("y","alive")
    print(character_guess)
    q11.destroy()
def no():
    global character_guess
    character_guess=take_chance("n","alive")
    print(character_guess)
    q11.destroy()

img83=Image.open(r"D:\Users\Dhruva\Desktop\python mini projec\yes.png")
resize83=img83.resize((80,80))
img183=ImageTk.PhotoImage(resize83)
start=Button(q11,text="",image=img183,command=lambda:yes()).place(x=305,y=305)
img97=Image.open(r"D:\Users\Dhruva\Desktop\python mini projec\no.png")
resize97=img97.resize((80,80))
img197=ImageTk.PhotoImage(resize97)
start=Button(q11,text="",image=img197,command=lambda:no()).place(x=435,y=305)
q11.mainloop()

q12=Tk()
q12.geometry("900x950")
l12=Label(q12,text="is ur character in the MCU",font=("Courier",15),fg="blue").place(x=275,y=210)
def yes():
    global character_guess
    character_guess=take_chance("y","MCU")
    print(character_guess)
    q12.destroy()
def no():
    global character_guess
    character_guess=take_chance("n","MCU")
    print(character_guess)
    q12.destroy()

img81=Image.open(r"D:\Users\Dhruva\Desktop\python mini projec\yes.png")
resize81=img81.resize((80,80))
img181=ImageTk.PhotoImage(resize81)
start=Button(q12,text="",image=img181,command=lambda:yes()).place(x=305,y=305)
img99=Image.open(r"D:\Users\Dhruva\Desktop\python mini projec\no.png")
resize99=img99.resize((80,80))
img199=ImageTk.PhotoImage(resize99)
start=Button(q12,text="",image=img199,command=lambda:no()).place(x=435,y=305)
q12.mainloop()

q13=Tk()
q13.geometry("900x950")
l13=Label(q13,text="is ur character a footballer",font=("Courier",15),fg="blue").place(x=275,y=210)
def yes():
    global character_guess
    character_guess=take_chance("y","football")
    print(character_guess)
    q13.destroy()
def no():
    global character_guess
    character_guess=take_chance("n","football")
    print(character_guess)
    q13.destroy()

img868=Image.open(r"D:\Users\Dhruva\Desktop\python mini projec\yes.png")
resize868=img868.resize((80,80))
img1868=ImageTk.PhotoImage(resize868)
start=Button(q13,text="",image=img1868,command=lambda:yes()).place(x=305,y=305)
img9499=Image.open(r"D:\Users\Dhruva\Desktop\python mini projec\no.png")
resize9499=img9499.resize((80,80))
img9499=ImageTk.PhotoImage(resize9499)
start=Button(q13,text="",image=img9499,command=lambda:no()).place(x=435,y=305)
q13.mainloop()

q14=Tk()
q14.geometry("900x950")
l14=Label(q14,text="is ur character a cricketer",font=("Courier",15),fg="blue").place(x=275,y=210)
def yes():
    global character_guess
    character_guess=take_chance("y","cricket")
    print(character_guess)
    q14.destroy()
def no():
    global character_guess
    character_guess=take_chance("n","cricket")
    print(character_guess)
    q14.destroy()

img8788=Image.open(r"D:\Users\Dhruva\Desktop\python mini projec\yes.png")
resize8788=img8788.resize((80,80))
img18788=ImageTk.PhotoImage(resize8788)
start=Button(q14,text="",image=img18788,command=lambda:yes()).place(x=305,y=305)
img9188=Image.open(r"D:\Users\Dhruva\Desktop\python mini projec\no.png")
resize9188=img9188.resize((80,80))
img19188=ImageTk.PhotoImage(resize9188)
start=Button(q14,text="",image=img19188,command=lambda:no()).place(x=435,y=305)
q14.mainloop()

q15=Tk()
q15.geometry("900x950")
l15=Label(q15,text="is ur character bald",font=("Courier",15),fg="blue").place(x=275,y=210)
def yes():
    global character_guess
    character_guess=take_chance("y","bald")
    print(character_guess)
    q15.destroy()
def no():
    global character_guess
    character_guess=take_chance("n","bald")
    print(character_guess)
    q15.destroy()

img8711=Image.open(r"D:\Users\Dhruva\Desktop\python mini projec\yes.png")
resize8711=img8711.resize((80,80))
img18711=ImageTk.PhotoImage(resize8711)
start=Button(q15,text="",image=img18711,command=lambda:yes()).place(x=305,y=305)
img9111=Image.open(r"D:\Users\Dhruva\Desktop\python mini projec\no.png")
resize9111=img9111.resize((80,80))
img19111=ImageTk.PhotoImage(resize9111)
start=Button(q15,text="",image=img19111,command=lambda:no()).place(x=435,y=305)
q15.mainloop()

ro=Tk()
ro.geometry("900x950")
character_guess=character_guess.upper()
t=Label(ro,text=character_guess,anchor=CENTER,font=("Courier,95"),fg="blue").place(x=275,y=210)
ro.mainloop()

root.mainloop()