from tkinter import*

from tkinter import messagebox
class login:
    def __init__(self,root):
        
        self.root=root
        self.root.title("login system")
        self.root.geometry("800x600+100+50")
        self.root.resizable(False,False)

     

        Frame_login= Frame(self.root,bg= "black")
        Frame_login.place(x = 0, y =0,height = 2400 ,width = 3000)

        # frame login
        Frame_login = Frame(self.root,bg ="gray")
        Frame_login.place(x = 150, y = 150,height = 400 ,width = 600)


        title = Label(Frame_login,text = "Login Here",font=("Impact",35,"bold"),fg="black",bg = "gray").place(x = 90,y = 30)
        desc = Label(Frame_login,text = "Accountant Employee Login Area",font=("Goudyvold Style",15,"bold"),fg="black",bg="gray").place(x = 90,y = 100)


        lbl_user=Label(Frame_login,text="Username",font=("Goundy old style",15,"bold"),fg="#1d1d1d",bg="gray").place(x=90,y=140)
        self.txt_user=Entry(Frame_login,font=("time new roman",15))
        self.txt_user.place(x=90,y=170,width=350,height=35)

        lbl_user=Label(Frame_login,text="Email address",font=("Goundy old style",15,"bold"),fg="#1d1d1d",bg="gray").place(x=90,y=210)
        self.txt_email=Entry(Frame_login,font=("time new roman",15))
        self.txt_email.place(x=90,y=240,width=350,height=35)

        lbl_user=Label(Frame_login,text="Password",font=("Goundy old style",15,"bold"),fg="#1d1d1d",bg="gray").place(x=90,y=275)
        self.txt_pass=Entry(Frame_login,font=("time new roman",15))
        self.txt_pass.place(x=90,y=300,width=350,height=35)

        forget_btn=Button(command=Frame_login,text ="Forget password?",cursor="hand2",bg="gray",fg="#1d1d1d",bd=0,font=("times new roman",12)).place(x=240,y=485)
        Login_btn=Button(self.root,command=self.login_function,cursor="hand2",text="Login",fg="black",bg="gray",font=("times new roman",20)).place(x=300,y=520)

    def login_function(self):
        if self.txt_user.get()=="" or self.txt_pass.get()==""  or self.txt_email.get()=="":
             messagebox.showerror("Error","All fields are required",parent=self.root)
        elif self.txt_user.get()!="thanshi" or self.txt_pass.get()!="123456"  or self.txt_email.get()!="thanshi@gmail.com":
             messagebox.showerror("Error","Invalid Username/Password",parent=self.root)
              
        else:
             messagebox.showinfo("welcome",f"welcome{self.txt_user.get()}\nYour password:{self.txt_pass.get()}",parent=self.root)   


root = Tk()


obj = login(root)
root.mainloop()    
