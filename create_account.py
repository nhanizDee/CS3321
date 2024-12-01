import tkinter as tk
from tkinter import messagebox
from utils import save_user
import re  # For regular expression-based validation

def create_account_interface():
    def register():
        username = entry_username.get().strip()
        password = entry_password.get().strip()
        role = role_var.get()

        # Validate username and password
        if not username or not password:
            messagebox.showerror("Error", "Username and password cannot be blank.")
            return

        # Check password strength
        if not is_valid_password(password):
            messagebox.showerror("Error", "Password must be 8-16 characters long, "
                                          "include an uppercase letter, a lowercase letter, "
                                          "a special character, and a digit.")
            return

        # Hash password
        import bcrypt
        hashed_password = bcrypt.hashpw(password.encode(), bcrypt.gensalt()).decode()

        # Save user to Excel
        save_user(username, hashed_password, role)
        messagebox.showinfo("Registration Successful", "Account created successfully!")
        account_window.destroy()
        import login_interface
        login.main_interface()  # Return to the login interface

    # Helper function to validate password
    def is_valid_password(password):
        # At least 8 characters, max 16 characters
        if len(password) < 8 or len(password) > 16:
            return False
        # At least one uppercase letter
        if not re.search(r'[A-Z]', password):
            return False
        # At least one lowercase letter
        if not re.search(r'[a-z]', password):
            return False
        # At least one digit
        if not re.search(r'\d', password):
            return False
        # At least one special character
        if not re.search(r'[!@#$%^&*(),.?":{}|<>]', password):
            return False
        return True

    account_window = tk.Tk()
    account_window.title("Create Account")

    # Center align the interface
    account_window.geometry("400x300")
    account_window.resizable(False, False)

    frame = tk.Frame(account_window)
    frame.pack(expand=True)

    # Registration form
    tk.Label(frame, text="Username:").grid(row=0, column=0, pady=10, sticky="e")
    entry_username = tk.Entry(frame, width=25)
    entry_username.grid(row=0, column=1, pady=10)

    tk.Label(frame, text="Password:").grid(row=1, column=0, pady=10, sticky="e")
    entry_password = tk.Entry(frame, show="*", width=25)
    entry_password.grid(row=1, column=1, pady=10)

    tk.Label(frame, text="Role:").grid(row=2, column=0, pady=10, sticky="e")
    role_var = tk.StringVar(value="Customer")
    tk.OptionMenu(frame, role_var, "Admin", "Staff", "Customer").grid(row=2, column=1, pady=10)

    # Register button
    tk.Button(frame, text="Register", command=register, width=15).grid(row=3, column=1, pady=20)

    account_window.mainloop()
