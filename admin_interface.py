import tkinter as tk
from tkinter import ttk, messagebox
from admin_backend import get_staff, add_staff, delete_staff, get_all_bookings, cancel_booking
from service_interface import service_interface  # Reuse the service interface

def admin_interface(admin_name):
    def refresh_staff_list():
        # Clear the treeview
        for item in staff_tree.get_children():
            staff_tree.delete(item)
        # Fetch updated staff list
        staff = get_staff()
        for index, person in enumerate(staff):
            staff_tree.insert("", "end", values=(index + 1, *person))

    def add_new_staff():
        name = name_entry.get()
        role = role_entry.get()
        email = email_entry.get()
        if not name or not role or not email:
            messagebox.showerror("Error", "All fields are required!")
            return
        add_staff(name, role, email)
        messagebox.showinfo("Success", "Staff member added successfully!")
        refresh_staff_list()

    def delete_selected_staff():
        selected_item = staff_tree.selection()
        if not selected_item:
            messagebox.showerror("Error", "Please select a staff member to delete.")
            return
        row_index = int(staff_tree.item(selected_item)["values"][0]) - 1
        delete_staff(row_index)
        messagebox.showinfo("Success", "Staff member deleted successfully!")
        refresh_staff_list()

    def refresh_bookings_list():
        # Clear the treeview
        for item in bookings_tree.get_children():
            bookings_tree.delete(item)
        # Fetch updated bookings
        bookings = get_all_bookings()
        for index, booking in enumerate(bookings):
            bookings_tree.insert("", "end", values=(index + 1, *booking))

    def cancel_selected_booking():
        selected_item = bookings_tree.selection()
        if not selected_item:
            messagebox.showerror("Error", "Please select a booking to cancel.")
            return
        row_index = int(bookings_tree.item(selected_item)["values"][0]) - 1
        cancel_booking(row_index)
        messagebox.showinfo("Success", "Booking cancelled successfully!")
        refresh_bookings_list()

    window = tk.Tk()
    window.title(f"Admin Dashboard - {admin_name}")
    window.geometry("800x600")

    # Service Management Section
    tk.Label(window, text="Service Management").pack()
    tk.Button(window, text="Manage Services", command=lambda: service_interface("Admin")).pack(pady=10)

    # Staff Management Section
    tk.Label(window, text="Staff Management").pack()
    staff_frame = tk.Frame(window)
    staff_frame.pack(pady=10)

    staff_tree = ttk.Treeview(staff_frame, columns=("Index", "Name", "Role", "Email"), show="headings", height=5)
    for col in ("Index", "Name", "Role", "Email"):
        staff_tree.heading(col, text=col)
        staff_tree.column(col, width=100)
    staff_tree.pack(side=tk.LEFT)

    staff_scrollbar = tk.Scrollbar(staff_frame, command=staff_tree.yview)
    staff_scrollbar.pack(side=tk.RIGHT, fill=tk.Y)
    staff_tree.config(yscrollcommand=staff_scrollbar.set)

    refresh_staff_list()

    # Add and delete staff
    staff_form = tk.Frame(window)
    staff_form.pack(pady=10)
    tk.Label(staff_form, text="Name:").grid(row=0, column=0)
    name_entry = tk.Entry(staff_form)
    name_entry.grid(row=0, column=1)
    tk.Label(staff_form, text="Role:").grid(row=0, column=2)
    role_entry = tk.Entry(staff_form)
    role_entry.grid(row=0, column=3)
    tk.Label(staff_form, text="Email:").grid(row=0, column=4)
    email_entry = tk.Entry(staff_form)
    email_entry.grid(row=0, column=5)

    tk.Button(staff_form, text="Add Staff", command=add_new_staff).grid(row=1, column=0, columnspan=3)
    tk.Button(staff_form, text="Delete Staff", command=delete_selected_staff).grid(row=1, column=3, columnspan=3)

    # Booking Management Section
    tk.Label(window, text="Booking Management").pack()
    bookings_tree = ttk.Treeview(window, columns=("Index", "Booking ID", "Customer Name", "Service Name", "Date", "Time", "Staff Name", "Status"), show="headings", height=5)
    for col in ("Index", "Booking ID", "Customer Name", "Service Name", "Date", "Time", "Staff Name", "Status"):
        bookings_tree.heading(col, text=col)
        bookings_tree.column(col, width=100)
    bookings_tree.pack(pady=10)

    refresh_bookings_list()

    tk.Button(window, text="Cancel Booking", command=cancel_selected_booking).pack(pady=10)

    window.mainloop()
