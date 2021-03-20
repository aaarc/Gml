import tkinter
from tkinter import *
import sklearn
from sklearn import tree

f_apple=[[1,140,1],[0,170,0],[1,6,1],[1,100,0],[1,180,1],[0,600,0],[0,170,0],[0,160,1]]
l_apple=[1,0,0,1,1,0,0,0]

f_dog =[[8,46,1],[8,56,0],[9,40,0],[11,40,0],[5,30,0],[4,39,0],[7,29,0],[29,70,1],[27,65,1]]
l_dog= [1,0,1,0,0,0,0,1,1]

def mlfn(fx,lx,ix):#ix>> input
    clf1 = tree.DecisionTreeClassifier()
    clf1 = clf1.fit(fx, lx)
    a = clf1.predict([ix])
    return a


#_____________apple_or_no_______##

def aont():
    cd_1 = tkinter.Toplevel()
    cd_1.config(bg='black')
    cd_1.geometry('800x400+275+100')
    cd_1.title('GML-Enter data')
    cd_1.iconbitmap("devspci.ico")
    cd_1.resizable(0, 0)
    lab3m = tkinter.Label(cd_1, text="Enter the Data  in the given format", bg='black', fg='#ccffff',font=('Arial', 18))
    lab3m.pack(padx=10, pady=10)
    lab4m = tkinter.Label(cd_1,text=" format ==> [texture of surface(smooth is 1,bumpy is 0),\nWieght(in g),colour(1 if red, 0 if not red)]\nexample input:[1,140,1](example for a apple input)",bg='black', fg='#ccffff', font=('Arial', 18))
    lab4m.pack(padx=10, pady=10)
    i1 = tkinter.Entry(cd_1)
    i1.pack(padx=10, pady=10)

    def isaple():
        global l_apple
        global f_apple
        itx = i1.get()
        print(itx,type(itx))
        ix1 = eval(itx)
        res = mlfn(f_apple, l_apple, ix1)
        if (res == 1):
            cd_2 = tkinter.Toplevel()
            cd_2.config(bg='black')
            cd_2.geometry('400x300+275+100')
            cd_2.title('GML-Result')
            cd_2.iconbitmap("devspci.ico")
            cd_2.resizable(0, 0)
            ldg = tkinter.Label(cd_2, text="The details entered belongs an Apple!!", bg="black", fg="#ccffff",font=30)
            ldg.pack()

        else:
            cd_2 = tkinter.Toplevel()
            cd_2.config(bg='black')
            cd_2.geometry('400x300+275+100')
            cd_2.title('GML-Result')
            cd_2.iconbitmap("devspci.ico")
            cd_2.resizable(0, 0)
            ldg = tkinter.Label(cd_2, text="The details entered does not  belong to an Apple !!!", bg="black", fg="#ccffff",font=30)
            ldg.pack()
        cd_1.destroy()

    b1_z = tkinter.Button(cd_1, text='Continue', bg='black', fg='#ccffff', command=isaple)
    b1_z.pack(pady=23)




#_________cat_or_dog____________#
def cod():
    cd_1 = tkinter.Toplevel()
    cd_1.config(bg='black')
    cd_1.geometry('800x400+275+100')
    cd_1.title('GML-Enter data')
    cd_1.iconbitmap("devspci.ico")
    cd_1.resizable(0, 0)
    lab3m = tkinter.Label(cd_1, text="Enter the Data  in the given format", bg='black', fg='#ccffff', font=('Arial', 18))
    lab3m.pack(padx=10, pady=10)
    lab4m = tkinter.Label(cd_1, text=" format ==> [wieght(in kg),Hieght(in cm),\nlong face or short face(1 if true, 0 if false)]\nexample input:[19,40,1](example for a dog input)", bg='black', fg='#ccffff', font=('Arial', 18))
    lab4m.pack(padx=10, pady=10)
    i1=tkinter.Entry(cd_1)
    i1.pack(padx=10,pady=10)
    def isdg():
        global l_dog
        global f_dog
        itx=i1.get()
        ix1=eval(itx)
        res=mlfn(f_dog,l_dog,ix1)
        if (res == 1):
            cd_2 = tkinter.Toplevel()
            cd_2.config(bg='black')
            cd_2.geometry('400x300+275+100')
            cd_2.title('GML-Result')
            cd_2.iconbitmap("devspci.ico")
            cd_2.resizable(0, 0)
            ldg=tkinter.Label(cd_2,text="The details entered belongs to a DOG!!!",bg="black",fg="#ccffff",font=30)
            ldg.pack()

        else:
            cd_2 = tkinter.Toplevel()
            cd_2.config(bg='black')
            cd_2.geometry('400x300+275+100')
            cd_2.title('GML-Result')
            cd_2.iconbitmap("devspci.ico")
            cd_2.resizable(0, 0)
            ldg = tkinter.Label(cd_2, text="The details entered belongs to a Cat!!!", bg="black", fg="#ccffff",font=30)
            ldg.pack()
        cd_1.destroy()

    b1_z = tkinter.Button(cd_1, text='Continue', bg='black', fg='#ccffff',command=isdg)
    b1_z.pack(pady=23)













##________________________functions_______##

def str_bc():
    st_b1=tkinter.Toplevel()
    st_b1.config(bg='black')
    st_b1.geometry('400x400+275+100')
    st_b1.title('GML-Choose the data set')
    st_b1.iconbitmap("devspci.ico")
    st_b1.resizable(0, 0)
    lab1m=tkinter.Label(st_b1,text="Choose the Data Set",bg='black',fg='#ccffff',font=('Arial',20))
    lab1m.pack(padx=10,pady=10)
    def fun1():
        aont()
        st_b1.destroy()
    def fun2():
        cod()
        st_b1.destroy()
    b= tkinter.Button(st_b1, text='Apple and Not Apple', bg='black', fg='#ccffff',command=fun1)
    b.pack(pady=23)
    b1_= tkinter.Button(st_b1, text='Dog or Cat', bg='black', fg='#ccffff',command=fun2)
    b1_.pack(pady=23)

######################3____admin



##########################_main_window####

rt=tkinter.Tk()
rt.title("GLK")
rt.iconbitmap("devspci.ico")
rt.config(bg="black")
rt.geometry('800x500+250+100')
rt.resizable(1,1)

top_bar=tkinter.Frame(rt,bg='black')
mid_sec=tkinter.Frame(rt,bg='black')
mid_sec2=tkinter.Frame(rt,bg='black')
mid_sec3=tkinter.Frame(rt,bg='#e6b800')
end_section=tkinter.Frame(rt,bg='black')

####################################################Top_bar_components

b1=tkinter.Button(top_bar,text='|',bg='black',fg='black',relief=FLAT,font={'Arial',42})
b1.config(activebackground="#99ffff")
b1.grid(row=0,column=0,sticky='w',ipadx=5,padx=1)
sp1=tkinter.Label(top_bar,text='',bg='black',fg='black',font={'Arial',42})
sp1.grid(row=0,column=1)
title0=tkinter.Label(top_bar,text=" ",bg='black',fg='#ccffff',font={'Arial',60})
title0.grid(row=0,column=2,padx=155,pady=5)
title1=tkinter.Label(top_bar,text="G",bg='black',fg='#00ffff',font={'Arial',60})
title1.grid(row=0,column=3,padx=1,pady=5)
title2=tkinter.Label(top_bar,text="M",bg='black',fg='#ff751a',font={'Arial',60})
title2.grid(row=0,column=4,padx=1,pady=5)
title3=tkinter.Label(top_bar,text="L",bg='black',fg='#33ff33',font={'Arial',60})
title3.grid(row=0,column=5,padx=1,pady=5)
title4=tkinter.Label(top_bar,text=" ",bg='black',fg='#ccffff',font={'Arial',60})
title4.grid(row=0,column=6,padx=180,pady=5)


######################################################mid_section components

lab1m=tkinter.Label(mid_sec,text="\n\n\n Give Machine learning a Try today!\n\n Its Easy!\n\n",bg='black',fg='#ccffff',font='Arial')
lab1m.pack()

b1m=tkinter.Button(mid_sec,text='START',bg='black',fg='#80ffd4',relief=FLAT,font={'Comfortaa',52},command=str_bc)
b1m.config(activebackground="#99ffff")
b1m.pack(pady=25)

######################################################placing frames
top_bar.pack(anchor='w',padx=10,pady=5)

mid_sec.pack(pady=15)

###########################################################main_loop
rt.mainloop()