from customtkinter import *
from tkinter import *
import speedtest

# Create main window
window = CTk()
window.title("Internet Speed Test")
window.geometry("360x600")
window.resizable(False, False)
window.configure(fg_color='#060E3F')  # Correcting to fg_color

def check_speed():
    try:
        test = speedtest.Speedtest()

        download_speed = round(test.download() / (1024 * 1024), 2)
        upload_speed = round(test.upload() / (1024 * 1024), 2)
        ping_result = test.results.ping

        download.config(text=f"{download_speed} MBPS")
        upload.config(text=f"{upload_speed} MBPS")
        ping.config(text=f"{ping_result} MS")
        Download.config(text=f"{download_speed} MBPS")
    except Exception as e:
        print(f"An error occurred: {e}")
        download.config(text="Error")
        upload.config(text="Error")
        ping.config(text="Error")
        Download.config(text="Error")

# Setting up window icon and images

Top = PhotoImage(file="D:\\PythonProjects\\Tkinter\\top.png")
Label(master=window, image=Top, bg="#060E3F").pack(pady=15)

Main = PhotoImage(file="D:\\PythonProjects\\Tkinter\\bottom.png")
Label(window, image=Main, bg="#060E3F").pack(pady=(5, 0))

button = PhotoImage(file="D:\\PythonProjects\\Tkinter\\button.png")
Button(window, image=button, bg="#060E3F", bd=0, activebackground="#060E3F", cursor="hand2", command=check_speed).pack(pady=10)

# Adding labels to display results
Label(window, text="PING", font="arial 8 bold", bg="#060E3F", fg="#D07A2A").place(x=50, y=0)
Label(window, text="DOWNLOAD", font="arial 8 bold", bg="#060E3F", fg="#D07A2A").place(x=150, y=0)
Label(window, text="UPLOAD", font="arial 8 bold", bg="#060E3F", fg="#D07A2A").place(x=270, y=0)

Label(window, text="MS", font="arial 7 bold", bg="#060E3F", fg="white").place(x=55, y=100)
Label(window, text="MBPS", font="arial 7 bold", bg="#060E3F", fg="white").place(x=165, y=100)
Label(window, text="MBPS", font="arial 7 bold", bg="#060E3F", fg="white").place(x=280, y=100)

Label(window, text="Download", font="arial 15 bold", bg="#060E3F", fg="white").place(x=135, y=300)
Label(window, text="MBPS", font="arial 15 bold", bg="#060E3F", fg="white").place(x=150, y=390)

ping = Label(window, text="00", font="arial 10 bold", bg="#060E3F", fg="white")
ping.place(x=65, y=75, anchor="center")

download = Label(window, text="00", font="arial 10 bold", bg="#060E3F", fg="white")
download.place(x=180, y=75, anchor="center")

upload = Label(window, text="00", font="arial 10 bold", bg="#060E3F", fg="white")
upload.place(x=295, y=75, anchor="center")

Download = Label(window, text="00", font="arial 25 bold", bg="#060E3F", fg="Black")
Download.place(x=182, y=360, anchor="center")

# Run the main loop
window.mainloop()
