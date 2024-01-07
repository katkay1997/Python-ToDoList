import tkinter as tk
from tkinter import messagebox

# To do List

def add_task():
    input_text = entry_task.get(1.0, "end-1c")
    if input_text == "":
        messagebox.showwarning(title="Warning!", message="Please Enter some text")
    else:
        list_contents.insert(tk.END, input_text)
        root1.destroy()

def delete_text():
    selected = list_contents.curselection()
    list_contents.delete(selected)

def task_complete():
    marked = list_contents.curselection()
    text_line = marked[0]
    # store the text of the selected item in a string
    list_item = list_contents.get(marked)
    # update it
    checkmark = list_item + " \u2713"
    list_contents.delete(text_line)
    list_contents.insert(text_line, checkmark)

def create_new_note():
    global root1  # make root1 a global variable
    root1 = tk.Toplevel(window)
    root1.geometry("300x100")
    root1.title("Enter Notes")
    global entry_task
    entry_task = tk.Text(root1, width=40, height=4)
    entry_task.pack()
    button_temp = tk.Button(root1, text="Create task", command=add_task)
    button_temp.pack()

# Main window
window = tk.Tk()
window.geometry("500x450")
window.title("To Do List")
window.resizable(0, 0)

box_frame = tk.Frame(window)
box_frame.pack()

list_contents = tk.Listbox(box_frame, bg="#FF5347", fg="#FCE6F3", height=20, width=80, font=("Arial", 12))
list_contents.pack(side=tk.LEFT)

scrolling_bar = tk.Scrollbar(box_frame)
scrolling_bar.pack(side=tk.RIGHT, fill=tk.Y)
list_contents.config(yscrollcommand=scrolling_bar.set)
scrolling_bar.config(command=list_contents.yview)

plus_button = tk.Button(window, text="Create New Note", width=20, command=create_new_note)
plus_button.pack(pady=5)

delete_button = tk.Button(window, text="Delete Note", width=20, command=delete_text)
delete_button.pack(pady=5)

done_button = tk.Button(window, text="Mark as completed", width=20, command=task_complete)
done_button.pack(pady=5)

if __name__ == '__main__':
    window.mainloop()




# import tkinter
# from tkinter import *
# from tkinter import messagebox
# from tkinter import LEFT
#
# # To do List
#
# window = Tk()
# window.geometry("500x500")
# window.title("To Do List")
# window.resizable(0, 0)
#
# boxFrame = Frame(window)
# boxFrame.pack()
#
# listContents = Listbox(boxFrame, bg = "#FF5347", fg ="#FCE6F3", height=20, width= 70, font = ("Arial", 12))
# listContents.pack(side=LEFT)
#
# scrollingBar = Scrollbar(boxFrame)
# scrollingBar.pack(side=RIGHT, fill=Y)
# listContents.config(yscrollcommand=scrollingBar.set)
# scrollingBar.config(command=listContents.yview)
#
# def firstButton():
#     input_text = ""
#     first_selected = listContents.curselection()
#     def add():
#         input_text= entry_task.get(1.0, "end-1c")
#         if input_text=="":
#             tkinter.messagebox.showwarning(title="Warning!", message= "Please Enter some text")
#         else:
#             listContents.insert(END, input_text)
#             #close root1 window
#             root1.destroy()
#
#     root1 = Tk()
#     root1.geometry("200x200")
#     root1.title("Enter Notes")
#     entry_task = Text(root1,width=40,height=4)
#     button_temp = Button(root1, text="Create task", command=add)
#     button_temp.pack()
#     root1.mainloop()
#
# def deleteText():
#     selected=listContents.curselection()
#     listContents.event_delete(selected[0])
# def taskComplete():
#     marked=listContents.curselection()
#     textLine=marked[0]
#     #store the text of selected item in a string
#     listItem = listContents.get(marked)
#     # update it
#     checkmark = listItem+ "*"
#     listContents.delete(textLine)
#     listContents.insert(textLine,checkmark)
#
#
#
#
#
# #button widget
# plusButton = Button(window, text="Create New Note", width=20, command=firstButton)
# plusButton.pack(pady=10)
#
# deleteButton = Button(window, text="Delete Note", width=20, command=deleteText)
# deleteButton.pack(pady=10)
#
# doneButton = Button(window, text="Mark as completed", width=20, command=taskComplete)
# doneButton.pack(pady=10)
# # Press the green button in the gutter to run the script.
# if __name__ == '__main__':
#     window.mainloop()







#type text in message box, click on submit button on the right side
#pop up displays text afterwards below the message box
#type another text statement, click on submit button again
#older messages at the bottom
#pop up (or button) displays the entered text
#clicking pop up (or text button) deletes the whole text
#or delete button next to each pop up entry
#have the option to .resize() window

#create a window
    #background color
    #title
    #font
    #name of title