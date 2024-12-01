import tkinter as tk

def admin_interface(username):
    window = tk.Tk()
    window.title(f"Admin Dashboard - {username}")
    window.geometry("400x300")

    tk.Label(window, text=f"Welcome, {username}!", font=("Arial", 16)).pack(pady=20)
    tk.Label(window, text="This is the Admin Interface.", font=("Arial", 12)).pack(pady=10)

    # Example features for admin (to be implemented)
    tk.Label(window, text="Manage Staff").pack()
    tk.Label(window, text="Manage Services").pack()
    tk.Button(window, text="View All Bookings").pack(pady=5)

    window.mainloop()
