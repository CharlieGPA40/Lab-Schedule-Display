import tkinter as tk
from datetime import datetime

def update_time():
    current_time = datetime.now().strftime("%H:%M:%S")
    time_label.config(text=current_time)
    window.after(1000, update_time)  # Update every 1000 milliseconds (1 second)

# Create the main window
window = tk.Tk()
window.title("Current Time")

# Create a label for displaying the time
time_label = tk.Label(window, text="", font=("Arial", 24))
time_label.pack(padx=20, pady=20)

# Start updating the time
update_time()

# Start the Tkinter event loop
window.mainloop()