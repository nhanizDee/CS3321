import tkinter as tk
from tkinter import ttk, messagebox
from service_backend import get_services, add_service, edit_service, delete_service

def service_interface(role):
    def refresh_services():
        # Clear the treeview
        for item in tree.get_children():
            tree.delete(item)
        # Fetch updated services
        services = get_services()
        for index, service in enumerate(services):
            tree.insert("", "end", values=(index + 1, *service))

    def add_new_service():
        if role != "Admin":
            return
        name = name_entry.get()
        category = category_entry.get()
        duration = duration_entry.get()
        price = price_entry.get()
        if not name or not category or not duration or not price:
            messagebox.showerror("Error", "All fields are required!")
            return
        add_service(name, category, duration, price)
        messagebox.showinfo("Success", "Service added successfully!")
        refresh_services()

    def delete_selected_service():
        if role != "Admin":
            return
        selected_item = tree.selection()
        if not selected_item:
            messagebox.showerror("Error", "Please select a service to delete.")
            return
        row_index = int(tree.item(selected_item)["values"][0]) - 1  # Row index is one-based
        delete_service(row_index)
        messagebox.showinfo("Success", "Service deleted successfully!")
        refresh_services()

    def edit_selected_service():
        if role != "Admin":
            return
        selected_item = tree.selection()
        if not selected_item:
            messagebox.showerror("Error", "Please select a service to edit.")
            return
        row_index = int(tree.item(selected_item)["values"][0]) - 1
        name = name_entry.get()
        category = category_entry.get()
        duration = duration_entry.get()
        price = price_entry.get()
        if not name or not category or not duration or not price:
            messagebox.showerror("Error", "All fields are required!")
            return
        edit_service(row_index, name, category, duration, price)
        messagebox.showinfo("Success", "Service updated successfully!")
        refresh_services()

    window = tk.Tk()
    window.title(f"Service Management ({role})")
    window.geometry("700x500")

    # Treeview for displaying services
    columns = ("Index", "Service Name", "Category", "Duration", "Price")
    tree = ttk.Treeview(window, columns=columns, show="headings", height=10)
    for col in columns:
        tree.heading(col, text=col)
        tree.column(col, width=100)
    tree.pack(pady=10)

    # Admin controls
    if role == "Admin":
        form_frame = tk.Frame(window)
        form_frame.pack(pady=10)

        tk.Label(form_frame, text="Service Name:").grid(row=0, column=0, padx=5, pady=5)
        name_entry = tk.Entry(form_frame)
        name_entry.grid(row=0, column=1, padx=5, pady=5)

        tk.Label(form_frame, text="Category:").grid(row=0, column=2, padx=5, pady=5)
        category_entry = tk.Entry(form_frame)
        category_entry.grid(row=0, column=3, padx=5, pady=5)

        tk.Label(form_frame, text="Duration:").grid(row=1, column=0, padx=5, pady=5)
        duration_entry = tk.Entry(form_frame)
        duration_entry.grid(row=1, column=1, padx=5, pady=5)

        tk.Label(form_frame, text="Price:").grid(row=1, column=2, padx=5, pady=5)
        price_entry = tk.Entry(form_frame)
        price_entry.grid(row=1, column=3, padx=5, pady=5)

        tk.Button(form_frame, text="Add Service", command=add_new_service).grid(row=2, column=0, columnspan=2, pady=10)
        tk.Button(form_frame, text="Edit Service", command=edit_selected_service).grid(row=2, column=2, columnspan=2, pady=10)
        tk.Button(window, text="Delete Selected Service", command=delete_selected_service).pack(pady=10)

    # Refresh services on load
    refresh_services()

    window.mainloop()
