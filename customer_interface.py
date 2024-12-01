import tkinter as tk
from tkinter import ttk, messagebox
from booking_backend import get_services, save_booking, get_staff_names
import calendar  # Built-in module for date handling
from datetime import date

def customer_interface(customer_name):
    def update_days():
        # Get the selected month and year
        selected_month = int(month_var.get())
        selected_year = int(year_var.get())
        # Calculate the number of days in the selected month and year
        days_in_month = calendar.monthrange(selected_year, selected_month)[1]
        # Update the day dropdown
        day_menu["values"] = [f"{i:02}" for i in range(1, days_in_month + 1)]
        # Reset the selected day to the first day of the month
        day_var.set("01")

    def book_service():
        service_name = service_var.get()
        # Get selected date from the dropdown menus
        selected_date = f"{year_var.get()}-{month_var.get()}-{day_var.get()}"
        time = time_entry.get()
        staff_name = staff_listbox.get(tk.ACTIVE)

        if not service_name or not selected_date or not time:
            messagebox.showerror("Error", "Please fill in all required fields.")
            return

        # Save booking
        booking_id = save_booking(customer_name, service_name, selected_date, time, staff_name)
        messagebox.showinfo("Success", f"Booking successful! Your Booking ID is {booking_id}.")

    # Create dropdowns for date selection
    def create_date_dropdowns(frame):
        today = date.today()
        current_year = today.year

        # Day dropdown
        tk.Label(frame, text="Day:").grid(row=1, column=1, sticky="e")
        global day_var, day_menu
        day_var = tk.StringVar(value=f"{today.day:02}")
        day_menu = ttk.Combobox(frame, textvariable=day_var, width=5, state="readonly")
        day_menu.grid(row=1, column=2)

        # Month dropdown
        tk.Label(frame, text="Month:").grid(row=2, column=1, sticky="e")
        global month_var
        month_var = tk.StringVar(value=f"{today.month:02}")
        month_menu = ttk.Combobox(frame, textvariable=month_var, values=[f"{i:02}" for i in range(1, 13)], width=5, state="readonly")
        month_menu.grid(row=2, column=2)
        month_menu.bind("<<ComboboxSelected>>", lambda e: update_days())  # Update days when month changes

        # Year dropdown
        tk.Label(frame, text="Year:").grid(row=3, column=1, sticky="e")
        global year_var
        year_var = tk.StringVar(value=current_year)
        year_menu = ttk.Combobox(frame, textvariable=year_var, values=[str(y) for y in range(current_year, current_year + 5)], width=7, state="readonly")
        year_menu.grid(row=3, column=2)
        year_menu.bind("<<ComboboxSelected>>", lambda e: update_days())  # Update days when year changes

        # Initialize the day dropdown with the current month and year
        update_days()

    window = tk.Tk()
    window.title("Service Booking System")
    window.geometry("600x500")

    # Booking form
    frame = tk.Frame(window)
    frame.pack(pady=10)

    # Service selection
    tk.Label(frame, text="Select Service:").grid(row=0, column=0, pady=5, sticky="e")
    service_var = tk.StringVar()
    service_menu = ttk.Combobox(frame, textvariable=service_var, values=list(get_services().keys()), state="readonly")
    service_menu.grid(row=0, column=1, pady=5)

    # Date selection
    tk.Label(frame, text="Select Date:").grid(row=1, column=0, sticky="e")
    create_date_dropdowns(frame)

    # Time entry
    tk.Label(frame, text="Select Time (HH:MM):").grid(row=4, column=0, pady=5, sticky="e")
    time_entry = tk.Entry(frame)
    time_entry.grid(row=4, column=1, pady=5)

    # Staff selection with scrollable listbox
    tk.Label(frame, text="Select Staff:").grid(row=5, column=0, pady=5, sticky="e")
    staff_frame = tk.Frame(frame)
    staff_frame.grid(row=5, column=1, pady=5)
    staff_listbox = tk.Listbox(staff_frame, height=5)
    staff_listbox.pack(side=tk.LEFT)
    staff_scrollbar = tk.Scrollbar(staff_frame, command=staff_listbox.yview)
    staff_scrollbar.pack(side=tk.RIGHT, fill=tk.Y)
    staff_listbox.config(yscrollcommand=staff_scrollbar.set)

    for staff in get_staff_names():
        staff_listbox.insert(tk.END, staff)

    # Book service button
    tk.Button(frame, text="Book Service", command=book_service).grid(row=6, column=1, pady=10)

    window.mainloop()
