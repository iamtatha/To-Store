
'''Importing ALl needed Libraries'''

from tkinter import *
import time
from tkinter.filedialog import askopenfilename
from tkinter.filedialog import asksaveasfilename
#from tkinter import Entry
#from tkinter import Button
#from tkinter import StringVar
import matplotlib.pyplot as plt
import csv
import math
#from selenium import webdriver 
#from selenium.webdriver.support.ui import WebDriverWait 
#from selenium.webdriver.support import expected_conditions as EC 
#from selenium.webdriver.common.keys import Keys 
#from selenium.webdriver.common.by import By
import webbrowser
import pkg_resources.py2_warn
import warnings
warnings.filterwarnings("ignore", "(?s).*MATPLOTLIBDATA.*", category=UserWarning)






'''User Interface Starts'''

#print('SET OF INSTRUCTIONS ARE AS FOLLOWS:\n')
#print('1.SOON A GRAPHICAL WINDOW WILL APPEAR.')
#print('2.THIS IS THE OFFICIAL MODULE TO DRAW POLAR GRAPHS.')
#print('3.GIVE INPUT THE FILE.')
#print('4.CHOOSE SAVING NAME OF CSV AND GRAPH.')
#print('5.AND AT LAST WRITE THE NAME OF VIRUS.')

root=Tk()
root.geometry('1200x800')
root["bg"] = "#141414"
root.title('2D Polar Plot Software')


lab1=Label(root,text='2D Polar Co-Ordinate Representation of Amino Acid Sequences and qR Characterization',font='Garamond 20 bold',fg='yellow',bg='#141414').pack()
lab2=Label(root,text='By Centre for Interdisciplinary Research and Education',font='cambria 16 bold',fg='white',bg='#141414').pack()

def callback(url):
    webbrowser.open_new(url)

link1 = Label(root, text="Link: Our Home Page | CIRE", font = 'Times', fg="PeachPuff", cursor="hand2", bg='#141414')
link1.pack()
link1.bind("<Button-1>", lambda e: callback("http://cire.co.in/"))

cire='''
CIRE is a non-profit Organization working in Interdisciplinary Research Projects in the field of Bioinformatics and Computational Biology for many years. Our Recent Accomplishments
include proposing peptide vaccines for various viral organisms along with characterising nucleotide or protein sequences with mathematical descriptors and graphical representations.
This 2D Polar plot is one of the fruits of such theoritical approaches. In this method we assign certain angles to each amino acid upon their various biochemical properties and while
plotting the graph we move through a vector by unit magnitude to the assigned direction. In this way we get a graph and calculating the centre of mass of this graph we get the qR value.
Our experiments and analysis indicates this qR value to be characteristic property for a sequence.
'''

lab5=Label(root,text=cire,bg='#141414',fg='Moccasin',font='calibri 11').pack()

fr1=Frame(root,bg='black',padx=5).pack(fill='x')

lab3=Label(fr1,text='SET OF INSTRUCTIONS TO FOLLOW:',fg='#7c9cff',font='georgia 16 bold',padx=377,pady=5,bg='#141414').pack(anchor="w")
lab4=Label(fr1,text='1. THIS IS THE OFFICIAL MODULE TO DRAW POLAR GRAPHS.',fg='#7c9cff',font='times 11',padx=377,pady=5,bg='#141414').pack(anchor="w")
lab12=Label(fr1,text='2. CLICK THE START BUTTON TO GET STARTED.',fg='#7c9cff',font='times 11',padx=377,pady=5,bg='#141414').pack(anchor="w")
lab7=Label(fr1,text='3. THEN A GRAPHICAL WINDOW WILL APPEAR.',fg='#7c9cff',font='times 11',padx=377,pady=5,bg='#141414').pack(anchor="w")
lab8=Label(fr1,text='4. GIVE THE FASTA FILE AS INPUT.',fg='#7c9cff',font='times 11',padx=377,pady=5,bg='#141414').pack(anchor="w")
lab11=Label(fr1,text='5. THEN THE PROGRAM WILL ASK YOU TO SAVE OUTPUTS.',fg='#7c9cff',font='times 11',padx=377,pady=5,bg='#141414').pack(anchor="w")
lab9=Label(fr1,text='6. CHOOSE SAVING NAME OF OUTPUT CSV AND GRAPH.',fg='#7c9cff',font='times 11',padx=377,pady=5,bg='#141414').pack(anchor="w")
lab12=Label(fr1,text='7. THEN THE PROGRAM WILL ASK FOR THE VIRUS NAME.',fg='#7c9cff',font='times 11',padx=377,pady=5,bg='#141414').pack(anchor="w")
lab10=Label(fr1,text='8. WRITE THE NAME OF VIRUS AND SUBMIT.',fg='#7c9cff',font='times 11',padx=377,pady=5,bg='#141414').pack(anchor="w")

fr2=Frame(root,bg='black',padx=5).pack(fill='x')
link2 = Label(fr2, text="My Linkedin", font = 'Times', fg="PeachPuff", cursor="hand2", bg='#141414')
link2.pack(side='bottom',anchor='se')
#link2.grid(row=20,column=10)
link2.bind("<Button-1>", lambda e: callback("https://www.linkedin.com/in/tathagata-dey-580245172"))
lab6=Label(root,text='Developed by Tathagata Dey  |  Contact: tathagata2403@gmail.com',font='Cambria 12',fg='white',pady=5,padx=10,bg='#141414').pack(side='bottom',anchor='se')
#lab6=Label(root,text='Developed by Tathagata Dey  |  Contact: tathagata2403@gmail.com',font='Cambria 12',fg='white',pady=5,padx=10,bg='#141414').grid(row=20,column=12)

#root.filename=askopenfilename(filetypes=(),title='Select File to open')


'''

def savecsv():
    fout=open()


csvname=Stringvar()
pngname=Stringvar()

l1=Label(root,text='Enter CSV Output File Name:').grid()
l2=Label(root,text='Enter PNG Output File Name:').grid()

e1=Entry(root,textvariable=csvname)
e2=Entry(root,textvariable=pngname)
b1=Button(root,text='Submit',command=savecsv)
'''






def job():

    def polar(s):
        seq=s.upper()
        a=0
        x=0
        y=0
        cox=[0]
        coy=[0]
        qrx=0
        qry=0
        qr=0
        z=0
        n=0

        amino=['E','A','C','V','F','L','I','W','M','T','Y','G','Q','R','N','P','H','K','D','S']
        angle={}

        k=0
        for i in range(0,360,18):
            angle[amino[k]]=i
            k+=1


        for i in range(len(seq)):
            if seq[i] in amino:
                a=angle[seq[i]]

                x+=math.cos(((math.pi)/180)*a)
                y+=math.sin(((math.pi)/180)*a)
                qrx+=x
                qry+=y
                n+=1

                cox.append(x)
                coy.append(y)
            elif seq[i]==' ':
                pass
            elif seq[i]=='\n':
                pass
            else:
                z+=1

        qr=(((qrx/n)**2)+((qry/n)**2))**0.5
        plotx.append(cox)
        ploty.append(coy)
        sumx.append(qrx)
        sumy.append(qry)
        total.append(n)
        unknown.append(z)
        qrval.append(qr)
    
    root.filename=askopenfilename(filetypes=(),title='Select File to open')
    f=open(root.filename)
    c=f.read()
    cds=[]
    data=[]
    l=c.split('>')[1:]
    for i in range(len(l)):
        t=l[i].split('|')
        s=t[-1]
        t.pop(-1)
        t.append('')
        k=0
        for i in s:
            if i=='\n':
                break
            else:
                t[-2]+=i
            k+=1
        data.append(t)
        cds.append(s[k:].replace('\n',''))


    (plotx,ploty,sumx,sumy,total,unknown,qrval)=([],[],[],[],[],[],[])

    
    m=0
    for i in range(len(data)):
        m=max(m,len(data[i]))
    for i in range(len(data)):
        if len(data[i])<m:
            while len(data[i])!=m:
                data[i].append('')




    for i in range(len(cds)):
        polar(cds[i])
        data[i].append(total[-1])
        data[i].append(unknown[-1])
        data[i].append(sumx[-1])
        data[i].append(sumy[-1])
        data[i].append(qrval[-1])


    root.csvname=asksaveasfilename(filetypes=(),title='Save The Csv Data File As')
    fout=open(root.csvname+'.csv','w',newline='')
    w=csv.writer(fout)

    l=['']*m
    l.append('Total Length')
    l.append('Unknown Bases')
    l.append('Sumx')
    l.append('Sumy')
    l.append('Qr Value')

    w.writerow(l)

    for i in data:
        w.writerow(i)
    fout.close()


    root.pngname=asksaveasfilename(filetypes=(),title='Save The Png Graph File As')
    fig=plt.figure(figsize=(105,85))

    plt.tick_params(axis="x", labelsize=70)
    plt.tick_params(axis="y", labelsize=70)

    for i in range(len(plotx)):
        fig=plt.plot(plotx[i],ploty[i],label=str(data[i][0])+str(total[i]),linewidth=5)




    
    virusname=StringVar()
    legendopt=StringVar()
    opt=0
    
    def naming():
        plt.title('Polar Co-ordinate Representation of '+virusname.get(),fontsize=105)
        #print(virusname.get())
        #print(legendopt.get())
        if legendopt.get()[:3].upper()=='Yes' or legendopt.get()[:3]=='yes' or legendopt.get()[:3]=='Yes':
            plt.legend(prop={'size':70})

            
    l1=Label(root,text='\nEnter Virus Name',font='Georgia 10',fg='white',bg='#141414').pack()
    vname=Entry(root,bg='white',textvariable=virusname).pack()
    l2=Label(root,text='\nDo You want legends label in the image(Yes/No/Default is No)',font='Georgia 10',fg='white',bg='#141414').pack()  
    lname=Entry(root,bg='white',textvariable=legendopt).pack()
    l=Label(root,text='\n',bg='#141414').pack()
    b=Button(root,text='Submit',font='arial 12 bold',command=naming,padx=7,pady=0.5,bg='#c4d1f1',relief=RAISED,bd=6).pack()
    
    #print(opt)
    
    
    plt.savefig(root.pngname+'.png')   








#lab13=Label(root,text='\n',bg='#141414').pack()
b1=Button(root,text='Start',font='arial 12 bold',command=job,padx=7,pady=0.5,bg='#c4d1f1',relief=RAISED,bd=5).pack()

#root.after(5000,job)














