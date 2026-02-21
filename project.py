import tkinter as tk
from tkinter import messagebox

# Create main window
root = tk.Tk()
root.title("Student Management System")
root.geometry("800x500")

# ===== Title (Bold) =====
title = tk.Label(root,
                 text="Student Management System",
                 font=("Arial", 20, "bold"))
title.pack(pady=10)

# ===== Form Frame =====
form_frame = tk.Frame(root)
form_frame.pack(pady=10)

# Name
tk.Label(form_frame, text="Name").grid(row=0, column=0, padx=5, pady=5)
name_entry = tk.Entry(form_frame)
name_entry.grid(row=0, column=1, padx=5, pady=5)

# Age
tk.Label(form_frame, text="Age").grid(row=1, column=0, padx=5, pady=5)
age_entry = tk.Entry(form_frame)
age_entry.grid(row=1, column=1, padx=5, pady=5)

# Course
tk.Label(form_frame, text="Course").grid(row=2, column=0, padx=5, pady=5)
course_entry = tk.Entry(form_frame)
course_entry.grid(row=2, column=1, padx=5, pady=5)

# Gender
tk.Label(form_frame, text="Gender").grid(row=3, column=0, padx=5, pady=5)

gender_var = tk.StringVar()
gender_var.set("Male")

tk.Radiobutton(form_frame, text="Male", variable=gender_var, value="Male").grid(row=3, column=1)
tk.Radiobutton(form_frame, text="Female", variable=gender_var, value="Female").grid(row=3, column=2)

# ===== Functions =====
def add_student():
    name = name_entry.get()
    age = age_entry.get()
    course = course_entry.get()
    gender = gender_var.get()

    if name == "" or age == "" or course == "":
        messagebox.showwarning("Warning", "Please fill all fields!")
        return

    student_data = f"Name: {name} | Age: {age} | Course: {course} | Gender: {gender}"
    listbox.insert(tk.END, student_data)

    # Clear entries
    name_entry.delete(0, tk.END)
    age_entry.delete(0, tk.END)
    course_entry.delete(0, tk.END)

def delete_student():
    selected = listbox.curselection()
    if not selected:
        messagebox.showwarning("Warning", "Please select a record to delete!")
        return
    listbox.delete(selected)

# ===== Add Button =====
add_button = tk.Button(root, text="Add Student", command=add_student)
add_button.pack(pady=5)

# ===== Listbox (Display Area) =====
listbox = tk.Listbox(root, width=100, height=10)
listbox.pack(pady=10)

# ===== Delete Button (Bottom) =====
delete_button = tk.Button(root, text="Delete Selected", command=delete_student)
delete_button.pack(pady=10)

# Run window
root.mainloop()
