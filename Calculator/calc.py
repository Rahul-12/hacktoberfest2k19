
from tkinter import *
expression = "" 
def press(num): 
    	global expression
    	expression = expression + str(num)
    	equation.set(expression)
 
def equalpress(): 
	try: 
		global expression 
		total = str(eval(expression)) 
		equation.set(total) 
		expression = "" 
	except: 
		equation.set(" error ") 
		expression = "" 

def clear(): 
	global expression 
	expression = "" 
	equation.set("") 


if __name__ == "__main__": 
	gui = Tk() 
	gui.configure(background="black") 

	gui.title("GIT Calculator") 
	gui.geometry("265x125") 

	equation = StringVar() 

	expression_field = Entry(gui, font=("Courier", 13) ,background="black",fg='white', textvariable=equation) 
	expression_field.grid(columnspan=14, ipadx=14, ipady=30) 

	equation.set('Enter') 
	button1 = Button(gui, text=' 1 ', fg='black', bg='#20D3F9', 
					command=lambda: press(1), height=4, width=7) 
	button1.grid(row=2, column=0) 
	button2 = Button(gui, text=' 2 ', fg='black', bg='#20D3F9', 
					command=lambda: press(2), height=4, width=7) 
	button2.grid(row=2, column=1) 
	button3 = Button(gui, text=' 3 ', fg='black', bg='#20D3F9', 
					command=lambda: press(3), height=4, width=7) 
	button3.grid(row=2, column=2) 
	button4 = Button(gui, text=' 4 ', fg='black', bg='#20D3F9', 
					command=lambda: press(4), height=4, width=7) 
	button4.grid(row=3, column=0) 
	button5 = Button(gui, text=' 5 ', fg='black', bg='#20D3F9', 
					command=lambda: press(5), height=4, width=7) 
	button5.grid(row=3, column=1) 
	button6 = Button(gui, text=' 6 ', fg='black', bg='#20D3F9', 
					command=lambda: press(6), height=4, width=7) 
	button6.grid(row=3, column=2) 
	button7 = Button(gui, text=' 7 ', fg='black', bg='#20D3F9', 
					command=lambda: press(7), height=4, width=7) 
	button7.grid(row=4, column=0) 
	button8 = Button(gui, text=' 8 ', fg='black', bg='#20D3F9', 
					command=lambda: press(8), height=4, width=7) 
	button8.grid(row=4, column=1) 
	button9 = Button(gui, text=' 9 ', fg='black', bg='#20D3F9', 
					command=lambda: press(9), height=4, width=7) 
	button9.grid(row=4, column=2) 
	button0 = Button(gui, text=' 0 ', fg='black', bg='#20D3F9', 
					command=lambda: press(0), height=4, width=7) 
	button0.grid(row=5, column=0) 
	plus = Button(gui, text=' + ', fg='black', bg='#00FF63', 
				command=lambda: press("+"), height=4, width=7) 
	plus.grid(row=2, column=3) 
	minus = Button(gui, text=' - ', fg='black', bg='#00FF63', 
				command=lambda: press("-"), height=4, width=7) 
	minus.grid(row=3, column=3) 
	multiply = Button(gui, text=' * ', fg='black', bg='#00FF63', 
					command=lambda: press("*"), height=4, width=7) 
	multiply.grid(row=4, column=3) 
	divide = Button(gui, text=' / ', fg='black', bg='#00FF63', 
					command=lambda: press("/"), height=4, width=7) 
	divide.grid(row=5, column=3) 
	equal = Button(gui, text=' = ', fg='black', bg='#00FF63', 
				command=equalpress, height=4, width=7) 
	equal.grid(row=5, column=2) 
	clear = Button(gui, text='Clear', fg='black', bg='#00FF63', 
				command=clear, height=4, width=7) 
	clear.grid(row=5, column=1) 
	gui.mainloop() 
=======
from tkinter import*

me=Tk()
me.geometry("354x460")
me.title("CALCULATOR")
melabel = Label(me,text="CALCULATOR",bg='White',font=("Courier New",30,'bold'))
melabel.pack(side=TOP)
me.config(background='Dark gray')

textin=StringVar()#nentered by the user
operator=""#used for the math symbols

def clickbut(number):   #lambda:clickbut(1)
     global operator
     operator=operator+str(number)
     textin.set(operator)

def equlbut():
     global operator
     add=float(eval(str(operator)))
     textin.set(add)
     operator=''
def equlbut():
     global operator
     sub=float(eval(str(operator)))
     textin.set(sub)
     operator=''
def equlbut():
     global operator
     mul=float(eval(str(operator)))
     textin.set(mul)
     operator=''
def equlbut():
     global operator
     div=float(eval((operator)))
     textin.set(div)
     operator=''

def clrbut():
     textin.set('')
metext=Entry(me,font=("Courier New",12,'bold'),textvar=textin,width=25,bd=5,bg='powder blue')
metext.pack()

but1=Button(me,padx=14,pady=14,bd=4,bg='white',command=lambda:clickbut(1),text="1",font=("Courier New",16,'bold'))
but1.place(x=10,y=100)

but2=Button(me,padx=14,pady=14,bd=4,bg='white',command=lambda:clickbut(2),text="2",font=("Courier New",16,'bold'))
but2.place(x=10,y=170)

but3=Button(me,padx=14,pady=14,bd=4,bg='white',command=lambda:clickbut(3),text="3",font=("Courier New",16,'bold'))
but3.place(x=10,y=240)

but4=Button(me,padx=14,pady=14,bd=4,bg='white',command=lambda:clickbut(4),text="4",font=("Courier New",16,'bold'))
but4.place(x=75,y=100)

but5=Button(me,padx=14,pady=14,bd=4,bg='white',command=lambda:clickbut(5),text="5",font=("Courier New",16,'bold'))
but5.place(x=75,y=170)

but6=Button(me,padx=14,pady=14,bd=4,bg='white',command=lambda:clickbut(6),text="6",font=("Courier New",16,'bold'))
but6.place(x=75,y=240)

but7=Button(me,padx=14,pady=14,bd=4,bg='white',command=lambda:clickbut(7),text="7",font=("Courier New",16,'bold'))
but7.place(x=140,y=100)

but8=Button(me,padx=14,pady=14,bd=4,bg='white',command=lambda:clickbut(8),text="8",font=("Courier New",16,'bold'))
but8.place(x=140,y=170)

but9=Button(me,padx=14,pady=14,bd=4,bg='white',command=lambda:clickbut(9),text="9",font=("Courier New",16,'bold'))
but9.place(x=140,y=240)

but0=Button(me,padx=14,pady=14,bd=4,bg='white',command=lambda:clickbut(0),text="0",font=("Courier New",16,'bold'))
but0.place(x=10,y=310)

butdot=Button(me,padx=47,pady=14,bd=4,bg='white',command=lambda:clickbut("."),text=".",font=("Courier New",16,'bold'))
butdot.place(x=75,y=310)

butpl=Button(me,padx=14,pady=14,bd=4,bg='white',text="+",command=lambda:clickbut("+"),font=("Courier New",16,'bold'))
butpl.place(x=205,y=100)

butsub=Button(me,padx=14,pady=14,bd=4,bg='white',text="-",command=lambda:clickbut("-"),font=("Courier New",16,'bold'))
butsub.place(x=205,y=170)

butml=Button(me,padx=14,pady=14,bd=4,bg='white',text="*",command=lambda:clickbut("*"),font=("Courier New",16,'bold'))
butml.place(x=205,y=240)

butdiv=Button(me,padx=14,pady=14,bd=4,bg='white',text="/",command=lambda:clickbut("/"),font=("Courier New",16,'bold'))
butdiv.place(x=205,y=310)

butclear=Button(me,padx=14,pady=119,bd=4,bg='white',text="CE",command=clrbut,font=("Courier New",16,'bold'))
butclear.place(x=270,y=100)


butequal=Button(me,padx=151,pady=14,bd=4,bg='white',command=equlbut,text="=",font=("Courier New",16,'bold'))
butequal.place(x=10,y=380)
me.mainloop()
