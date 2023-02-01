import tkinter as tk
from tkinter import*
from tkinter import ttk
import tkinter.messagebox as Messagebox
import mysql.connector


root = Tk()
root.title("Insert Data")
root.geometry("800x600")
connection = mysql.connector.connect(host='localhost',user='root',password='',port='3307',database='python_mysql')
c = connection.cursor()

frame = tk.Frame(root, bg="#eee",)
frame.grid(row=0, column=0)


label_title = tk.Label(frame ,text="Title: ")

entry_title =tk.Entry(frame,width=30)

label_info = tk.Label(frame ,text="Info: ")
entry_info =tk.Entry(frame,width=30)


def insertData():
    title = entry_title.get()
    info = entry_info.get()

    if(title=="" or info==""):
        Messagebox.showinfo("Insert Status","All fields are required!")
    else:
     insert_query ="INSERT INTO `tbl_sample`(`title`,`info`) VALUES (%s,%s)"
     vals = (title,info)
     c.execute(insert_query,vals)
     connection.commit()
     entry_title.delete(0, 'end')
     entry_info.delete(0, 'end')
     Messagebox.showinfo("Insert Status","Successfully Inserted!")
     list_data()
   
button_insert = tk.Button(frame, text="Insert" ,command = insertData,width=20)

label_title.grid(row=0, column=0)
entry_title.grid(row=0, column=1)

label_info.grid(row=1, column=0)
entry_info.grid(row=1, column=1)

button_insert.grid(row=5, column=1)



def list_data():
    my_connect=mysql.connector.connect(host='localhost',user='root',password='',port='3307',database='python_mysql')
    my_conn = my_connect.cursor()
    my_conn.execute("SELECT * FROM tbl_sample limit 0,12")
    i=0
    Table_frame = Frame(root,bd=2 ,relief=RIDGE,)
    Table_frame.grid(row=12,column=0,pady=80)
    #my_w = tk.Tk()

    for sample in my_conn: 
        for j in range(len(sample)):
            e = Entry(Table_frame, width=15, fg='black',font=('Arial', 12))
            e.grid(row=i+9, column=j) 
            e.insert(END, sample[j])
            e["state"] = DISABLED
        i=i+1

    e = Label(Table_frame,width=15, text=sample[j],borderwidth=2,relief='ridge',font=('Arial', 12))
    e=Label(Table_frame,width=15,text='id',borderwidth=2, relief='ridge',anchor='w',font=('Arial', 12),fg='white',bg='grey')
    e.grid(row=9,column=0)
    e=Label(Table_frame,width=15,text='Name',borderwidth=2, relief='ridge',anchor='w',bg='grey',fg='white',font=('Arial', 12))
    e.grid(row=9,column=1)
    e=Label(Table_frame,width=15,text='Info',borderwidth=2, relief='ridge',anchor='w',bg='grey',fg='white',font=('Arial', 12))
    e.grid(row=9,column=2)
    i=1
    
list_data()


root.mainloop()




