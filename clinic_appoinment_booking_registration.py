import tkinter as tk
import mysql.connector
from tkinter import ttk
from tkinter import messagebox

# Connect to the MySQL database
mydb = mysql.connector.connect(
    host="localhost",
    user="root",
    password="",
    database="clinic_appoinment_booking_registration"
)

mycursor = mydb.cursor()

def calculate_booking_price():
    # Get selected time and calculate booking price with tax
    selected_time = selected_time_combobox.get()
    booking_price = 10  # RM10 per session
    tax = 0.05  # 5% tax
    total_price = booking_price * (1 + tax)

    # Update the entry field with the calculated price
    total_price_entry.delete(0, tk.END)
    total_price_entry.insert(0, f"RM {total_price:.2f}")

def register_patient():
    # Get values from the entry fields and dropdown
    patient_name = patient_name_entry.get()
    patient_age = patient_age_entry.get()
    selected_doctor = selected_doctor_combobox.get()
    selected_date = selected_date_entry.get()
    selected_time = selected_time_combobox.get()

    # Calculate booking price with tax
    booking_price = 10  # RM10 per session
    tax = 0.05  # 5% tax
    total_price = booking_price * (1 + tax)

    # Insert data into the database
    sql = "INSERT INTO appointments (patient_name, patient_age, selected_doctor, selected_date, selected_time, total_price) VALUES (%s, %s, %s, %s, %s, %s)"
    values = (patient_name, patient_age, selected_doctor, selected_date, selected_time, total_price)

    mycursor.execute(sql, values)
    mydb.commit()
    
    # Show a message box to confirm successful registration
    messagebox.showinfo("Success", "Patient registered successfully!")

# Create GUI
root = tk.Tk()
root.title("Clinic Appointment Booking")
root.configure(bg="#89CFF0")
root.geometry("600x300")

frame = tk.Frame(root, bg="#89CFF0")
frame.pack(padx=20, pady=10)

header = tk.Label(root, text="Welcome to Hello Clinic!", font=("cooper black", 16), bg="#89CFF0")
header.pack(pady=10)

# Patient name
patient_name_label = tk.Label(frame, text="Patient Name:", bg="#C154C1")
patient_name_label.grid(row=0, column=0)
patient_name_entry = tk.Entry(frame)
patient_name_entry.grid(row=0, column=1)

# Patient age
patient_age_label = tk.Label(frame, text="Patient Age:", bg="#C154C1")
patient_age_label.grid(row=1, column=0)
patient_age_entry = tk.Entry(frame)
patient_age_entry.grid(row=1, column=1)

# Select Doctor
selected_doctor_label = tk.Label(frame, text="Select Doctor:", bg="#C154C1")
selected_doctor_label.grid(row=2, column=0)
doctors = ["DR. KARIM", "DR. AMINAH", "DR. QHAIRINA"]
selected_doctor_combobox = ttk.Combobox(frame, values=doctors)
selected_doctor_combobox.grid(row=2, column=1)

# Select Date
selected_date_label = tk.Label(frame, text="Select Date (YYYY-MM-DD):", bg="#C154C1")
selected_date_label.grid(row=3, column=0)
selected_date_entry = tk.Entry(frame)
selected_date_entry.grid(row=3, column=1)

# Select Time
selected_time_label = tk.Label(frame, text="Select Time:", bg="#C154C1")
selected_time_label.grid(row=4, column=0)
times = ["9:00 AM", "10:00 AM", "11:00 AM", "2:00 PM", "3:00 PM"]
selected_time_combobox = ttk.Combobox(frame, values=times)
selected_time_combobox.grid(row=4, column=1)

# Total Booking Price
total_price_label = tk.Label(frame, text="Total Booking Price: (just click on the 'Calculate Price' button) ", bg="#C154C1")
total_price_label.grid(row=5, column=0)
total_price_entry = tk.Entry(frame)
total_price_entry.grid(row=5, column=1)

# Calculate Button
calculate_button = tk.Button(frame, text="Calculate Price", command=calculate_booking_price, bg="#C154C1")
calculate_button.grid(row=6, columnspan=2, pady=5)

# Register Button
register_button = tk.Button(frame, text="Register", command=register_patient, bg="#C154C1")
register_button.grid(row=7, columnspan=2, pady=10)

root.mainloop()
mydb.close()