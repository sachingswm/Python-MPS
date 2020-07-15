import tkinter as tk
import mysql.connector

mydb = mysql.connector.connect(host="localhost", user = "ish" , passwd = "1234" , database = "pyprj")
if(mydb):
    print("Connection sucessfull")
else:
    print("Connection fail")
mycursor = mydb.cursor()
mycursor.close()
del mycursor
#mycursor.execute(“select * from medicine”)
class front:
    def __init__(self,master):
        self.master = master
        self.master.title("MPS")
        self.master.resizable(0,0)
        self.b1 = tk.Button(text = "Enter \n Condition",command=self.b1)
        self.f = tk.LabelFrame(master , padx = 10).pack()
        self.l1 = tk.Label(self.f , text="---------------------Medicine Prescription System---------------------\n\n This Application is designed to prescribe Medicine to the Patients.\n By entering the Disease you have you can get Medicine\n Or you can enter your Symptoms so that system can diagnose\n your disease and prescribe medicine accordingly.")
        self.l1.pack(side=tk.TOP)
        self.b2 = tk.Button(text = "Due \n Orders",command=self.b2)
        self.b3 = tk.Button(text = "Update \n Patients",command=self.b3)
        self.b1.pack(side = tk.RIGHT , pady=5,padx=5)
        self.b2.pack(side = tk.RIGHT, pady=5, padx=5)
        self.b3.pack(side = tk.RIGHT, pady=5,padx=5)

    def b1(self):
        self.newWindow = tk.Toplevel(self.master)
        self.app = direct(self.newWindow)
    def b2(self):
        self.newWindow = tk.Toplevel(self.master)
        self.app = Due(self.newWindow)
    def b3(self):
        self.newWindow = tk.Toplevel(self.master)
        self.app = upd(self.newWindow)
class upd:
    def __init__(self,master):
        self.master = master
        self.master.title("MPS")
        self.text3 = tk.StringVar()
        self.text3.set("Updation Window")
        self.l6 = tk.Label(self.master,textvariable = self.text3).grid(row=0,column=1)
        tk.Label(master, text="Customer ID").grid(row=3)
        tk.Label(master, text="Customer Name").grid(row=4)
        tk.Label(master, text="Prescription").grid(row=5)
        self.e1 = tk.Entry(master).grid(row=3, column=1)
        self.e2 = tk.Entry(master).grid(row=4, column=1)
        self.e3 = tk.Entry(master).grid(row=5, column=1)
        self.b7 = tk.Button(self.master,text = "Add\nCustomer",command=self.b7).grid(row=6,column=3,pady=5,padx=5)
        self.b8 = tk.Button(self.master,text = "Remove\nCustomer",command=self.b8).grid(row=6,column=7,pady=5,padx=5)
    def b7(self):
        self.text3.set("Addition Sucessfull")
        self.x1 = self.e1.get()
        self.x2 = self.e2.get()
        self.x3 = self.e3.get()
        mydb = mysql.connector.connect(host = "localhost",user = "ish",passwd = "1234",database = "pyprj")
        mycursor=mydb.cursor()
        mycursor.execute("insert into customers value("+self.x1+",'"+str(self.x2)+"',curdate(),curdate()+30,'"+str(self.x3)+"');")
        mycursor.close()
        del mycursor
    def b8(self):
        self.text3.set("Deletion Sucessfull")
        self.x1 = self.e1.get()
        self.x2 = self.e2.get()
        self.x3 = self.e3.get()
        mydb = mysql.connector.connect(host = "localhost",user = "ish",passwd = "1234",database = "pyprj")
        mycursor=mydb.cursor()
        mycursor.execute("insert into customers value("+self.x1+",'"+str(self.x2)+"',curdate(),curdate()+30,'"+str(self.x3)+"');")
        mycursor.close()
        del mycursor
class Due:
    def __init__(self, master):
        self.master = master
        self.master.title("MPS")
        #self.master.resizable(0,0)
        self.text1 = tk.StringVar()
        self.l5 = tk.Label(self.master,textvariable = self.text1).pack()
        self.b9 = tk.Button(self.master,text="Orders \n Completed",command=self.b9).pack(side=tk.RIGHT,padx=5,pady=5)
        mydb = mysql.connector.connect(host = "localhost", user = "ish", passwd = "1234", database = "pyprj")
        mycursor = mydb.cursor()
        mycursor.execute("select * from customers where r_date = curdate()")
        data = mycursor.fetchall();
        s1 = " "
        for i in data:
            s1+=str(i)+"\n"
        print(s1)
        self.text1.set(s1)
        del mycursor
    def b9(self):
        mydb = mysql.connector.connect(host = "localhost", user = "ish", passwd = "1234", database = "pyprj")
        mycursor = mydb.cursor()
        mycursor.execute("set sql_safe_updates = 0;update customers set l_date = curdate(),r_date = curdate()+30 where r_date=curdate();")
        mycursor.close()
        del mycursor
class direct:
    def __init__(self, master):
        self.master = master
        self.master.title("MPS")
        self.master.resizable(0,0)
        self.l1 = tk.Label(self.master , text = "Enter \n Condition").grid(row = 1 , column = 1)
        self.inp = tk.Entry(self.master , width = 30)
        self.inp.grid(row = 1 , column = 2, padx = 20 , pady = 20)
        self.b = tk.Button(self.master , text = "Enter" , command = self.medi).grid(row =1 ,column = 3, padx = 20)
        self.text = tk.StringVar()
        self.text.set(" ")
        self.l2 = tk.Label(self.master , text = "Recomended Medication :").grid( row = 2 , column = 2 , pady = 10)
        self.l3 = tk.Label(self.master , textvariable = self.text).grid( row = 3 , column = 2)
    def medi(self):
        self.text.set(" ")
        count=0
        a = self.inp.get()
        if len(a)==0:
            self.text.set("No Input Entered")
        else:
            print(a)
            mydb = mysql.connector.connect(host="localhost" , user = "ish" , passwd = "1234" , database = "pyprj")
            mycursor = mydb.cursor()
            mycursor.execute("select medi from medicine where cond ='"+a+"' ")
            for i in mycursor:
                self.text.set(i)
                break;
            else:
                self.text.set("No Medication Found")
        mycursor.close()
        del mycursor

def main():
    root = tk.Tk()
    app=front(root)
    root.mainloop()

if __name__ == "__main__":
    main()
