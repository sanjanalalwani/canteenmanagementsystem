from tkinter import *
from tkinter import ttk
import tkinter.messagebox
import pymysql
class ConnectorDB:
 def __init__(self,root):
 self.root=root
 titlespace = " "
 self.root.title(102 * titlespace + "TSEC CANTEEN")
 self.root.geometry("800x700+300+0")
 self.root.resizable(width=False, height=False)
 MainFrame = Frame(self.root, bd=10, width=770, height=700,relief = RIDGE, bg='cadet blue')
 MainFrame.grid()
 TitleFrame=Frame(MainFrame, bd=7, width=770, height=100, relief=RIDGE)
 TitleFrame.grid(row=0,column=0)
 TopFrame3=Frame(MainFrame, bd=5, width=770, height=500, relief=RIDGE)
 TopFrame3.grid(row=1,column=0)
 LeftFrame=Frame(TopFrame3, bd=5, width=770, height=400, padx=2, bg="cadet blue",
relief=RIDGE)
 LeftFrame.pack(side=LEFT)
 LeftFrame1=Frame(LeftFrame, bd=5, width=600, height=180, padx=12, pady=9, relief=RIDGE)
 LeftFrame1.pack(side=TOP)
 RightFrame1=Frame(TopFrame3, bd=5, width=100, height=400, padx=2, bg="cadet blue",
relief=RIDGE)
 RightFrame1.pack(side=RIGHT)
 RightFrame1a=Frame(RightFrame1, bd=5, width=90, height=300, padx=2, pady=2, relief=RIDGE)
 RightFrame1a.pack(side=TOP)
 studentID=StringVar()
 Firstname=StringVar()
 Surname=StringVar()
 Address=StringVar()
 Gender=StringVar()
 Mobile=StringVar()
 def iExit():
 iExit=tkinter.messagebox.askyesno("TSEC CANTEEN","Confirm if you want to exit")
 if iExit>0:
 root.destroy()
 return
 def Reset():
 self.entstudentID.delete(0,END)
 self.entFirstname.delete(0,END)
 self.entsurname.delete(0,END)
 self.entAddress.delete(0,END)
 Gender.set(" ")
 self.entMobile.delete(0,END)
 def addData():
 if studentID.get()=="" or Firstname.get()=="" or Surname.get()=="":
 tkinter.messagebox.showerror("TSEC CANTEEN","Enter Correct Details")
 else:
sqlCon=pymysql.connect(host="localhost",user="root",password="7777",database="tseccanteendb"
)
 cur =sqlCon.cursor()
 cur.execute("insert into tseccanteendb
values(%s,%s,%s,%s,%s,%s)",(studentID.get(),Firstname.get(),Surname.get(),Address.get(),Gender.get
(),Mobile.get()))
 sqlCon.commit()
 sqlCon.close()
 tkinter.messagebox.showinfo("TSEC CANTEEN","Record Entered Successfully")
 def DisplayData():
 if studentID.get()=="" or Firstname.get()=="" or Surname.get()=="":
 tkinter.messagebox.showerror("TSEC CANTEEN","Emter Correct Details")
 else:
sqlCon=pymysql.connect(host="localhost",user="root",password="7777",database="tseccanteendb"
)
 cur =sqlCon.cursor()
 cur.execute("select * from tseccanteendb")
 result=cur.fetchall()
 if len(result)!=0:
 self.student_records.delete(*self.student_records.get_children())
 for row in result:
 self.student_records.insert('',END,values=row)
 sqlCon.commit()
 sqlCon.close()
 def CanteenInfo(ev):
 viewInfo=self.student_records.focus()
 learnerData=self.student_records.item(viewInfo)
 row=learnerData['values']
 studentID.set(row[0])
 Firstname.set(row[1])
 Surname.set(row[2])
 Address.set(row[3])
 Gender.set(row[4])
 Mobile.set(row[5])
 def update():
sqlCon=pymysql.connect(host="localhost",user="root",password="7777",database="tseccanteendb"
)
 cur =sqlCon.cursor()
 cur.execute("update tseccanteendb set
firstname=%s,surname=%s,address=%s,gender=%s,mobile=%s where studentID=%s", (
 Firstname.get(),
 Surname.get(),
 Address.get(),
 Gender.get(),
 Mobile.get(),
 studentID.get()
 ))
 sqlCon.commit()
 sqlCon.close()
 tkinter.messagebox.showinfo("TSEC CANTEEN","Record Updated Successfully")
 def deleteDB():
sqlCon=pymysql.connect(host="localhost",user="root",password="7777",database="tseccanteendb"
)
 cur =sqlCon.cursor()
 cur.execute("delete from tseccanteendb where studentID=%s",studentID.get())
 sqlCon.commit()
 DisplayData()
 sqlCon.close()
 tkinter.messagebox.showinfo("TSEC CANTEEN","Record Deleted Successfully")
 Reset()
 def searchDB():
 try:
sqlCon=pymysql.connect(host="localhost",user="root",password="7777",database="tseccanteendb"
)
 cur =sqlCon.cursor()
 cur.execute("select * from tseccanteendb where studentId=%s",studentID.get())
 row=cur.fetchone()
 studentID.set(row[0])
 Firstname.set(row[1])
 Surname.set(row[2])
 Address.set(row[3])
 Gender.set(row[4])
 Mobile.set(row[5])
 sqlCon.commit()
 except:
 tkinter.messagebox.showinfo("TSEC CANTEEN","No Such Record Found")
 Reset()
 sqlCon.close()
 self.lbtitle=Label(TitleFrame, font=('arial',40,'bold'), text="TSEC CANTEEN",bd=7)
 self.lbtitle.grid(row=0,column=0,padx=132)
 self.lblstudentID=Label(LeftFrame1, font=('arial',12,'bold'), text="Roll Number",bd=7)
 self.lblstudentID.grid(row=0,column=0,sticky=W, padx=5)
 self.entstudentID=Entry(LeftFrame1, font=('arial',12,'bold'),bd=5, width=44,
justify='left',textvariable=studentID)
 self.entstudentID.grid(row=0,column=1,sticky=W, padx=5)
 self.lblFirstname=Label(LeftFrame1, font=('arial',12,'bold'), text="Name",bd=7)
 self.lblFirstname.grid(row=1,column=0,sticky=W, padx=5)
 self.entFirstname=Entry(LeftFrame1, font=('arial',12,'bold'),bd=5, width=44,
justify='left',textvariable=Firstname)
 self.entFirstname.grid(row=1,column=1,sticky=W, padx=5)
 self.lblsurname=Label(LeftFrame1, font=('arial',12,'bold'), text="Branch",bd=7)
 self.lblsurname.grid(row=2,column=0,sticky=W, padx=5)
 self.entsurname=Entry(LeftFrame1, font=('arial',12,'bold'),bd=5, width=44,
justify='left',textvariable=Surname)
 self.entsurname.grid(row=2,column=1,sticky=W, padx=5)
 self.lblAddress=Label(LeftFrame1, font=('arial',12,'bold'), text="Division",bd=7)
 self.lblAddress.grid(row=3,column=0,sticky=W, padx=5)
 self.entAddress=Entry(LeftFrame1, font=('arial',12,'bold'),bd=5, width=44,
justify='left',textvariable=Address)
 self.entAddress.grid(row=3,column=1,sticky=W, padx=5)
 self.lblGender=Label(LeftFrame1, font=('arial',12,'bold'), text="Menu",bd=5)
 self.lblGender.grid(row=4,column=0,sticky=W, padx=5)
 self.cboGender=ttk.Combobox(LeftFrame1, font=('arial',12,'bold'),
width=42,state='readonly',textvariable=Gender)
 self.cboGender['values']=(' ','dal_pakwan','veg thali','samosa','chai','koki','masala toast','misal
pav','dosa','pizza','burger','coffee','uttapa','pav bhaji','fried rice','noodels','nachos','dhokla','mango
juice','pastry','gulab jamun')
 self.cboGender.current(0)
 self.cboGender.grid(row=4,column=1)
 self.lblMobile=Label(LeftFrame1, font=('arial',12,'bold'), text="Quantity",bd=5)
 self.lblMobile.grid(row=5,column=0,sticky=W, padx=5)
 self.entMobile=Entry(LeftFrame1, font=('arial',12,'bold'),bd=5, width=44,
justify='left',textvariable=Mobile)
 self.entMobile.grid(row=5,column=1,sticky=W, padx=5)
 scroll_y=Scrollbar(LeftFrame, orient= VERTICAL)
 self.student_records=ttk.Treeview(LeftFrame, height=14,
columns=("rollno","name","branch","division","menu","quantity"), yscrollcommand=scroll_y.set)
 scroll_y.pack(side=RIGHT,fill=Y)
 self.student_records.heading("rollno",text="RollNumber")
 self.student_records.heading("name",text="Name")
 self.student_records.heading("branch",text="Branch")
 self.student_records.heading("division",text="Division")
 self.student_records.heading("menu",text="Menu")
 self.student_records.heading("quantity",text="Quantity")
 self.student_records['show']='headings'
 self.student_records.column("rollno",width=70)
 self.student_records.column("name",width=100)
 self.student_records.column("branch",width=100)
 self.student_records.column("division",width=100)
 self.student_records.column("menu",width=70)
 self.student_records.column("quantity",width=70)
 self.student_records.pack(fill=BOTH, expand=1)
 self.student_records.bind("<ButtonRelease-1>",CanteenInfo)
 #DisplayData()
 self.btnAddNew=Button(RightFrame1a,font=('arial',16,'bold'),text="Add
New",bd=4,pady=1,padx=24,
 width=8,height=2,command=addData).grid(row=0,column=0,padx=1)
 self.btnDisplay=Button(RightFrame1a,font=('arial',16,'bold'),text="Display",bd=4,pady=1,padx=24,
 width=8,height=2,command=DisplayData).grid(row=1,column=0,padx=1)
self.btnUpdate=Button(RightFrame1a,font=('arial',16,'bold'),text="Update",bd=4,pady=1,padx=24,
 width=8,height=2,command=update).grid(row=2,column=0,padx=1)
 self.btnDelete=Button(RightFrame1a,font=('arial',16,'bold'),text="Delete",bd=4,pady=1,padx=24,
 width=8,height=2,command=deleteDB).grid(row=3,column=0,padx=1)
self.btnSearch=Button(RightFrame1a,font=('arial',16,'bold'),text="Search",bd=4,pady=1,padx=24,
 width=8,height=2,command=searchDB).grid(row=4,column=0,padx=1)
 self.btnReset=Button(RightFrame1a,font=('arial',16,'bold'),text="Reset",bd=4,pady=1,padx=24,
 width=8,height=2, command=Reset).grid(row=5,column=0,padx=1)
 self.btnExit=Button(RightFrame1a,font=('arial',16,'bold'),text="Exit",bd=4,pady=1,padx=24,
 width=8,height=2,command=iExit).grid(row=6,column=0,padx=1)
if __name__=='__main__':
 root=Tk()
 application=ConnectorDB(root)
 root.mainloop()