import tkinter as tk
from tkinter import messagebox
from login_backend import authenticate_user
import customer_interface
import staff_interface
import admin_interface

def main_interface():
    def login():
        username = entry_username.get().strip()
        password = entry_password.get().strip()

        # Authenticate the user
        role, error = authenticate_user(username, password)
        if error:
            messagebox.showerror("Login Failed", error)
        else:
            messagebox.showinfo("Login Successful", f"Welcome, {username}!")
            main_window.destroy()
            # Redirect to the respective interface
            if role == "Admin":
                admin_interface.admin_interface(username)
            elif role == "Staff":
                staff_interface.staff_interface(username)
            elif role == "Customer":
                customer_interface.customer_interface(username)

    def open_create_account_interface():
        # Close the login interface and open the account creation interface
        main_window.destroy()
        import create_account
        create_account.create_account_interface()

    # Tkinter window for login
    main_window = tk.Tk()
    main_window.title("Beauty Service Booking System")

    # Center align the interface
    main_window.geometry("400x300")
    main_window.resizable(False, False)

    # Main frame for alignment
    frame = tk.Frame(main_window)
    frame.pack(expand=True)

    # Login form
    tk.Label(frame, text="Username:").grid(row=0, column=0, pady=10, sticky="e")
    entry_username = tk.Entry(frame, width=25)
    entry_username.grid(row=0, column=1, pady=10)

    tk.Label(frame, text="Password:").grid(row=1, column=0, pady=10, sticky="e")
    entry_password = tk.Entry(frame, show="*", width=25)
    entry_password.grid(row=1, column=1, pady=10)

    # Login button
    tk.Button(frame, text="Login", command=login, width=15).grid(row=2, column=1, pady=20)

    # Create account link
    tk.Label(frame, text="Don't have an account?").grid(row=3, column=0, pady=10, sticky="e")
    create_account_link = tk.Label(frame, text="Create One!", fg="blue", cursor="hand2")
    create_account_link.grid(row=3, column=1, pady=10, sticky="w")
    create_account_link.bind("<Button-1>", lambda e: open_create_account_interface())

    main_window.mainloop()
