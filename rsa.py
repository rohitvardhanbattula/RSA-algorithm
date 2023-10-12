from tkinter import *
from PIL import ImageTk,Image
from tkinter import messagebox
from random import randint
import math

root = Tk()
root.geometry("398x300")

Label(text = "Enter text for encryption or decryption",fg = "black",font = ("calbri",13)).place(x=10,y=10)
text = Entry(root,font = ("calbri",15))
text.place(x=10,y=50,width=380,height=70)

def generate_prime():
    x = randint(2,100)
    while True:
        if is_prime(x):
            break
        else:
            x+=1
    return x

def is_prime(x):
    i = 2
    root = math.ceil(math.sqrt(x))
    while i<= root:
        if x % i == 0:
            return False
        i+=1
    return True

def gcd(a,b):
    while b:
        a,b = b,a%b
    return a

def egcd(a,b):
    if a==0:
        return(b,0,1)
    else:
        g,y,x = egcd(b%a,a)
        return (g,x-(b//a)*y,y)
    
def modinv(a,m):
    g,x,y = egcd(a,m)
    if g!=1:
        return None
    else:
        return x%m
    
p = generate_prime()
while True:
    q = generate_prime()
    if q!=p:
        break
        
print("p")
print(p)
print("q")
print(q)

n = p*q
print('n')
print(n)
#euler's totient
n1 = (p-1)*(q-1)

r = randint(2,100)
while True:
    if gcd(r,n1) == 1:
        break
    else:
        r+=1
        
e = r
print("e")
print(e)

#(e.d)modeuler==1
d = modinv(e,n1)
print("d")
print(d)

def enc():
    global enwin
    text1_en = text.get()
    e1_en = key_en.get()
    e1_en = int(e1_en)
    n1_en = n_en.get()
    n1_en = int(n1_en)
    x = []
    m=0
    for i in text1_en:
        m = ord(i)
        #ascii**encryption%product
        c = (m**e1_en)%n1_en
        x.append(c)
    enc = []
    for i in x:
        c = chr(i)
        enc.append(c)
    enc_msg = ''.join(enc)
    
    print(enc_msg)
    #enwin.withdraw()
    ans = Toplevel()
    ans.geometry("300x100")
    #ans.configure(bg = "#adaaa3")
    Label(ans,text = "The encrypted text is:",fg = "black",font = ("Helvetica",15)).grid(row=1,column=0)
    my_text1 = StringVar()
    my_text1.set(enc_msg)

    my_entry1 = Entry(ans,font = ("Helvetica",15),bd = 0,state = "readonly",textvariable = my_text1)
    #my_entry1.place(x = 10, y = 8,width = 398,height = 150)
    my_entry1.grid(row = 3,column = 0)
    #root.deiconify()
    

def dec():
    text1_de = text.get()
    e1_de = key_de.get()
    e1_de = int(e1_de)
    n1_de = n_de.get()
    n1_de = int(n1_de)
    x = []
    m=0
    for i in text1_de:
        m = ord(i)
        c = (m**e1_de)%n1_de
        x.append(c)
    dec = []
    for i in x:
        c = chr(i)
        dec.append(c)
    dec_msg = ''.join(dec)
    
    print(dec_msg)
    ans = Toplevel()
    ans.geometry("300x100")
    Label(ans,text = "The decrypted text is:",fg = "black",font = ("Helvetica",15)).grid(row=1,column=0)
    my_text1 = StringVar()
    my_text1.set(dec_msg)

    my_entry1 = Entry(ans,font = ("Helvetica",15),bd = 0,state = "readonly",textvariable = my_text1)
    #my_entry1.place(x = 10, y = 170,width = 355,height = 150)
    my_entry1.grid(row=3,column=0)
