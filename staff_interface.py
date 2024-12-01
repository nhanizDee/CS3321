import tkinter as tk

def staff_interface(username):
    window = tk.Tk()
    window.title(f"Staff Dashboard - {username}")
    window.geometry("400x300")

    tk.Label(window, text=f"Welcome, {username}!", font=("Arial", 16)).pack(pady=20)
    tk.Label(window, text="This is the Staff Interface.", font=("Arial", 12)).pack(pady=10)

    # Example features for staff (to be implemented)
    tk.Label(window, text="View Schedule").pack()
    tk.Button(window, text="View Bookings").pack(pady=5)

    window.mainloop()
