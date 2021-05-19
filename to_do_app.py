from tkinter import *
def remove():
    ind = listbox.curselection()
    if ind:
        file = open("todo.txt","r")
        notes = file.readlines()
        file.close()
        file = open('todo.txt','w')
        notes.pop(ind[0])
        for i in notes:
            file.write(i)
        file.close()
        listbox.delete(ANCHOR)

def add():
    note = text.get()
    if note:
        file = open("todo.txt","a+")
        listbox.insert(END,note)
        textbox.delete(0,END)
        file.write(note+'\n')
        file.close()

root = Tk()
text = StringVar()
root.title("TO DO APP")
root.geometry("500x550")
root.configure(bg = '#D5CABD')
frame = Frame(root,height = 455,width = 399)
frame.pack()
listbox = Listbox(frame,height = 27,width = 60,font = ('arial',10))
ysb = Scrollbar(frame, orient=VERTICAL, command=listbox.yview)
xsb = Scrollbar(frame, orient=HORIZONTAL, command=listbox.xview)
listbox.configure(yscroll=ysb.set, xscroll=xsb.set)
listbox.grid(row = 0,column = 0)
ysb.grid(row=0, column=1, sticky='ns')
xsb.grid(row=1, column=0, sticky='ew')
textbox = Entry(root,width = 30,font = 10,textvariable = text)
textbox.pack()
add_button = Button(root,text = "Add Note",command = add)
add_button.place(x = 110,y = 515)
remove_button = Button(root,text = "Remove Note",command=remove)
remove_button.place(x = 310,y = 515)
file = open("todo.txt",'r')
prev = file.readlines()
file.close()
for i in prev:
    listbox.insert(END,i)
root.mainloop()
