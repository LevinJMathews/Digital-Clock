from tkinter import *
import datetime

#DRIVER CODE
def date_time():
    time=datetime.datetime.now()
    hr=time.strftime('%I')
    mi=time.strftime('%M')
    sec=time.strftime('%S')
    am=time.strftime('%p')
    dat=time.strftime('%d')
    month=time.strftime('%m')
    year=time.strftime('%y')
    day=time.strftime('%a')
    lb_hr.config(text=hr)
    lb_min.config(text=mi)
    lb_sec.config(text=sec)
    lb_am.config(text=am)
    lb_date.config(text=dat)
    lb_mo.config(text=month)
    lb_year.config(text=year)
    lb_day.config(text=day)
    lb_hr.after(200,date_time)




#GUI 
clock= Tk()
clock.title("Digital Clock")
clock.geometry("1000x500")
clock.config(bg="Yellow")

lb_hr=Label(clock,text="00",font=("Time New Roman",60,"bold"),bg="red",fg="white")  #for HOUR box
lb_hr.place(x=120,y=50,height=100,width=100)
lb_hr_txt=Label(clock,text="Hour",font=("Time New Roman",30,"bold"),bg="red",fg="white")
lb_hr_txt.place(x=120,y=190,height=40,width=100)

lb_min=Label(clock,text="00",font=("Time New Roman",60,"bold"),bg="red",fg="white")  #for MINUTE box
lb_min.place(x=340,y=50,height=100,width=100)
lb_min_txt=Label(clock,text="Min",font=("Time New Roman",30,"bold"),bg="red",fg="white")
lb_min_txt.place(x=340,y=190,height=40,width=100)

lb_sec=Label(clock,text="00",font=("Time New Roman",60,"bold"),bg="red",fg="white")  #for SECOND box
lb_sec.place(x=560,y=50,height=100,width=100)
lb_sec_txt=Label(clock,text="Sec",font=("Time New Roman",30,"bold"),bg="red",fg="white")
lb_sec_txt.place(x=560,y=190,height=40,width=100)

lb_am=Label(clock,text="00",font=("Time New Roman",50,"bold"),bg="red",fg="white")   #for AM/PM box
lb_am.place(x=780,y=50,height=100,width=100)
lb_am_txt=Label(clock,text="AM/PM",font=("Time New Roman",22,"bold"),bg="red",fg="white")
lb_am_txt.place(x=780,y=190,height=40,width=100)

lb_date=Label(clock,text="00",font=("Time New Roman",60,"bold"),bg="red",fg="white")   #for Date box
lb_date.place(x=120,y=270,height=100,width=100)
lb_date_txt=Label(clock,text="Date",font=("Time New Roman",30,"bold"),bg="red",fg="white")
lb_date_txt.place(x=120,y=410,height=40,width=100)

lb_mo=Label(clock,text="00",font=("Time New Roman",60,"bold"),bg="red",fg="white")    #for Month box
lb_mo.place(x=340,y=270,height=100,width=100)
lb_mo_txt=Label(clock,text="Month",font=("Time New Roman",26,"bold"),bg="red",fg="white")
lb_mo_txt.place(x=340,y=410,height=40,width=100)

lb_year=Label(clock,text="00",font=("Time New Roman",60,"bold"),bg="red",fg="white")   #for YEAR box
lb_year.place(x=560,y=270,height=100,width=100)
lb_year_txt=Label(clock,text="Year",font=("Time New Roman",30,"bold"),bg="red",fg="white")
lb_year_txt.place(x=560,y=410,height=40,width=100)

lb_day=Label(clock,text="00",font=("Time New Roman",35,"bold"),bg="red",fg="white")   #for DAY box
lb_day.place(x=780,y=270,height=100,width=100)
lb_day_txt=Label(clock,text="Day",font=("Time New Roman",30,"bold"),bg="red",fg="white")
lb_day_txt.place(x=780,y=410,height=40,width=100)

date_time()
clock.mainloop()