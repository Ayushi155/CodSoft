import tkinter as tk
def on_click(button):
    current_text=display_var.get()
    if button == '=':
        try:
            result= eval(current_text)
            display_var.set(str(result))
        except Exception as e:
            display_var.set("Error")
    elif button =='c':
        display_var.set("")
    else:
        display_var.set(current_text + button)
root=tk.Tk()
root.title("calculator")
display_var=tk.StringVar()
display_var.set("")
display_label=tk.Label(root,textvariable=display_var,font=("Helvetica",18),anchor="e",bd=10)
display_label.grid(row=0,column=0,columnspan=4)
button_texts=[
    ['7','8','9','/'],
    ['4','5','6','*'],
    ['1','2','3','-'],
    ['0','.','=','+'],
    ['c']
    ]
for i in range(len(button_texts)):
    for j in range(len(button_texts[i])):
        button_text=button_texts[i][j]
        button=tk.Button(root,text=button_text,font=("Helvetica",14),padx=20,pady=20,command=lambda text=button_text: on_click(text))
        button.grid(row=i+1,column=j)
root.mainloop()
