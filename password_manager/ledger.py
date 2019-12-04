# Simple password manager system
# Borrowed from Martial Himanshu for personal learning purposes.  All rights reserved by Martial Himanshu for initial build.
# Developed By: Lucas Carlson: https://github.com/lucascrlsn

from tkinter import *
import tkinter as ttk
import ledger_bk
import tkinter.messagebox
import datetime
import time
import pyperclip
from time import strftime, ctime, gmtime

window = Tk()
window.title("Password Manager")
window.geometry('800x400')
# highlight color = box around GUI
window.config(bg='light grey', highlightcolor='red', highlightthickness=5, highlightbackground='black', relief='sunken',
              borderwidth=5, pady=8)
toolbar = Frame(window, bg='black')


def copy_password():
    # Copies password from the GUI
    p = e3.get()  # Current password in e3 password entry widget
    n = e1.get()  # Current name off account password belongs to in e1 entry widget
    pyperclip.copy(p)
    print(datetime.datetime.strptime(time.ctime(), "%a %b %d %H:%M:%S %Y")), print(
        ' ' + '|' + ' ' + 'User copied the' + ' ' + n + ' ' + 'account password to the clipboard')


def view_command():
    lb.delete(0,END)
    lb_2.delete(0,END)
    for row in ledger_bk.viewall():
        lb.insert(END,row)
    print(datetime.datetime.strptime(time.ctime(), "%a %b %d %H:%M:%S %Y")), print(' ' + '|' + ' ' + 'User viewed all records')


def search_command():
    lb.delete(0,END)
    for row in ledger_bk.search(name=name.get(),user=user.get(),password=password.get(),category=category.get(),url=url.get()):
        lb.insert(END,row)
    print(datetime.datetime.strptime(time.ctime(), "%a %b %d %H:%M:%S %Y")), print(' ' + '|' + ' ' +
                                                                                   'User searched records')


def add_command():
    # print(get_date)
    ledger_bk.add(name.get(),user.get(),password.get(),category.get(),url.get())
    lb.delete(0,END)
    lb.insert(END,name.get())
    lb_2.insert(END, user.get(), password.get(), category.get(), url.get())
    e1.delete(0,END)
    e2.delete(0,END)
    e3.delete(0,END)
    e4.delete(0,END)
    e5.delete(0,END)
    print(datetime.datetime.strptime(time.ctime(), "%a %b %d %H:%M:%S %Y")), print(' ' + '|' + ' ' +
                                                                                   'User added a record')


def get_selected_row(event):
    # Fills all entries
    try:
        global selected_tuple
        index=lb.curselection()[0]
        selected_tuple = lb.get(index)
        e1.delete(0,END)
        e1.insert(END,selected_tuple[1])
        e2.delete(0,END)
        e2.insert(END,selected_tuple[2])
        e3.delete(0,END)
        e3.insert(END,selected_tuple[3])
        e4.delete(0,END)
        e4.insert(END,selected_tuple[4])
        e5.delete(0,END)
        e5.insert(END,selected_tuple[5])
        lb_2.delete(0,END)
        lb_2.insert(END, user.get(), password.get(), category.get(), url.get())
    except IndexError:
        pass


def get_selected_metadata(event):
    # Fills all entries
    try:
        global selected_tuple
        index=lb.curselection()[0]
        selected_tuple = lb.get(index)
        e1.delete(0,END)
        e1.insert(END,selected_tuple[1])
        e2.delete(0,END)
        e2.insert(END,selected_tuple[2])
        e3.delete(0,END)
        e3.insert(END,selected_tuple[3])
        e4.delete(0,END)
        e4.insert(END,selected_tuple[4])
        e5.delete(0,END)
        e5.insert(END,selected_tuple[5])
    except IndexError:
        pass


def update_command():
    ledger_bk.update(selected_tuple[0],name.get(),user.get(),password.get(),category.get(),url.get())
    view_command()
    r = name.get()
    print(datetime.datetime.strptime(time.ctime(), "%a %b %d %H:%M:%S %Y")), print(' ' + '|' + ' ' + 'User updated the'
                                                                                   + r + 'record')


def delete_command():
    # lb.delete(END,get_selected_row.selected_tuple)
    tkinter.messagebox.askyesno(title='Alert', message='''Are you sure you want to delete this record? 
    This action cannot be undone.''')
    ledger_bk.delete(selected_tuple[0])
    print(datetime.datetime.strptime(time.ctime(), "%a %b %d %H:%M:%S %Y")), print(' ' + '|' + ' ' +
                                                                                   'User deleted a record')
    lb.delete(0, END)
    for row in ledger_bk.viewall():
        lb.insert(END, row)


def clear_command():
    lb.delete(0,END)
    lb_2.delete(0, END)
    e1.delete(0,END)
    e2.delete(0,END)
    e3.delete(0,END)
    e4.delete(0,END)
    e5.delete(0,END)
    print(datetime.datetime.strptime(time.ctime(), "%a %b %d %H:%M:%S %Y")), print(' ' + '|' + ' ' +
                                                                                   'User cleared all records')


l1 = Label(window,text="Name")
l1.grid(row=0,column=0, sticky=E)
l2 = Label(window,text="Username/Email")
l2.grid(row=1,column=0, sticky=E)
l3 = Label(window,text="Password")
l3.grid(row=2,column=0, sticky=E)
l4 = Label(window,text="Category")
l4.grid(row=3,column=0, sticky=E)
l5 = Label(window,text="URL")
l5.grid(row=4,column=0, sticky=E)

name = StringVar()
e1 = ttk.Entry(window,textvariable=name,width=25)
e1.grid(row=0,column=2,columnspan=10, sticky=W)

user = StringVar()
e2 = ttk.Entry(window,textvariable=user,width=25)
e2.grid(row=1,column=2,columnspan=10, sticky=W)

# show='*' in line e3 to show *** when password entered
password = StringVar()
e3 = ttk.Entry(window,textvariable=password, width=25, show='*')
e3.grid(row=2,column=2,columnspan=10, sticky=W)

category = StringVar()
e4 = ttk.Entry(window,textvariable=category,width=25)
e4.grid(row=3,column=2,columnspan=10, sticky=W)

url = StringVar()
e5 = ttk.Entry(window,textvariable=url,width=25)
e5.grid(row=4,column=2,columnspan=10, sticky=W)

b1 = ttk.Button(window,text="Add",width=12, command=add_command)
b1.grid(row=6,column=0, padx=10)

b2 = ttk.Button(window,text="Update",width=12,command=update_command)
b2.grid(row=7,column=0, padx=10)

b3 = ttk.Button(window,text="Search",width=12,command=search_command)
b3.grid(row=8,column=0, padx=10)

b4 = ttk.Button(window,text="View All",width=12,command=view_command)
b4.grid(row=9,column=0, padx=10)

b5 = ttk.Button(window,text="Delete",width=12,command=delete_command)
b5.grid(row=10,column=0, padx=10)

b6 = ttk.Button(window,text="Clear All",width=12,command=clear_command)
b6.grid(row=11,column=0, padx=10)

b7 = ttk.Button(window,text="Close", width=12, command=window.destroy)
b7.grid(row=12, column=0, padx=10)

# Str Var Action Buttons, needs better grid management before IMP

b8 = ttk.Button(window,text="Copy",width=12, command=copy_password)
b8.grid(row=2,column=3, padx=10)

# # Combobox for email service
# email_service_chooser = ttk.Combobox(window, width="10", values=['gmail', 'outlook', 'aol', 'icloud', 'mail'])
# email_service_chooser.current(0)
# email_service_chooser.grid(row=1,column=5)
# # End Combobox
#
# # Combobox for email domain
# email_domain_chooser = ttk.Combobox(window, width="10", values=['.com', '.edu', '.net', '.mil', '.org'])
# email_domain_chooser.current(0)
# email_domain_chooser.grid(row=1,column=6)
# # End Combobox

# listbox_1
lb = Listbox(window,height=10, width=30, highlightcolor='black', highlightthickness=3, exportselection=False)
lb.grid(row=6,column=2,rowspan=8, pady=10)

sb = Scrollbar(window)
sb.grid(row=7,column=1,rowspan=8, padx=5)
lb.configure(yscrollcommand=sb.set)
sb.configure(command=lb.yview)

# listbox_2
lb_2 = Listbox(window, height=10, width=30, highlightcolor='black', highlightthickness=3, exportselection=False)
lb_2.grid(row=6,column=3,columnspan=6,rowspan=8, pady=10)

lb.bind('<<ListboxSelect>>',get_selected_row)
window.mainloop()
