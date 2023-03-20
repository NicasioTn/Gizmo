from tkinter import *
import hashlib
import os
import re

myGui = Tk()
myGui.geometry('500x400+700+250')
myGui.title('Password Generator')
guiFont = font = dict(family='Courier New, monospaced', size=18, color='#7f7f7f')


#====== Password Entry ==========
eLabel = Label(myGui, text="Please Enter you Password:   ", font=guiFont)
eLabel.grid(row=0, column=0)
ePassword = Entry(myGui, show="*")
ePassword.grid(row=0, column=1)



#====== Strength Check =======


def checkPassword():
    strength = ['Password can not be Blank', 'Very Weak', 'Weak', 'Medium', 'Strong', 'Very Strong']
    score = 1
    password = ePassword.get()
    print(password, len(password))

    if len(password) == 0:
        passwordStrength.set(strength[0])
        return

    if len(password) < 4:
        passwordStrength.set(strength[1])
        return

    if len(password) >= 8:
        score += 1

    if re.search("[0-9]", password):
        score += 1

    if re.search("[a-z]", password) and re.search("[A-Z]", password):
        score += 1

    if re.search(".", password):
        score += 1

    passwordStrength.set(strength[score])

passwordStrength = StringVar()
checkStrBtn = Button(myGui, text="Check Strength", command=checkPassword, height=2, width=25, font=guiFont)
checkStrBtn.grid(row=2, column=0)
checkStrLab = Label(myGui, textvariable=passwordStrength)
checkStrLab.grid(row=2, column=1, sticky=W)

#====== Hash the Password ======


def passwordHash():
    hash_obj1 = hashlib.md5()
    pwmd5 = ePassword.get().encode('utf-8')
    hash_obj1.update(pwmd5)
    md5pw.set(hash_obj1.hexdigest())

md5pw = StringVar()
hashBtn = Button(myGui, text="Generate Hash", command=passwordHash, height=2, width=25, font=guiFont)
hashBtn.grid(row=3, column=0)
hashLbl = Label(myGui, textvariable=md5pw)
hashLbl.grid(row=3, column=1, sticky=W)


#====== Log the Hash to a file =======


def hashlog():
    loghash = md5pw.get()

    if os.path.isfile('password_hash_log.txt'):
        obj1 = open('password_hash_log.txt', 'a')
        obj1.write(loghash)
        obj1.write("\n")
        obj1.close()

    else:
        obj2 = open('password_hash_log.txt', 'w')
        obj2.write(loghash)
        obj2.write("\n")
        obj2.close()

btnLog = Button(myGui, text="Log Hash", command=hashlog, height=2, width=25, font=guiFont)
btnLog.grid(row=4, column=0)

#====== Re enter password and check against stored hash ======
lblVerify = Label(myGui, text="Enter Password to Verify:   ", font=guiFont)
lblVerify.grid(row=5, column=0, sticky=W)


myGui.mainloop()