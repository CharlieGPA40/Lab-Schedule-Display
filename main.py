import tkinter as tk
from tkinter import ttk
import sv_ttk
from PIL import Image, ImageTk
from datetime import datetime



def create_schedule_app():
    # Create the main window
    window = tk.Tk()
    window.title("Lab Status")

    # Get the screen width and height
    screen_width = window.winfo_screenwidth()
    screen_height = window.winfo_screenheight()

    # Set the window size to fit the screen
    window.geometry(f"{screen_width}x{screen_height}")

    # green_layer = tk.Frame(window, bg='#75A85E', bd=0)
    # green_layer.place(x=0, y=0, relwidth=1, relheight=1)

    image = Image.open('Gradient.jpg')
    resize_image = image.resize((screen_width, screen_height), Image.LANCZOS)
    resize_image.save('Gradient_Resized.png')

    # Set the background image with opacity
    image = Image.open("Gradient_Resized.png")
    image = image.convert("RGBA")
    # image_with_opacity = image.copy()
    # image_with_opacity.putalpha(128)
    # background = ImageTk.PhotoImage(image_with_opacity)
    background = ImageTk.PhotoImage(image)
    background_label = tk.Label(window, image=background)
    background_label.place(x=0, y=0, relwidth=1, relheight=1)

    color_layer = tk.Frame(window, bg='#283747', bd=0)
    color_layer.place(relx=0.6, rely=0, relwidth=1, relheight=1)

    status_layer_1 = tk.Frame(window, bg='#27AE60', bd=0)
    status_layer_1.place(relx=0, rely=0, relwidth=0.6, relheight=0.045)
    status_layer_1 = tk.Frame(window, bg='#27AE60', bd=0)
    status_layer_1.place(relx=0, rely=0.955, relwidth=0.6, relheight=0.045)

    func_layer = tk.Frame(window, bg='#1C2833', bd=0)
    func_layer.place(relx=0.6, rely=0.955, relwidth=0.6, relheight=0.045)

    def update_time():
        date_object = datetime.now()
        current_time = date_object.strftime("%I:%M")
        current_time_24hr = date_object.strftime("%p")
        current_date = date_object.strftime("%A, %B %d, %Y")
        time_label.config(text=current_time)
        Date_label.config(text=current_date)
        time_label_24hr.config(text=current_time_24hr)
        window.after(1000, update_time)  # Update every 1000 milliseconds (1 second)


    time_label = tk.Label(window, text="", font=("Helvetica Neue", 100), bg='#283747', fg='white')
    time_label.place(relx=0.71, rely=0.1)
    time_label_24hr = tk.Label(window, text="", font=("Helvetica Neue", 50), bg='#283747', fg='white')
    time_label_24hr.place(relx=0.865, rely=0.146)
    Date_label = tk.Label(window, text="", font=("Helvetica Neue", 32), bg='#283747', fg='white')
    Date_label.place(relx=0.714, rely=0.22)
    update_time()
    # Green color layer on top of the image
    # green_layer = tk.Frame(window, bg="green", bd=0)
    # green_layer.place(x=0, y=0, relwidth=1, relheight=1)

    # Outer green ring
    # outer_ring = tk.Label(window, text="", bg="green", fg="white", font=("Arial", 50), bd=0)
    # outer_ring.place(relx=0.5, rely=0.5, anchor="center", relwidth=0.8, relheight=0.8)

    # Schedule lines
    lab_label = tk.Label(window, text="UNO", font=("Helvetica Neue", 40), bg='#283747', fg="#ABB2B9")
    lab_label.place(relx=0.1, rely=0.2, anchor="center")


    line1_label = tk.Label(window, text="Laser Status", font=("Helvetica Neue", 32), bg='#283747', fg="#ABB2B9")
    line1_label.place(relx=0.64, rely=0.43, anchor="sw")
    status_layer_laser = tk.Frame(window, bg='#C0392B', bd=0)
    status_layer_laser.place(relx=0.63, rely=0.3995, relwidth=0.006, relheight=0.0228)

    line2_label = tk.Label(window, text="Camera Status", font=("Helvetica Neue", 32), bg='#283747', fg="#ABB2B9")
    line2_label.place(relx=0.64, rely=0.58, anchor="sw")
    status_layer_camera = tk.Frame(window, bg='#C0392B', bd=0)
    status_layer_camera.place(relx=0.63, rely=0.5495, relwidth=0.006, relheight=0.0228)

    line3_label = tk.Label(window, text="Experiment Status", font=("Helvetica Neue", 32), bg='#283747', fg="#ABB2B9")
    line3_label.place(relx=0.64, rely=0.73, anchor="sw")
    status_layer_experiment = tk.Frame(window, bg='#C0392B', bd=0)
    status_layer_experiment.place(relx=0.63, rely=0.6995, relwidth=0.006, relheight=0.0228)

    line1_lock_button = tk.Button(window, text="On", font=("Helvetica Neue", 22), bg='#283747', fg="#ABB2B9", bd=0)
    line1_lock_button.place(relx=0.85, rely=0.4093, anchor="center")
    line1_unlock_button = tk.Button(window, text="Off", font=("Helvetica Neue", 22), bg='#283747', fg="#ABB2B9", bd=0)
    line1_unlock_button.place(relx=0.92, rely=0.4093, anchor="center")

    line2_lock_button = tk.Button(window, text="On", font=("Helvetica Neue", 22), bg='#283747', fg="#ABB2B9", bd=0)
    line2_lock_button.place(relx=0.85, rely=0.5593, anchor="center")
    line2_unlock_button = tk.Button(window, text="Off", font=("Helvetica Neue", 22), bg='#283747', fg="#ABB2B9", bd=0)
    line2_unlock_button.place(relx=0.92, rely=0.5593, anchor="center")

    line3_lock_button = tk.Button(window, text="On", font=("Helvetica Neue", 22), bg='#283747', fg="#ABB2B9", bd=0)
    line3_lock_button.place(relx=0.85, rely=0.7093, anchor="center")
    line3_unlock_button = tk.Button(window, text="Off", font=("Helvetica Neue", 22), bg='#283747', fg="#ABB2B9", bd=0)
    line3_unlock_button.place(relx=0.92, rely=0.7093, anchor="center")
    # Run the application

    # status_layer_1 = tk.Frame(window, bg='#C0392B', bd=0)
    # status_layer_1.place(relx=0, rely=0, relwidth=0.6, relheight=0.045)
    # status_layer_1 = tk.Frame(window, bg='#C0392B', bd=0)
    # status_layer_1.place(relx=0, rely=0.955, relwidth=0.6, relheight=0.045)

    sv_ttk.set_theme("light")
    window.mainloop()


# Run the conference room schedule app
create_schedule_app()