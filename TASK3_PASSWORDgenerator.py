import tkinter as tk
import random
import string
def generate_password():
    password_length = int(length_entry.get())
    characters=string.ascii_letters + string.digits + string.punctuation
    generated_password=''.join(random.choice(characters) for _ in range(password_length))
    password_label.config(text=generated_password)
root=tk.Tk()
root.title("password Generator")
user_label=tk.Label(root,text="user name:")
user_label.pack()
user_entry=tk.Entry(root)
user_entry.pack()
length_label=tk.Label(root,text="password length:")
length_label.pack()
length_entry=tk.Entry(root)
length_entry.pack()
generate_button=tk.Button(root,text="Generate password",command=generate_password)
generate_button.pack()
password_label=tk.Label(root,text="")
password_label.pack()
root.mainloop()
