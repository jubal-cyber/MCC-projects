import sqlite3
from tkinter import *
from tkinter import messagebox

# Database connection
conn = sqlite3.connect("users.db")
cursor = conn.cursor()

# Create table
cursor.execute("""
CREATE TABLE IF NOT EXISTS users (
    username TEXT,
    password TEXT
)
""")

# Insert default user
cursor.execute("INSERT INTO users VALUES ('admin', '1234')")
conn.commit()

# Login function
def login():
    username = entry_username.get()
    password = entry_password.get()

    cursor.execute(
        "SELECT * FROM users WHERE username=? AND password=?",
        (username, password)
    )

    result = cursor.fetchone()

    if result:
        messagebox.showinfo("Login", "Login Successful!")
    else:
        messagebox.showerror("Login", "Invalid Username or Password")

# GUI Window
root = Tk()
root.title("Login System")
root.geometry("300x200")

Label(root, text="Username").pack(pady=5)
entry_username = Entry(root)
entry_username.pack()

Label(root, text="Password").pack(pady=5)
entry_password = Entry(root, show="*")
entry_password.pack()

Button(root, text="Login", command=login).pack(pady=20)

root.mainloop()

conn.close()