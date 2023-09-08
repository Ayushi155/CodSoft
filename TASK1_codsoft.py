import tkinter as tk
def addtask():
    task=task_entry.get()
    if task:
        task_list.insert(tk.END,task)
        task_entry.delete(0,tk.END)
def removetask():
    selected_task_index=task_list.curselection()
    if selected_task_index:
       task_list.delete(selected_task_index)
root=tk.Tk()
root.title("to-do list")
task_entry=tk.Entry(root)
add_button=tk.Button(root,text="add task",command=addtask)
remove_button=tk.Button(root,text="remove task",command=removetask)
task_list=tk.Listbox(root)
task_entry.pack(pady=10)
add_button.pack()
remove_button.pack()
task_list.pack()
root.mainloop()
